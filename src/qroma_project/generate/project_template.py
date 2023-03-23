import os
import shutil
from distutils.dir_util import copy_tree
import requests
import zipfile
import io
from pathlib import Path
import tempfile

import typer

from constants import PROJECT_TEMPLATE_ZIP_URL
from config import LOCAL_TEMPLATE_DIR, JINJA_TEST_TEMPLATE_DIR
from qroma_enums import QromaProjectLocation

# from qp_new.generate_project import GenerateProjectOptions
# from qroma_types import QromaProjectInfoFromUserInput

# home_dir = Path.home()
# QROMA_PROJECTS_ROOT_DIR = os.path.join(home_dir, "qroma-projects")
# from qroma_types import GenerateProjectOptions
from qroma_project.qroma_project import QROMA_PROJECTS_ROOT_DIR, QromaProject
# from qroma_types import NewQromaProjectInfoFromUserInput, \
#     ExistingQromaProjectInfoFromUserInput

# QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX = ":"
#
# VALID_PROJECT_ID_CHARS = "abcdefghijklmnopqrstuvwxyz" + \
#                          "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
#                          "0123456789-_"

#
# class NewQromaProjectException(Exception):
#     def __init__(self, message):
#         super().__init__(message)


# def create_project_info_for_current_project_id(project_id: str) -> QromaProjectInfoFromUserInput:
#     pass
#
#
# def create_project_info_for_qroma_projects_dir_project_id(project_id: str) -> QromaProjectInfoFromUserInput:
#     pass

#
# def calculate_project_dir(project_id: str, project_location: QromaProjectLocation):
#     if project_location == QromaProjectLocation.qroma_project_dir:
#         return os.path.join(QROMA_PROJECTS_ROOT_DIR, project_id)
#     elif project_location == QromaProjectLocation.current_dir:
#         return os.path.join(os.getcwd(), project_id)
#     else:
#         raise NewQromaProjectException(f"Unable to determine project directory for {project_id} using {project_location}")

#
# def create_new_qroma_project_info_from_user_input(user_project_id: str) -> NewQromaProjectInfoFromUserInput:
#     project_id = user_project_id
#     project_location = QromaProjectLocation.current_dir
#
#     if user_project_id.startswith(QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX):
#         project_id = user_project_id[1:]
#         project_location = QromaProjectLocation.qroma_project_dir
#
#     if not is_valid_project_id(project_id):
#         raise NewQromaProjectException(f"Invalid project ID: {project_id}")
#
#     project_dir = calculate_project_dir(project_id, project_location)
#     # os.path.join(QROMA_PROJECTS_ROOT_DIR, project_id)
#
#     return NewQromaProjectInfoFromUserInput(
#         project_id=project_id,
#         project_location=project_location,
#         project_dir=project_dir,
#     )
#     # if project_in_qroma_projects_dir:
#     #     project_dir = os.path.join(QROMA_PROJECTS_ROOT_DIR, project_id)
#     #     project_location = QromaProjectLocation.qroma_project_dir
#
#
# def create_existing_qroma_project_info_from_user_input(user_project_id: str | None) -> ExistingQromaProjectInfoFromUserInput:
#     if user_project_id is None:
#         qroma_project = load_current_dir_qroma_project()
#         if qroma_project is None:
#             raise typer.BadParameter(f"No qroma.toml file found in current directory")
#
#     project_in_qroma_projects_dir = False
#     if user_project_id.startswith(QROMA_PROJECTS_DIR_PROJECT_ID_PREFIX):
#         project_id = user_project_id[1:]
#         return create_project_info_for_qroma_projects_dir_project_id(project_id)
#
#         project_in_qroma_projects_dir = True
#
#     project_id = user_project_id
#
#     if not is_valid_project_id(project_id):
#         raise NewQromaProjectException(f"Invalid project ID: {project_id}")
#
#     project_location = QromaProjectLocation.current_dir
#     if project_in_qroma_projects_dir:
#         project_dir = os.path.join(QROMA_PROJECTS_ROOT_DIR, project_id)
#         project_location = QromaProjectLocation.qroma_project_dir
#
#
#         # project_root_dir = QROMA_PROJECTS_ROOT_DIR
#         # project_dir = os.path.join(QROMA_PROJECTS_ROOT_DIR, project_id)
#     # else:
#     project_id = user_project_id
#     project_location = QromaProjectLocation.current_dir
#     project_dir = os.getcwd()
#
#
#     # project_dir = os.path.join(project_root_dir, project_id)
#
#     project_exists = os.path.exists(project_dir)
#     if not project_exists:
#         project_location = QromaProjectLocation.does_not_exist
#
#     return ExistingQromaProjectInfoFromUserInput(
#         project_id,
#         project_dir,
#         project_location,
#     )


