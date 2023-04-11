import os
import shutil
import tempfile
from enum import Enum

from jinja2 import Environment, FileSystemLoader, BaseLoader

from qroma_dirs import get_project_site_static_dir, get_protobufs_build_dest_and_publish_dirs
from qroma_project.qroma_project import QromaProject
# from steps.firmware.fw_files import get_firmware_file_path
from steps.site.qroma_site_bundle_models import QromaFirmwareBuildManifest, QromaEsp32LoaderManifest, \
    QromaSiteManifests, QromaSiteManifest, QromaSiteManifestType
from utils import qroma_os_remove, qroma_copy_file, qroma_copy_dir, ensure_file_exists


class QromaSiteRootType(str, Enum):
    source = "source"
    dest = "dest"
    manifest = "manifest"


# def _get_site_qroma_root_path_chain(root_type: QromaSiteRootType) -> tuple[str, ...]:
#     if root_type == QromaSiteRootType.source:
#         return "static", "qroma",
#     elif root_type == QromaSiteRootType.dest:
#         return "static", "qroma",
#     elif root_type == QromaSiteRootType.manifest:
#         return "qroma",
#     else:
#         raise Exception(f"Unrecognized QromaSiteRootType: {root_type}")
#
#
# def _get_site_qroma_bundle_path_chain(root_type: QromaSiteRootType) -> tuple[str, ...]:
#     return _get_site_qroma_root_path_chain(root_type) + ("versions", )
#
#
# def _get_site_qroma_bundle_version_path_chain(qroma_project: QromaProject, root_type: QromaSiteRootType) -> tuple[str, ...]:
#     return _get_site_qroma_root_path_chain(root_type) + ("versions", qroma_project.config.qroma.project.version)
#
#
# def _get_site_qroma_root_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
#     site_dir = get_project_site_www_dir(qroma_project)
#     site_qroma_root_path = _get_site_qroma_root_path_chain(root_type)
#     site_qroma_root_dir = os.path.join(site_dir, *site_qroma_root_path)
#     return site_qroma_root_dir
#
#
def _get_site_qroma_versions_root_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
    site_www_dir = get_project_site_static_dir(qroma_project)
    # qroma_versions_path = _get_site_qroma_bundle_path_chain(root_type)
    site_qroma_versions_root_dir = qroma_project.config.qroma.project.stages.sw.sites.bundle\
        .bundle_version_content_root_dir_template.format(bundle_root_path=site_www_dir)
    # site_qroma_versions_root_dir = os.path.join(site_www_dir, *qroma_versions_path)
    return site_qroma_versions_root_dir




def _get_site_bundle_root_dir_parameter(qroma_project: QromaProject) -> str:
    return qroma_project.config.qroma.project.stages.sw.sites.bundle.bundle_static_dir


def _get_site_bundle_version_content_dir_parameter(qroma_project: QromaProject) -> str:
    bundle_root_dir = _get_site_bundle_root_dir_parameter(qroma_project)
    return bundle_root_dir


def _get_site_bundle_version_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
    # project_version = get_qroma_project_version(qroma_project)
    qroma_versions_root_dir = _get_site_qroma_versions_root_dir(qroma_project, root_type)
    qroma_version_dir = os.path.join(qroma_versions_root_dir, qroma_project.project_version)
    return qroma_version_dir


def _clean_site_bundle_version_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
    qroma_version_dir = _get_site_bundle_version_content_dir_parameter(qroma_project)
    # qroma_version_dir = os.path.join(qroma_project.project_dir, QromaSiteRootType.dest)
    # qroma_version_dir = _get_site_bundle_version_dir(qroma_project, QromaSiteRootType.dest)
    if os.path.exists(qroma_version_dir) and os.path.isdir(qroma_version_dir):
        print("TO REMOVE: " + qroma_version_dir)
        qroma_os_remove(qroma_version_dir)


