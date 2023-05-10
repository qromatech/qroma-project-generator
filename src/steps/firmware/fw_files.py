from qroma_enums import FirmwareFramework
from qroma_infra.qroma_infrastructure import load_qroma_user_profile
from qroma_project.qroma_project import QromaProject
from steps.firmware import fw_platformio, fw_arduino


# def get_firmware_file_path(qroma_project: QromaProject):
#     user_profile = load_qroma_user_profile()
#     user_default_firmware_platform = user_profile.defaults.tools.firmware_platform

#     if user_default_firmware_platform == FirmwareFramework.platformio:
#         return fw_platformio.get_firmware_file_path(qroma_project)

#     elif user_default_firmware_platform == FirmwareFramework.arduino:
#         return fw_arduino.get_firmware_file_path(qroma_project)

#     else:
#         return None
