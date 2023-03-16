import os.path


def convert_qroma_file_references(fpath, project_id):
    with open(fpath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('qroma-project', project_id)

    # Write the file out again
    with open(fpath, 'w') as file:
        file.write(filedata)


def update_arduino_project_dir(project_dir: os.PathLike, project_id):
    esp32_arduino_device_board_dir = os.path.join(project_dir, "device-boards", "esp32")
    print(f"ESP32 {esp32_arduino_device_board_dir}")

    project_template_board_dir = os.path.join(esp32_arduino_device_board_dir, "qroma-project")
    new_sketch_dir = os.path.join(esp32_arduino_device_board_dir, project_id)
    os.rename(project_template_board_dir, new_sketch_dir)

    new_ino_file_path = os.path.join(new_sketch_dir, f"{project_id}.ino")
    os.rename(os.path.join(new_sketch_dir, "qroma-project.ino"),
              new_ino_file_path)


def setup_device_project(project_dir: os.PathLike, project_id):
    # download_arduino_cli(project_dir)
    # init_arduino_project(project_dir, project_id)
    print(f"PROJECT DIR: {project_dir}")
    update_arduino_project_dir(project_dir, project_id)
