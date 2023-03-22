from pydantic.dataclasses import dataclass
from typing import List, Optional

from qp_config.firmware.qroma_project_framework_config import QromaProjectFrameworkConfig
from qroma_enums import FirmwareFramework
from qroma_defaults import DEFAULT_FIRMWARE_FRAMEWORKS


@dataclass
class QromaFirmwareConfig:
    user_platforms: List[FirmwareFramework]

    project_configs: List[QromaProjectFrameworkConfig]
    #
    # def __init__(self, *,
    #              user_platforms: Optional[List[FirmwareFramework]],
    #              ):
    #     if not user_platforms:
    #         self.user_platforms = DEFAULT_FIRMWARE_FRAMEWORKS
    #     else:
    #         self.user_platforms = user_platforms
