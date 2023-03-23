import os
import tomllib
import env_checks
from build_info import qroma_build_info


def get_version():
    version = qroma_build_info['app_version']
    build_time = qroma_build_info['build_time']

    if env_checks.is_running_as_cli_executable():
        qroma_app_version = f"{version} [{build_time}]"
        executable_message = "running from packaged executable"

    else:
        pyproject_toml_path = os.path.join(os.getcwd(), 'pyproject.toml')
        with open(pyproject_toml_path, 'rb') as f:
            py_project = tomllib.load(f)
            qroma_app_version = py_project['tool']['poetry']['version']
        executable_message = "running from Python"

    return f"{qroma_app_version} - {executable_message}"