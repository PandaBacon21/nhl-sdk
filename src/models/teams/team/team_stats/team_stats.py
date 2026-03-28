"""
TEAM STATS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import _check_cache
from .team_stats_result import TeamStatsResult
from .team_season_game_types import TeamSeasonGameTypes
from .team_scoreboard import TeamScoreboard

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamStats:
    """
    TeamStats sub-resource.

    Provides access to per-team skater and goalie stats, season/game-type
    metadata, and the current team scoreboard.

    Accessed via `teams.stats`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.stats")
        self._ttl: int = 60 * 60 * 1

    def get_team_stats(
        self,
        team: str,
        season: int | None = None,
        g_type: int | None = None,
    ) -> TeamStatsResult:
        """
        Retrieve skater and goalie stats for a specific club.

        Args:
            team (str): Three-letter team code (e.g. ``"TOR"``).
            season (int, optional): Season in YYYYYYYY format. Defaults to current season.
            g_type (int, optional): Game type (e.g. ``2`` for regular season). Required when ``season`` is provided.
        """
        if season and g_type:
            key = f"teams:stats:{team}:{season}:{g_type}"
        else:
            key = f"teams:stats:{team}:now"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_team_stats(team=team, season=season, g_type=g_type)
        result = TeamStatsResult.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get_game_types_per_season(self, team: str) -> list[TeamSeasonGameTypes]:
        """
        Retrieve the list of seasons and game types available for a club.

        Args:
            team (str): Three-letter team code (e.g. ``"TOR"``).
        """
        key = f"teams:stats:{team}:seasons"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_game_types_per_season(team=team)
        result = [TeamSeasonGameTypes.from_dict(s) for s in res.data or []]
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get_team_scoreboard(self, team: str) -> TeamScoreboard:
        """
        Retrieve the current scoreboard for a specific club.

        Args:
            team (str): Three-letter team code (e.g. ``"TOR"``).
        """
        key = f"teams:scoreboard:{team}:now"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_team_scoreboard(team=team)
        result = TeamScoreboard.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result
