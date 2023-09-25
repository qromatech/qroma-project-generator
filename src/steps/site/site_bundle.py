import os
import shutil
import logging

import typer
from jinja2 import Environment, BaseLoader

from qroma_project.qroma_project import QromaProject
from steps.site.qroma_site_bundle_models import QromaFirmwareBuildManifest, QromaEsp32LoaderManifest, \
    QromaSiteManifests, QromaSiteManifest, QromaSiteManifestType
from utils import qroma_copy_file, qroma_copy_dir, ensure_file_exists, qroma_os_rmdir
from qroma_enums import ExitReason


def _zip_dirs_and_add_to_content_dir(qroma_project: QromaProject):
    to_zip_dirs = qroma_project.config.qroma.project.stages.sw.sites.bundle.publish_version.zipped_dirs
    for to_zip_dir in to_zip_dirs:
        source_dir = to_zip_dir.source_dir
        dest_zip_file=to_zip_dir.local_publication_zip_file
        if dest_zip_file.endswith(".zip"):
            dest_zip_file = dest_zip_file[:-4]
        print(f"ZIPPING {source_dir} INTO {dest_zip_file}")
        shutil.make_archive(dest_zip_file, 'zip', source_dir)


def _add_firmware_files_to_content_dir(qroma_project: QromaProject) -> list[QromaEsp32LoaderManifest]:
    firmware_file_replications = qroma_project.config.qroma.project.stages.sw.sites.bundle.publish_version.firmware_file_replications

    for ffr in firmware_file_replications:
        firmware_file_from_path = ffr.source_filepath
        firmware_file_to_path = ffr.local_publication_filepath
        if not os.path.exists(firmware_file_from_path):
            logging.error(f"Unable to find file to bundle at '{firmware_file_from_path}'")
            raise typer.Exit(ExitReason.BUNDLE_FIRMWARE_MISSING_FILE.value)

        print(f"REPLICATING FIRMWARE FILE {firmware_file_from_path} TO {firmware_file_to_path}")
        firmware_file_to_dir = os.path.dirname(firmware_file_to_path)
        if not os.path.exists(firmware_file_to_dir):
            os.makedirs(firmware_file_to_dir)
        qroma_copy_file(firmware_file_from_path, firmware_file_to_path)

    esp32_loader_manifests = []
    files_to_generate = qroma_project.config.qroma.project.stages.sw.sites.bundle.publish_version.generated_files
    for file_to_generate in files_to_generate:
        template_str = file_to_generate.template_str
        rtemplate = Environment(loader=BaseLoader()).from_string(template_str)
        content = rtemplate.render(qroma_project=qroma_project)
        content_file_path = file_to_generate.local_publication_filepath

        content_file_to_dir = os.path.dirname(content_file_path)
        if not os.path.exists(content_file_to_dir):
            os.makedirs(content_file_to_dir)

        with open(content_file_path, "w") as f:
            f.write(content)

        manifest_path = file_to_generate.hosted_publication_filepath
        esp32_loader_manifest = QromaEsp32LoaderManifest(
            name=qroma_project.project_id,
            manifestPath=manifest_path,
        )
        esp32_loader_manifests.append(esp32_loader_manifest)

    return esp32_loader_manifests


def _create_bundle_version_manifest(qroma_project: QromaProject,
                                    esp32_loader_manifests: list[QromaEsp32LoaderManifest],
                                    ) -> QromaFirmwareBuildManifest:
    manifest = QromaFirmwareBuildManifest(
        project_id=qroma_project.project_id,
        version=qroma_project.config.qroma.project.version,
        qromaEsp32LoaderManifests=esp32_loader_manifests,
    )

    return manifest


def _create_bundle_content(qroma_project: QromaProject) -> QromaFirmwareBuildManifest:
    local_bundle_version_content_root_dir = qroma_project.config.qroma.project.stages.sw.sites.bundle.local_bundle_version_content_root_dir

    _zip_dirs_and_add_to_content_dir(qroma_project)

    esp32_loader_manifests = _add_firmware_files_to_content_dir(qroma_project)

    manifest = _create_bundle_version_manifest(qroma_project, esp32_loader_manifests)
    manifest_json = manifest.json(indent=2)
    manifest_file_path = os.path.join(local_bundle_version_content_root_dir, "manifest.json")

    print(f"WRITING CONTENT TO {manifest_file_path}")
    print(manifest_json)

    with open(manifest_file_path, "w") as f:
        f.write(manifest_json)

    return manifest


def _copy_bundle_version_dir_to_site_dir(bundle_contents_dir, site_bundle_version_dir):
    print(f"COPYING BUNDLE VERSION DIR {bundle_contents_dir} TO {site_bundle_version_dir}")
    if os.path.exists(site_bundle_version_dir):
        qroma_os_rmdir(site_bundle_version_dir)
    qroma_copy_dir(bundle_contents_dir, site_bundle_version_dir)


def _get_qroma_site_manifests_file_path(qroma_project: QromaProject):
    site_qroma_root_dir = qroma_project.config.qroma.project.stages.sw.sites.bundle.local_bundle_static_qroma_dir
    qroma_site_manifests_path = os.path.join(site_qroma_root_dir, "manifests.json")
    return qroma_site_manifests_path


def _get_qroma_site_manifests(qroma_project: QromaProject) -> QromaSiteManifests:
    qroma_site_manifests_path = _get_qroma_site_manifests_file_path(qroma_project)
    print(f"QROMA SITE MANIFESTS PATH... {qroma_site_manifests_path}")
    ensure_file_exists(qroma_site_manifests_path,
"""{
    "manifests": []
}
""")
    qsm = QromaSiteManifests.parse_file(qroma_site_manifests_path)
    return qsm


def _update_qroma_site_manifests_json(qroma_project: QromaProject,
                                      new_manifest):
    print("_update_qroma_site_manifests_json")
    print(new_manifest)
    if isinstance(new_manifest, QromaFirmwareBuildManifest):
        existing_manifests = _get_qroma_site_manifests(qroma_project)
        print("EXISTING MANIFESTS")
        print(existing_manifests)

        site_bundle_version_path = qroma_project.config.qroma.project.stages.sw.sites.bundle.hosted_bundle_version_path

        manifest_type = QromaSiteManifestType.publishedQromaFirmwareBuild
        manifest_path = f"/{site_bundle_version_path}/manifest.json"
        manifest_details = {}

        if any(m.path == manifest_path and
               m.type == manifest_type
               for m in existing_manifests.manifests):
            print("MANIFEST RETURNING")
            return

        existing_manifests.manifests.append(
            QromaSiteManifest(
                type=manifest_type,
                path=f"{site_bundle_version_path}/manifest.json",
                details=manifest_details,
            ))

        updated_manifests_json = existing_manifests.json(indent=2)

        qroma_site_manifests_path = _get_qroma_site_manifests_file_path(qroma_project)
        print(f"UPDATING MANIFEST AT {qroma_site_manifests_path}")
        with open(qroma_site_manifests_path, "w") as f:
            f.write(updated_manifests_json)

    else:
        print(f"UNRECOGNIZED MANIFEST TYPE: {type(new_manifest)} - not updating manifests.json")


def do_site_bundle_work(qroma_project: QromaProject):
    manifest = _create_bundle_content(qroma_project)
    _update_qroma_site_manifests_json(qroma_project, manifest)
