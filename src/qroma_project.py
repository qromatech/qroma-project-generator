import os
from pathlib import Path
from typing import Optional

import yaml


class QromaProject:
    project_dir: str
    project_id: str

    def __init__(self, project_dir, project_id):
        self.project_dir = project_dir
        self.project_id = project_id


def get_yaml_location(project_id: str):
    project_dir = os.path.join(os.getcwd(), project_id)
    qroma_yaml_path = Path(os.path.join(project_dir, "qroma.yaml"))
    return qroma_yaml_path


def save_qroma_project(data: QromaProject, save_location: os.PathLike):
    with open(save_location, 'w') as file:
        print("SAVING YAML")
        print(data)
        yaml.dump({
            "projectId": data.project_id
        }, file)


def load_qroma_project_from_directory(qroma_dir: os.PathLike) -> Optional[QromaProject]:
    qroma_yaml_path = Path(qroma_dir, "qroma.yaml")
    return load_qroma_project_from_yaml_file(qroma_yaml_path)


def load_qroma_project_from_yaml_file(qroma_yaml_file_location: os.PathLike) -> Optional[QromaProject]:
    try:
        with open(qroma_yaml_file_location, 'r') as file:
            qroma_yaml_obj = yaml.safe_load(file)
            project_dir = os.path.dirname(qroma_yaml_file_location)

            qp = QromaProject(
                project_dir=project_dir,
                project_id=qroma_yaml_obj['projectId']
            )

            return qp

    except FileNotFoundError:
        return None


def load_current_dir_qroma_project() -> QromaProject:
    qroma_yaml_path = Path(os.path.join(os.getcwd(), "qroma.yaml"))
    return load_qroma_project_from_yaml_file(qroma_yaml_path)

#
# def load_qroma_project(project_id: str) -> QromaProject:
#     qp_yaml_location = get_yaml_location(project_id)
#     return load_qroma_project_from_yaml_file(qp_yaml_location)
