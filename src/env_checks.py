from shutil import which
from collections import namedtuple
from typing import Optional, List

MissingToolSummary = namedtuple("MissingToolSummary",
                                ['tool_name', 'install_link', 'description'])


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