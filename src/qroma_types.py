# from dataclasses import dataclass
from typing import List
from pydantic.dataclasses import dataclass

from qroma_enums import DeviceBoardPlatform
from build_project import BuildParameters
from qp_config import QromaProjectConfig


# class QromaProjectConfig:
#     dev_board_platforms: List[DeviceBoardPlatform]
#
#     def __init__(self, *,
#                  dev_board_platforms: List[DeviceBoardPlatform],
#                  ):
#         self.dev_board_platforms = dev_board_platforms

@dataclass
class GenerateProjectOptions:
    project_config: QromaProjectConfig
    build_parameters: BuildParameters
    #
    # def __init__(self, *,
    #              project_config: QromaProjectConfig,
    #              build_parameters: BuildParameters,
    #              ):
    #     self.project_config = project_config
    #     self.build_parameters = build_parameters
