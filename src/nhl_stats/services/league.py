"""
LEAGUE COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.utilities import CacheFetchMixin
from ..core.cache import get_cache
from ..models.league.league_schedule import LeagueScheduleResult
from ..models.league.league_calendar import LeagueCalendarResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class League(CacheFetchMixin):
    """
    League Collection

    This is the primary interface for league-wide data.

    Provides access to the league schedule and schedule calendar.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.league")
        self._ttl: int = 60 * 60 * 1

    def get_schedule(self, date: str | None = None) -> LeagueScheduleResult:
        """
        Retrieve the league-wide schedule.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to the current week.
        """
        return self._fetch(
            f"league:schedule:{date or 'now'}",
            lambda: self._client._api.api_web.call_nhl_league.get_schedule(date=date),
            self._logger, self._cache, self._ttl,
            LeagueScheduleResult.from_dict,
        )

    def get_schedule_calendar(self, date: str | None = None) -> LeagueCalendarResult:
        """
        Retrieve the league schedule calendar.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to the current window.
        """
        return self._fetch(
            f"league:calendar:{date or 'now'}",
            lambda: self._client._api.api_web.call_nhl_league.get_schedule_calendar(date=date),
            self._logger, self._cache, self._ttl,
            LeagueCalendarResult.from_dict,
        )

    def get_seasons(self) -> list[int]:
        """
        Retrieve the list of all NHL season IDs, past and present.
        """
        return self._fetch(
            "league:seasons",
            lambda: self._client._api.api_web.call_nhl_seasons.get_seasons(),
            self._logger, self._cache, self._ttl,
            lambda d: d or [],
        )

    def get_season_details(self) -> list[dict]:
        """
        Retrieve detailed season metadata from the NHL Stats API.

        Returns a list of season records with start/end dates and other
        metadata not available from the standard seasons endpoint.
        """
        return self._fetch(
            "league:season-details",
            lambda: self._client._api.api_stats.call_nhl_stats_seasons.get_season(),
            self._logger, self._cache, self._ttl,
            lambda d: d.get("data") or [],
        )

    def get_component_season(self) -> list[dict]:
        """
        Retrieve component season information from the NHL Stats API.

        Returns metadata about the structural components of the current season.
        """
        return self._fetch(
            "league:component-season",
            lambda: self._client._api.api_stats.call_nhl_stats_seasons.get_component_season(),
            self._logger, self._cache, self._ttl,
            lambda d: d.get("data") or [],
        )
