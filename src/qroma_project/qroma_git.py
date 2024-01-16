import datetime
import os
import time

import env_checks
import git_qroma_utils
import qroma_dirs
from qroma_enums import ExitReason
from qroma_project.qroma_project import QromaProject
from utils import qroma_exit_with_work, qroma_exit, qroma_os_remove, qroma_os_rmdir


def _validate_git_and_if_project_repo(qroma_project: QromaProject, should_be_git_repo: bool, why_git_required: str):
    git_summary = env_checks.check_for_git()
    if git_summary is not None:
        with qroma_exit_with_work(why_git_required, ExitReason.MISSING_TOOL_GIT):
            env_checks.print_missing_tool_summary(git_summary)

    is_git_repo = git_qroma_utils.check_if_dir_is_git_repo(qroma_project.project_dir)
    if is_git_repo == should_be_git_repo:
        return

    if is_git_repo:
        qroma_exit(f"PROJECT REPO FOR {qroma_project.project_id} IS ALREADY A GIT REPO. WILL NOT CONTINUE.",
                   ExitReason.INVALID_ENV_ALREADY_GIT_REPO)
    else:
        qroma_exit(f"PROJECT REPO FOR {qroma_project.project_id} NEEDS TO BE A GIT REPO. WILL NOT CONTINUE.",
                   ExitReason.INVALID_ENV_NOT_A_GIT_REPO)


def _validate_qroma_project_on_git_branch(qroma_project: QromaProject, expected_branch_name):
    _validate_git_and_if_project_repo(qroma_project, True, "GIT REQUIRED TO CHECK PROJECT REPO BRANCH")
    git_branch = git_qroma_utils.get_repo_dir_current_branch(qroma_project.project_dir)

    if git_branch != expected_branch_name:
        qroma_exit(f"PROJECT REPO FOR {qroma_project.project_id} EXPECTED TO BE ON BRANCH "
                   f"'{expected_branch_name}' (ON {git_branch}).",
                   ExitReason.INVALID_ENV_ALREADY_GIT_REPO)


def do_init_add_and_commit_project(qroma_project: QromaProject):
    _validate_git_and_if_project_repo(qroma_project, False, "GIT REQUIRED TO INIT/ADD/COMMIT TO PROJECT REPO")

    now = datetime.datetime.now()
    f_now = f"{now.year:04d}-{now.month:02d}-{now.day:02d} at {now.hour:02d}:{now.minute:02d}"
    commit_message = f"Creating '{qroma_project.project_id}' git repo based on " \
                     f"https://github.com/qromatech/qroma-project-template on {f_now}"

    # change to project directory
    curr_dir = os.getcwd()
    os.chdir(qroma_project.project_dir)
    print("CHDIR TO PROJECT DIR: " + os.getcwd())

    git_qroma_utils.do_git_cmd(["init"])
    git_qroma_utils.do_git_cmd(["add", "*"])
    git_qroma_utils.do_git_cmd(["commit", f"-m {commit_message}"])

    print(f"INITIALIZED PROJECT GIT REPO: {commit_message}")

    # change back to original directory
    os.chdir(curr_dir)
    print("CHDIR BACK: " + os.getcwd())


def do_add_and_commit_branch(qroma_project: QromaProject, branch_name, commit_message):
    _validate_qroma_project_on_git_branch(qroma_project, branch_name)

    # change to project directory
    curr_dir = os.getcwd()
    os.chdir(qroma_project.project_dir)
    print("CHDIR TO PROJECT DIR: " + os.getcwd())

    print(f"BRANCH NAME: {branch_name}")
    print(f"COMMIT MESSAGE: {commit_message}")

    git_qroma_utils.do_git_cmd(["add", "*"])
    git_qroma_utils.do_git_cmd(["commit", f"-m {commit_message}"])

    print(f"COMMITTING TO PROJECT GIT REPO: {commit_message}")

    # change back to original directory
    os.chdir(curr_dir)
    print("CHDIR BACK: " + os.getcwd())
