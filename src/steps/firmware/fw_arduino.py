import os
import subprocess

from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile


def build_arduino(user_profile: QromaUserProfile, qroma_project: QromaProject):
    arduino_exe = user_profile.commands.firmware.arduino.arduino_exe
    build_command = user_profile.commands.firmware.arduino.build_command

    dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)

    subprocess.run([arduino_exe, build_command], shell=True, cwd=dir_path)


def upload_arduino(user_profile: QromaUserProfile, qroma_project: QromaProject):
    arduino_exe = user_profile.commands.firmware.arduino.arduino_exe
    upload_command = user_profile.commands.firmware.arduino.upload_command

    dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)

    subprocess.run([arduino_exe, upload_command], shell=True, cwd=dir_path)


# def get_firmware_file_path(qroma_project):
#     return "Not implemented yet"
#     return None
