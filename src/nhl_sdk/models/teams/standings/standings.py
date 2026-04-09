"""
STANDINGS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .standings_result import StandingsResult

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient


class Standings(CacheFetchMixin):
    """
    Standings sub-resource.

    Provides access to NHL standings as of a given date or the current moment,
    and the list of seasons for which standings are available.

    Accessed via ``client.teams.standings``.
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
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_teams.get_standings(date=date),
            self._logger, self._cache, self._ttl,
            StandingsResult.from_dict,
        )

    def get_standings_by_season(self) -> list:
        """
        Retrieve the list of seasons for which standings are available.
        """
        return self._fetch(
            "teams:standings:seasons",
            lambda: self._client._api.api_web.call_nhl_teams.get_standings_per_season(),
            self._logger, self._cache, self._ttl,
        )
