from multiprocessing import Pool
from typing import Generator
import re


def read_file(file_path: str) -> Generator[str, None, None]:
    """Lazy read file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def check_logs(file_path: str) -> None:
    """This function is used to check logs"""
    # Log pattern
    pattern = re.compile(
        r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} '
        r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) .*?: .*?(?P<path>/[^\s\[]+)'
    )

    # Read file line by line
    for log in read_file(file_path):
        # Check if line is empty or not contains django.request
        if not log.strip() or "django.request:" not in log:
            continue

        match = pattern.match(log)
        level = match.group('level')
        path = match.group('path')
        print(f"Level: {level} | Path: {path}")


def get_handler_stats(files: list[str]) -> None:
    """Get stats for all files with multiprocessing"""
    for file in files:
        print(f"Start read file {file}")
        check_logs(file_path=file)

