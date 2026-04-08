"""
DRAFT PICKS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .picks_result import DraftPicksResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class DraftPicks(CacheFetchMixin):
    """
    Draft picks sub-resource.

    Provides access to NHL draft picks for the current draft or a specific
    season and round.

    Accessed via `draft.picks`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.draft.picks")
        self._ttl: int = 60 * 60 * 6

    def get_all(self, year: int) -> DraftPicksResult:
        """
        Retrieve all picks across every round for a specific draft year.

        Parameters
        ----------
        year : int
            Draft year (e.g. 2024).
        """
        return self._fetch(
            f"draft:picks:{year}:all",
            lambda: self._client._api.api_web.call_nhl_draft.get_all_picks(year=year),
            self._logger, self._cache, self._ttl,
            DraftPicksResult.from_dict,
        )

    def get_picks(self, season: int | None = None, round: str | None = None) -> DraftPicksResult:
        """
        Retrieve draft picks.

        Without arguments returns picks for the current draft cycle.
        With both arguments returns picks for a specific season and round.

        Args:
            season (int, optional): Draft year (e.g. 2025).
            round (str, optional): Round number ("1"–"7") or "all" for all rounds.
        """
        if season and round:
            cache_key = f"draft:picks:{season}:{round}"
        else:
            cache_key = "draft:picks:now"

        return self._fetch(
            cache_key,
            lambda: self._client._api.api_web.call_nhl_draft.get_picks(season=season, round=round),
            self._logger, self._cache, self._ttl,
            DraftPicksResult.from_dict,
        )
