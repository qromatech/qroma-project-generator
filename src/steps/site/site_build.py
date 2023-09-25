import subprocess

import qroma_dirs
from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from steps import pb_steps, firmware_steps
from steps.site.site_bundle import do_site_bundle_work

from utils import typer_progress_message


def do_site_npm_install_step(qroma_project: QromaProject):
    with typer_progress_message("WWW SITE - NPM INSTALL"):
        site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
        install_process = subprocess.Popen("npm install",
                                           stdout=subprocess.PIPE,
                                           shell=True,
                                           cwd=site_www_dir)
        install_process.wait()
        print(install_process)


def do_full_site_build(qroma_project: QromaProject, user_profile: QromaUserProfile):
    pb_steps.run_pb_build_step(qroma_project)
    firmware_steps.run_firmware_build_step(qroma_project, user_profile)
    do_site_bundle_work(qroma_project)
    do_site_npm_install_step(qroma_project)
