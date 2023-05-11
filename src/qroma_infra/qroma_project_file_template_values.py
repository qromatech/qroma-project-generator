from qp_config.qroma_project_basics import QromaProjectBasics
from qroma_user_profile.qroma_user_profile import QromaUserProfile


def create_qroma_project_file_template_values(project_root_dir, qroma_project_basics: QromaProjectBasics, qroma_user_profile: QromaUserProfile):
    qroma_project_file_template_values = {
        "project_id": qroma_project_basics.qroma.project.id,
        "project_version": qroma_project_basics.qroma.project.version,
        "project_root_dir": project_root_dir,
        "project_dirs": qroma_project_basics.qroma.project.dirs,
        "user_profile_dirs": qroma_user_profile.dirs,
    }

    return qroma_project_file_template_values
