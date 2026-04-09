"""
LOGGING CONFIGURATION
"""
from __future__ import annotations
import logging
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .config import BaseConfig

class NhlLogger:
    def __init__(self, config: BaseConfig):
        log_level = config.log_level.upper()
        self.logger = logging.getLogger(config.log_name)
        self.logger.setLevel(getattr(logging, log_level, logging.INFO))

        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        if config.log_file:
            log_path = Path(config.log_file).expanduser()
            log_path.parent.mkdir(parents=True, exist_ok=True)
            handler = logging.FileHandler(log_path)
        else:
            handler = logging.StreamHandler()

        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)
        self.logger.debug(f"Logger: '{self.logger.name}' created. Log Level: {log_level}")

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
