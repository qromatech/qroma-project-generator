import os

import env_checks
from qroma_project.generate import template_processor, project_template
from qroma_types import GenerateProjectOptions
from utils import qroma_os_rmdir, typer_show_to_user


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

    # # use project ID to name Arduino project directory
    # device_boards.setup_device_project(qroma_project, generate_project_options)
    #
    # # setup web sites for interacting with project installed on board
    # # www_sites.do_docusaurus_setup(project_dir, project_id)
    # www_sites.setup_site_project(qroma_project)

    return project_dir


def do_generate_project_structure(generate_project_options: GenerateProjectOptions):
    # check to see if tools installed (e.g. docker, pio, npm, etc.)
    env_checks.do_env_checks()

    # download and unzip template contents from https://github.com/qromatech/qroma-project-template
    template_directory = project_template.setup_project_template_directory()

    init_project_directory_from_project_template_directory(
        generate_project_options, template_directory.name)

    project_template.remove_project_template_directory(template_directory)
