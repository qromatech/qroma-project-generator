from typing import List

from pydantic.dataclasses import dataclass

from qroma_enums import FirmwareFramework


@dataclass
class QromaProjectTemplateData:
    project_dir: str
    project_id: str
    firmware_platforms: List[FirmwareFramework]
