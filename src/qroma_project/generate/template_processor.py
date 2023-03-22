import os

from jinja2 import Environment, FileSystemLoader

from qp_new.dev_boards_processor import dev_boards_processor
from qroma_project.qroma_project import QromaProject
from qroma_types import GenerateProjectOptions


def process_qroma_project_template_dir(qroma_project: QromaProject,
                                       generate_project_options: GenerateProjectOptions,
                                       project_template_dir: os.PathLike,
                                       ):
    qroma_project_env = Environment(
        loader=FileSystemLoader(project_template_dir)
    )

    def do_template_work(path, directories, files):
        # new_dir = path.replace(project_template_dir, qroma_project.project_dir)
        template_file_path = path.replace(project_template_dir, "")[1:].replace("\\", "/")
        rendered_file_path = template_file_path.replace("qroma-project", qroma_project.project_id)
        rendered_file_dir = os.path.join(qroma_project.project_dir, rendered_file_path)
        os.makedirs(rendered_file_dir)

        for f in files:
            template_file = f"{template_file_path}/{f}"
            rendered_file = os.path.join(rendered_file_dir, f)
            print(f"PATH: {path}\nDIR:{directories}\nFILE:{files}\nTEMPLATE_FILE:{template_file}\nRENDERED FILE:{rendered_file}")
            try:
                template = qroma_project_env.get_template(template_file)
                rendered_content = template.render(
                    qroma_project=qroma_project,
                    dev_boards=dev_boards_processor(qroma_project),
                )
                with open(rendered_file, 'w') as f:
                    f.write(rendered_content)
            except Exception as e:
                print(f"ERROR RENDERING TEMPLATE {template_file}")
                print(e)

    print(project_template_dir)

    for path, directories, files in os.walk(project_template_dir):
        do_template_work(path, directories, files)
