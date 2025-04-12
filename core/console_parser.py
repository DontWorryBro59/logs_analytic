import argparse
import os


def parse_args() -> argparse.Namespace:
    """Function to parse arguments"""
    parser = argparse.ArgumentParser(description="Logs Analytic utils")
    parser.add_argument('log_paths', nargs='+', help="List of logs paths, example: logs/test.log")
    parser.add_argument('--report', choices=get_list_folder_in_reports(),
                        help=f"Report name, available reports are: {get_list_folder_in_reports()}")
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


def get_list_folder_in_reports() -> list[str]:
    """Function to get list of folders in reports"""
    list_dir = os.listdir('reports')
    return list_dir