#
# def _add_protofiles_to_content_dir(qroma_project: QromaProject, version_content_root_dir: str) -> QromaSiteProtoDetails:
#     protofile_dest_and_publish_dirs = get_protobufs_build_dest_and_publish_dirs(qroma_project)
#
#     input_bundle_version_path_chain = _get_site_qroma_bundle_version_path_chain(qroma_project, QromaSiteRootType.manifest)
#     site_bundle_version_path = "/".join(input_bundle_version_path_chain)
#
#     all_protofile_details = []
#
#     for from_dir, to_dir in protofile_dest_and_publish_dirs:
#         full_from_dir = os.path.join(from_dir, "proto")
#         full_to_dir = os.path.join(version_content_root_dir, to_dir)
#         qroma_copy_dir(full_from_dir, full_to_dir)
#
#         for path, directories, files in os.walk(full_to_dir):
#             rel_path = path.replace(version_content_root_dir, "")
#             rel_path = rel_path.replace("\\", "/")
#             for f in files:
#                 pdpp = f"/{site_bundle_version_path}{rel_path}/{f}"
#                 protofile_details = QromaSiteProtoFileDetails(
#                     protoPath=pdpp
#                 )
#                 all_protofile_details.append(protofile_details)
#
#     return QromaSiteProtoDetails(protofileDetails=all_protofile_details)


def _zip_dirs_and_add_to_content_dir(qroma_project: QromaProject, bundle_version_content_dir: str):
    to_zip_dirs = qroma_project.config.qroma.project.stages.sw.sites.bundle.publish_version.zipped_dirs
    for to_zip_dir in to_zip_dirs:
        source_dir = os.path.join(qroma_project.project_dir, to_zip_dir.source_dir)
        # dest_zip_file_template = os.path.join(bundle_version_content_dir, to_zip_dir.dest_zip_file)
        # firmware_file_to_path = ffr.dest_filepath.format(bundle_version_root_dir=bundle_version_root_dir)
        dest_zip_file_path = to_zip_dir.publication_zip_file.format(bundle_version_content_dir=bundle_version_content_dir)
        dest_zip_file = os.path.join(bundle_version_content_dir, dest_zip_file_path)
        print(f"ZIPPING {source_dir} INTO {dest_zip_file}")
        shutil.make_archive(source_dir, 'zip', dest_zip_file)


# def _add_firmware_files_to_content_dir(qroma_project: QromaProject, content_root_dir: str) -> list[QromaEsp32LoaderManifest]:
#     firmware_file_path = get_firmware_file_path(qroma_project)
#     firmware_file_to_path = os.path.join(content_root_dir, "firmware")
#     os.makedirs(firmware_file_to_path)
#     qroma_copy_file(firmware_file_path, firmware_file_to_path)
#
#     manifest_path = f"/qroma/versions/{qroma_project.config.qroma.project.version}/firmware/manifest-firmware.json"
#     esp32_loader_manifest = QromaEsp32LoaderManifest(
#         name=qroma_project.project_id,
#         manifestPath=manifest_path,
#     )
#
#     return [esp32_loader_manifest]


def _add_firmware_files_to_content_dir(qroma_project: QromaProject, bundle_version_content_dir: str) -> list[QromaEsp32LoaderManifest]:
    firmware_file_replications = qroma_project.config.qroma.project.stages.sw.sites.bundle.publish_version.firmware_file_replications
    # firmware_file_path = get_firmware_file_path(qroma_project)
    # firmware_file_to_path = os.path.join(content_root_dir, "firmware")

    for ffr in firmware_file_replications:
        print("FFR")
        print(ffr)
        if not os.path.isabs(ffr.source_filepath):
            firmware_file_from_path = os.path.join(qroma_project.project_dir, *(ffr.source_filepath.split('/')))
        else:
            firmware_file_from_path = ffr.source_filepath

        # firmware_file_to_path_template = os.path.join(content_root_dir, ffr.dest_filepath)
        # firmware_file_to_path = firmware_file_to_path_template.format(qroma_project=qroma_project)
        firmware_file_to_path = os.path.join(bundle_version_content_dir,
                                             *(ffr.publication_filepath.format(bundle_version_content_dir=bundle_version_content_dir).split("/")))

        # dest_zip_file_template = os.path.join(content_root_dir, to_zip_dir.dest_zip_file)
        # dest_zip_file = dest_zip_file_template.format(qroma_project=qroma_project)

        print(f"REPLICATING FIRMWARE FILE {firmware_file_from_path} TO {firmware_file_to_path}")
        firmware_file_to_dir = os.path.dirname(firmware_file_to_path)
        if not os.path.exists(firmware_file_to_dir):
            os.makedirs(firmware_file_to_dir)
        qroma_copy_file(firmware_file_from_path, firmware_file_to_path)

    # qroma_project_env = Environment(
    #     loader=FileSystemLoader(project_template_dir)
    # )
    # template = qroma_project_env.get_template(template_file)
    # rendered_content = template.render(
    #     qroma_project=qroma_project_data,
    #     firmware=firmware_processor(qroma_project_data),
    # )

    esp32_loader_manifests = []
    files_to_generate = qroma_project.config.qroma.project.stages.sw.sites.bundle.publish_version.generated_files
    for file_to_generate in files_to_generate:
        template_str = file_to_generate.template_str
        rtemplate = Environment(loader=BaseLoader()).from_string(template_str)
        # content = template_str.format(qroma_project=qroma_project)
        content = rtemplate.render(qroma_project=qroma_project)
        content_file_path = os.path.join(bundle_version_content_dir,
                                         file_to_generate.publication_filepath)

        print("CONTENT FILE PATH")
        print(content_file_path)
        print(content)

        with open(content_file_path, "w") as f:
            f.write(content)

        manifest_path = f"/qroma/versions/{qroma_project.project_version}/{file_to_generate.publication_filepath}"
        esp32_loader_manifest = QromaEsp32LoaderManifest(
            name=qroma_project.project_id,
            manifestPath=manifest_path,
        )
        esp32_loader_manifests.append(esp32_loader_manifest)

    return esp32_loader_manifests


