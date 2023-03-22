from pydantic.dataclasses import dataclass
from typing import List, Optional

from qroma_enums import FirmwareFramework
from qroma_defaults import DEFAULT_FIRMWARE_FRAMEWORKS


@dataclass
class QromaProjectFrameworkConfig:
    framework: FirmwareFramework
    com_port: str
