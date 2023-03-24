import os
import tomllib
from pathlib import Path

from qp_config.qroma_project_config import create_project_config
from qroma_project.qroma_project import QromaProject, QROMA_PROJECT_CONFIG_FILE_NAME
from typing import Optional


def load_qroma_project(qroma_project: QromaProject) -> Optional[QromaProject]:
    return load_qroma_project_from_directory(qroma_project.project_dir)


def load_qroma_project_from_directory(qroma_dir: str | os.PathLike) -> Optional[QromaProject]:
    qroma_project_config_file_path = Path(qroma_dir, QROMA_PROJECT_CONFIG_FILE_NAME)
    return load_qroma_project_from_file(qroma_project_config_file_path)


def load_qroma_project_from_file(qroma_project_config_file_location: str | os.PathLike) -> Optional[QromaProject]:
    try:
        with open(qroma_project_config_file_location, 'rb') as file:
            qroma_dict = tomllib.load(file)

            qp = QromaProject(
                project_dir=os.path.dirname(qroma_project_config_file_location),
                project_id=qroma_dict['qroma']['project']['name']
            )

            qp_config = create_project_config(qroma_dict)
            qp.set_config(qp_config)

            return qp

    except FileNotFoundError:
        return None


def load_current_dir_qroma_project() -> QromaProject:
    qroma_project_config_file_path = Path(os.path.join(os.getcwd(), QROMA_PROJECT_CONFIG_FILE_NAME))
    return load_qroma_project_from_file(qroma_project_config_file_path)
