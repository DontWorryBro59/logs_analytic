from typing import Generator


def read_file(file_path: str) -> Generator[str]:
    """Lazy read file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line