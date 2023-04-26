import os.path
import shutil
import tomllib


def get_project_version():
    with open("pyproject.toml", "rb") as f:
        py_project = tomllib.load(f)

        project_version = py_project['tool']['poetry']['version']
        print(project_version)
        return project_version


project_version = get_project_version()

downloads_version_dir = os.path.join(os.getcwd(), "downloads", project_version)
print(downloads_version_dir)

if os.path.exists(downloads_version_dir):
    print(f"REMOVING {downloads_version_dir}")
    shutil.rmtree(downloads_version_dir)

os.mkdir(downloads_version_dir)

FILE_NAME = "qroma.exe"

src_file = os.path.join(os.getcwd(), "dist", FILE_NAME)
dest_file = os.path.join(downloads_version_dir, FILE_NAME)

print(f"COPYING {src_file} TO {dest_file}")
shutil.copyfile(src_file, dest_file)
