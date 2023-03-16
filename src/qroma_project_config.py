from typing import List, Optional

from qroma_enums import DeviceBoardPlatform
from qroma_defaults import DEFAULT_DEV_BOARD_PLATFORMS


class QromaProjectConfig:
    dev_board_platforms: List[DeviceBoardPlatform]

    def __init__(self, *,
                 dev_board_platforms: Optional[List[DeviceBoardPlatform]],
                 ):
        if not dev_board_platforms:
            self.dev_board_platforms = DEFAULT_DEV_BOARD_PLATFORMS
        else:
            self.dev_board_platforms = dev_board_platforms
