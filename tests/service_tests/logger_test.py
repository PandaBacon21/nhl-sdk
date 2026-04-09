import logging
from nhl_sdk.core.logger import NhlLogger
from nhl_sdk.core.config import DefaultConfig


def test_logger_stdout_handler() -> None:
    config = DefaultConfig(log_name="test_stdout_handler", log_file=None)
    nl = NhlLogger(config)
    assert nl.logger.name == "test_stdout_handler"
    assert any(isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
               for h in nl.logger.handlers)


def test_logger_file_handler(tmp_path) -> None:
    log_file = str(tmp_path / "test.log")
    config = DefaultConfig(log_name="test_file_handler", log_file=log_file)
    nl = NhlLogger(config)
    assert any(isinstance(h, logging.FileHandler) for h in nl.logger.handlers)


def test_logger_file_creates_parent_dirs(tmp_path) -> None:
    log_file = str(tmp_path / "nested" / "dir" / "test.log")
    config = DefaultConfig(log_name="test_nested_dir", log_file=log_file)
    NhlLogger(config)
    import os
    assert os.path.isdir(str(tmp_path / "nested" / "dir"))


def test_logger_level_warning() -> None:
    config = DefaultConfig(log_name="test_level_warn", log_level="WARNING")
    nl = NhlLogger(config)
    assert nl.logger.level == logging.WARNING


def test_logger_level_debug() -> None:
    config = DefaultConfig(log_name="test_level_debug", log_level="DEBUG")
    nl = NhlLogger(config)
    assert nl.logger.level == logging.DEBUG


def test_logger_info(caplog) -> None:
    config = DefaultConfig(log_name="test_info_call")
    nl = NhlLogger(config)
    with caplog.at_level(logging.INFO, logger="test_info_call"):
        nl.info("hello info")
    assert "hello info" in caplog.text


def test_logger_debug_msg(caplog) -> None:
    config = DefaultConfig(log_name="test_debug_call")
    nl = NhlLogger(config)
    with caplog.at_level(logging.DEBUG, logger="test_debug_call"):
        nl.debug("hello debug")
    assert "hello debug" in caplog.text


def test_logger_warning_msg(caplog) -> None:
    config = DefaultConfig(log_name="test_warning_call")
    nl = NhlLogger(config)
    with caplog.at_level(logging.WARNING, logger="test_warning_call"):
        nl.warning("hello warning")
    assert "hello warning" in caplog.text


def test_logger_error_msg(caplog) -> None:
    config = DefaultConfig(log_name="test_error_call")
    nl = NhlLogger(config)
    with caplog.at_level(logging.ERROR, logger="test_error_call"):
        nl.error("hello error")
    assert "hello error" in caplog.text
