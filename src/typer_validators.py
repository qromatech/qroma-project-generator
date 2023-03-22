import logging
from typing import Optional
import typer

#
# def _convert_user_project_id_to_qroma_project_info(user_project_id) -> QromaProjectInfoFromUserInput:
#     logging.info("CONVERTING PROJECT ID TO PROJECT USER INFO: " + user_project_id)
#
#     is_valid_qroma_project: bool
#     project_id: str
#     project_path: str
#     project_location: QromaProjectLocation
#
#     if user_project_id is None:
#         qroma_project = load_current_dir_qroma_project()
#         if qroma_project is None:
#             return QromaProjectInfoFromUserInput(
#                 qroma_project.project_id
#             )


#
# def typer_validate_project_info_from_user_project_id(user_project_id: str) -> QromaProjectInfoFromUserInput:
#     logging.info("VALIDATING PROJECT ID FOR TYPER: " + user_project_id)
#     qpi = project_template.get_qroma_project_info_from_user_input(user_project_id)
#     try:
#         qroma_project_info = project_template.get_qroma_project_info_from_user_input(user_project_id)
#         # if does_qroma_project_dir_exist(qp):
#         #     raise typer.BadParameter(f"Project ID {qp.project_id} already created. See {qp.project_dir}.")
#
#     except project_template.NewQromaProjectException as e:
#         raise typer.BadParameter(f"Invalid project ID value: {user_project_id}")
#
#     return user_project_id
from qroma_project import user_input
from qroma_project.qroma_project import load_current_dir_qroma_project, QromaProjectException


def typer_validate_new_user_project_id_from_user(user_project_id: str) -> str:
    logging.info("VALIDATING PROJECT ID FOR TYPER: " + user_project_id)
    qroma_project_info = user_input.create_new_qroma_project_info_from_user_input(user_project_id)
    try:
        # qroma_project_info = project_template.get_qroma_project_info_from_user_input(user_project_id)
        # if does_qroma_project_dir_exist(qp):
        #     raise typer.BadParameter(f"Project ID {qp.project_id} already created. See {qp.project_dir}.")
        if qroma_project_info.project_dir_exists:
            raise typer.BadParameter(f"Project ID {qroma_project_info.project_id} already created. See {qroma_project_info.project_dir}.")

    except QromaProjectException as e:
        raise typer.BadParameter(f"Invalid project ID value: {user_project_id}")

    return user_project_id


def typer_validate_existing_project_id_from_user_project_id(user_project_id: Optional[str]) -> str:
    qroma_project = user_input.load_existing_qroma_project_from_user_input(user_project_id)
    if user_project_id is None:
        qroma_project = load_current_dir_qroma_project()
        if qroma_project is None:
            raise typer.BadParameter(f"No qroma.toml file found in current directory")

        return qroma_project.project_id

    # qroma_project_info = project_template.get_qroma_project_info_from_user_input(user_project_id)
    # if not does_qroma_project_dir_exist(qroma_project_info):
    #     raise typer.BadParameter(f"No project found at {qroma_project_info.project_dir}.")

    # if not is_qroma_project_valid(qroma_project):
    # # validated_project_id = project_template.validate_project_id(project_id)
    # # if validated_project_id == "":
    #     raise typer.BadParameter(f"Invalid Qroma project found at: {qroma_project.project_dir}.")

    # project_dir = os.path.join(os.getcwd(), validated_project_id)
    # qroma_project = load_qroma_project_from_directory(project_dir)
    # if qroma_project is None:
    #     raise typer.BadParameter(f"No qroma.yaml file found in directory {project_dir}")

    return user_project_id


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
