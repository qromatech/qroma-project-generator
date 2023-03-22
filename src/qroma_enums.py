from enum import Enum


class QromaProjectLocation(Enum):
    current_dir = "current_dir"
    qroma_project_dir = "qroma_project_dir"


class FirmwareFramework(str, Enum):
    platformio = "platformio"
    arduino = "arduino"
    # micropython = "micropython"
