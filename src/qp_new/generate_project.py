import sys, os
from pathlib import Path

import env_checks, www_sites
from qp_new import project_template
from build_frameworks import device_boards
from qroma_project import QromaProject, save_qroma_project
from qroma_types import GenerateProjectOptions
from build_project import do_build_project


def do_generate_project(qroma_project: QromaProject, generate_project_options: GenerateProjectOptions) -> QromaProject:
    project_id, project_root_dir = qroma_project.project_id, qroma_project.project_root_dir

    # check to see if you have docker, pio, and npm installed
    env_checks.do_env_checks()

    # download and unzip template contents from https://github.com/qromatech/qroma-project-template
    project_dir = project_template.setup_project_directory(qroma_project, generate_project_options)

    # use project ID to name Arduino project directory
    device_boards.setup_device_project(qroma_project, generate_project_options)

    # setup web sites for interacting with project installed on board
    # www_sites.do_docusaurus_setup(project_dir, project_id)
    www_sites.setup_site_project(qroma_project)

    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        print("QROMA-CLI PATH")
        print(sys.executable)
        project_app_path = os.path.join(project_dir, "qroma.exe")
        print(project_app_path)

    else:
        print("RUNNING FROM PYTHON EXECUTABLE, NOT AS CLI APP")

    this_project: QromaProject = QromaProject(project_root_dir, project_id)
    save_location = Path(os.path.join(this_project.project_dir, "qroma.yaml"))
    save_qroma_project(this_project, save_location)

    do_build_project(qroma_project=this_project,
                     build_parameters=generate_project_options.build_parameters,
                     )

    return this_project
