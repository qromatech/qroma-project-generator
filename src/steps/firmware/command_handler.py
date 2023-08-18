import subprocess

from qroma_enums import FirmwareFramework
from utils import typer_progress_message, typer_show_to_user


def do_firmware_build(platform: FirmwareFramework, build_command: str, firmware_dir: str):
    build_command_parts = build_command.split(" ")

    with typer_progress_message(f"RUNNING BUILD FOR {platform}"):
        typer_show_to_user("ARGS: " + build_command)
        typer_show_to_user("PATH: " + firmware_dir)

    subprocess.run(build_command_parts, shell=True, cwd=firmware_dir)


def do_firmware_upload(platform: FirmwareFramework, upload_command: str, firmware_dir: str):
    upload_command_parts = upload_command.split(' ')

    with typer_progress_message(f"RUNNING UPLOAD FOR {platform}"):
        typer_show_to_user("ARGS: " + upload_command)
        typer_show_to_user("PATH: " + firmware_dir)

        subprocess.run(upload_command_parts, shell=True, cwd=firmware_dir)
