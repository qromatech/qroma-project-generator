import os

from qroma_project import QromaProject
import qroma_dirs
from utils import qroma_os_remove


def remove_arduino_from_project_dir(qroma_project: QromaProject):
    print("REMOVING INO")
    devboard_esp_project_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    project_ino_file_path = os.path.join(devboard_esp_project_dir, f"{qroma_project.project_id}.ino")
    qroma_os_remove(project_ino_file_path)





def install_firmware_onto_arduino_device_board():
    pass