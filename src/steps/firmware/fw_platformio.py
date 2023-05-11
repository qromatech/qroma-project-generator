from qroma_enums import FirmwareFramework
from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
import command_handler


def do_build(user_profile: QromaUserProfile, qroma_project: QromaProject):
    build_command = user_profile.tools.firmware_platforms.platformio.build_command
    dir_path = qroma_project.config.qroma.project.dirs.firmware_root
    command_handler.do_firmware_build(FirmwareFramework.platformio, build_command, dir_path)


def do_upload(user_profile: QromaUserProfile, qroma_project: QromaProject):
    upload_command = user_profile.tools.firmware_platforms.platformio.upload_command
    dir_path = qroma_project.config.qroma.project.dirs.firmware_root
    command_handler.do_firmware_upload(FirmwareFramework.platformio, upload_command, dir_path)
