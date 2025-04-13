import logging

from core.logger import get_logger

def test_logger():
    logger = get_logger("test")
    assert type(logger) == logging.Logger
    assert logger.name == "test"
    assert logger.level == 0 # This is default level for child loggers, real(father) = 20
    assert logger.handlers == [] # This is default handlers for child loggers, real(father) = [<StreamHandler>]
    assert logger.propagate is True # Message to parent