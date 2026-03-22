"""
LEADERS OBJECT
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING, Optional

from .player_leaders import SkaterLeaders, GoalieLeaders
from ....core.utilities import _check_cache
from ....core.cache import get_cache

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Leaders:
    """
    Access NHL statistical leaders.

    This class provides helper methods for retrieving league leaders
    for both skaters and goalies, with optional season, game type,
    category filtering, and result limits.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.leaders")
        self._ttl: int = 60 * 60 * 1

    def _cache_key(self, position: str, season: Optional[int] = None, game_type: Optional[int] = None,
                   categories: Optional[str] = None, limit: Optional[int] = None) -> str:
        key = f"leaders:{position}"
        key += f":{season}" if season else ":now"
        if game_type:
            key += f":{game_type}"
        if categories:
            key += f":{categories}"
        if limit:
            key += f":{limit}"
        return key

    def _fetch(self, cache_key: str, api_fn, model_cls):
        cached = _check_cache(cache=self._cache, cache_key=cache_key)
        if cached is not None:
            self._logger.debug(f"{cache_key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{cache_key}: Cache Miss")
        res = api_fn()
        result = model_cls(res.data, client=self._client)
        self._cache.set(cache_key, result, self._ttl)
        self._logger.debug(f"{cache_key}: Cached | ttl: {self._ttl}")
        return result

    def goalies(self, season: Optional[int] = None, game_type: Optional[int] = None,
                categories: Optional[str] = None, limit: Optional[int] = None) -> GoalieLeaders:
        """
        Retrieve goalie statistical leaders.
        No season and game_type retrieves current leaders.

        Args:
            season (int, optional): NHL season (e.g. 20232024).
            game_type (int, optional): 2 - regular season, 3 - playoffs.
            categories (str, optional): example, wins.
            limit (int, optional): Maximum number of goalies to return.
        """
        cache_key = self._cache_key("g", season, game_type, categories, limit)
        return self._fetch(
            cache_key,
            lambda: self._client._api.api_web.call_nhl_players.get_goalie_leaders(
                season=season, g_type=game_type, categories=categories, limit=limit
            ),
            GoalieLeaders,
        )

    def skaters(self, season: Optional[int] = None, game_type: Optional[int] = None,
                categories: Optional[str] = None, limit: Optional[int] = None) -> SkaterLeaders:
        """
        Retrieve skater statistical leaders.
        No season and game_type retrieves current leaders.

        Args:
            season (int, optional): NHL season (e.g. 20232024).
            game_type (int, optional): 2 - regular season, 3 - playoffs.
            categories (str, optional): example, goals.
            limit (int, optional): Maximum number of skaters to return.
        """
        cache_key = self._cache_key("s", season, game_type, categories, limit)
        return self._fetch(
            cache_key,
            lambda: self._client._api.api_web.call_nhl_players.get_skater_leaders(
                season=season, g_type=game_type, categories=categories, limit=limit
            ),
            SkaterLeaders,
        )
