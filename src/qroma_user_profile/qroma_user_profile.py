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


@dataclass
class QromaUserProfileDefaults:
    tools: DefaultTools
    preferences: DefaultPreferences


@dataclass
class QromaUserProfile:
    defaults: QromaUserProfileDefaults
