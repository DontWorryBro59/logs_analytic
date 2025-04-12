from multiprocessing import Pool
from typing import Generator


def read_file(file_path: str) -> Generator[str, None, None]:
    """Lazy read file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def check_logs(file_path: str) -> None:
    # Read file line by line
    for log in read_file(file_path):
        # Check if line is empty or not contains django.request
        if not log.strip() or "django.request:" not in log:
            continue
        print(log)

def get_handler_stats(files: list[str]) -> None:
    """Get stats for all files with multiprocessing"""
    for file in files:
        check_logs(file_path=file)

