from qroma_project.qroma_project import QromaProject


def dev_boards_processor(qroma_project: QromaProject):

    def include_statement(include_str):
        s = include_str.format(qroma_project=qroma_project)
        return s

    return {
        'include_statement': include_statement,
    }
