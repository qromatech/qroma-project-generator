from typing import List

from pydantic.dataclasses import dataclass

from qroma_enums import FirmwareFramework


@dataclass
class DefaultPreferences:
    firmware_platforms: List[FirmwareFramework]


@dataclass
class DefaultTools:
    editor_command: str
    docker_command: str
    firmware_platform: FirmwareFramework


@dataclass
class FirmwarePlatformIo:
    platformio_exe: str
    build_command: str
    upload_command: str
    monitor_command: str


@dataclass
class FirmwareArduino:
    arduino_exe: str
    build_command: str
    upload_command: str
    monitor_command: str


@dataclass
class FirmwareCommands:
    platformio: FirmwarePlatformIo
    arduino: FirmwareArduino


@dataclass
class QromaUserProfileCommands:
    firmware: FirmwareCommands


@dataclass
class QromaUserProfileDefaults:
    tools: DefaultTools
    preferences: DefaultPreferences


@dataclass
class QromaUserProfile:
    defaults: QromaUserProfileDefaults
    commands: QromaUserProfileCommands
