from multiprocessing import Pool
from typing import Generator

from reports.handlers.handler_conf import config
from core.logger import get_logger

logger = get_logger('handlers_report')

def read_file(file_path: str) -> Generator[str, None, None]:
    """Lazy read file (generator)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line
    except FileNotFoundError:
        logger.error("File not found: %s", file_path)
        return


def check_logs(file_path: str) -> dict:
    """Analyzes log file and extracts statistics for django.request paths.

    Args:
        file_path: Path to the log file. Example: /logs/app1.log
    """

    pattern = config.handler_pattern

    stats = {}
    # Read file line by line
    for log in read_file(file_path):
        # Check if line is empty or not contains django.request
        if not log.strip() or "django.request:" not in log:
            continue

        match = pattern.match(log)
        if not match:
            continue
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
    final_stats = {}

    for stat in stats:
        for path, levels in stat.items():
            if path not in final_stats:
                # Init all levels for path
                final_stats[path] = {level: 0 for level in config.all_levels}
            for level, count in levels.items():
                # Check if level is in
                final_stats[path][level] += count
    return final_stats


def print_stats(stats: dict) -> None:
    """Print stats.

    Example:
        HANDLERS                       DEBUG    INFO    WARNING ERROR   CRITICAL
        /admin/dashboard/              0        13      0       4       0
        ...
        TOTAL                          0        148     0       40      0
    """
    # Total number of logs for all handlers
    total = {level: 0 for level in config.all_levels}
    print("HANDLERS".ljust(30), "\t".join(config.all_levels))
    for handler in sorted(stats.keys()):
        metrics = []
        for level in config.all_levels:
            total[level] += stats[handler][level]
            metrics.append(str(stats[handler][level]))
        print(handler.ljust(30), "\t".join(metrics))
    print("TOTAL".ljust(30), "\t".join([str(total[level]) for level in config.all_levels]))


def get_handler_stats(files: list[str]) -> None: # pragma: no cover
    """Get stats for all files with multiprocessing"""
    # Create a pool of workers
    with Pool() as pool:
        # Start all tasks in parallel
        logger.info("Starting parallel processing of files...")
        all_stats = pool.map(check_logs, files)

    # Combine files data
    final_stats = combine_data(stats=all_stats)

    # Print stats
    print_stats(stats=final_stats)
