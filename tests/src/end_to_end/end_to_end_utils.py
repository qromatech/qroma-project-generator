import datetime
import random
import os


def create_project_id():
    now = datetime.datetime.now()
    today_key = f"{now.year:04d}-{now.month:02d}-{now.day:02d}"
    today_time_key = f"{now.hour:02d}{now.minute:02d}{now.second:02d}"
    test_id = random.randint(1, 999)

    project_id = f"test-project-{today_key}.{today_time_key}.{test_id:03d}"
    return project_id


def get_test_user_qroma_dir():
    from pathlib import Path
    home_dir = Path.home()
    qroma_dir = os.path.join(home_dir, "qroma-projects")
    return qroma_dir


def get_pb_build_compiled_by_qroma_receipt_location(project_id):
    user_qroma_dir = get_test_user_qroma_dir()
    location = os.path.join(user_qroma_dir, project_id, "protobufs", "protofiles-out", "compiled-by-qroma.txt")
    return location


def get_firmware_build_output_bin_file_locations(project_id):
    user_qroma_dir = get_test_user_qroma_dir()
    esp32dev_location = os.path.join(user_qroma_dir, project_id, "firmware", "esp32", project_id,
                                     ".pio", "build", "esp32dev", "firmware.bin")
    qtpy_location = os.path.join(user_qroma_dir, project_id, "firmware", "esp32", project_id,
                                 ".pio", "build", "adafruit_qtpy_esp32c3", "firmware.bin")
    return [esp32dev_location, qtpy_location]


def check_file_contains_string(file_location, expected_str):
    with open(file_location) as f:
        return expected_str in f.read()

