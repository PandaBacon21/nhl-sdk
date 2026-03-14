"""
BASE CONFIG FILE
"""

from abc import ABC
from typing import Optional
from dataclasses import dataclass, field, replace
from pathlib import Path
from .cache.base_cache import BaseCache
from .cache.mem_cache import MemCache

# api-web.nhle.com/ 
BASE_URL_API_WEB: str = "https://api-web.nhle.com"
V: str  = "v1"

# api.nhle.com/stats/rest/ 
BASE_URL_API_STATS: str = "https://api.nhle.com/stats/rest"
LANG: str = "en"

FILE_PATH = Path("~/.config/nhl_sdk/nhl.log")

@dataclass(slots=True, frozen=True)
class BaseConfig(ABC):
    _base_url_api_web: str = field(default=BASE_URL_API_WEB, init=True)
    _base_url_api_stats: str = field(default=BASE_URL_API_STATS, init=True)
    _v: str = field(default=V, init=True)

    log_name: str = "nhl_sdk" 
    log_level: str = "DEBUG"
    lang: str = LANG
    log_file: Optional[str] = None  # None -> print only
    cache: BaseCache = field(default_factory=MemCache)  # None -> local cache

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
            lang = lang if lang is not None else config.lang,
            log_name = log_name if log_name is not None else config.log_name,
            log_level = log_level if log_level is not None else config.log_level,
            log_file = log_file if log_file is not None else config.log_file,
            cache = cache if cache is not None else config.cache,
        )
    if config_from_object: 
        config = config_from_object

    return config
