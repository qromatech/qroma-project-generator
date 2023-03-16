import os
import shutil


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


def qroma_os_move_file_to_dir(fpath, newdir):
    typer_show_to_user(f"MOVING FILE {fpath} TO DIR {newdir}")
    shutil.move(fpath, newdir)
