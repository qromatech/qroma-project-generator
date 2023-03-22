import os
from pathlib import Path
from typing import Optional, Union

from qp_config import QromaProjectConfig
from qroma_enums import QromaProjectLocation


QROMA_PROJECT_CONFIG_FILE_NAME = "qroma.toml"

home_dir = Path.home()
QROMA_PROJECTS_ROOT_DIR = os.path.join(home_dir, "qroma-projects")


class QromaProject:
    # project_root_dir: Union[str, os.PathLike]
    project_dir: Union[str, os.PathLike]
    project_id: str

    _config: QromaProjectConfig

    @property
    def config(self):
        return self._config

    # def __init__(self, project_root_dir: str, project_id: str):
    #     self.project_root_dir = project_root_dir
    #     self.project_id = project_id
    #     self.project_dir = os.path.join(project_root_dir, self.project_id)

    def __init__(self, project_dir: str, project_id: str):
        # self.project_root_dir = project_root_dir
        self.project_id = project_id
        self.project_dir = project_dir
        # self.project_dir = os.path.join(project_root_dir, self.project_id)

    def set_config(self, config: QromaProjectConfig):
        self._config = config


class QromaProjectException(Exception):
    def __init__(self, message):
        super().__init__(message)


def calculate_project_dir(project_id: str, project_location: QromaProjectLocation):
    if project_location == QromaProjectLocation.qroma_project_dir:
        return os.path.join(QROMA_PROJECTS_ROOT_DIR, project_id)
    elif project_location == QromaProjectLocation.current_dir:
        return os.path.join(os.getcwd(), project_id)
    else:
        raise QromaProjectException(f"Unable to determine project directory for {project_id} using {project_location}")


def is_qroma_project_valid(qroma_project: QromaProject):
    qroma_project_config_file_path = Path(os.path.join(qroma_project.project_dir, QROMA_PROJECT_CONFIG_FILE_NAME))
    return os.path.exists(qroma_project_config_file_path)


def is_qroma_project_dir_valid(qroma_project_dir: str):
    qroma_project_config_file_path = Path(os.path.join(qroma_project_dir, QROMA_PROJECT_CONFIG_FILE_NAME))
    return os.path.exists(qroma_project_config_file_path)

