from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from steps.site import site_build
from steps.site.site_bundle import do_site_bundle_work
from utils import typer_progress_message


def run_site_bundle_step(qroma_project: QromaProject):
    do_site_bundle_work(qroma_project)


def run_site_npm_install_step(qroma_project: QromaProject):
    site_build.do_site_npm_install_step(qroma_project)


def run_site_build_step(qroma_project: QromaProject, user_profile: QromaUserProfile):
    with typer_progress_message("WWW SITE - FULL BUILD"):
        site_build.do_full_site_build(qroma_project, user_profile)
