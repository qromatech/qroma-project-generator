import os

import typer

from qroma_enums import QromaProjectLocation
from qroma_project.qp_loader import load_qroma_project_from_directory, load_current_dir_qroma_project
from qroma_project.qroma_project import calculate_project_dir, QromaProjectException,\
    QromaProject, is_qroma_project_dir_valid
from qroma_types import NewQromaProjectInfoFromUserInput


QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX = ":"

VALID_PROJECT_ID_CHARS = "abcdefghijklmnopqrstuvwxyz" + \
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
                         "0123456789-_"


def is_valid_project_id(project_id: str) -> bool:
    trimmed_project_id = project_id.strip()
    for c in trimmed_project_id:
        if c not in VALID_PROJECT_ID_CHARS:
            return False

    return True


def create_new_qroma_project_info_from_user_input(user_project_id: str) -> NewQromaProjectInfoFromUserInput:
    project_id = user_project_id
    project_location = QromaProjectLocation.current_dir

    if user_project_id.startswith(QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX):
        project_id = user_project_id[1:]
        project_location = QromaProjectLocation.qroma_project_dir

    if not is_valid_project_id(project_id):
        raise QromaProjectException(f"Invalid project ID: {project_id}")

    project_dir = calculate_project_dir(project_id, project_location)

    project_dir_exists = False
    if os.path.exists(project_dir):
        project_dir_exists = True

    return NewQromaProjectInfoFromUserInput(
        project_id=project_id,
        project_location=project_location,
        project_dir=project_dir,
        project_dir_exists=project_dir_exists,
    )


def load_existing_qroma_project_from_user_input(user_project_id: str | None) -> QromaProject:
    if user_project_id is None:
        qroma_project = load_current_dir_qroma_project()
        if qroma_project is None:
            raise typer.BadParameter(f"No qroma.toml file found in current directory")
        return qroma_project

    project_in_qroma_projects_dir = False
    project_id = user_project_id

    if user_project_id.startswith(QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX):
        project_id = user_project_id[1:]
        project_in_qroma_projects_dir = True

    if not is_valid_project_id(project_id):
        raise QromaProjectException(f"Unable to load - invalid project ID: {project_id}")

    qroma_project_dir = calculate_project_dir(project_id, QromaProjectLocation.current_dir)
    if project_in_qroma_projects_dir:
        qroma_project_dir = calculate_project_dir(project_id, QromaProjectLocation.qroma_project_dir)

    if not is_qroma_project_dir_valid(qroma_project_dir):
        raise QromaProjectException(f"Invalid project dir for project ID {project_id}: {qroma_project_dir}")

    qroma_project = load_qroma_project_from_directory(qroma_project_dir)
    return qroma_project
