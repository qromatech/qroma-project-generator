# import os
#
# from qp_config import toml_template_map
# from qroma_project import QromaProject
#
#
# def create_toml_str(qroma_project: QromaProject, toml_template_location: os.PathLike):
#     try:
#         toml_template_items = {
#             "#REPLACE_WITH_PROJECT_ID": toml_template_map.get_project_id(qroma_project)
#         }
#
#         with open(toml_template_location, "r") as toml_template_file:
#             toml_content = toml_template_file.read()
#             for key, value in toml_template_items:
#                 toml_content = toml_content.replace(key, value)
#             return toml_content
#
#     except Exception as e:
#         raise Exception(f"Unable to generate Qroma TOML: {e}")
#
#
# def save_qroma_project_toml(qroma_project: QromaProject):
#     toml_template_location = os.path.join(qroma_project.project_dir, "qroma-template.toml")
#     # toml_config_save_location = os.path.join(qroma_project.project_dir, "qroma-template.toml")
#     toml_content = create_toml_str(qroma_project, toml_template_location)
#     project_toml_location = os.path.join(qroma_project.project_dir, "qroma.toml")
#     with open(project_toml_location, "w") as toml_file:
#         toml_file.write(toml_content)
#
