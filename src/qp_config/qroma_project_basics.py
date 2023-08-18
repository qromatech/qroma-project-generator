from pydantic.dataclasses import dataclass


@dataclass
class QromaBasicsProjectDirs:
    pb_root: str
    firmware_root: str
    app_root: str
    site_root: str


@dataclass
class QromaBasicsProjectDict:
    id: str
    name: str
    version: str
    dirs: QromaBasicsProjectDirs


@dataclass
class QromaBasicsRoot:
    project: QromaBasicsProjectDict


@dataclass
class QromaProjectBasics:
    qroma: QromaBasicsRoot


def create_project_basics(qroma_basics_file_dict: dict) -> QromaProjectBasics:
    project_basics = QromaProjectBasics(**qroma_basics_file_dict)
    return project_basics
