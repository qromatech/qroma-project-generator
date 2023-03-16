import os.path

from utils import qroma_os_rename, qroma_os_remove
from qroma_project import QromaProject
from qroma_types import GenerateProjectOptions
from qroma_enums import DeviceBoardPlatform
import qroma_dirs


def convert_qroma_file_references(fpath, project_id):
    with open(fpath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('qroma-project', project_id)

    # Write the file out again
    with open(fpath, 'w') as file:
        file.write(filedata)


def remove_platformio_from_project_dir(qroma_project: QromaProject):
    esp32_device_board_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    print("REMOVING PLATFORMIO FROM ESP32 DEVICE BOARD DIR: " + esp32_device_board_dir)

    qroma_os_remove(os.path.join(esp32_device_board_dir, "platformio.ini"))
    qroma_os_remove(os.path.join(esp32_device_board_dir, "src", "main.cpp"))


def update_board_dir_with_project_options(qroma_project: QromaProject, project_options: GenerateProjectOptions):
    project_dir, project_id = qroma_project.project_dir, qroma_project.project_id

    esp32_device_boards_dir = qroma_dirs.get_device_boards_esp_dir(qroma_project)
    print(f"ESP32 {esp32_device_boards_dir}")

    project_template_board_dir = os.path.join(esp32_device_boards_dir, "qroma-project")
    new_board_dir = os.path.join(esp32_device_boards_dir, project_id)
    qroma_os_rename(project_template_board_dir, new_board_dir)

    project_template_ino_file_path = os.path.join(new_board_dir, "qroma-project.ino")
    new_project_ino_file_path = os.path.join(new_board_dir, f"{project_id}.ino")
    qroma_os_rename(project_template_ino_file_path, new_project_ino_file_path)

    if DeviceBoardPlatform.arduino in project_options.project_config.dev_board_platforms:
        print("RENAMING INO")
        new_ino_file_path = os.path.join(new_board_dir, f"{project_id}.ino")
        qroma_os_rename(new_project_ino_file_path, new_ino_file_path)
    else:
        print("REMOVING INO")
        qroma_os_remove(new_project_ino_file_path)

    if DeviceBoardPlatform.platformio not in project_options.project_config.dev_board_platforms:
        remove_platformio_from_project_dir(qroma_project)


def install_to_pio_device_board():
    pass
    # run --target upload --environment esp32dev


def install_to_arduino_device_board():
    pass


def setup_device_project(qroma_project: QromaProject, project_options: GenerateProjectOptions):
    project_dir, project_id = qroma_project.project_dir, qroma_project.project_id

    # download_arduino_cli(project_dir)
    # init_arduino_project(project_dir, project_id)

    print(f"PROJECT DIR: {project_dir}")
    update_board_dir_with_project_options(qroma_project, project_options)
