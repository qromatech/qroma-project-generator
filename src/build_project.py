import subprocess

import qroma_dirs
from qroma_project import QromaProject


def build_esp32_project_with_platformio(qroma_project: QromaProject):
    esp_project_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    print("RUNNING BUILD ESP 32 PROJECT SUBPROCESS")
    subprocess.run(["pio", "run"], shell=True, cwd=esp_project_dir)
    print("DONE RUNNING BUILD PROJECT SUBPROCESS")


def build_site_www_project(qroma_project: QromaProject):
    site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
    print("RUNNING BUILD WWW SITE SUBPROCESS")
    subprocess.run(["npm", "install"], shell=True, cwd=site_www_dir)
    subprocess.run(["npm", "run", "build"], shell=True, cwd=site_www_dir)
    print("DONE RUNNING BUILD WWW SITE SUBPROCESS")


def run_build_all_projects(qroma_project: QromaProject):
    print("RUNNING BUILD ALL PROJECTS")
    build_esp32_project_with_platformio(qroma_project)
    build_site_www_project(qroma_project)
    print("DONE RUNNING BUILD ALL PROJECTS")


def do_build_project(qroma_project: QromaProject):
    run_build_all_projects(qroma_project)
