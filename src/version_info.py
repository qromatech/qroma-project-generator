import os
import tomllib
import env_checks


def get_version():
    pyproject_toml_path = os.path.join(os.getcwd(), 'pyproject.toml')

    with open(pyproject_toml_path, 'rb') as f:
        py_project = tomllib.load(f)
        qroma_app_version = py_project['tool']['poetry']['version']

    if env_checks.is_running_as_cli_executable():
        return f"{qroma_app_version} - running from packaged executable"

    else:
        return f"{qroma_app_version} - running from Python"
