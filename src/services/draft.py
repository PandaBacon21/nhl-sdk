"""
DRAFT COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache import get_cache
from ..models.draft.rankings import DraftRankings
from ..models.draft.tracker import DraftTracker
from ..models.draft.picks import DraftPicks

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Draft:
    """
    Draft Collection

    This is the primary interface for NHL Draft data.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.draft")

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
