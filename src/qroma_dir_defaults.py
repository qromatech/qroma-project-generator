import os
# from qroma_project import QromaProject
from constants import QROMA_PROTOBUFS_DIR_NAME
from qroma_project.qroma_project import QromaProject


def extend_dir_chain(root: list, to_extend: list):
    d = root[:]
    d.extend(to_extend)
    return d


PROTOBUFS_ROOT_DIR_CHAIN = ["dev-io", "protobufs"]
PROTOBUFS_OUT_NANOPB_DIR_CHAIN = extend_dir_chain(PROTOBUFS_ROOT_DIR_CHAIN, ["protofiles-out", "nanopb"])
PROTOBUFS_OUT_PYTHON_DIR_CHAIN = extend_dir_chain(PROTOBUFS_ROOT_DIR_CHAIN, ["protofiles-out", "python"])
PROTOBUFS_OUT_TYPESCRIPT_DIR_CHAIN = extend_dir_chain(PROTOBUFS_ROOT_DIR_CHAIN, ["protofiles-out", "typescript"])
PROTOBUFS_OUT_DART_DIR_CHAIN = extend_dir_chain(PROTOBUFS_ROOT_DIR_CHAIN, ["protofiles-out", "dart"])

FIRMWARE_ROOT_DIR_CHAIN = ["firmware"]
FIRMWARE_ESP32_DIR_CHAIN = extend_dir_chain(FIRMWARE_ROOT_DIR_CHAIN, "esp32")

APPS_ROOT_DIR_CHAIN = ["apps"]
APPS_PYTHON_QROMA_IO_DIR_CHAIN = extend_dir_chain(APPS_ROOT_DIR_CHAIN, ["py-qroma-io"])
APPS_PYTHON_QROMA_IO_PROTO_DIR_CHAIN = extend_dir_chain(APPS_PYTHON_QROMA_IO_DIR_CHAIN, ["py-qroma-io"])


def compute_dir_from_project(qroma_project: QromaProject, dir_chain: list[str]):
    computed = os.path.join(qroma_project.project_dir, *dir_chain)
    return computed


def get_protobufs_dir(qroma_project: QromaProject):
    return compute_dir_from_project(qroma_project, PROTOBUFS_ROOT_DIR_CHAIN)


def get_protobufs_out_nanopb_dir(qroma_project: QromaProject):
    return compute_dir_from_project(qroma_project, PROTOBUFS_OUT_NANOPB_DIR_CHAIN)


def get_protobufs_out_python_dir(qroma_project: QromaProject):
    return compute_dir_from_project(qroma_project, PROTOBUFS_OUT_PYTHON_DIR_CHAIN)


def get_protobufs_out_typescriptpb_dir(qroma_project: QromaProject):
    return compute_dir_from_project(qroma_project, PROTOBUFS_OUT_TYPESCRIPT_DIR_CHAIN)


def get_device_boards_esp_dir(qroma_project: QromaProject):
    return compute_dir_from_project(qroma_project, FIRMWARE_ESP32_DIR_CHAIN)


def get_device_boards_esp_project_dir(qroma_project: QromaProject):
    esp_boards_dir = get_device_boards_esp_dir(qroma_project)
    esp_project_dir = os.path.join(esp_boards_dir, qroma_project.project_id)
    return esp_project_dir


def get_device_boards_esp_project_src_dir(qroma_project: QromaProject):
    esp_boards_dir = get_device_boards_esp_project_dir(qroma_project)
    esp_project_dir = os.path.join(esp_boards_dir, "src")
    return esp_project_dir


def get_device_boards_esp_project_pb_dir(qroma_project: QromaProject):
    project_src_dir = get_device_boards_esp_project_src_dir(qroma_project)
    dev_pb_dir = os.path.join(project_src_dir, QROMA_PROTOBUFS_DIR_NAME)
    return dev_pb_dir


def get_apps_dir(qroma_project: QromaProject):
    return compute_dir_from_project(qroma_project, APPS_ROOT_DIR_CHAIN)


def get_apps_python_pb_dir(qroma_project: QromaProject):
    return compute_dir_from_project(qroma_project, APPS_PYTHON_QROMA_IO_PROTO_DIR_CHAIN)


def get_project_site_www_dir(qroma_project: QromaProject):
    # project_site_www_dir = os.path.join(qroma_project.project_dir, "sites", "site-www-" + qroma_project.project_id)
    bundle_root_dir = qroma_project.config.qroma.project.stages.sw.sites.bundle.bundle_root_dir
    project_site_www_dir = os.path.join(qroma_project.project_dir, bundle_root_dir)
    return project_site_www_dir


def get_site_www_pb_dir(qroma_project: QromaProject):
    project_site_www_dir = get_project_site_www_dir(qroma_project)
    site_www_pb_dir = os.path.join(project_site_www_dir, "src", QROMA_PROTOBUFS_DIR_NAME)
    return site_www_pb_dir
