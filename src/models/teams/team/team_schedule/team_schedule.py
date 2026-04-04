"""
TEAM SCHEDULE SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_schedule_result import TeamScheduleResult, TeamMonthScheduleResult, TeamWeekScheduleResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamSchedule(CacheFetchMixin):
    """
    TeamSchedule sub-resource.

    Provides access to a team's full-season schedule, current or historical.

    Accessed via ``team.schedule`` on a ``Team`` object.
    """
    def __init__(self, client: NhlClient, abbrev: str) -> None:
        self._client = client
        self._abbrev = abbrev
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.schedule")
        self._ttl: int = 60 * 60

    def get_schedule(self, season: int | None = None) -> TeamScheduleResult:
        """
        Retrieve the full-season schedule for the team.

        Args:
            season (int, optional): Eight-digit season identifier (e.g. ``20242025``).
                Defaults to the current season.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:schedule:{team}:{season or 'now'}",
            lambda: self._client._api.api_web.call_nhl_teams.get_schedule(team=team, season=season),
            self._logger, self._cache, self._ttl,
            TeamScheduleResult.from_dict,
        )

    def get_schedule_month(self, month: str | None = None) -> TeamMonthScheduleResult:
        """
        Retrieve the monthly schedule for the team.

        Args:
            month (str, optional): Month in ``YYYY-MM`` format (e.g. ``"2024-11"``).
                Defaults to the current month.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:schedule:{team}:month:{month or 'now'}",
            lambda: self._client._api.api_web.call_nhl_teams.get_schedule_month(team=team, month=month),
            self._logger, self._cache, self._ttl,
            TeamMonthScheduleResult.from_dict,
        )

    def get_schedule_week(self, week: str | None = None) -> TeamWeekScheduleResult:
        """
        Retrieve the weekly schedule for the team.

        Args:
            week (str, optional): Week start date in ``YYYY-MM-DD`` format
                (e.g. ``"2024-11-04"``). Defaults to the current week.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:schedule:{team}:week:{week or 'now'}",
            lambda: self._client._api.api_web.call_nhl_teams.get_schedule_week(team=team, week=week),
            self._logger, self._cache, self._ttl,
            TeamWeekScheduleResult.from_dict,
        )
