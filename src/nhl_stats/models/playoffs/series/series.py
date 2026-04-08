"""
PLAYOFF SERIES SCHEDULE SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .series_result import SeriesScheduleResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class PlayoffSeriesSchedule(CacheFetchMixin):
    """
    Playoff series schedule sub-resource.

    Provides the game-by-game schedule for a specific playoff series.

    Accessed via `playoffs.series_schedule`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.playoffs.series_schedule")
        self._ttl: int = 60 * 60

    def get_series_schedule(self, season: int, series_letter: str) -> SeriesScheduleResult:
        """
        Retrieve the schedule for a specific playoff series.

        Args:
            season (int): Season in YYYYYYYY format (e.g. 20242025).
            series_letter (str): Series letter (e.g. "A", "B", "C", ...).
        """
        cache_key = f"playoffs:series:{season}:{series_letter.upper()}"
        return self._fetch(
            cache_key,
            lambda: self._client._api.api_web.call_nhl_playoffs.get_series_schedule(
                season=season, series_letter=series_letter
            ),
            self._logger, self._cache, self._ttl,
            SeriesScheduleResult.from_dict,
        )
