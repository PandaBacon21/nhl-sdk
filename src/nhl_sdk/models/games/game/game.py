"""
GAME GATEWAY OBJECT
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from ..pbp.pbp_result import PlayByPlayResult
from ..landing.landing_result import GameLandingResult
from ..boxscore.boxscore_result import GameBoxscoreResult
from ..story.story_result import GameStoryResult
from ..shifts.shift_chart import ShiftChart

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient


class Game(CacheFetchMixin):
    """
    Gateway object for a single NHL game.

    Provides access to game-specific data including play-by-play, landing,
    boxscore, story, and shift chart data, all with the game ID baked in.

    Obtained via ``client.games.get(game_id)``.
    """
    def __init__(self, client: NhlClient, game_id: int) -> None:
        self._client = client
        self._game_id = game_id
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.game")
        self._ttl: int = 60 * 60

    @property
    def game_id(self) -> int:
        """The NHL game ID this object is bound to."""
        return self._game_id

    def pbp(self) -> PlayByPlayResult:
        """
        Retrieve play-by-play data for this game.

        Returns full event data including plays, period info, and team details.
        """
        return self._fetch(
            f"games:pbp:{self._game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_play_by_play(game_id=self._game_id),
            self._logger, self._cache, self._ttl,
            PlayByPlayResult.from_dict,
        )

    def landing(self) -> GameLandingResult:
        """
        Retrieve landing data for this game.

        Returns scoring by period, three stars, and penalty information.
        """
        return self._fetch(
            f"games:landing:{self._game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_game_landing(game_id=self._game_id),
            self._logger, self._cache, self._ttl,
            GameLandingResult.from_dict,
        )

    def boxscore(self) -> GameBoxscoreResult:
        """
        Retrieve boxscore data for this game.

        Returns per-player game stats for skaters and goalies on both teams.
        """
        return self._fetch(
            f"games:boxscore:{self._game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_boxscore(game_id=self._game_id),
            self._logger, self._cache, self._ttl,
            GameBoxscoreResult.from_dict,
        )

    def story(self) -> GameStoryResult:
        """
        Retrieve game story data for this game.

        Returns scoring summary, three stars, and team-level game statistics.
        """
        return self._fetch(
            f"games:story:{self._game_id}",
            lambda: self._client._api.api_web.call_nhl_games.get_game_story(game_id=self._game_id),
            self._logger, self._cache, self._ttl,
            GameStoryResult.from_dict,
        )

    def shifts(self) -> ShiftChart:
        """
        Retrieve shift chart data for this game.

        Returns all shift entries indexed by player and period.
        """
        return self._fetch(
            f"games:shifts:{self._game_id}",
            lambda: self._client._api.api_stats.call_nhl_sdk_misc.get_shift_charts(game_id=self._game_id),
            self._logger, self._cache, self._ttl,
            lambda d: ShiftChart.from_dict(game_id=self._game_id, data=d),
        )
