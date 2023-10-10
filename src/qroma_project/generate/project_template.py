import os
import shutil
from distutils.dir_util import copy_tree
import requests
import zipfile
import io
import tempfile

import env_checks
from constants import PROJECT_TEMPLATE_ZIP_URL, REACT_QROMA_LIB_ZIP_URL
from utils import qroma_os_rmdir, qroma_copy_file


def download_template_to_dir(project_dir: os.PathLike) -> str:
    response = requests.get(PROJECT_TEMPLATE_ZIP_URL)
    project_site_dir = os.path.join(project_dir, 'sites', 'site-www-qroma-project')

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

    print(f"REMOVING TEMPLATE DIR: {template_dir}")
    qroma_os_rmdir(template_dir)

    # download react-qroma-lib and put it in place - https://github.com/qromatech/react-qroma-lib
    rql_response = requests.get(REACT_QROMA_LIB_ZIP_URL)
    rql_final_dir = os.path.join(project_site_dir, 'src', 'react-qroma-lib')
    rql_download_dir = os.path.join(project_site_dir, 'react-qroma-lib-download')

    # Create a ZipFile object from the content of the response
    with zipfile.ZipFile(io.BytesIO(rql_response.content)) as myzip:
        myzip.extractall(rql_download_dir)

    downloaded_rql_dir_name = os.listdir(rql_download_dir)[0]
    rql_dir = os.path.join(rql_download_dir, downloaded_rql_dir_name)
    print(f"DOWNLOADED_REACT_QROMA_LIB_DIR: {rql_dir}")
    rql_dir_contents = os.listdir(rql_dir)
    for td_content in rql_dir_contents:
        print(f"{td_content}")
        shutil.move(os.path.join(rql_dir, td_content), rql_final_dir)

    print(f"REMOVING QROMA REACT LIB DOWNLOAD DIR: {rql_download_dir}")
    qroma_os_rmdir(rql_download_dir)

    return template_dir


def copy_local_template_to_dir(copy_to_dir: os.PathLike):
    DIRS_TO_EXCLUDE = [".git", ".vscode", ".pio"]
    FILES_TO_EXCLUDE = [".git", ".gitignore"]

    template_source_dir = env_checks.get_local_template_source_dir()

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

    if env_checks.is_running_as_cli_executable():
        template_dir = download_template_to_dir(temp_directory.name)
    else:
        template_dir = copy_local_template_to_dir(temp_directory.name)

    print("SETUP TEMPLATE DIR: " + template_dir)

    return temp_directory


def remove_project_template_directory(template_temp_dir: tempfile.TemporaryDirectory):
    template_temp_dir.cleanup()

#
# def setup_project_directory(qroma_project: QromaProject) -> os.PathLike:
#
#     project_dir = qroma_project.project_dir
#
#     if os.path.exists(project_dir):
#         shutil.rmtree(project_dir)
#
#     os.makedirs(project_dir)
#
#     if LOCAL_TEMPLATE_DIR:
#         template_dir = copy_local_template_to_dir(project_dir)
#     else:
#         template_dir = download_template_to_dir(project_dir)
#
#     print("SETUP PROJECT DIR: " + template_dir)
#
#     # shutil.rmtree(template_dir)
#
#     return project_dir
