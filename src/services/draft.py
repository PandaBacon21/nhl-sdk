"""
DRAFT COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache import get_cache
from ..core.utilities import CacheFetchMixin
from ..models.draft.rankings import DraftRankings
from ..models.draft.tracker import DraftTracker
from ..models.draft.picks import DraftPicks

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Draft(CacheFetchMixin):
    """
    Draft Collection

    This is the primary interface for NHL Draft data.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.draft")
        self._ttl: int = 60 * 60 * 6

    @property
    def rankings(self) -> DraftRankings:
        """
        Access NHL draft prospect rankings.

        Returns a DraftRankings sub-resource with methods for retrieving
        current midterm rankings or rankings for a specific draft year and category.
        """
        return DraftRankings(self._client)

    @property
    def tracker(self) -> DraftTracker:
        """
        Access the live NHL draft tracker.

        Returns a DraftTracker sub-resource with methods for retrieving
        the current round's picks and draft state.
        """
        return DraftTracker(self._client)

    @property
    def picks(self) -> DraftPicks:
        """
        Access NHL draft pick data.

        Returns a DraftPicks sub-resource with methods for retrieving
        picks for the current draft or a specific season and round.
        """
        return DraftPicks(self._client)

    def query(
        self,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        """
        Query NHL draft data from the NHL Stats API.

        Returns raw draft records filterable via cayenneExp expressions.
        Useful for querying historical draft data by year, round, team, etc.

        Parameters
        ----------
        cayenne_exp : str | None
            Filter expression (e.g. ``"draftYear=2023"``).
        sort : str | None
            Field to sort by.
        dir : str | None
            Sort direction ("ASC" or "DESC").
        start : int | None
            Pagination offset.
        limit : int | None
            Maximum results (-1 for all).
        """
        key = f"draft:query:{cayenne_exp or 'all'}:{sort}:{start}:{limit}"
        return self._fetch(
            key,
            lambda: self._client._api.api_stats.call_nhl_stats_draft.get_draft(
                cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
            ),
            self._logger, self._cache, self._ttl,
            lambda d: d.get("data") or [],
        )
