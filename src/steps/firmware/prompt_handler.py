import typer

from qroma_enums import FirmwareFramework


def do_firmware_build_prompt(platform: FirmwareFramework, build_prompt: str, firmware_dir: str):
    typer.prompt(f"Firmware project root is here: {firmware_dir}. {build_prompt}. Hit enter when done >>> ")


def do_firmware_upload_prompt(platform: FirmwareFramework, upload_prompt: str, firmware_dir: str):
    typer.prompt(f"Firmware project root is here: {firmware_dir}. {upload_prompt}. Hit enter when done >>> ")
