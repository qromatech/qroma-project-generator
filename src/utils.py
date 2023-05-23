import os
import shutil
import subprocess
import platform
from contextlib import contextmanager

import typer

from qroma_enums import ExitReason


indent_level = 0


def typer_show_to_user(message: str):
    indent = " " * indent_level
    print(f"{indent}{message}")


def typer_show_lines_to_user(lines: list[str]):
    for line in lines:
        typer_show_to_user(line)


def qroma_os_rename(src, dest):
    typer_show_to_user(f"RENAMING {src} -> {dest}")
    # os.rename(src, dest)
    shutil.move(src, dest)


def qroma_os_remove(path):
    typer_show_to_user(f"REMOVING {path}")
    os.remove(path)


def qroma_os_rmdir(path):
    typer_show_to_user(f"REMOVING DIRECTORY {path}")
    # os.rmdir(path)
    shutil.rmtree(path)


def qroma_copy_file(from_path, to_fpath):
    typer_show_to_user(f"COPYING FROM {from_path} to {to_fpath}")
    shutil.copy(from_path, to_fpath)


def qroma_copy_dir(from_dir, to_dir):
    typer_show_to_user(f"COPYING DIR CONTENTS FROM {from_dir} TO {to_dir}")
    shutil.copytree(from_dir, to_dir)


def qroma_os_move_file_to_dir(fpath, newdir):
    typer_show_to_user(f"MOVING FILE {fpath} TO DIR {newdir}")
    shutil.move(fpath, newdir)


def qroma_show_dir(dir_path: os.PathLike):
    if platform.system() == "Windows":
        subprocess.run(["explorer", "."], cwd=dir_path)
    else:
        print(f"Unable to show directory {dir_path} on {platform.system()}")


def qroma_edit_dir(dir_path: os.PathLike):
    print(f"qroma_edit_dir: {dir_path}")
    subprocess.run(["code", "."], shell=True, cwd=dir_path)


@contextmanager
def qroma_exit_with_work(exit_msg: str, exit_code: ExitReason):
    typer_show_to_user(exit_msg)
    yield
    exit(exit_code)


def qroma_exit(exit_msg: str, exit_code: ExitReason = ExitReason.UNSPECIFIED):
    with qroma_exit_with_work(exit_msg, exit_code):
        pass


@contextmanager
def typer_progress_message(message: str):
    global indent_level

    typer_show_to_user(f"STARTING: {message}")
    indent_level = indent_level + 2
    yield

    indent_level = indent_level - 2
    typer_show_to_user(f"COMPLETED: {message}")


def prompt_user_for_dir_choice(root_dir):
    candidate_dirs = [x for x in os.listdir(root_dir)
                      if os.path.isdir(os.path.join(root_dir, x))]
    if len(candidate_dirs) == 1:
        return os.path.join(root_dir, candidate_dirs[0])

    sorted_candidate_dirs = sorted(candidate_dirs)
    sorted_candidate_dirs.insert(0, ".")
    for i, d in enumerate(sorted_candidate_dirs):
        print(f"[{i + 1}] {d}")

    d = typer.prompt("Choose the directory to open >> ")
    d_index = int(d) - 1

    if 0 <= d_index < len(sorted_candidate_dirs):
        dir_choice = os.path.join(root_dir, sorted_candidate_dirs[d_index])
        print("CHOSE " + dir_choice)
        return dir_choice

    return None


def ensure_dir_exists(dir_path):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        return
    os.makedirs(dir_path)


def ensure_file_exists(file_path, default_contents=""):
    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            f.write(default_contents)
