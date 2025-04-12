from core.console_parser import parse_args, check_paths_exist


def get_report(report_name: str, paths: list[str]) -> None:
    """Function to get report"""
    print(f"Report name: {report_name}, paths: {paths}")
    pass


def main() -> None:
    """Entry point of the program"""
    # get arguments from command line
    args = parse_args()
    # check if paths exist
    correct_paths = check_paths_exist(args.log_paths)
    if not correct_paths:
        print("[Error!]: no correct paths !")
        return
    # get report
    get_report(args.report, correct_paths)


if __name__ == '__main__':
    main()
