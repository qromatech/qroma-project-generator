import os
import tempfile
from enum import Enum

from qroma_dirs import get_project_site_www_dir, get_protobufs_build_dest_and_publish_dirs
from qroma_project.qroma_project import QromaProject, get_qroma_project_version
from steps.firmware.fw_files import get_firmware_file_path
from steps.site.qroma_site_bundle_models import QromaFirmwareBuildManifest, QromaEsp32LoaderManifest, \
    QromaSiteManifests, QromaSiteManifest, QromaSiteManifestType, QromaSiteProtoDetails, QromaSiteProtoFileDetails
from utils import qroma_os_remove, qroma_copy_file, qroma_copy_dir, ensure_file_exists


class QromaSiteRootType(str, Enum):
    source = "source"
    dest = "dest"
    manifest = "manifest"


def _get_site_qroma_root_path_chain(root_type: QromaSiteRootType) -> tuple[str, ...]:
    if root_type == QromaSiteRootType.source:
        return "static", "qroma",
    elif root_type == QromaSiteRootType.dest:
        return "static", "qroma",
    elif root_type == QromaSiteRootType.manifest:
        return "qroma",
    else:
        raise Exception(f"Unrecognized QromaSiteRootType: {root_type}")


def _get_site_qroma_bundle_path_chain(root_type: QromaSiteRootType) -> tuple[str, ...]:
    return _get_site_qroma_root_path_chain(root_type) + ("versions", )


def _get_site_qroma_bundle_version_path_chain(qroma_project: QromaProject, root_type: QromaSiteRootType) -> tuple[str, ...]:
    return _get_site_qroma_root_path_chain(root_type) + ("versions", qroma_project.config.qroma.project.version)


def _get_site_qroma_root_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
    site_dir = get_project_site_www_dir(qroma_project)
    site_qroma_root_path = _get_site_qroma_root_path_chain(root_type)
    site_qroma_root_dir = os.path.join(site_dir, *site_qroma_root_path)
    return site_qroma_root_dir


def _get_site_qroma_versions_root_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
    site_www_dir = get_project_site_www_dir(qroma_project)
    qroma_versions_path = _get_site_qroma_bundle_path_chain(root_type)
    site_qroma_versions_root_dir = os.path.join(site_www_dir, *qroma_versions_path)
    return site_qroma_versions_root_dir


def _get_site_bundle_version_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
    project_version = get_qroma_project_version(qroma_project)
    qroma_versions_root_dir = _get_site_qroma_versions_root_dir(qroma_project, root_type)
    qroma_version_dir = os.path.join(qroma_versions_root_dir, project_version)
    return qroma_version_dir


def _clean_site_bundle_version_dir(qroma_project: QromaProject, root_type: QromaSiteRootType):
    qroma_version_dir = _get_site_bundle_version_dir(qroma_project, QromaSiteRootType.dest)
    if os.path.exists(qroma_version_dir) and os.path.isdir(qroma_version_dir):
        print("TO REMOVE: " + qroma_version_dir)
        qroma_os_remove(qroma_version_dir)


def _add_protofiles_to_content_dir(qroma_project: QromaProject, version_content_root_dir: str) -> QromaSiteProtoDetails:
    protofile_dest_and_publish_dirs = get_protobufs_build_dest_and_publish_dirs(qroma_project)

    input_bundle_version_path_chain = _get_site_qroma_bundle_version_path_chain(qroma_project, QromaSiteRootType.manifest)
    site_bundle_version_path = "/".join(input_bundle_version_path_chain)

    all_protofile_details = []

    for from_dir, to_dir in protofile_dest_and_publish_dirs:
        full_from_dir = os.path.join(from_dir, "proto")
        full_to_dir = os.path.join(version_content_root_dir, to_dir)
        qroma_copy_dir(full_from_dir, full_to_dir)

        for path, directories, files in os.walk(full_to_dir):
            rel_path = path.replace(version_content_root_dir, "")
            rel_path = rel_path.replace("\\", "/")
            for f in files:
                pdpp = f"/{site_bundle_version_path}{rel_path}/{f}"
                protofile_details = QromaSiteProtoFileDetails(
                    protoPath=pdpp
                )
                all_protofile_details.append(protofile_details)

    return QromaSiteProtoDetails(protofileDetails=all_protofile_details)


