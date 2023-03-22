from pydantic.dataclasses import dataclass
from typing import List, Optional

from qp_config.firmware.qroma_firmware_config import QromaFirmwareConfig
# from qroma_project.generate.qroma_project_config_user_inputs import QromaProjectConfigUserInputs
from qroma_enums import FirmwareFramework
from qroma_defaults import DEFAULT_FIRMWARE_FRAMEWORKS


@dataclass
class QromaProjectConfig:
    firmware: QromaFirmwareConfig

    # active_com_port: str

    # def __init__(self, *,
    #              dev_board_platforms: Optional[List[FirmwareFramework]],
    #              ):
    #     if not dev_board_platforms:
    #         self.dev_board_platforms = DEFAULT_FIRMWARE_FRAMEWORKS
    #     else:
    #         self.dev_board_platforms = dev_board_platforms

        # self.active_com_port = "TBD"


def create_project_config(qroma_config_file_dict: dict) -> QromaProjectConfig:
    firmware = QromaFirmwareConfig(
        user_platforms=qroma_config_file_dict["qroma"]["project"]["firmware"]["platforms"],
        project_configs=[],
    )
    project_config = QromaProjectConfig(
        firmware=firmware,
    )
    return project_config

#
# def create_project_config_from_user_inputs(user_inputs: QromaProjectConfigUserInputs) -> QromaProjectConfig:
#     firmware = QromaFirmwareConfig()
#     project_config = QromaProjectConfig(
#         # dev_board_platforms=qroma_config_file_dict["qroma"]["project"]["dev_board"]["build_frameworks"]
#     )
#     return project_config
