import os

from constants import QROMA_PROTOBUFS_DIR_NAME
from qp_config import qp_config_shortcuts
from qroma_project.qroma_project import QromaProject


def get_protobufs_root_dir(qroma_project: QromaProject):
    pb_build_stage = qp_config_shortcuts.get_protobuf_stage_config(qroma_project)
    dir_from_config = pb_build_stage.root_dir
    protobufs_dir = os.path.join(qroma_project.project_dir, dir_from_config)
    return protobufs_dir


def get_protobufs_build_src_and_dest_dirs(qroma_project: QromaProject):
    pb_build_stage = qp_config_shortcuts.get_protobuf_stage_config(qroma_project)
    root_dir = get_protobufs_root_dir(qroma_project)
    src_and_dest_dirs = [(os.path.join(root_dir, s.source_path), os.path.join(root_dir, s.dest_path)) for
                         s in pb_build_stage.sources]
    return src_and_dest_dirs


def get_protobufs_build_dest_and_publish_dirs(qroma_project: QromaProject) -> (str, str):
    pb_build_stage = qp_config_shortcuts.get_protobuf_stage_config(qroma_project)
    root_dir = get_protobufs_root_dir(qroma_project)
    dest_and_publish_dirs = [(os.path.join(root_dir, s.dest_path), s.site_path) for
                             s in pb_build_stage.sources]
    return dest_and_publish_dirs


def get_apps_dir(qroma_project: QromaProject):
    apps_dir = os.path.join(qroma_project.project_dir, "apps")
    return apps_dir


def get_apps_python_pb_dir(qroma_project: QromaProject):
    apps_dir = get_apps_dir(qroma_project)
    apps_python_dir = os.path.join(apps_dir, "py-qroma-io", "qroma_proto")
    return apps_python_dir


def get_project_site_static_dir(qroma_project: QromaProject):
    project_site_static_dir = os.path.join(qroma_project.project_dir,
                                           qroma_project.config.qroma.project.stages.sw.sites.bundle.bundle_static_dir)
    return project_site_static_dir


def get_project_site_www_dir(qroma_project: QromaProject):
    project_site_www_dir = os.path.join(qroma_project.project_dir, "sites", "www-" + qroma_project.project_id)
    return project_site_www_dir


def get_site_www_pb_dir(qroma_project: QromaProject):
    project_site_www_dir = get_project_site_static_dir(qroma_project)
    site_www_pb_dir = os.path.join(project_site_www_dir, "src", QROMA_PROTOBUFS_DIR_NAME)
    return site_www_pb_dir