def _add_firmware_files_to_content_dir(qroma_project: QromaProject, content_root_dir: str) -> list[QromaEsp32LoaderManifest]:
    firmware_file_path = get_firmware_file_path(qroma_project)
    firmware_file_to_path = os.path.join(content_root_dir, "firmware")
    os.makedirs(firmware_file_to_path)
    qroma_copy_file(firmware_file_path, firmware_file_to_path)

    manifest_path = f"/qroma/versions/{qroma_project.config.qroma.project.version}/firmware/manifest-firmware.json"
    esp32_loader_manifest = QromaEsp32LoaderManifest(
        name=qroma_project.project_id,
        manifestPath=manifest_path,
    )

    return [esp32_loader_manifest]


def _create_bundle_version_manifest(qroma_project: QromaProject,
                                    esp32_loader_manifests: list[QromaEsp32LoaderManifest],
                                    proto_details: QromaSiteProtoDetails
                                    ) -> QromaFirmwareBuildManifest:
    manifest = QromaFirmwareBuildManifest(
        project_id=qroma_project.project_id,
        version=qroma_project.config.qroma.project.version,
        qromaEsp32LoaderManifests=esp32_loader_manifests,
        protoDetails=proto_details,
    )

    return manifest


def _create_temp_bundle_contents(qroma_project: QromaProject, version_content_root_dir: str) -> QromaFirmwareBuildManifest:
    proto_paths = _add_protofiles_to_content_dir(qroma_project, version_content_root_dir)
    esp32_loader_manifests = _add_firmware_files_to_content_dir(qroma_project, version_content_root_dir)

    manifest = _create_bundle_version_manifest(qroma_project, esp32_loader_manifests, proto_paths)
    manifest_json = manifest.json(indent=2)
    with open(os.path.join(version_content_root_dir, "manifest.json"), "w") as f:
        f.write(manifest_json)

    return manifest


def _copy_bundle_version_dir_to_site_dir(bundle_contents_dir, site_bundle_version_dir):
    qroma_copy_dir(bundle_contents_dir, site_bundle_version_dir)


def _get_qroma_site_manifests_file_path(qroma_project: QromaProject):
    site_qroma_root_dir = _get_site_qroma_root_dir(qroma_project, QromaSiteRootType.dest)
    qroma_site_manifests_path = os.path.join(site_qroma_root_dir, "manifests.json")
    return qroma_site_manifests_path


def _get_qroma_site_manifests(qroma_project: QromaProject) -> QromaSiteManifests:
    qroma_site_manifests_path = _get_qroma_site_manifests_file_path(qroma_project)
    ensure_file_exists(qroma_site_manifests_path,
"""{
    "manifests": []
}
""")
    qsm = QromaSiteManifests.parse_file(qroma_site_manifests_path)
    return qsm


def _update_qroma_site_manifests_json(qroma_project: QromaProject,
                                      new_manifest):
    if isinstance(new_manifest, QromaFirmwareBuildManifest):
        existing_manifests = _get_qroma_site_manifests(qroma_project)

        site_bundle_version_path_chain = _get_site_qroma_bundle_version_path_chain(qroma_project, QromaSiteRootType.manifest)
        site_bundle_version_path = "/".join(site_bundle_version_path_chain)

        manifest_type = QromaSiteManifestType.publishedQromaFirmwareBuild
        manifest_path = f"/{site_bundle_version_path}/manifest.json"
        manifest_details = {}

        if any(m.path == manifest_path and
               m.type == manifest_type
               for m in existing_manifests.manifests):
            return

        existing_manifests.manifests.append(
            QromaSiteManifest(
                type=manifest_type,
                path=f"/{site_bundle_version_path}/manifest.json",
                details=manifest_details,
            ))

        updated_manifests_json = existing_manifests.json(indent=2)

        qroma_site_manifests_path = _get_qroma_site_manifests_file_path(qroma_project)
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
