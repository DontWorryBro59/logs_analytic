import argparse
import os


def parse_args() -> argparse.Namespace:
    """Function to parse arguments"""
    parser = argparse.ArgumentParser(description="Logs Analytic utils")
    parser.add_argument('log_paths', nargs='+', help="List of logs paths")
    parser.add_argument('--report', help="Report name")
    return parser.parse_args()


def check_paths_exist(paths: list[str]) -> list[str]:
    """Function to check if paths exist"""
    correct_paths = []
    for path in paths:
        if os.path.isfile(path):
            correct_paths.append(path)
        else:
            print(f"Error: file {path} does not exist !")
    return correct_paths
