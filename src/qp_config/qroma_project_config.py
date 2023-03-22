from pydantic.dataclasses import dataclass
from typing import List, Optional

from qp_config.firmware.qroma_firmware_config import QromaFirmwareConfig
# from qroma_project.generate.qroma_project_config_user_inputs import QromaProjectConfigUserInputs
from qroma_enums import FirmwareFramework
from qroma_defaults import DEFAULT_FIRMWARE_FRAMEWORKS


@dataclass
class QromaProjectConfig:
    firmware: QromaFirmwareConfig


def create_project_config(qroma_config_file_dict: dict) -> QromaProjectConfig:
    firmware = QromaFirmwareConfig(
        user_platforms=qroma_config_file_dict["qroma"]["project"]["firmware"]["platforms"],
        project_configs=[],
    )
    project_config = QromaProjectConfig(
        firmware=firmware,
    )
    return project_config
