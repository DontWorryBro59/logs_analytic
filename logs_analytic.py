import argparse


def parse_args() -> argparse.Namespace:
    """Function to parse arguments"""
    parser = argparse.ArgumentParser(description="Logs Analytic utils")
    parser.add_argument('log_paths', nargs='+', help="List of logs paths")
    parser.add_argument('--report', help="Report name")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(args)


if __name__ == '__main__':
    main()
