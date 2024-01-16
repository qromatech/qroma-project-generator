from typing import Optional

import typer

import git_qroma_utils
from qroma_project import user_input
from qroma_project.qroma_git import do_init_add_and_commit_project, do_add_and_commit_branch
from utils import typer_show_to_user

app = typer.Typer(help="Qroma git conveniences")


@app.command()
def prepare(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    do_init_add_and_commit_project(qroma_project)


@app.command()
def get_current_branch(project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    current_branch_name = git_qroma_utils.get_repo_dir_current_branch(qroma_project.project_dir)
    typer_show_to_user(f"Current branch for {qroma_project.project_id} project: {current_branch_name}")


@app.command()
def make_checkpoint(branch_name, commit_message, project_id: Optional[str] = typer.Argument(None)):
    qroma_project = user_input.load_existing_qroma_project_from_user_input(project_id)
    do_add_and_commit_branch(qroma_project, branch_name, commit_message)
