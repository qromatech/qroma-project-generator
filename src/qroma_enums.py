from enum import Enum


class QromaProjectLocation(Enum):
    current_dir = "current_dir"
    qroma_project_dir = "qroma_project_dir"
    # does_not_exist = "does_not_exist"


class DeviceBoardPlatform(str, Enum):
    platformio = "platformio"
    arduino = "arduino"
    # micropython = "micropython"
