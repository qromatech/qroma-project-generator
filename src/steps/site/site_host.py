import subprocess

import qroma_dirs
from qroma_project.qroma_project import QromaProject

from utils import typer_progress_message


def do_site_npm_run_start_step(qroma_project: QromaProject):
    with typer_progress_message("WWW SITE - NPM RUN START"):
        site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
        install_process = subprocess.Popen("npm run start",
                                           stdout=subprocess.PIPE,
                                           shell=True,
                                           cwd=site_www_dir)
        install_process.wait()
        print(install_process)
