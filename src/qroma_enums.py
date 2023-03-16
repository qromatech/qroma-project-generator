from enum import Enum


class DeviceBoardPlatform(str, Enum):
    platformio = "platformio"
    arduino = "arduino"
    # micropython = "micropython"