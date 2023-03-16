from typing import List

from qroma_enums import DeviceBoardPlatform


class QromaProjectConfig:
    dev_board_platforms: List[DeviceBoardPlatform]

    def __init__(self, *,
                 dev_board_platforms: List[DeviceBoardPlatform],
                 ):
        self.dev_board_platforms = dev_board_platforms


class GenerateProjectOptions:
    project_config: QromaProjectConfig

    def __init__(self, *,
                 project_config: QromaProjectConfig,
                 ):
        self.project_config = project_config
