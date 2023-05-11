import command_handler
import prompt_handler
from qroma_enums import FirmwareFramework
from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from utils import typer_show_to_user


def do_build(user_profile: QromaUserProfile, qroma_project: QromaProject):
    firmware_root_dir = qroma_project.config.qroma.project.dirs.firmware_root

    build_prompt = user_profile.tools.firmware_platforms.user_managed.build_prompt
    if build_prompt:
        prompt_handler.do_firmware_build_prompt(build_prompt, firmware_root_dir)
        return

    build_command = user_profile.tools.firmware_platforms.user_managed.build_command
    if build_command:
        command_handler.do_firmware_build(FirmwareFramework.user_managed, build_command, firmware_dir=firmware_root_dir)
        return

    typer_show_to_user("NO BUILD INFO FOR USER MANAGED FIRMWARE PROCESS")


def do_upload(user_profile: QromaUserProfile, qroma_project: QromaProject):
    firmware_root_dir = qroma_project.config.qroma.project.dirs.firmware_root

    upload_prompt = user_profile.tools.firmware_platforms.user_managed.upload_prompt
    if upload_prompt:
        prompt_handler.do_firmware_upload_prompt(upload_prompt, firmware_root_dir)
        return

    upload_command = user_profile.tools.firmware_platforms.user_managed.upload_command
    if upload_command:
        command_handler.do_firmware_upload(FirmwareFramework.user_managed, upload_command, firmware_dir=firmware_root_dir)
        return

    typer_show_to_user("NO UPLOAD INFO FOR USER MANAGED FIRMWARE PROCESS")
