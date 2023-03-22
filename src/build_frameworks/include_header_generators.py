import os

import qroma_dirs
from qroma_project.qroma_project import QromaProject

PROJECT_HEADER_INCLUDE_REF = "#REPLACE_WITH_PROJECT_REF_HEADER_INCLUDE"
PROJECT_PROTO_HEADER_INCLUDE_REF = "#REPLACE_WITH_PROJECT_PROTO_REF_HEADER_INCLUDE"


def _replace_file_text(fpath, text_to_replace, new_text):
    # Open the input file
    with open(fpath, 'r') as f:
        filedata = f.read()

    # Replace the placeholder text with new text
    updated_file_text = filedata.replace(text_to_replace, new_text)

    # Open the output file and write the new data to it
    with open(fpath, 'w') as f:
        f.write(updated_file_text)


def update_include_for_arduino_ino(qroma_project: QromaProject):
    arduino_dir = qroma_dirs.get_device_boards_esp_project_dir(qroma_project)
    ino_file = os.path.join(arduino_dir, f"{qroma_project.project_id}.ino")
    header_include_text = f'#include "src/{qroma_project.project_id}/qroma-project.h"'
    _replace_file_text(ino_file, PROJECT_HEADER_INCLUDE_REF, header_include_text)


def update_include_for_src_main_cpp(qroma_project: QromaProject):
    src_dir = qroma_dirs.get_device_boards_esp_project_src_dir(qroma_project)
    main_cpp_file = os.path.join(src_dir, "main.cpp")
    header_include_text = f'#include "{qroma_project.project_id}/qroma-project.h"'
    _replace_file_text(main_cpp_file, PROJECT_HEADER_INCLUDE_REF, header_include_text)


def update_include_for_src_project_h(qroma_project: QromaProject):
    src_dir = qroma_dirs.get_device_boards_esp_project_src_dir(qroma_project)
    src_project_header_file = os.path.join(src_dir, qroma_project.project_id, "qroma-project.h")
    proto_header_include_text = f'#include "../qroma-proto/hello-qroma.pb.h"'
    _replace_file_text(src_project_header_file, PROJECT_PROTO_HEADER_INCLUDE_REF, proto_header_include_text)


def update_include_for_src_project_config_h(qroma_project: QromaProject):
    src_dir = qroma_dirs.get_device_boards_esp_project_src_dir(qroma_project)
    src_project_header_file = os.path.join(src_dir, qroma_project.project_id, "qroma-project-config.h")
    proto_header_include_text = f'#include "../qroma-proto/hello-qroma.pb.h"'
    _replace_file_text(src_project_header_file, PROJECT_PROTO_HEADER_INCLUDE_REF, proto_header_include_text)


def update_all_header_includes(qroma_project: QromaProject):
    update_include_for_arduino_ino(qroma_project)
    update_include_for_src_main_cpp(qroma_project)
    update_include_for_src_project_h(qroma_project)
    update_include_for_src_project_config_h(qroma_project)
