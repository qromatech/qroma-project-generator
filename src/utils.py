import os


def typer_show_to_user(message):
    print(message)


def qroma_os_rename(src, dest):
    typer_show_to_user(f"RENAMING {src} -> {dest}")
    os.rename(src, dest)


def qroma_os_remove(path):
    typer_show_to_user(f"REMOVING {path}")
    os.remove(path)
