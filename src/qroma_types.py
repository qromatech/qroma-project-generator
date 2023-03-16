from typing import List

from qroma_enums import DeviceBoardPlatform
from build_project import BuildParameters


class QromaProjectConfig:
    dev_board_platforms: List[DeviceBoardPlatform]

    def __init__(self, *,
                 dev_board_platforms: List[DeviceBoardPlatform],
                 ):
        self.dev_board_platforms = dev_board_platforms


class GenerateProjectOptions:
    project_config: QromaProjectConfig
    build_parameters: BuildParameters

    def __init__(self, *,
                 project_config: QromaProjectConfig,
                 build_parameters: BuildParameters,
                 ):
        self.project_config = project_config
        self.build_parameters = build_parameters
