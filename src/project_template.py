import os
import shutil
import requests
import zipfile
import io
from pathlib import Path

from constants import PROJECT_TEMPLATE_ZIP_URL
from config import LOCAL_TEMPLATE_DIR
from qroma_project import QromaProject
from generate_project import GenerateProjectOptions

home_dir = Path.home()
QROMA_DEFAULT_PROJECT_ROOT_DIR = os.path.join(home_dir, "qroma-projects")
QROMA_DEFAULT_PROJECT_ID_PREFIX = ":"

VALID_PROJECT_ID_CHARS = "abcdefghijklmnopqrstuvwxyz" + \
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
                         "0123456789-_"


class NewQromaProjectException(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_qroma_project_for_user_supplied_project_id(user_project_id) -> QromaProject:
    project_id = user_project_id
    project_root_dir = os.getcwd()

    if user_project_id.startswith(QROMA_DEFAULT_PROJECT_ID_PREFIX):
        project_id = user_project_id[1:]
        project_root_dir = QROMA_DEFAULT_PROJECT_ROOT_DIR

    if not is_valid_project_id(project_id):
        raise NewQromaProjectException(f"Invalid project ID: {project_id}")

    return QromaProject(
        project_root_dir,
        project_id,
    )


def is_valid_project_id(project_id: str) -> bool:
    trimmed_project_id = project_id.strip()
    for c in trimmed_project_id:
        if c not in VALID_PROJECT_ID_CHARS:
            return False

    return True


# def validate_project_id(project_id: str) -> str:
#     trimmed_project_id = project_id.strip()
#     for c in trimmed_project_id:
#         if c not in VALID_PROJECT_ID_CHARS:
#             return ""
#
#     return trimmed_project_id

#
# def validate_project_root_dir(project_root_dir: str) -> os.PathLike:
#     pass
#
#
# def get_project_id_from_user() -> str:
#     project_id_complete = False
#
#     while not project_id_complete:
#         project_id = input("Please enter a project ID >>> ")
#         print(f"You entered projectId: {project_id}")
#         validated_project_id = validate_project_id(project_id)
#         if validated_project_id != "":
#             project_id_complete = True
#         # project_dir = os.path.join(project_root_dir, project_id)
#         # if os.path.exists(project_dir):
#         #     print(f"A directory at '{project_dir}' already exists. Delete this directory or come up with a different "
#         #           "project ID.")
#         # else:
#         #     project_id_complete = True
#
#             return validated_project_id


def get_project_root_dir(project_id: str) -> str:
    print("GETTING PROJECT DIR 2")
    project_root_dir = ""
    project_dir_complete = False
    x = 1

    # while not os.path.isdir(project_root_dir):
    while not project_dir_complete:
        user_entered_project_dir = input(
            f"{x}: Enter a period (.) to create your project in the current " +
            f"directory or leave blank to use '{QROMA_DEFAULT_PROJECT_ROOT_DIR}' >>> "
        )
        print(f">>> {user_entered_project_dir}")

        if user_entered_project_dir.strip() == '.':
            print("USE CWD")
            project_root_dir = os.getcwd()
        elif user_entered_project_dir.strip() == '':
            print("USE DEFAULT")
            project_root_dir = QROMA_DEFAULT_PROJECT_ROOT_DIR
            # if not os.path.exists(QROMA_PROJECT_ROOT_DIR):
            #     os.makedirs(QROMA_PROJECT_ROOT_DIR)

        print("USER ENTERED: " + user_entered_project_dir)

        project_dir = os.path.join(project_root_dir, project_id)
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
            project_dir_complete = True
        else:
            print(
                f"A directory at '{project_dir}' already exists. Delete this directory or come up with a different "
                "project ID.")

        x += 1

    return project_root_dir


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


def copy_local_template_to_dir(project_dir: os.PathLike) -> str:
    copy_to_dir = os.path.join(project_dir, "template-copy")
    shutil.copytree(os.path.join(os.getcwd(), LOCAL_TEMPLATE_DIR),
                    copy_to_dir)

    copied_template_dir_name = os.listdir(project_dir)[0]
    template_dir = os.path.join(project_dir, copied_template_dir_name)
    print(f"COPIED_TEMPLATE_DIR: {template_dir}")
    template_dir_contents = os.listdir(template_dir)
    for td_content in template_dir_contents:
        print(f"{td_content}")
        shutil.move(os.path.join(template_dir, td_content), project_dir)

    return copy_to_dir


# def setup_project_directory(project_id: str, project_root_dir: Union[str, os.PathLike]) -> os.PathLike:
def setup_project_directory(qroma_project: QromaProject, project_options: GenerateProjectOptions) -> os.PathLike:

    project_dir = qroma_project.project_dir

    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)

    os.makedirs(project_dir)

    if LOCAL_TEMPLATE_DIR:
        template_dir = copy_local_template_to_dir(project_dir)
    else:
        template_dir = download_template_to_dir(project_dir)

    shutil.rmtree(template_dir)

    return project_dir
