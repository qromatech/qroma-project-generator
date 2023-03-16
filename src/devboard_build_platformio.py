import os
import subprocess

from qroma_project import QromaProject
import qroma_dirs
from utils import qroma_os_remove, qroma_os_move_file_to_dir, typer_show_to_user


def remove_platformio_from_project_dir(qroma_project: QromaProject):
    esp32_device_board_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    typer_show_to_user("REMOVING PLATFORMIO FROM ESP32 DEVICE BOARD DIR: " + esp32_device_board_dir)

    qroma_os_remove(os.path.join(esp32_device_board_dir, "platformio.ini"))
    qroma_os_remove(os.path.join(esp32_device_board_dir, "src", "main.cpp"))


def move_files_from_main_dir_into_src_main_project_dir(qroma_project: QromaProject):
    typer_show_to_user("MOVING PLATFORMIO FILES TO SRC PROJECT DIRECTORY")

    esp32_device_board_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    esp32_device_src_dir = os.path.join(esp32_device_board_dir, "src")
    esp32_device_src_project_dir = os.path.join(esp32_device_board_dir, "src", qroma_project.project_id)
    os.mkdir(esp32_device_src_project_dir)

    qroma_os_move_file_to_dir(os.path.join(esp32_device_src_dir, "qroma-project.h"), esp32_device_src_project_dir)
    qroma_os_move_file_to_dir(os.path.join(esp32_device_src_dir, "qroma-project.cpp"), esp32_device_src_project_dir)


def install_firmware_onto_pio_device_board(qroma_project: QromaProject):
    cwd_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    print("RUNNING BUILD ESP 32 PROJECT SUBPROCESS")
    subprocess.run(["pio", "run"], shell=True, cwd=cwd_dir)
    print("DONE RUNNING BUILD PROJECT SUBPROCESS")

    # run --target upload --environment esp32dev
