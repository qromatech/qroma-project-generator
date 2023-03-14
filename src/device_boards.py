import os.path

import requests
import zipfile
import io
import subprocess

# from constants import ARDUINO_CLI_ZIP_WIN64_URL
#
#
# def download_arduino_cli(project_dir: str):
#     response = requests.get(ARDUINO_CLI_ZIP_WIN64_URL)
#
#     # Create a ZipFile object from the content of the response
#     with zipfile.ZipFile(io.BytesIO(response.content)) as myzip:
#         # Extract all contents of the zip file to the current directory
#         myzip.extractall(project_dir)
#
#
# def init_arduino_project(project_dir, project_id):
#     ARDUINO_CLI_PATH = os.path.join(os.getcwd(), "arduino-cli")
#     DEVICE_BOARDS_DIR = os.path.join(os.getcwd(), "device-boards")
#     print(DEVICE_BOARDS_DIR)
#     print(ARDUINO_CLI_PATH)
#     subprocess.run([ARDUINO_CLI_PATH, "sketch", "new", project_id], cwd=DEVICE_BOARDS_DIR)


def convert_qroma_file_references(fpath, project_id):
    # Read in the file
    with open(fpath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('qroma-project', project_id)

    # Write the file out again
    with open(fpath, 'w') as file:
        file.write(filedata)


def update_arduino_project_dir(project_dir: os.PathLike, project_id):
    esp32_arduino_device_board_dir = os.path.join(project_dir, "device-boards", "esp32")
    print(f"ESP32 {esp32_arduino_device_board_dir}")
    project_template_board_dir = os.path.join(esp32_arduino_device_board_dir, "qroma-project")
    new_sketch_dir = os.path.join(esp32_arduino_device_board_dir, project_id)
    os.rename(project_template_board_dir, new_sketch_dir)

    # new_ino_file_path = os.path.join(new_sketch_dir, f"{project_id}.ino")
    # os.rename(os.path.join(new_sketch_dir, "qroma-project.ino"),
    #           new_ino_file_path)
    # convert_qroma_file_references(new_ino_file_path, project_id)
    #
    # new_src_h_file_path = os.path.join(new_sketch_dir, "src", f"{project_id}.h")
    # os.rename(os.path.join(new_sketch_dir, "src", "qroma-project.h"),
    #           new_src_h_file_path)
    # convert_qroma_file_references(new_src_h_file_path, project_id)
    #
    # new_src_cpp_file_path = os.path.join(new_sketch_dir, "src", f"{project_id}.cpp")
    # os.rename(os.path.join(new_sketch_dir, "src", "qroma-project.cpp"),
    #           new_src_cpp_file_path)
    # convert_qroma_file_references(new_src_cpp_file_path, project_id)


def setup_device_project(project_dir: os.PathLike, project_id):
    # download_arduino_cli(project_dir)
    # init_arduino_project(project_dir, project_id)
    print(f"PROJECT DIR: {project_dir}")
    update_arduino_project_dir(project_dir, project_id)
