"""
NHL CLIENT
"""
from .services import Players, Teams, League
from .resources import API

from .core.config import BaseConfig, _build_config
from .core.logger import NhlLogger
from .core.cache.base_cache import BaseCache
from .core.cache import init_cache


class NhlClient:
    """
    Main NHL Client

    This is the main interface for NHL Client. 
    Exposes Players and Teams collections (will expand to League, Edge, etc over time)

    """
    def __init__(self, *, config_from_object: BaseConfig | None = None, log_name: str | None = None, 
                 log_level: str | None = None, log_file: str | None = None, lang: str | None = None, 
                 cache: BaseCache | None = None) -> None: 

        self._config = _build_config(config_from_object, log_name, log_level, log_file, lang, cache)
        cache = self._config.cache 
        init_cache(cache)
        self._logger = NhlLogger(self._config)
        self.players = Players(self)
        self.teams = Teams(self)
        self.league = League(self)
        self._api = API()


        # Log Client Creation
        self._logger.debug(f"NHL Client initialized")
        self._logger.debug(f"Config - Log Name: {self._config.log_name} | Log Level: {self._config.log_level} | \
                           Log File: {self._config.log_file} | Lang: {self._config.lang} | Cache: {self._config.cache!r}")

