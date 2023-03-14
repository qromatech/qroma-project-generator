import subprocess
import os


def do_docusaurus_setup(project_dir, project_id):
    device_sites_dir = os.path.join(project_dir, "sites")
    subprocess.run(["npx",
                    "create-docusaurus@latest",
                    project_id,
                    "classic"], shell=True, cwd=device_sites_dir)
    print("DONE RUNNING SUBPROCESS")
