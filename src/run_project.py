import os
import subprocess
from typing import Optional

import qroma_dirs
from qroma_project.qroma_project import QromaProject


def run_and_install_platformio_project(qroma_project: QromaProject):
    esp_project_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    print("EXECUTING RUN ESP 32 PROJECT SUBPROCESS")
    subprocess.run(["pio", "run"], shell=True, cwd=esp_project_dir)
    exit("Need to figure out how to install PIO output onto device")
    print("DONE EXECUTING RUN ESP32 PROJECT SUBPROCESS")


def run_dev_site_www_project(qroma_project: QromaProject):
    site_www_dir = qroma_dirs.get_project_site_www_dir(qroma_project)
    print("EXECUTING START WWW SITE SUBPROCESS")
    subprocess.run(["npm", "install"], shell=True, cwd=site_www_dir)
    subprocess.run(["npm", "run", "start"], shell=True, cwd=site_www_dir)
    print("DONE EXECUTING START WWW SITE SUBPROCESS")


def do_run_project(qroma_project: QromaProject):
    print("EXECUTING RUN ALL PROJECTS")
    run_and_install_platformio_project(qroma_project)
    run_dev_site_www_project(qroma_project)
    print("DONE EXECUTING RUN ALL PROJECTS")
