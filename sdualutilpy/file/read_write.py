from typing import List


def read_all(file_path) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def read_line(file_path) -> str:
    with open(file_path, 'r') as f:
        return f.readline()


def read_lines(file_path) -> List[str]:
    with open(file_path, 'r') as f:
        return f.readlines()
