import os

import env_checks
from qroma_project.generate import template_processor, project_template
from qroma_project.qroma_project import QromaProject
from qroma_types import GenerateProjectOptions
from utils import qroma_os_rmdir, typer_show_to_user, qroma_os_remove


def init_project_directory_from_project_template_directory(generate_project_options: GenerateProjectOptions,
                                                           project_template_dir: os.PathLike,
                                                           ):
    project_dir = generate_project_options.project_config_user_inputs.project_info.project_dir
    project_id = generate_project_options.project_config_user_inputs.project_info.project_id

    if generate_project_options and os.path.exists(project_dir):
        typer_show_to_user(f"REMOVING {project_dir}")
        qroma_os_rmdir(project_dir)

    template_processor.process_qroma_project_template_dir(generate_project_options, project_template_dir)

    print(f"PROJECT {project_id} INITIALIZED AT {project_dir}")

    qroma_project_template_zip_path = os.path.join(project_dir, "qroma-project-template.zip")
    if os.path.exists(qroma_project_template_zip_path):
        qroma_os_remove(qroma_project_template_zip_path)

    react_qroma_lib_zip_path = os.path.join(project_dir, "react-qroma-lib.zip")
    if os.path.exists(react_qroma_lib_zip_path):
        qroma_os_remove(react_qroma_lib_zip_path)

    return project_dir


def do_generate_project_structure(generate_project_options: GenerateProjectOptions):
    # check to see if tools installed (e.g. docker, pio, npm, etc.)
    env_checks.do_env_checks()

    # download and unzip template contents from https://github.com/qromatech/qroma-project-template
    template_directory = project_template.setup_project_template_directory()

    project_dir = init_project_directory_from_project_template_directory(
        generate_project_options, template_directory.name)

    project_template.remove_project_template_directory(template_directory)

    # Arduino requires .ino files to have a parent directory with the same name as the file itself :shrug:
    project_template.rename_qroma_project_arduino_file_to_parent_dir_name(
        project_id=generate_project_options.project_config_user_inputs.project_info.project_id,
        project_dir=project_dir
    )
