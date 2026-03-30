"""
PLAYERS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.utilities import CacheFetchMixin
from ..core.cache import get_cache
from ..models.players import Spotlight, Leaders, Player

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class Players(CacheFetchMixin):
    """
    Players Collection

    This is the primary interface for player related data.

    This interface exposes methods for retrieving individual Player
    objects and access player-related aggregates such as stat leaders.

    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.players")
        self._ttl: int = 60 * 60 * 6

    def get(self, pid: int) -> Player:
        """
        Return a Player object for the given NHL player ID.

        Parameters
        ----------
        pid : int
            Unique player Id
        """
        self._logger.debug(f"GET Player({pid})")
        return Player(player_id=pid, client=self._client)

    @property
    def spotlight(self) -> list[Spotlight]:
        """
        Return a list of currently Spotlighted Players
        """
        return self._fetch(
            "players:spotlight",
            lambda: self._client._api.api_web.call_nhl_players.get_player_spotlight(),
            self._logger, self._cache, self._ttl,
            lambda d: [Spotlight.from_dict(p) for p in d or []],
        )

    @property
    def leaders(self) -> Leaders:
        """
        Return leaders of various statistics for skaters and goalies
        """
        self._logger.debug("Retrieve Players Leaders")
        return Leaders(self._client)
