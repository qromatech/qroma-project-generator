import os
from qroma_project import QromaProject


def get_protobufs_dir(qroma_project: QromaProject):
    protobufs_dir = os.path.join(qroma_project.project_dir, "device-io", "protobufs")
    return protobufs_dir


def get_protobufs_out_nanopb_dir(qroma_project: QromaProject):
    pb_dir = get_protobufs_dir(qroma_project)
    pb_out_nanopb_dir = os.path.join(pb_dir, "protofiles-out", "nanopb")
    return pb_out_nanopb_dir


def get_device_boards_esp_project_dir(qroma_project: QromaProject):
    esp_project_dir = os.path.join(qroma_project.project_dir, "device-boards", "esp32", qroma_project.project_id)
    return esp_project_dir


def get_esp_project_pb_dir(qroma_project: QromaProject):
    dev_dir = get_device_boards_esp_project_dir(qroma_project)
    dev_pb_dir = os.path.join(dev_dir, "src", "protobufs")
    return dev_pb_dir
