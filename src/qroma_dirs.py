import os
from qroma_project import QromaProject
from constants import QROMA_PROTOBUFS_DIR_NAME


def get_protobufs_dir(qroma_project: QromaProject):
    protobufs_dir = os.path.join(qroma_project.project_dir, "device-io", "protobufs")
    return protobufs_dir


def get_protobufs_out_nanopb_dir(qroma_project: QromaProject):
    pb_dir = get_protobufs_dir(qroma_project)
    pb_out_nanopb_dir = os.path.join(pb_dir, "protofiles-out", "nanopb")
    return pb_out_nanopb_dir


def get_protobufs_out_typescriptpb_dir(qroma_project: QromaProject):
    pb_dir = get_protobufs_dir(qroma_project)
    pb_out_dir = os.path.join(pb_dir, "protofiles-out", "typescript")
    return pb_out_dir


def get_device_boards_esp_dir(qroma_project: QromaProject):
    esp_boards_dir = os.path.join(qroma_project.project_dir, "device-boards", "esp32")
    return esp_boards_dir


def get_device_boards_esp_project_dir(qroma_project: QromaProject):
    esp_boards_dir = get_device_boards_esp_dir(qroma_project)
    esp_project_dir = os.path.join(esp_boards_dir, qroma_project.project_id)
    return esp_project_dir


def get_esp_project_pb_dir(qroma_project: QromaProject):
    dev_board_dir = get_device_boards_esp_project_dir(qroma_project)
    dev_pb_dir = os.path.join(dev_board_dir, "src", QROMA_PROTOBUFS_DIR_NAME)
    return dev_pb_dir


def get_project_site_www_dir(qroma_project: QromaProject):
    project_site_www_dir = os.path.join(qroma_project.project_dir, "sites", "site-www-" + qroma_project.project_id)
    return project_site_www_dir


def get_site_www_pb_dir(qroma_project: QromaProject):
    project_site_www_dir = get_project_site_www_dir(qroma_project)
    site_www_pb_dir = os.path.join(project_site_www_dir, "src", QROMA_PROTOBUFS_DIR_NAME)
    return site_www_pb_dir
