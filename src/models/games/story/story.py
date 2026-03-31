"""
GAME STORY SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .story_result import GameStoryResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GameStory(CacheFetchMixin):
    """
    Game story sub-resource.

    Provides access to game story data including scoring summary,
    three stars, and team-level game stats for a specific game.

    Accessed via `games.story`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.story")
        self._ttl: int = 60 * 60 * 1

    def get_game_story(self, game_id: int) -> GameStoryResult:
        """
        Retrieve game story data for a specific game.

        Args:
            game_id (int): Unique NHL game ID.
        """
        return self._fetch(
            f"games:story:{game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_game_story(game_id=game_id),
            self._logger, self._cache, self._ttl,
            GameStoryResult.from_dict,
        )
