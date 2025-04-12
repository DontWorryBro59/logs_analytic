import re
from typing import Generator

ALL_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


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

    stats = {}
    # Read file line by line
    for log in read_file(file_path):
        # Check if line is empty or not contains django.request
        if not log.strip() or "django.request:" not in log:
            continue

        match = pattern.match(log)
        level = match.group('level')
        path = match.group('path')
        # Check if path is in stats
        if path not in stats:
            stats[path] = {}
        # Check if level is in stats
        if level not in stats[path]:
            stats[path][level] = 0
        stats[path][level] += 1
    return stats


def combine_data(stats: list[dict]) -> dict:
    """Combine data from all files"""
    finally_stats = {}

    for stat in stats:
        for path, levels in stat.items():
            if path not in finally_stats:
                # Init all levels for path
                finally_stats[path] = {level: 0 for level in ALL_LEVELS}
            for level, count in levels.items():
                # Check if level is in
                finally_stats[path][level] += count
    return finally_stats


def print_stats(stats: dict) -> None:
    """Print stats"""
    print("HANDLERS".ljust(30), "\t".join(ALL_LEVELS))
    for handler in sorted(stats.keys()):
        metrics = []
        for level in ALL_LEVELS:
            metrics.append(str(stats[handler][level]))
        print(handler.ljust(30), "\t".join(metrics))
    # TODO: need doing TOTAL section


def get_handler_stats(files: list[str]) -> None:
    """Get stats for all files with multiprocessing"""
    all_stats = []
    for file in files:
        print(f"Start read file {file}")
        all_stats.append(check_logs(file_path=file))

    # Combine files data
    finally_stats = combine_data(stats=all_stats)

    # Print stats
    print_stats(stats=finally_stats)
