import sys
import os
from shutil import which
from collections import namedtuple
from typing import Optional, List
from pathlib import Path

from config import LOCAL_TEMPLATE_DIR

MissingToolSummary = namedtuple("MissingToolSummary",
                                ['tool_name', 'install_link', 'description'])


def check_cli():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        print("QROMA-CLI PATH")
        print(sys.executable)
        # project_app_path = os.path.join(project_dir, "qroma.exe")
        # print(project_app_path)

    else:
        print("RUNNING FROM PYTHON EXECUTABLE, NOT AS CLI APP")


def is_running_as_cli_executable():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.

        return True
    else:
        return False


def get_local_template_source_dir():
    this_file = Path(__file__)
    parent_dir = this_file.parent.parent
    template_source_dir = os.path.join(parent_dir, LOCAL_TEMPLATE_DIR)
    return template_source_dir


def check_for_docker() -> Optional[MissingToolSummary]:
    if which("docker") is None:
        return MissingToolSummary('docker',
                                  'https://docs.docker.com/get-docker/',
                                  'Docker is used in some build steps, like the protocol buffer compilation step.',
                                  )
    return None


def check_for_platform_io() -> Optional[MissingToolSummary]:
    if which("pio") is None:
        return MissingToolSummary('PlatformIO',
                                  'https://platformio.org/install/cli',
                                  'PlatformIO is the default ESP32 build platform for Qroma.',
                                  )
    return None


def check_for_npm() -> Optional[MissingToolSummary]:
    if which("npm") is None:
        return MissingToolSummary('NPM/Node.js',
                                  'https://nodejs.org/en/download/',
                                  'NPM/Node.js is required for building the default Qroma device sites.',
                                  )
    return None


def check_for_not_a_real_tool() -> Optional[MissingToolSummary]:
    if which("not_a_real_tool") is None:
        return MissingToolSummary('Not A Real Tool',
                                  'https://example.com/not-real/download/',
                                  'Dummy tool which should never exist to help with testing.',
                                  )
    return None


def print_missing_tool_summary(missing_tool_summary: MissingToolSummary):
    print(f"{missing_tool_summary.tool_name} could not be found on your PATH.")
    print(f"{missing_tool_summary.description}")
    print(f"You can use this link to download it - {missing_tool_summary.install_link}")


def do_env_checks() -> List[MissingToolSummary]:
    docker_summary = check_for_docker()
    platform_io_summary = check_for_platform_io()
    npm_summary = check_for_npm()
    nart_summary = check_for_not_a_real_tool()

    env_missing_tool_summaries = [ts for ts in [docker_summary,
                                                platform_io_summary,
                                                npm_summary,
                                                nart_summary,
                                                ]
                                  if ts is not None]

    for missing_tool_summary in env_missing_tool_summaries:
        print_missing_tool_summary(missing_tool_summary)

    return env_missing_tool_summaries
