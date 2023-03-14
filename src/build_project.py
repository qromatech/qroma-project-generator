
import os
import subprocess


def do_build_project():
    project_dir = os.getcwd()
    subprocess.run(["build-everything.bat"], shell=True, cwd=project_dir)
    print("DONE RUNNING BUILD PROJECT SUBPROCESS")
