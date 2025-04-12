from core.console_parser import parse_args


def main() -> None:
    """Entry point of the program"""
    # get arguments from command line
    args = parse_args()
    print(args)


if __name__ == '__main__':
    main()
