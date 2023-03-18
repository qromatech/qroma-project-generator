import os.path

from utils import qroma_os_rename
from qroma_project import QromaProject
from qroma_types import GenerateProjectOptions
from qroma_enums import DeviceBoardPlatform
import qroma_dirs
from build_frameworks import build_arduino, build_platformio, include_header_generators


def convert_qroma_file_references(fpath, project_id):
    with open(fpath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('qroma-project', project_id)

    # Write the file out again
    with open(fpath, 'w') as file:
        file.write(filedata)


def update_board_dir_with_project_options(qroma_project: QromaProject, project_options: GenerateProjectOptions):
    project_dir, project_id = qroma_project.project_dir, qroma_project.project_id

    esp32_device_boards_dir = qroma_dirs.get_device_boards_esp_dir(qroma_project)
    print(f"ESP32 {esp32_device_boards_dir}")

    project_template_board_dir = os.path.join(esp32_device_boards_dir, "qroma-project")
    new_board_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    qroma_os_rename(project_template_board_dir, new_board_dir)

    project_template_ino_file_path = os.path.join(new_board_dir, "qroma-project.ino")
    new_project_ino_file_path = os.path.join(new_board_dir, f"{project_id}.ino")
    qroma_os_rename(project_template_ino_file_path, new_project_ino_file_path)

    project_template_src_project_id_path = os.path.join(new_board_dir, "src", "qroma-project")
    new_src_project_id_path = os.path.join(new_board_dir, "src", project_id)
    qroma_os_rename(project_template_src_project_id_path, new_src_project_id_path)

    include_header_generators.update_all_header_includes(qroma_project)

    if DeviceBoardPlatform.arduino in project_options.project_config.dev_board_platforms:
        include_header_generators.update_include_for_arduino_ino(qroma_project)
    else:
        build_arduino.remove_arduino_from_project_dir(qroma_project)

    if DeviceBoardPlatform.platformio not in project_options.project_config.dev_board_platforms:
        build_platformio.remove_platformio_from_project_dir(qroma_project)





def setup_device_project(qroma_project: QromaProject, project_options: GenerateProjectOptions):
    project_dir, project_id = qroma_project.project_dir, qroma_project.project_id

    # download_arduino_cli(project_dir)
    # init_arduino_project(project_dir, project_id)

    print(f"PROJECT DIR: {project_dir}")
    update_board_dir_with_project_options(qroma_project, project_options)
