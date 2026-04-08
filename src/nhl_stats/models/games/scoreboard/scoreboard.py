"""
SCOREBOARD SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .scoreboard_result import ScoreboardResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class GameScoreboard(CacheFetchMixin):
    """
    Scoreboard sub-resource.

    Provides access to the current NHL scoreboard with games grouped by date.

    Accessed via `games.scoreboard`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.scoreboard")
        self._ttl: int = 60 * 60 * 1

    def get_scoreboard(self) -> ScoreboardResult:
        """
        Retrieve the current NHL scoreboard.
        """
        return self._fetch(
            "games:scoreboard:now",
            lambda: self._client._api.api_web.call_nhl_games.get_scoreboard_now(),
            self._logger, self._cache, self._ttl,
            ScoreboardResult.from_dict,
        )
