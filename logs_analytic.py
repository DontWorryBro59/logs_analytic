import time

from core.console_parser import parse_args, check_paths_exist
from core.logger import get_logger
from reports.handlers.handlers_report import get_handler_stats

logger = get_logger("logs_analytic")


def get_time_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_result = round(end_time - start_time, 3)
        logger.info(f"Function {func.__name__} executed in {time_result} seconds")
        return result

    return wrapper


def get_report(report_name: str, paths: list[str]) -> None:
    """Function to get report"""
    if report_name == "handlers":
        get_handler_stats(paths)
        # This place can be changed (We can add more reports with block elif, example: elif report_name == "methods" ...
        # And if we append more reports, we need to change reports/... example: reports/methods/methods_report.py)
    else:
        logger.error(f"Report name not found, your choice is: {report_name}")

@get_time_func
def main() -> None:
    """Entry point of the program"""
    # get arguments from command line
    args = parse_args()
    # check if paths exist
    correct_paths = check_paths_exist(args.log_paths)
    if not correct_paths:
        logger.error("No correct paths !")
        return
    # get report
    get_report(report_name=args.report, paths=correct_paths)


if __name__ == '__main__':
    main()
