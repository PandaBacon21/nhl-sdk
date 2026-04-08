"""
SCORES SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .daily_score import DailyScoreResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class GameScores(CacheFetchMixin):
    """
    Scores sub-resource.

    Provides access to daily game scores for the current day or a specific date.

    Accessed via `games.scores`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.scores")
        self._ttl: int = 60 * 60 * 1

    def get_daily_scores(self, date: str | None = None) -> DailyScoreResult:
        """
        Retrieve daily game scores.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to the current day.
        """
        return self._fetch(
            f"games:scores:{date or 'now'}",
            lambda: self._client._api.api_web.call_nhl_games.get_daily_scores(date=date),
            self._logger, self._cache, self._ttl,
            DailyScoreResult.from_dict,
        )
