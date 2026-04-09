"""
GAMES COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache import get_cache
from ..core.utilities import CacheFetchMixin
from ..models.games.game import Game
from ..models.games.streams import GameStreams
from ..models.games.network import GameNetwork
from ..models.games.scores import GameScores
from ..models.games.scoreboard import GameScoreboard
from ..models.games.odds import PartnerOdds

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient


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

    def get(self, game_id: int) -> Game:
        """
        Return a Game object for the given game ID.

        Provides access to play-by-play, landing, boxscore, story, and
        shift chart data for a specific game, all with the game ID baked in.

        Parameters
        ----------
        game_id : int
            NHL game ID (e.g. 2024020001).
        """
        return Game(self._client, game_id)

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
    def odds(self) -> PartnerOdds:
        """
        Access partner betting odds for games in a specific country.

        Returns a PartnerOdds sub-resource with methods for retrieving
        current odds by country code.
        """
        return PartnerOdds(self._client)

    @property
    def streams(self) -> GameStreams:
        """
        Access NHL where-to-watch streaming information.

        Returns a GameStreams sub-resource with a get() method.
        Note: this endpoint may be region-restricted.
        """
        return GameStreams(self._client)

    def query(
        self,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        """
        Query raw game records from the NHL Stats API.

        Returns game records filterable via cayenneExp expressions.

        Parameters
        ----------
        cayenne_exp : str | None
            Filter expression (e.g. ``"season=20232024 and gameType=2"``).
        sort : str | None
            Field to sort by.
        dir : str | None
            Sort direction ("ASC" or "DESC").
        start : int | None
            Pagination offset.
        limit : int | None
            Maximum results (-1 for all).
        """
        key = f"games:query:{cayenne_exp or 'all'}:{sort}:{start}:{limit}"
        return self._fetch(
            key,
            lambda: self._client._api.api_stats.call_nhl_sdk_games.get_game(
                cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
            ),
            self._logger, self._cache, self._ttl,
            lambda d: d.get("data") or [],
        )
