import subprocess
import os

import qroma_dirs
from qroma_project.qroma_project import QromaProject


def setup_site_project(qroma_project: QromaProject):
    project_template_site_dir = os.path.join(qroma_project.project_dir, "sites", "www-qroma-project")
    new_site_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
    os.rename(project_template_site_dir, new_site_dir)


def do_docusaurus_setup(project_dir, project_id):
    device_sites_dir = os.path.join(project_dir, "sites")
    subprocess.run(["npx",
                    "generate-docusaurus@latest",
                    project_id,
                    "classic"], shell=True, cwd=device_sites_dir)
    print("DONE RUNNING SUBPROCESS")
