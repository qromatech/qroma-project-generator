# from qroma_project import QromaProject
#
#
# def create_toml_str_list_str(key_name: str, l: list) -> str:
#     if len(l) == 0:
#         return f"{key_name} = []"
#     if len(l) == 1:
#         return f'{key_name} = ["{l[0]}"]'
#
#     formatted_items = [f'  "{i}",\n' for i in l]
#     content = "".join(formatted_items)
#     return f"""{key_name} = [
# {content}]"""
#
#
# def get_project_id(qroma_project: QromaProject):
#     return qroma_project.project_id
#
#
# def get_build_frameworks(qroma_project: QromaProject):
#     return create_toml_str_list_str(
#         "build_frameworks", [p.value for p in qroma_project.config.dev_board_platforms])
