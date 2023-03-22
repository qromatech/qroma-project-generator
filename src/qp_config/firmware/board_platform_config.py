from pydantic.dataclasses import dataclass
from typing import List, Optional

from qroma_enums import FirmwareFramework
from qroma_defaults import DEFAULT_FIRMWARE_FRAMEWORKS


@dataclass
class QromaBoardPlatformConfig:
    platform: FirmwareFramework

    com_port: str

    def __init__(self, *,
                 dev_board_platforms: Optional[List[FirmwareFramework]],
                 ):
        if not dev_board_platforms:
            self.dev_board_platforms = DEFAULT_FIRMWARE_FRAMEWORKS
        else:
            self.dev_board_platforms = dev_board_platforms

        self.com_port = "TBD"