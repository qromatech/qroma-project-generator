import os
from typing import Optional
import typer

import project_template
from qroma_project import load_current_dir_qroma_project, load_qroma_project_from_directory


def typer_validate_new_project_id(project_id: str):
    validated_project_id = project_template.validate_project_id(project_id)
    if validated_project_id == "":
        raise typer.BadParameter(f"Invalid project ID value: {project_id}")

    return validated_project_id


def typer_validate_existing_project_id(project_id: Optional[str]):
    if project_id is None:
        qroma_project = load_current_dir_qroma_project()
        if qroma_project is None:
            raise typer.BadParameter(f"No qroma.yaml file found in this directory")

        return qroma_project.project_id

    validated_project_id = project_template.validate_project_id(project_id)
    if validated_project_id == "":
        raise typer.BadParameter(f"Invalid project ID value: {project_id}")

    project_dir = os.path.join(os.getcwd(), validated_project_id)
    qroma_project = load_qroma_project_from_directory(project_dir)
    if qroma_project is None:
        raise typer.BadParameter(f"No qroma.yaml file found in directory {project_dir}")

    return qroma_project.project_id


# def typer_validate_project_root_dir(project_root_dir: str):
#     if project_root_dir.strip() == '':
#         print("USE DEFAULT")
#         project_root_dir = project_template.QROMA_DEFAULT_PROJECT_ROOT_DIR
#     elif project_root_dir.strip() == '.':
#         print("USE CWD")
#         project_root_dir = os.getcwd()
#     else:
#         raise typer.BadParameter(f"Invalid project root dir value: {project_root_dir}")
#
#     return project_root_dir
