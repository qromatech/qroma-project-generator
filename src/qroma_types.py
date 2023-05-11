from typing import List
from pydantic.dataclasses import dataclass

from build_project import BuildParameters
from qroma_enums import QromaProjectLocation, FirmwareFramework


@dataclass
class NewQromaProjectInfoFromUserInput:
    project_id: str
    project_dir: str
    project_location: QromaProjectLocation
    project_dir_exists: bool


@dataclass
class QromaProjectConfigUserInputs:
    project_info: NewQromaProjectInfoFromUserInput
    firmware_platform: FirmwareFramework


@dataclass
class GenerateProjectOptions:
    project_config_user_inputs: QromaProjectConfigUserInputs
    build_parameters: BuildParameters
    replace_existing_project_directory: bool
