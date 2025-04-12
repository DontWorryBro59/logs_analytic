from core.console_parser import parse_args, check_paths_exist


def main() -> None:
    """Entry point of the program"""
    # get arguments from command line
    args = parse_args()
    # check if paths exist
    correct_paths = check_paths_exist(args.log_paths)



if __name__ == '__main__':
    main()
