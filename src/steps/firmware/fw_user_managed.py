import subprocess

from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from utils import typer_progress_message, typer_show_to_user


def do_build(user_profile: QromaUserProfile, qroma_project: QromaProject):
    build_command_parts = user_profile.commands.firmware.user_managed.build_command.split(" ")

    dir_path = qroma_project.config.qroma.project.dirs.firmware_root

    with typer_progress_message("RUNNING USER MANAGED BUILD"):
        typer_show_to_user("ARGS: " + user_profile.commands.firmware.user_managed.build_command)
        typer_show_to_user("PATH: " + dir_path)

        subprocess.run(build_command_parts, shell=True, cwd=dir_path)


def do_upload(user_profile: QromaUserProfile, qroma_project: QromaProject):
    upload_command_parts = user_profile.commands.firmware.user_managed.upload_command.split(" ")

    dir_path = qroma_project.config.qroma.project.dirs.firmware_root

    with typer_progress_message("RUNNING PLATFORMIO UPLOAD"):
        typer_show_to_user("ARGS: " + user_profile.commands.firmware.user_managed.upload_command)
        typer_show_to_user("PATH: " + dir_path)

        subprocess.run([upload_command_parts, *upload_command_parts], shell=True, cwd=dir_path)
