"""
DRAFT RANKINGS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .rankings_result import DraftRankingsResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class DraftRankings(CacheFetchMixin):
    """
    Draft rankings sub-resource.

    Provides access to NHL draft prospect rankings by category,
    for the current cycle or a specific draft year.

    Accessed via `draft.rankings`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.draft.rankings")
        self._ttl: int = 60 * 60 * 6

    def get_rankings(self, season: int | None = None, category: int | None = None) -> DraftRankingsResult:
        """
        Retrieve draft prospect rankings.

        Without arguments returns current midterm rankings across all categories.
        With both arguments returns rankings for a specific draft year and category.

        Args:
            season (int, optional): Draft year (e.g. 2026).
            category (int, optional): Category ID (1=NA Skater, 2=Intl Skater,
                3=NA Goalie, 4=Intl Goalie).
        """
        if season and category:
            cache_key = f"draft:rankings:{season}:{category}"
        else:
            cache_key = "draft:rankings:now"

        return self._fetch(
            cache_key,
            lambda: self._client._api.api_web.call_nhl_draft.get_rankings(season=season, category=category),
            self._logger, self._cache, self._ttl,
            DraftRankingsResult.from_dict,
        )
