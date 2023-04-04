import os
from typing import Optional

import typer

from qroma_enums import FirmwareFramework, ExitReason
from qroma_infra.qroma_editor import open_firmware_editor
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project import user_input
from steps.firmware import fw_platformio, fw_arduino


app = typer.Typer(help="Qroma firmware management commands")


@app.command()
def edit(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    open_firmware_editor(qroma_project)


@app.command()
def build(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    user_default_firmware_platform = user_profile.defaults.tools.firmware_platform
    if user_default_firmware_platform == FirmwareFramework.platformio:
        fw_platformio.build_platformio(user_profile, qroma_project)

    elif user_default_firmware_platform == FirmwareFramework.arduino:
        fw_arduino.build_arduino(user_profile, qroma_project)

    else:
        print("Unable to build project - unsupported platform: " + user_default_firmware_platform)
        typer.Exit(ExitReason.INVALID_USER_FW_PLATFORM.value)


@app.command()
def upload(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    user_profile = load_qroma_user_profile()

    user_default_firmware_platform = user_profile.defaults.tools.firmware_platform
    if user_default_firmware_platform == FirmwareFramework.platformio:
        fw_platformio.upload_platformio(user_profile, qroma_project)

    elif user_default_firmware_platform == FirmwareFramework.arduino:
        fw_arduino.upload_arduino(user_profile, qroma_project)

    else:
        print("Unable to build project - unsupported platform: " + user_default_firmware_platform)
        typer.Exit(ExitReason.INVALID_USER_FW_PLATFORM.value)
