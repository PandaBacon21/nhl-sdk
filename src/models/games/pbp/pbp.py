"""
PLAY-BY-PLAY SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .pbp_result import PlayByPlayResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GamePlayByPlay(CacheFetchMixin):
    """
    Play-by-play sub-resource.

    Provides access to full play-by-play event data for a specific game.

    Accessed via `games.pbp`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.pbp")
        self._ttl: int = 60 * 60 * 1

    def get_play_by_play(self, game_id: int) -> PlayByPlayResult:
        """
        Retrieve play-by-play data for a specific game.

        Args:
            game_id (int): Unique NHL game ID.
        """
        return self._fetch(
            f"games:pbp:{game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_play_by_play(game_id=game_id),
            self._logger, self._cache, self._ttl,
            PlayByPlayResult.from_dict,
        )
