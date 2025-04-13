import re

from reports.handlers.handler_conf import config


def test_get_all_levels() -> None:
    """test get_all_levels"""
    assert config.all_levels == ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


def test_get_handler_pattern() -> None:
    """test get_handler_pattern"""
    print(type(config.handler_pattern))
    assert type(config.handler_pattern) == type(re.compile(""))
