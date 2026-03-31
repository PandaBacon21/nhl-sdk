"""
GAME LANDING SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .landing_result import GameLandingResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GameLanding(CacheFetchMixin):
    """
    Game landing sub-resource.

    Provides access to game summary data including scoring by period,
    three stars, and penalties for a specific game.

    Accessed via `games.landing`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.landing")
        self._ttl: int = 60 * 60 * 1

    def get_landing(self, game_id: int) -> GameLandingResult:
        """
        Retrieve landing data for a specific game.

        Args:
            game_id (int): Unique NHL game ID.
        """
        return self._fetch(
            f"games:landing:{game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_game_landing(game_id=game_id),
            self._logger, self._cache, self._ttl,
            GameLandingResult.from_dict,
        )
