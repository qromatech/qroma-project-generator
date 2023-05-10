import typer

from qroma_enums import FirmwareFramework, ExitReason
from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from steps.firmware import fw_platformio, fw_arduino, fw_user_handled


def get_firmware_platform_for_framework(framework: FirmwareFramework):
    if framework == FirmwareFramework.platformio:
        return fw_platformio
    elif framework == FirmwareFramework.user_handled:
        return fw_user_handled
    else:
        print("Unrecognized framwork: " + framework)
        typer.Exit(ExitReason.INVALID_USER_FW_PLATFORM.value)

    # user_default_firmware_platform = user_profile.defaults.tools.firmware_platform
    # if user_default_firmware_platform == FirmwareFramework.platformio:
    #     fw_platformio.build_platformio(user_profile, qroma_project)

    # elif user_default_firmware_platform == FirmwareFramework.arduino:
    #     fw_arduino.build_arduino(user_profile, qroma_project)

    # else:
    #     print("Unable to build project - unsupported platform: " + user_default_firmware_platform)
    #     typer.Exit(ExitReason.INVALID_USER_FW_PLATFORM.value)
    

def run_firmware_build_step(qroma_project: QromaProject, user_profile: QromaUserProfile):
    user_default_firmware_platform = user_profile.defaults.tools.firmware_platform
    fp = get_firmware_platform_for_framework(user_default_firmware_platform)

    fp.do_build(user_profile, qroma_project)

    # if user_default_firmware_platform == FirmwareFramework.platformio:
    #     fw_platformio.build_platformio(user_profile, qroma_project)

    # elif user_default_firmware_platform == FirmwareFramework.arduino:
    #     fw_arduino.build_arduino(user_profile, qroma_project)

    # else:
    #     print("Unable to build project - unsupported platform: " + user_default_firmware_platform)
    #     typer.Exit(ExitReason.INVALID_USER_FW_PLATFORM.value)


def run_firmware_upload_step(qroma_project, user_profile):
    user_default_firmware_platform = user_profile.defaults.tools.firmware_platform
    fp = get_firmware_platform_for_framework(user_default_firmware_platform)

    fp.do_upload(user_profile, qroma_project)

    # if user_default_firmware_platform == FirmwareFramework.platformio:
    #     fw_platformio.upload_platformio(user_profile, qroma_project)

    # elif user_default_firmware_platform == FirmwareFramework.arduino:
    #     fw_arduino.upload_arduino(user_profile, qroma_project)

    # else:
    #     print("Unable to build project - unsupported platform: " + user_default_firmware_platform)
    #     typer.Exit(ExitReason.INVALID_USER_FW_PLATFORM.value)
