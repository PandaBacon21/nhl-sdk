"""
TEAM SCHEDULE SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import _check_cache
from .team_schedule_result import TeamScheduleResult, TeamMonthScheduleResult, TeamWeekScheduleResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamSchedule:
    """
    TeamSchedule sub-resource.

    Provides access to a team's full-season schedule, current or historical.

    Accessed via `teams.schedule`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.schedule")
        self._ttl: int = 60 * 60

    def get_schedule(self, team: str, season: int | None = None) -> TeamScheduleResult:
        """
        Retrieve the full-season schedule for a team.

        Args:
            team (str): Three-letter team code (e.g. ``"COL"``).
            season (int, optional): Eight-digit season identifier (e.g. ``20242025``).
                Defaults to the current season.
        """
        key = f"teams:schedule:{team}:{season or 'now'}"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_schedule(team=team, season=season)
        result = TeamScheduleResult.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get_schedule_month(self, team: str, month: str | None = None) -> TeamMonthScheduleResult:
        """
        Retrieve the monthly schedule for a team.

        Args:
            team (str): Three-letter team code (e.g. ``"COL"``).
            month (str, optional): Month in ``YYYY-MM`` format (e.g. ``"2024-11"``).
                Defaults to the current month.
        """
        key = f"teams:schedule:{team}:month:{month or 'now'}"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_schedule_month(team=team, month=month)
        result = TeamMonthScheduleResult.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get_schedule_week(self, team: str, week: str | None = None) -> TeamWeekScheduleResult:
        """
        Retrieve the weekly schedule for a team.

        Args:
            team (str): Three-letter team code (e.g. ``"COL"``).
            week (str, optional): Week start date in ``YYYY-MM-DD`` format
                (e.g. ``"2024-11-04"``). Defaults to the current week.
        """
        key = f"teams:schedule:{team}:week:{week or 'now'}"
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_teams.get_schedule_week(team=team, week=week)
        result = TeamWeekScheduleResult.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result
