import os
from pathlib import Path
import tomllib
from typing import Optional, Union

# import yaml

from qp_config import QromaProjectConfig
from qp_config.qroma_project_config import create_project_config
from qroma_enums import QromaProjectLocation


QROMA_PROJECT_CONFIG_FILE_NAME = "qroma.toml"

home_dir = Path.home()
QROMA_PROJECTS_ROOT_DIR = os.path.join(home_dir, "qroma-projects")


class QromaProject:
    # project_root_dir: Union[str, os.PathLike]
    project_dir: Union[str, os.PathLike]
    project_id: Union[str, os.PathLike]

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


# def does_qroma_project_dir_exist(qroma_project: QromaProject):
#     return os.path.exists(qroma_project.project_dir)

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
    # qroma_project_config_file_path = Path(os.path.join(qroma_project.project_dir, "qroma.yaml"))
    qroma_project_config_file_path = Path(os.path.join(qroma_project.project_dir, QROMA_PROJECT_CONFIG_FILE_NAME))
    return os.path.exists(qroma_project_config_file_path)


def is_qroma_project_dir_valid(qroma_project_dir: str):
    # qroma_project_config_file_path = Path(os.path.join(qroma_project.project_dir, "qroma.yaml"))
    qroma_project_config_file_path = Path(os.path.join(qroma_project_dir, QROMA_PROJECT_CONFIG_FILE_NAME))
    return os.path.exists(qroma_project_config_file_path)


# def save_qroma_project(qroma_project: QromaProject):
#     save_location = Path(os.path.join(qroma_project.project_dir, "qroma.yaml"))
#     with open(save_location, 'w') as file:
#         print("SAVING YAML")
#         print(qroma_project)
#         yaml.dump({
#             "projectId": qroma_project.project_id
#         }, file)
#
#     create_initial_project_toml(qroma_project)


def load_qroma_project(qroma_project: QromaProject) -> Optional[QromaProject]:
    return load_qroma_project_from_directory(qroma_project.project_dir)


def load_qroma_project_from_directory(qroma_dir: str | os.PathLike) -> Optional[QromaProject]:
    qroma_project_config_file_path = Path(qroma_dir, QROMA_PROJECT_CONFIG_FILE_NAME)
    return load_qroma_project_from_file(qroma_project_config_file_path)


# def load_qroma_project_from_yaml_file(qroma_yaml_file_location: Union[str, os.PathLike]) -> Optional[QromaProject]:
#     try:
#         with open(qroma_yaml_file_location, 'r') as file:
#             qroma_yaml_obj = yaml.safe_load(file)
#             project_root_dir = os.path.join(os.path.dirname(qroma_yaml_file_location), "..")
#
#             qp = QromaProject(
#                 project_root_dir=project_root_dir,
#                 project_id=qroma_yaml_obj['projectId']
#             )
#
#             return qp
#
#     except FileNotFoundError:
#         return None

def load_qroma_project_from_file(qroma_project_config_file_location: str | os.PathLike) -> Optional[QromaProject]:
    try:
        with open(qroma_project_config_file_location, 'rb') as file:
            # qroma_yaml_obj = yaml.safe_load(file)
            qroma_dict = tomllib.load(file)
            # project_root_dir = os.path.join(os.path.dirname(qroma_project_config_file_location), "..")
            print(qroma_dict)

            qp = QromaProject(
                # project_root_dir=project_root_dir,
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

