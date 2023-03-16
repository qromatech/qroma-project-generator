from .imp2 import imp2_exe


def imp1_exe(arg: str):
    imp2_exe(arg)
    print(f"In imp1_exe: {arg}")
