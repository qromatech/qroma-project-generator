from qroma_project.generate.qroma_project_template_data import QromaProjectTemplateData


def firmware_processor(qroma_project_data: QromaProjectTemplateData):

    def include_statement(include_str):
        s = include_str.format(qroma_project=qroma_project_data)
        return s

    return {
        'include_statement': include_statement,
    }
