"""
GAME BOXSCORE SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .boxscore_result import GameBoxscoreResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GameBoxscore(CacheFetchMixin):
    """
    Game boxscore sub-resource.

    Provides access to per-player game stats (skaters and goalies) for
    both teams in a specific game.

    Accessed via `games.boxscore`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.boxscore")
        self._ttl: int = 60 * 60 * 1

    def get_boxscore(self, game_id: int) -> GameBoxscoreResult:
        """
        Retrieve boxscore data for a specific game.

        Args:
            game_id (int): Unique NHL game ID.
        """
        return self._fetch(
            f"games:boxscore:{game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_boxscore(game_id=game_id),
            self._logger, self._cache, self._ttl,
            GameBoxscoreResult.from_dict,
        )
