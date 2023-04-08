import subprocess

import qroma_dirs
from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from steps.site import site_build
from steps.site.site_bundle import do_site_bundle_work


def run_site_bundle_step(qroma_project: QromaProject):
    do_site_bundle_work(qroma_project)


def run_site_npm_install_step(qroma_project: QromaProject):
    site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
    subprocess.run(["npm", "install"], shell=True, cwd=site_www_dir)
    # subprocess.run(["npm", "run", "build"], shell=True, cwd=site_www_dir)
    print("DONE RUNNING BUILD WWW SITE SUBPROCESS")


def run_site_build_step(qroma_project: QromaProject, user_profile: QromaUserProfile):
    site_build.do_full_site_build(qroma_project, user_profile)
