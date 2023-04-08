from qroma_project.qroma_project import QromaProject
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from steps import pb_steps, firmware_steps
from steps.site.site_bundle import do_site_bundle_work


# def build_site_www_project(qroma_project: QromaProject):
#     site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
#     print("RUNNING BUILD WWW SITE SUBPROCESS")
#     subprocess.run(["npm", "install"], shell=True, cwd=site_www_dir)
#     subprocess.run(["npm", "run", "build"], shell=True, cwd=site_www_dir)
#     print("DONE RUNNING BUILD WWW SITE SUBPROCESS")
#
#


def do_full_site_build(qroma_project: QromaProject, user_profile: QromaUserProfile):
    pb_steps.run_pb_build_step(qroma_project)
    firmware_steps.run_firmware_build_step(qroma_project, user_profile)
    do_site_bundle_work(qroma_project)
