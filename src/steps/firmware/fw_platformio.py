import os.path
import subprocess

from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile


def build_platformio(user_profile: QromaUserProfile, qroma_project: QromaProject):
    platformio_exe = user_profile.commands.firmware.platformio.platformio_exe
    build_command = user_profile.commands.firmware.platformio.build_command

    dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)

    subprocess.run([platformio_exe, build_command], shell=True, cwd=dir_path)


def upload_platformio(user_profile: QromaUserProfile, qroma_project: QromaProject):
    platformio_exe = user_profile.commands.firmware.platformio.platformio_exe
    upload_command_parts = user_profile.commands.firmware.platformio.upload_command.split(' ')

    dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)

    subprocess.run([platformio_exe, *upload_command_parts], shell=True, cwd=dir_path)
