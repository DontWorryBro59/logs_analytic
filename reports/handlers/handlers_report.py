from typing import Generator

from reports.handlers.handler_conf import HandlerConf


def read_file(file_path: str) -> Generator[str, None, None]:
    """Lazy read file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def check_logs(file_path: str) -> None:
    """This function is used to check logs"""
    # Log pattern
    pattern = HandlerConf.handler_pattern

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
                finally_stats[path] = {level: 0 for level in HandlerConf.all_levels}
            for level, count in levels.items():
                # Check if level is in
                finally_stats[path][level] += count
    return finally_stats


def print_stats(stats: dict) -> None:
    """Print stats"""
    # Total number of logs for all handlers
    total = {level: 0 for level in HandlerConf.all_levels}
    print("HANDLERS".ljust(30), "\t".join(HandlerConf.all_levels))
    for handler in sorted(stats.keys()):
        metrics = []
        for level in HandlerConf.all_levels:
            total[level] += stats[handler][level]
            metrics.append(str(stats[handler][level]))
        print(handler.ljust(30), "\t".join(metrics))
    print("TOTAL".ljust(30), "\t".join([str(total[level]) for level in HandlerConf.all_levels]))


from multiprocessing import Pool


def get_handler_stats(files: list[str]) -> None:
    """Get stats for all files with multiprocessing"""
    # Create a pool of workers
    with Pool() as pool:
        # Start all tasks in parallel
        print("Starting parallel processing of files...")
        all_stats = pool.map(check_logs, files)

    # Combine files data
    finally_stats = combine_data(stats=all_stats)

    # Print stats
    print_stats(stats=finally_stats)
