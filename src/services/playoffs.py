"""
PLAYOFFS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache import get_cache
from ..models.playoffs.carousel import PlayoffCarousel
from ..models.playoffs.series import PlayoffSeriesSchedule
from ..models.playoffs.bracket import PlayoffBracket

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Playoffs:
    """
    Playoffs Collection

    This is the primary interface for NHL Playoffs data.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.playoffs")

    @property
    def carousel(self) -> PlayoffCarousel:
        """
        Access the playoff series carousel.

        Returns a PlayoffCarousel sub-resource with methods for retrieving
        a season's playoff series overview.
        """
        return PlayoffCarousel(self._client)

    @property
    def series_schedule(self) -> PlayoffSeriesSchedule:
        """
        Access the playoff series schedule.

        Returns a PlayoffSeriesSchedule sub-resource with methods for retrieving
        the game-by-game schedule for a specific playoff series.
        """
        return PlayoffSeriesSchedule(self._client)

    @property
    def bracket(self) -> PlayoffBracket:
        """
        Access the playoff bracket.

        Returns a PlayoffBracket sub-resource with methods for retrieving
        the full bracket for a playoff year across all rounds.
        """
        return PlayoffBracket(self._client)
