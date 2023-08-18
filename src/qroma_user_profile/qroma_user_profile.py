from typing import List, Dict, Optional

from pydantic.dataclasses import dataclass

from qroma_enums import FirmwareFramework


@dataclass
class DefaultTools:
    editor_command: str
    docker_command: str
    firmware_platforms: List[FirmwareFramework]


@dataclass
class FirmwarePlatform:
    build_prompt: Optional[str] = None
    upload_prompt: Optional[str] = None
    build_command: Optional[str] = None
    upload_command: Optional[str] = None


@dataclass
class QromaFirmwarePlatforms:
    user_managed: FirmwarePlatform
    arduino: FirmwarePlatform
    platformio: FirmwarePlatform


@dataclass
class QromaUserProfileTools:
    firmware_platforms: QromaFirmwarePlatforms


@dataclass
class QromaUserProfileDefaults:
    new_project_firmware_platform: FirmwareFramework
    tools: DefaultTools


@dataclass
class QromaUserProfile:
    defaults: QromaUserProfileDefaults
    tools: QromaUserProfileTools
    dirs: Dict[str, str]
