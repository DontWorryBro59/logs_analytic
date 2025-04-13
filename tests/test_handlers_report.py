import pytest
from reports.handlers.handlers_report import read_file, check_logs, combine_data, print_stats


def test_read_file_with_correct_path() -> None:
    """Test read_file function with correct content"""

    generator = read_file("tests/logs/app1.log")
    assert next(
        generator).strip() == "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]"
    assert next(
        generator).strip() == "2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [192.168.1.68]"
    assert next(
        generator).strip() == "2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected"


def test_read_file_with_wrong_path() -> None:
    """Test read_file function with wrong content"""
    generator = read_file("wrong_path")
    assert not next(generator, False)


def test_check_logs_with_correct_path() -> None:
    """Test check_logs function with correct path"""
    path = "tests/logs/app1.log"
    stats = check_logs(path)
    print(stats)
    assert type(stats) == dict
    assert len(stats) == 12


def test_check_logs_with_wrong_path() -> None:
    """Test check_logs function with wrong path"""
    path = "wrong_path"
    stats = check_logs(path)
    assert stats == {}


def test_combine_data_with_correct_dict() -> None:
    """Test combine_data function with correct dict"""
    test_data = [
                {
                     '/api/v1/reviews/': {'INFO': 5, 'DEBUG': 1},
                     '/admin/dashboard/': {'INFO': 6, 'ERROR': 2, 'CRITICAL': 2},
                     '/api/v1/users/': {'INFO': 4, 'WARNING': 2}
                 },
                {
                    '/api/v1/reviews/': {'INFO': 5, 'DEBUG': 1},
                    '/admin/dashboard/': {'INFO': 6, 'ERROR': 2, 'CRITICAL': 2},
                    '/api/v1/users/': {'INFO': 4, 'WARNING': 2}
                },]
    result = combine_data(test_data)
    assert result['/api/v1/reviews/'] == {'DEBUG': 2, 'INFO': 10, 'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0}
    assert result['/admin/dashboard/'] == {'DEBUG': 0, 'INFO': 12, 'WARNING': 0, 'ERROR': 4, 'CRITICAL': 4}
    assert result['/api/v1/users/'] == {'DEBUG': 0, 'INFO': 8, 'WARNING': 4, 'ERROR': 0, 'CRITICAL': 0}


def test_print_stats(capsys: pytest.CaptureFixture) -> None:
    """Test print_stats function
    Example:
        HANDLERS                       DEBUG    INFO    WARNING ERROR   CRITICAL
        /admin/dashboard/              0        13      0       4       0
        ...
        TOTAL                          0        148     0       40      0
    """
    test_stats = {
        "/admin/dashboard/": {"DEBUG": 1, "INFO": 13, "WARNING": 4, "ERROR": 4, "CRITICAL": 5},
        "/api/users/": {"DEBUG": 3, "INFO": 5, "WARNING": 0, "ERROR": 1, "CRITICAL": 8},
    }

    print_stats(test_stats)

    captured = capsys.readouterr()
    output = captured.out

    assert "/admin/dashboard/" in output
    assert "/api/users/" in output
    assert "4"  in output
    assert "18" in output
    assert "13" in output
    assert "TOTAL" in output