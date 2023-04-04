import os.path
import subprocess

from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from utils import typer_progress_message, typer_show_to_user


def build_platformio(user_profile: QromaUserProfile, qroma_project: QromaProject):
    platformio_exe = user_profile.commands.firmware.platformio.platformio_exe
    build_command = user_profile.commands.firmware.platformio.build_command

    dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)

    with typer_progress_message("RUNNING PLATFORMIO BUILD"):
        typer_show_to_user("EXEC: " + platformio_exe)
        typer_show_to_user("ARGS: " + user_profile.commands.firmware.platformio.build_command)
        typer_show_to_user("PATH: " + dir_path)

        subprocess.run([platformio_exe, build_command], shell=True, cwd=dir_path)


def upload_platformio(user_profile: QromaUserProfile, qroma_project: QromaProject):
    platformio_exe = user_profile.commands.firmware.platformio.platformio_exe
    upload_command_parts = user_profile.commands.firmware.platformio.upload_command.split(' ')

    dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)

    with typer_progress_message("RUNNING PLATFORMIO UPLOAD"):
        typer_show_to_user("EXEC: " + platformio_exe)
        typer_show_to_user("ARGS: " + user_profile.commands.firmware.platformio.upload_command)
        typer_show_to_user("PATH: " + dir_path)

        subprocess.run([platformio_exe, *upload_command_parts], shell=True, cwd=dir_path)
