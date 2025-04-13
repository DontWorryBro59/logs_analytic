import argparse
import os

from core.logger import get_logger

logger = get_logger("console_parser")

def parse_args() -> argparse.Namespace:
    """Function to parse arguments (CLI)"""
    available_reports = get_list_folder_in_reports()
    parser = argparse.ArgumentParser(description="Logs Analytic utils")
    parser.add_argument('log_paths', nargs='+', help="List of logs paths, example: logs/test.log")
    parser.add_argument('--report', choices=available_reports,
                        help=f"Report name, available reports are: {available_reports}")
    return parser.parse_args()


def check_paths_exist(paths: list[str]) -> list[str]:
    """Function to check if paths exist"""
    correct_paths = []
    for path in paths:
        if os.path.isfile(path):
            correct_paths.append(path)
        else:
            logger.warning(f"File {path} does not exist !")
    return correct_paths


def get_list_folder_in_reports() -> list[str]:
    """Function to get list of folders in reports"""
    list_dir = os.listdir('reports')
    return list_dir
