import os
from typing import Optional

import typer

from qroma_enums import FirmwareFramework, ExitReason
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project import user_input
from steps.firmware import fw_platformio, fw_arduino
from utils import qroma_edit_dir

app = typer.Typer(help="Qroma firmware management commands")


@app.command()
def edit(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    edit_dir_path = os.path.join(qroma_project.project_dir, "firmware", "esp32", qroma_project.project_id)
    qroma_edit_dir(edit_dir_path)


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

    print("In firmware upload - not yet implemented")


# @app.command()
# def build(project_id: Optional[str] = typer.Argument(None,
#                                                      # callback=typer_validate_existing_project_id_from_user_project_id
#                                                      ),
#           pb: bool = typer.Option(False, help="Compile protobufs as part of build (equivalent to running 'protobuf')."),
#           ):
#     """
#     Build Qroma software for this project. Provide no arguments to build the Qroma project in
#     the current directory. Use ':' before the project_id to build a project in the global 'qroma-projects' directory.
#     """
#     qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
#
#     typer_show_to_user("Building Qroma software")
#
#     build_parameters = create_build_parameters_with_all_steps_enabled()
#     build_parameters.include_pb = pb
#
#     do_build_project(qroma_project, build_parameters)
#
#     typer_show_to_user("Done building Qroma software")