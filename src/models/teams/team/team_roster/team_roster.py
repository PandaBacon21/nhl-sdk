"""
TEAM ROSTER SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import _check_cache
from .team_prospects import ProspectsResult
from .team_roster_result import TeamRosterResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamRoster:
    """
    TeamRoster sub-resource.

    Provides access to team roster data including current/historical rosters,
    season availability, and prospects.

    Accessed via `teams.roster`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.roster")
        self._ttl: int = 60 * 60 * 6

    def get_team_prospects(self, team: str) -> ProspectsResult:
        """
        Retrieve the prospect list for a specific club.

        Args:
            team (str): Three-letter team code (e.g. ``"COL"``).
        """
        key = f"teams:roster:{team}:prospects"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_team_prospects(team=team)
        result = ProspectsResult.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get_team_roster(self, team: str, season: int | None = None) -> TeamRosterResult:
        """
        Retrieve the roster for a specific team.

        Args:
            team (str): Three-letter team code (e.g. ``"COL"``).
            season (int, optional): Eight-digit season identifier (e.g. ``20242025``).
                Defaults to the current roster.
        """
        key = f"teams:roster:{team}:{season or 'now'}"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_team_roster(team=team, season=season)
        result = TeamRosterResult.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get_roster_seasons(self, team: str) -> list[int]:
        """
        Retrieve the list of seasons for which a team has roster data.

        Args:
            team (str): Three-letter team code (e.g. ``"COL"``).
        """
        key = f"teams:roster:{team}:seasons"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_roster_season_by_team(team=team)
        result: list[int] = res.data or []
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result