# def is_valid_project_id(project_id: str) -> bool:
#     trimmed_project_id = project_id.strip()
#     for c in trimmed_project_id:
#         if c not in VALID_PROJECT_ID_CHARS:
#             return False
#
#     return True


# def get_project_root_dir(project_id: str) -> str:
#     print("GETTING PROJECT DIR 2")
#     project_root_dir = ""
#     project_dir_complete = False
#     x = 1
#
#     # while not os.path.isdir(project_root_dir):
#     while not project_dir_complete:
#         user_entered_project_dir = input(
#             f"{x}: Enter a period (.) to generate your project in the current " +
#             f"directory or leave blank to use '{QROMA_DEFAULT_PROJECT_ROOT_DIR}' >>> "
#         )
#         print(f">>> {user_entered_project_dir}")
#
#         if user_entered_project_dir.strip() == '.':
#             print("USE CWD")
#             project_root_dir = os.getcwd()
#         elif user_entered_project_dir.strip() == '':
#             print("USE DEFAULT")
#             project_root_dir = QROMA_DEFAULT_PROJECT_ROOT_DIR
#             # if not os.path.exists(QROMA_PROJECT_ROOT_DIR):
#             #     os.makedirs(QROMA_PROJECT_ROOT_DIR)
#
#         print("USER ENTERED: " + user_entered_project_dir)
#
#         project_dir = os.path.join(project_root_dir, project_id)
#         if not os.path.exists(project_dir):
#             os.makedirs(project_dir)
#             project_dir_complete = True
#         else:
#             print(
#                 f"A directory at '{project_dir}' already exists. Delete this directory or come up with a different "
#                 "project ID.")
#
#         x += 1
#
#     return project_root_dir
from utils import qroma_os_remove, qroma_os_rmdir, qroma_copy_file


def download_template_to_dir(project_dir: os.PathLike) -> str:
    response = requests.get(PROJECT_TEMPLATE_ZIP_URL)

    # Create a ZipFile object from the content of the response
    with zipfile.ZipFile(io.BytesIO(response.content)) as myzip:
        # Extract all contents of the zip file to the current directory
        myzip.extractall(project_dir)

    downloaded_template_dir_name = os.listdir(project_dir)[0]
    template_dir = os.path.join(project_dir, downloaded_template_dir_name)
    print(f"DOWNLOADED_TEMPLATE_DIR: {template_dir}")
    template_dir_contents = os.listdir(template_dir)
    for td_content in template_dir_contents:
        print(f"{td_content}")
        shutil.move(os.path.join(template_dir, td_content), project_dir)

    return template_dir


def copy_local_template_to_dir(copy_to_dir: os.PathLike):
    DIRS_TO_EXCLUDE = [".git", ".vscode", ".pio"]
    FILES_TO_EXCLUDE = [".git", ".gitignore"]

    template_source_dir = os.path.join(os.getcwd(), LOCAL_TEMPLATE_DIR)

    for c in os.listdir(template_source_dir):
        full_path = os.path.join(template_source_dir, c)
        if os.path.isdir(full_path):
            if c not in DIRS_TO_EXCLUDE:
                copy_to_dir_path = os.path.join(copy_to_dir, c)
                print(full_path)
                copy_tree(full_path, copy_to_dir_path)
        else:
            if c not in FILES_TO_EXCLUDE:
                copy_to_dir_path = os.path.join(copy_to_dir, c)
                qroma_copy_file(full_path, copy_to_dir_path)

    return copy_to_dir


def setup_project_template_directory() -> tempfile.TemporaryDirectory:
    temp_directory = tempfile.TemporaryDirectory(prefix="qroma-template-copy-dir-")

    if LOCAL_TEMPLATE_DIR:
        template_dir = copy_local_template_to_dir(temp_directory.name)
    else:
        template_dir = download_template_to_dir(temp_directory.name)

    print("SETUP TEMPLATE DIR: " + template_dir)

    return temp_directory


def remove_project_template_directory(template_temp_dir: tempfile.TemporaryDirectory):
    template_temp_dir.cleanup()


def setup_project_directory(qroma_project: QromaProject) -> os.PathLike:

    project_dir = qroma_project.project_dir

    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)

    os.makedirs(project_dir)

    if LOCAL_TEMPLATE_DIR:
        template_dir = copy_local_template_to_dir(project_dir)
    else:
        template_dir = download_template_to_dir(project_dir)

    print("SETUP PROJECT DIR: " + template_dir)

    # shutil.rmtree(template_dir)

    return project_dir
