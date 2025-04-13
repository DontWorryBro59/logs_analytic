import os
import sys

import pytest

from core.console_parser import get_list_folder_in_reports, check_paths_exist, parse_args


def test_get_list_folder_in_reports() -> None:
    """Test for get_list_folder_in_reports function"""
    assert get_list_folder_in_reports() == os.listdir('reports')


def test_check_paths_exist() -> None:
    """Test for check_paths_exist function"""
    assert check_paths_exist(['test']) == []
    assert check_paths_exist(["logs_analytic.py"]) == ['logs_analytic.py']
    assert check_paths_exist(["test", "test1.log", "logs_analytic.py", "logs_analytic"]) == ['logs_analytic.py']
    assert check_paths_exist([]) == []
    assert check_paths_exist([0,]) == []


def test_parse_args_with_correct_paths_and_report() -> None:
    """Test CLI with correct paths and report"""

    original_argv = sys.argv
    try:
        sys.argv = [
            "logs_analytic.py",
            "logs/app1.log",
            "logs/app2.log",
            "logs/app3.log",
            "--report",
            "handlers"
        ]
        args = parse_args()

    finally:
        sys.argv = original_argv
        assert args.log_paths == ["logs/app1.log", "logs/app2.log", "logs/app3.log"]
        assert args.report == "handlers"


def test_parse_args_with_wrong_paths_and_correct_report() -> None:
    """Test CLI with correct paths and wrong report"""

    original_argv = sys.argv
    try:
        sys.argv = [
            "logs_analytic.py",
            "logs/app1.log",
            "logs/app2.log",
            "logs/app3.log",
            "--report",
            "handlers1"
        ]
        with pytest.raises(SystemExit) as exif:
            parse_args()

    finally:
        sys.argv = original_argv
        assert exif.type == SystemExit
        assert exif.value.code == 2


def test_parse_args_with_correct_paths_and_wrong_report() -> None:
    """Test CLI with correct paths and wrong report"""

    original_argv = sys.argv
    try:
        sys.argv = [
            "logs_analytic.py",
            "logs/app1.log",
            "logs/appp2.log",
            "logs/app3.log",
            "--report",
            "handlers"
        ]
        args = parse_args()

    finally:
        sys.argv = original_argv
        # This is correct, because wrong path has been skipped in check_paths_exist function
        assert args.log_paths == ['logs/app1.log', 'logs/appp2.log', 'logs/app3.log']
        assert args.report == 'handlers'
