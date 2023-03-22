import logging
from typing import Optional
import typer

from qroma_project import user_input
from qroma_project.qp_loader import load_current_dir_qroma_project
from qroma_project.qroma_project import QromaProjectException


def typer_validate_new_user_project_id_from_user(user_project_id: str) -> str:
    logging.info("VALIDATING PROJECT ID FOR TYPER: " + user_project_id)
    qroma_project_info = user_input.create_new_qroma_project_info_from_user_input(user_project_id)
    try:
        if qroma_project_info.project_dir_exists:
            raise typer.BadParameter(f"Project ID {qroma_project_info.project_id} already created. See {qroma_project_info.project_dir}.\n"
                                     "  Add --replace-existing if you want to delete the existing project.")

    except QromaProjectException as e:
        raise typer.BadParameter(f"Invalid project ID value: {user_project_id}")

    return user_project_id


def typer_validate_existing_project_id_from_user_project_id(user_project_id: Optional[str]) -> str:
    if user_project_id is None:
        qroma_project = load_current_dir_qroma_project()
        if qroma_project is None:
            raise typer.BadParameter(f"No qroma.toml file found in current directory")

        return qroma_project.project_id

    return user_project_id
