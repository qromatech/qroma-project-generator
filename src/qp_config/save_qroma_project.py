# import os.path
#
# from qp_config import toml_template_map
# # from qroma_project import QromaProject
# from qroma_project.qroma_project import QromaProject
# from utils import qroma_os_remove
#
#
# def create_toml_str(qroma_project: QromaProject, toml_template_location: os.PathLike):
#     try:
#         toml_template_replacements = {
#             "#REPLACE_WITH_PROJECT_ID": toml_template_map.get_project_id(qroma_project),
#             "#REPLACE_WITH_BUILD_FRAMEWORKS": toml_template_map.get_build_frameworks(qroma_project),
#         }
#         print(toml_template_replacements)
#
#         with open(toml_template_location, "r") as toml_template_file:
#             toml_content = toml_template_file.read()
#             for (key, value) in toml_template_replacements.items():
#                 toml_content = toml_content.replace(key, value)
#             return toml_content
#
#     except Exception as e:
#         raise Exception(f"Unable to create Qroma TOML: {e}")
#
# #
# # def create_toml_for_qroma_project_config(project_id: str, qpc: QromaProjectConfig) -> str:
# #     build_frameworks = create_toml_str_list_str("build_frameworks", [p.value for p in qpc.dev_board_platforms])
# #     return f"""
# # [qroma.project]
# # name = "{project_id}"
# # version = "0.1.0"
# #
# #
# # [qroma.project.dev_board]
# # {build_frameworks}
# #
# #
# # [qroma.project.run.commands.dev_boards.platformio]
# # build = "run"
# # install = "run --target upload --environment esp32dev"
# # monitor = ""
# #     """
#
# #
# # def save_qroma_project_toml(qroma_project: QromaProject):
# #     toml_template_location = os.path.join(qroma_project.project_dir, "qroma-template.toml")
# #     toml_content = create_toml_str(qroma_project, toml_template_location)
# #     project_toml_location = os.path.join(qroma_project.project_dir, "qroma.toml")
# #
# #     with open(project_toml_location, "w") as toml_file:
# #         toml_file.write(toml_content)
# #
# #
# # def delete_qroma_project_template(qroma_project):
# #     toml_template_location = os.path.join(qroma_project.project_dir, "qroma-template.toml")
# #     qroma_os_remove(toml_template_location)
# #
# #
# # def save_qroma_project(qroma_project: QromaProject):
# #     save_qroma_project_toml(qroma_project)
# #     delete_qroma_project_template(qroma_project)
#
#     # s = create_toml_for_qroma_project_config(qp.project_id, qp.config)
#     # save_location = os.path.join(qp.project_dir, "qroma-draft.toml")
#     # with open(save_location, "w") as f:
#     #     f.write(s)
#
# #
# # def create_initial_project_toml(qroma_project: QromaProject):
# #     toml_file_path = os.path.join(qroma_project.project_root_dir, "qroma.toml")
# #     with open(toml_file_path, 'w') as f:
# #         print("SAVING TOML")
# #         print(qroma_project)
# #         s = toml_writer.dumps(qroma_project)
# #         f.write(s)
