import os
import subprocess

import env_checks


def do_git_cmd(cmd_args: list[str]) -> str:
    if env_checks.check_for_git() is not None:
        raise Exception(f"No git available for commands {cmd_args}")

    git_command_args: list[str] = ["git"]
    git_command_args.extend(cmd_args)

    p = subprocess.run(git_command_args,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       )

    result_line = p.stdout.decode("utf-8").strip()
    return result_line


def check_if_dir_is_git_repo(dir_to_check):
    curr_dir = os.getcwd()
    os.chdir(dir_to_check)

    # to see if get is set up in directory -- git rev-parse --abbrev-ref HEAD
    already_git_repo_check_result = do_git_cmd(["rev-parse", "--is-inside-work-tree"])

    os.chdir(curr_dir)

    return already_git_repo_check_result.lower() == "true"


def get_repo_dir_current_branch(dir_to_check):
    curr_dir = os.getcwd()
    os.chdir(dir_to_check)

    # to get current branch name -- git rev-parse --abbrev-ref HEAD
    branch_name = do_git_cmd(["rev-parse", "--abbrev-ref", "HEAD"])

    os.chdir(curr_dir)

    return branch_name
