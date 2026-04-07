"""
GAMES COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache import get_cache
from ..core.utilities import CacheFetchMixin
from ..models.games.shifts import GameShifts
from ..models.games.network import GameNetwork
from ..models.games.scores import GameScores
from ..models.games.scoreboard import GameScoreboard
from ..models.games.pbp import GamePlayByPlay
from ..models.games.landing import GameLanding
from ..models.games.boxscore import GameBoxscore
from ..models.games.story import GameStory
from ..models.games.odds import PartnerOdds

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Games(CacheFetchMixin):
    """
    Games Collection

    This is the primary interface for game-related data.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games")
        self._ttl: int = 60 * 60

    @property
    def network(self) -> GameNetwork:
        """
        Access NHL Network broadcast schedule data.

        Returns a GameNetwork sub-resource with methods for the current or
        historical TV broadcast schedule.
        """
        return GameNetwork(self._client)

    @property
    def scores(self) -> GameScores:
        """
        Access daily game score data.

        Returns a GameScores sub-resource with methods for current or
        historical daily scores including goals and clock state.
        """
        return GameScores(self._client)

    @property
    def scoreboard(self) -> GameScoreboard:
        """
        Access the current NHL scoreboard.

        Returns a GameScoreboard sub-resource with games grouped by date.
        """
        return GameScoreboard(self._client)

    @property
    def pbp(self) -> GamePlayByPlay:
        """
        Access play-by-play data for a specific game.

        Returns a GamePlayByPlay sub-resource with methods for retrieving
        full event data for a game by ID.
        """
        return GamePlayByPlay(self._client)

    @property
    def landing(self) -> GameLanding:
        """
        Access game landing data for a specific game.

        Returns a GameLanding sub-resource with methods for retrieving
        scoring by period, three stars, and penalties for a game by ID.
        """
        return GameLanding(self._client)

    @property
    def boxscore(self) -> GameBoxscore:
        """
        Access boxscore data for a specific game.

        Returns a GameBoxscore sub-resource with per-player stats for
        forwards, defense, and goalies for both teams.
        """
        return GameBoxscore(self._client)

    @property
    def story(self) -> GameStory:
        """
        Access game story data for a specific game.

        Returns a GameStory sub-resource with methods for retrieving
        scoring summary, three stars, and team game stats for a game by ID.
        """
        return GameStory(self._client)

    @property
    def odds(self) -> PartnerOdds:
        """
        Access partner betting odds for games in a specific country.

        Returns a PartnerOdds sub-resource with methods for retrieving
        current odds by country code.
        """
        return PartnerOdds(self._client)

    @property
    def shifts(self) -> GameShifts:
        """
        Access shift chart data for a specific game.

        Returns a GameShifts sub-resource with a get(game_id) method.
        """
        return GameShifts(self._client)
