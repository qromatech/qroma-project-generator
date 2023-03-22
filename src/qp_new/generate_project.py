import os

import env_checks
from qroma_project.generate import template_processor, project_template
from qroma_project.qroma_project import QromaProject
from qroma_types import GenerateProjectOptions
from build_project import do_build_project
# from qp_config import save_qroma_project
from utils import qroma_os_rmdir, typer_show_to_user


def init_project_directory_from_project_template_directory(qroma_project: QromaProject,
                                                           generate_project_options: GenerateProjectOptions,
                                                           project_template_dir: os.PathLike,
                                                           ):
    project_dir = qroma_project.project_dir

    if generate_project_options and os.path.exists(project_dir):
        typer_show_to_user(f"REMOVING {qroma_project.project_dir}")
        qroma_os_rmdir(project_dir)

    template_processor.process_qroma_project_template_dir(qroma_project, generate_project_options, project_template_dir)

    print(f"PROJECT {qroma_project.project_id} INITIALIZED AT {qroma_project.project_dir}")

    # # use project ID to name Arduino project directory
    # device_boards.setup_device_project(qroma_project, generate_project_options)
    #
    # # setup web sites for interacting with project installed on board
    # # www_sites.do_docusaurus_setup(project_dir, project_id)
    # www_sites.setup_site_project(qroma_project)

    return project_dir


def do_generate_project(qroma_project: QromaProject, generate_project_options: GenerateProjectOptions) -> QromaProject:
    # project_id, project_root_dir = qroma_project.project_id, qroma_project.project_root_dir
    project_id = qroma_project.project_id

    # check to see if you have docker, pio, and npm installed
    env_checks.do_env_checks()

    # download and unzip template contents from https://github.com/qromatech/qroma-project-template
    template_directory = project_template.setup_project_template_directory()

    project_dir = init_project_directory_from_project_template_directory(
        qroma_project, generate_project_options, template_directory.name)

    project_template.remove_project_template_directory(template_directory)
    #
    # if getattr(sys, 'frozen', False):
    #     # If the application is run as a bundle, the PyInstaller bootloader
    #     # extends the sys module by a flag frozen=True and sets the app
    #     # path into variable _MEIPASS'.
    #     print("QROMA-CLI PATH")
    #     print(sys.executable)
    #     project_app_path = os.path.join(project_dir, "qroma.exe")
    #     print(project_app_path)
    #
    # else:
    #     print("RUNNING FROM PYTHON EXECUTABLE, NOT AS CLI APP")

    this_project: QromaProject = QromaProject(project_dir, project_id)
    this_project.set_config(generate_project_options.project_config)
    # save_qroma_project(this_project)

    do_build_project(qroma_project=this_project,
                     build_parameters=generate_project_options.build_parameters,
                     )

    return this_project
