import typer

from qroma_enums import FirmwareFramework, ExitReason
from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from steps.firmware import fw_platformio, fw_user_managed


def get_firmware_platform_for_framework(framework: FirmwareFramework):
    if framework == FirmwareFramework.platformio:
        return fw_platformio
    elif framework == FirmwareFramework.user_managed:
        return fw_user_managed
    else:
        print("Unrecognized framework: " + framework)
        typer.Exit(ExitReason.INVALID_USER_FW_PLATFORM.value)
    

def run_firmware_build_step(qroma_project: QromaProject, user_profile: QromaUserProfile):
    user_platforms = user_profile.defaults.tools.firmware_platforms
    project_platforms = qroma_project.config.qroma.project.firmware.platforms

    selected_platform = None
    for p in user_platforms:
        if p in project_platforms:
            selected_platform = p
            break

    fp = get_firmware_platform_for_framework(selected_platform)

    fp.do_build(user_profile, qroma_project)


def run_firmware_upload_step(qroma_project, user_profile):
    user_platforms = user_profile.defaults.tools.firmware_platforms
    project_platforms = qroma_project.config.qroma.project.firmware.platforms

    selected_platform = None
    for p in user_platforms:
        if p in project_platforms:
            selected_platform = p
            break

    fp = get_firmware_platform_for_framework(selected_platform)

    fp.do_upload(user_profile, qroma_project)
    