def _create_bundle_version_manifest(qroma_project: QromaProject,
                                    esp32_loader_manifests: list[QromaEsp32LoaderManifest],
                                    # proto_details: QromaSiteProtoDetails
                                    ) -> QromaFirmwareBuildManifest:
    manifest = QromaFirmwareBuildManifest(
        project_id=qroma_project.project_id,
        version=qroma_project.config.qroma.project.version,
        qromaEsp32LoaderManifests=esp32_loader_manifests,
        # protoDetails=proto_details,
    )

    return manifest


def _create_temp_bundle_contents(qroma_project: QromaProject, temp_version_content_root_dir: str) -> QromaFirmwareBuildManifest:
    # proto_paths = _add_protofiles_to_content_dir(qroma_project, version_content_root_dir)
    # bundle_version_content_path = qroma_project.config.qroma.project.stages.sw.sites.bundle\
    #     .bundle_version_content_path_template.format(qroma_project=qroma_project)
    # bundle_version_content_dir = os.path.join(version_content_root_dir, bundle_version_content_path)
    _zip_dirs_and_add_to_content_dir(qroma_project, temp_version_content_root_dir)

    esp32_loader_manifests = _add_firmware_files_to_content_dir(qroma_project, temp_version_content_root_dir)

    manifest = _create_bundle_version_manifest(qroma_project, esp32_loader_manifests)  #, proto_paths)
    manifest_json = manifest.json(indent=2)
    manifest_file_path = os.path.join(temp_version_content_root_dir, "manifest.json")

    print(f"WRITING CONTENT TO {manifest_file_path}")
    print(manifest_json)

    with open(manifest_file_path, "w") as f:
        f.write(manifest_json)

    return manifest


def _copy_bundle_version_dir_to_site_dir(bundle_contents_dir, site_bundle_version_dir):
    print(f"COPYING BUNDLE VERSION DIR {bundle_contents_dir} TO {site_bundle_version_dir}")
    qroma_copy_dir(bundle_contents_dir, site_bundle_version_dir)


def _get_qroma_site_manifests_file_path(qroma_project: QromaProject):
    # site_qroma_root_dir = _get_site_qroma_root_dir(qroma_project, QromaSiteRootType.dest)
    site_qroma_root_dir = os.path.join(get_project_site_static_dir(qroma_project), "qroma")
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
        print("ExISTING MANIFESTS")
        print(existing_manifests)

        # site_bundle_version_path_chain = _get_site_qroma_bundle_version_path_chain(qroma_project, QromaSiteRootType.manifest)
        # site_bundle_version_path = "/".join(site_bundle_version_path_chain)

        site_bundle_version_path = f"/qroma/versions/{qroma_project.project_version}"

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
    # create manifest
    # create dir contents for manifest
    # do work to fill dir contents
    # copy dir contents to bundle location
    # append manifest data to manifests.json

    tmp_bundle_root = tempfile.TemporaryDirectory(prefix="qroma-site-bundle-dir-")
    tmp_bundle_root_dir = tmp_bundle_root.name

    manifest = _create_temp_bundle_contents(qroma_project, tmp_bundle_root_dir)
    site_bundle_version_dir = _get_site_bundle_version_dir(qroma_project, QromaSiteRootType.source)
    _clean_site_bundle_version_dir(qroma_project, QromaSiteRootType.dest)
    _copy_bundle_version_dir_to_site_dir(tmp_bundle_root_dir, site_bundle_version_dir)

    _update_qroma_site_manifests_json(qroma_project, manifest)
