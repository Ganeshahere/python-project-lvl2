from gendiff.parsing import parse


def load(file_path):
    with open(file_path) as file:
        return parse(file_path, file)
