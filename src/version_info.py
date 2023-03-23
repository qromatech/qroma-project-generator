import os
import tomllib
import env_checks


def get_version():
    if env_checks.is_running_as_cli_executable():
        build_info_toml_path = os.path.join(os.getcwd(), 'build_info.toml')
        with open(build_info_toml_path, 'rb') as f:
            build_info = tomllib.load(f)
            version = build_info['qroma']['version']
            build_time = build_info['qroma']['build_time']
            qroma_app_version = f"{version} [{build_time}]"
        executable_message = "running from packaged executable"

    else:
        pyproject_toml_path = os.path.join(os.getcwd(), 'pyproject.toml')
        with open(pyproject_toml_path, 'rb') as f:
            py_project = tomllib.load(f)
            qroma_app_version = py_project['tool']['poetry']['version']
        executable_message = "running from Python"

    return f"{qroma_app_version} - {executable_message}"