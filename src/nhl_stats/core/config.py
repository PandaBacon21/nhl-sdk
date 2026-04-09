"""
BASE CONFIG FILE
"""

from abc import ABC

from dataclasses import dataclass, field, replace
from pathlib import Path
from platformdirs import user_log_dir
from .cache.base_cache import BaseCache

# api-web.nhle.com/
BASE_URL_API_WEB: str = "https://api-web.nhle.com"
V: str = "v1"

# api.nhle.com/stats/rest/
BASE_URL_API_STATS: str = "https://api.nhle.com/stats/rest"
LANG: str = "en"

FILE_PATH: Path = Path(user_log_dir("nhl_sdk")) / "nhl.log"

@dataclass(slots=True, frozen=True)
class BaseConfig(ABC):
    _base_url_api_web: str = field(default=BASE_URL_API_WEB, init=True)
    _base_url_api_stats: str = field(default=BASE_URL_API_STATS, init=True)
    _v: str = field(default=V, init=True)

    log_name: str = "nhl_sdk"
    log_level: str = "WARNING"
    lang: str = LANG
    # log_file: str | None = str(FILE_PATH)  # default log path; set to None for stdout only
    log_file: str | None = None # Set to None for stdout only - Currently set just for testing
    cache: BaseCache | None = None

@dataclass(slots=True, frozen=True)
class DefaultConfig(BaseConfig):
    """Default Client configuration."""
    pass


def _build_config(config_from_object: BaseConfig | None, log_name: str | None, 
                    log_level: str | None, log_file: str | None, lang: str | None, 
                    cache: BaseCache | None) -> BaseConfig: 
    
    config: BaseConfig = DefaultConfig()
    
    if config_from_object or log_name or log_level or log_file or lang or cache:
        config: BaseConfig = replace(
            config,
            lang=lang if lang is not None else config.lang,
            log_name=log_name if log_name is not None else config.log_name,
            log_level=log_level if log_level is not None else config.log_level,
            log_file=log_file if log_file is not None else config.log_file,
            cache=cache if cache is not None else config.cache,
        )
    if config_from_object: 
        config = config_from_object

    return config
