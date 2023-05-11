import os

from jinja2 import Environment, FileSystemLoader

from qroma_project.generate.firmware_processor import firmware_processor
from qroma_project.generate.qroma_project_template_data import QromaProjectTemplateData
from qroma_types import GenerateProjectOptions
from utils import qroma_copy_file


def process_qroma_project_template_dir(generate_project_options: GenerateProjectOptions,
                                       project_template_dir: os.PathLike,
                                       ):
    project_id = generate_project_options.project_config_user_inputs.project_info.project_id
    project_dir = generate_project_options.project_config_user_inputs.project_info.project_dir

    qroma_project_env = Environment(
        loader=FileSystemLoader(project_template_dir)
    )

    qroma_project_data = QromaProjectTemplateData(
        project_id=project_id,
        project_dir=project_dir,
        firmware_platforms=[generate_project_options.project_config_user_inputs.firmware_platform],
    )

    print("TEMPLATE DATA")
    print(qroma_project_data)

    def do_template_work(path, directories, files):
        template_file_path = path.replace(project_template_dir, "")[1:].replace("\\", "/")
        rendered_file_path = template_file_path.replace("qroma-project", project_id)
        rendered_file_dir = os.path.join(project_dir, rendered_file_path)
        os.makedirs(rendered_file_dir)

        NON_TEMPLATE_FILE_EXTENSIONS = [".png", ".jpg", ".ico", ".jpeg"]

        template_files = []
        non_template_files = []
        for f in files:
            is_ntfx = False
            for ntfx in NON_TEMPLATE_FILE_EXTENSIONS:
                if f.lower().endswith(ntfx):
                    is_ntfx = True
            if is_ntfx:
                non_template_files.append(f)
            else:
                template_files.append(f)

        for f in template_files:
            template_file = f"{template_file_path}/{f}"
            rendered_file = os.path.join(rendered_file_dir, f)

            try:
                template = qroma_project_env.get_template(template_file)
                rendered_content = template.render(
                    qroma_project=qroma_project_data,
                    firmware=firmware_processor(qroma_project_data),
                )
                with open(rendered_file, 'w') as file_to_render:
                    file_to_render.write(rendered_content)
            except Exception as e:
                print(f"ERROR RENDERING TEMPLATE {template_file}")
                print(e)
                qroma_copy_file(os.path.join(path, f), rendered_file)

        for f in non_template_files:
            dest_file = os.path.join(rendered_file_dir, f)
            qroma_copy_file(os.path.join(path, f), dest_file)

    for path, directories, files in os.walk(project_template_dir):
        do_template_work(path, directories, files)
