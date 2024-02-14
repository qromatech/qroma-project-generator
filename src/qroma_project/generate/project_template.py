import hashlib
import os
import shutil
import requests
import zipfile
import io
import tempfile

import typer

import config
import env_checks
# from constants import PROJECT_TEMPLATE_ZIP_URL, REACT_QROMA_LIB_ZIP_URL
from config import QROMA_PROJECT_TEMPLATE_ZIP_URL, REACT_QROMA_LIB_ZIP_URL
from qroma_enums import ExitReason
from utils import qroma_os_rmdir


def download_template_to_dir(project_dir: os.PathLike) -> str:
    response = requests.get(QROMA_PROJECT_TEMPLATE_ZIP_URL)
    project_site_dir = os.path.join(project_dir, 'sites', 'www-qroma-project')

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


def unzip_local_templates_to_dir(project_dir: os.PathLike) -> str:
    project_site_dir = os.path.join(project_dir, 'sites', 'www-qroma-project')

    qroma_project_template_zip_path = env_checks.get_local_template_zip_resource_path(
        config.LOCAL_TEMPLATE_QROMA_PROJECT_ZIP_FILENAME)
    react_qroma_lib_zip_path = env_checks.get_local_template_zip_resource_path(
        config.LOCAL_TEMPLATE_REACT_QROMA_LIB_ZIP_FILENAME)

    # Extract ZipFile from the project template zip
    qroma_project_template_zip_f = open(qroma_project_template_zip_path, "rb")
    with zipfile.ZipFile(qroma_project_template_zip_f) as myzip:
        myzip.extractall(project_dir)

    downloaded_template_dir_name = os.listdir(project_dir)[0]
    template_dir = os.path.join(project_dir, downloaded_template_dir_name)
    template_dir_contents = os.listdir(template_dir)
    for td_content in template_dir_contents:
        print(f"{td_content}")
        shutil.move(os.path.join(template_dir, td_content), project_dir)

    qroma_os_rmdir(template_dir)

    # download react-qroma-lib and put it in place - https://github.com/qromatech/react-qroma-lib
    rql_final_dir = os.path.join(project_site_dir, 'src', 'react-qroma-lib')
    rql_download_dir = os.path.join(project_site_dir, 'react-qroma-lib-extract')

    # Extract ZipFile object from react-qroma-lib zip
    react_qroma_lib_zip_f = open(react_qroma_lib_zip_path, "rb")
    with zipfile.ZipFile(react_qroma_lib_zip_f) as myzip:
        myzip.extractall(rql_download_dir)

    downloaded_rql_dir_name = os.listdir(rql_download_dir)[0]
    rql_dir = os.path.join(rql_download_dir, downloaded_rql_dir_name)
    rql_dir_contents = os.listdir(rql_dir)
    for td_content in rql_dir_contents:
        print(f"{td_content}")
        shutil.move(os.path.join(rql_dir, td_content), rql_final_dir)

    qroma_os_rmdir(rql_download_dir)

    return template_dir


def download_template_zips_and_compare_to_local_versions():
    for template_source_zip_local_filename, template_zip_url in config.TEMPLATE_SOURCE_ZIP_URLS_AND_LOCAL_FILENAMES:
        template_zip_download_bytes = requests.get(template_zip_url).content
        download_bytes_file_like_object = io.BytesIO(template_zip_download_bytes)
        zip_download_hash = hashlib.file_digest(download_bytes_file_like_object, 'sha256').hexdigest()

        zip_filepath = env_checks.get_local_template_zip_resource_path(template_source_zip_local_filename)

        if not os.path.exists(zip_filepath):
            with open(zip_filepath, "wb") as zip_to_save:
                zip_to_save.write(template_zip_download_bytes)
                print(f"DOWNLOADING AND SAVING '{template_zip_url}' TO {zip_filepath}")

        zip_file = open(zip_filepath, "rb", buffering=0)
        zip_file_hash = hashlib.file_digest(zip_file, 'sha256').hexdigest()

        if zip_download_hash != zip_file_hash:
            # if this becomes a hassle, we could add a flag to command line to force ignore or
            # prompt via typer right here
            print(f"Zip download hash and local file hash don't match for "
                             f"{template_source_zip_local_filename} / {template_zip_url}")
            raise typer.Exit(ExitReason.TEMPLATE_FILES_MISMATCH.value)


            # what_to_do = typer.prompt("Type 'dl' to use downloaded template")
            # if what_to_do != "dl":
            #     raise typer.Exit(ExitReason.TEMPLATE_FILES_MISMATCH.value)


def setup_project_template_directory() -> tempfile.TemporaryDirectory:
    temp_directory = tempfile.TemporaryDirectory(prefix="qroma-template-copy-dir-")

    if env_checks.is_running_as_cli_executable():
        template_dir = download_template_to_dir(temp_directory.name)
    else:
        download_template_zips_and_compare_to_local_versions()
        template_dir = unzip_local_templates_to_dir(temp_directory.name)

    print("SETUP TEMPLATE DIR: " + template_dir)

    return temp_directory


def remove_project_template_directory(template_temp_dir: tempfile.TemporaryDirectory):
    template_temp_dir.cleanup()
