"""
PLAYERS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.utilities import _check_cache
from ..core.cache import get_cache
from ..models.players import Spotlight, Leaders, Player

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class Players:
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
        self._spotlight_key: str = "players:spotlight"

    def _fetch(self, key: str, api_fn, builder):
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = api_fn()
        result = builder(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def get(self, pid: int) -> Player:
        """
        Return a Player object for the given NHL player ID.

        Parameters
        ----------
        data : int
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
            self._spotlight_key,
            lambda: self._client._api.api_web.call_nhl_players.get_player_spotlight(),
            lambda d: [Spotlight.from_dict(p) for p in d or []],
        )

    @property
    def leaders(self) -> Leaders:
        """
        Return leaders of various statistics for skaters and goalies
        """
        self._logger.debug(f"Retrieve Players Leaders")
        return Leaders(self._client)
