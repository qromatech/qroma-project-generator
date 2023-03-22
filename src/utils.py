import os
import shutil
import subprocess
import platform


def typer_show_to_user(message):
    print(message)


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


def qroma_os_move_file_to_dir(fpath, newdir):
    typer_show_to_user(f"MOVING FILE {fpath} TO DIR {newdir}")
    shutil.move(fpath, newdir)


def qroma_show_dir(dir_path: os.PathLike):
    if platform.system() == "Windows":
        subprocess.run(["explorer", "."], cwd=dir_path)
    else:
        print(f"Unable to show directory {dir_path} on {platform.system()}")