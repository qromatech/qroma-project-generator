# from dataclasses import dataclass
from pydantic.dataclasses import dataclass
from typing import List, Optional

from qroma_enums import DeviceBoardPlatform
from qroma_defaults import DEFAULT_DEV_BOARD_PLATFORMS


@dataclass
class QromaProjectConfig:
    dev_board_platforms: List[DeviceBoardPlatform]

    com_port: str

    def __init__(self, *,
                 dev_board_platforms: Optional[List[DeviceBoardPlatform]],
                 ):
        if not dev_board_platforms:
            self.dev_board_platforms = DEFAULT_DEV_BOARD_PLATFORMS
        else:
            self.dev_board_platforms = dev_board_platforms

        self.com_port = "TBD"


def create_project_config(qroma_config_file_dict: dict) -> QromaProjectConfig:
    project_config = QromaProjectConfig(
        dev_board_platforms=qroma_config_file_dict["qroma"]["project"]["dev_board"]["build_frameworks"]
    )
    return project_config
