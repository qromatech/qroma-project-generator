import os
import tomllib

from qroma_enums import ExitReason
from qroma_infra import qroma_user
from qroma_user_profile import default_qroma_user_profile_toml
from qroma_user_profile.qroma_user_profile import QromaUserProfile
from utils import qroma_exit


def ensure_qroma_user_profile_exists():
    if not os.path.exists(qroma_user.QROMA_USER_ROOT_DIR):
        os.mkdir(qroma_user.QROMA_USER_ROOT_DIR)

    qroma_user_profile_file_path = os.path.join(qroma_user.QROMA_USER_ROOT_DIR,
                                                qroma_user.QROMA_USER_PROFILE_FILE_NAME)

    if not os.path.exists(qroma_user_profile_file_path) and not os.path.isfile(qroma_user_profile_file_path):
        with open(qroma_user_profile_file_path, "w") as f:
            f.write(default_qroma_user_profile_toml.DEFAULT_QROMA_USER_PROFILE_TOML.lstrip())


def load_qroma_user_profile() -> QromaUserProfile:
    qroma_user_profile_file_path = os.path.join(qroma_user.QROMA_USER_ROOT_DIR,
                                                qroma_user.QROMA_USER_PROFILE_FILE_NAME)
    with open(qroma_user_profile_file_path, 'rb') as file:
        qroma_user_dict = tomllib.load(file)
        try:
            qroma_user_profile = QromaUserProfile(**qroma_user_dict['qroma']['user']['profile'])
            return qroma_user_profile
        except KeyError as e:
            qroma_exit(f"Invalid qroma user profile at {qroma_user_profile_file_path}: Missing config key: {e}",
                       ExitReason.INVALID_USER_PROFILE)
        except Exception as e:
            qroma_exit(f"Invalid qroma user profile at {qroma_user_profile_file_path}: {e}", ExitReason.UNSPECIFIED)
