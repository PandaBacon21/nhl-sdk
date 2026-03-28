"""
STANDINGS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import _check_cache
from .standings_result import StandingsResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Standings:
    """
    Standings sub-resource.

    Provides access to NHL standings as of a given date or the current moment,
    and the list of seasons for which standings are available.

    Accessed via `teams.standings`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.standings")
        self._ttl: int = 60 * 60 * 1

    def get_standings(self, date: str | None = None) -> StandingsResult:
        """
        Retrieve NHL standings.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to current standings.
        """
        key = f"teams:standings:{date or 'now'}"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_standings(date=date)
        result = StandingsResult.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get_standings_by_season(self) -> list:
        """
        Retrieve the list of seasons for which standings are available.
        """
        key = "teams:standings:seasons"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_standings_per_season()
        result = res.data
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result
