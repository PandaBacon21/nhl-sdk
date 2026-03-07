"""
PLAYER CLASS
"""

from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from datetime import datetime

from ....core.utilities import _check_cache
from .bio import Bio
from .stats import Stats
from ....core.cache.cache_item import CacheItem
from ....core.cache.init_cache import get_cache

if TYPE_CHECKING: 
    from nhl_stats.src.client import NhlClient

class Player: 
    """
    Represents a single NHL player.

    A Player object provides structured access to biographical and
    statistical data for an individual player. Data is fetched lazily
    from the NHL API and cached for the lifetime of the object.

    Use `refresh()` to clear cached data and retrieve the latest
    information from the API.

    Use the Players collection to obtain Player instances.
    """
    def __init__(self, player_id: int, client: NhlClient): 
        """
        Parameters
        ----------
        player_id : int
            Unique NHL player ID.
        client : NhlClient
            NHL API client used for requests and caching.
        """
        self._client = client
        self._cache = get_cache()
        self._api_web = self._client._api.api_web
        self._logger = logging.getLogger("nhl_sdk.player")
        self._pid: int = player_id
        self._landing_key: str = f"player:{self._pid}:landing"
        self._cache_ttl: int = 60 * 60 * 4

        self._bio: Bio | None = None
        self._stats: Stats | None = None
        self._version: dict[str, datetime]= {}

        self._logger.info(f"Player object - pid: {self._pid} initialized")

    def __repr__(self): 
        """
        Return a string representation of the player.
        """
        return f"Player(pid: {self._pid})"
    
    def __str__(self): 
        """
        Return a string representation of the player.
        """
        if self._bio:
            return f"{self.bio.first_name} {self.bio.last_name}, Player Id: {self._pid}" 
        else: 
            return f"Player Id: {self._pid}. Call .bio() to retrieve name."

    def _get_player_landing(self) -> CacheItem:
        """
        Retrieve from cache or NHL landing API for the specific player
        For internal use only
        """
        cached = _check_cache(self._cache, self._landing_key)
        if cached is not None:
            self._logger.info(f"{self._landing_key}: valid and retrieved from cache")
            return cached
        self._logger.debug(f"{self._landing_key}: not cached or expired. Retrieving {self._landing_key}")
        
        res = self._api_web.call_nhl_players.get_player_landing(pid=self._pid)

        if not res.ok == True:
            self._logger.warning(f"Player pid {self._pid} failed to fetch player landing")
            raise RuntimeError(res.data["error"] or f"Failed to fetch player landing: {self._pid}")  
        cache_item = self._cache.set(self._landing_key, res.data, ttl=self._cache_ttl)
        self._logger.info(f"{self._landing_key}: set in cache | ttl: {self._cache_ttl}")
        return cache_item

    def _clear(self) -> None: 
        """
        Clear any cached data for the particular player 
        For internal use only
        """
        self._bio = None
        self._stats = None
        self._logger.info(f"Player {self._pid}:  data cleared")

    @property
    def bio(self) -> Bio:
        """
        Player biographical information.

        Returns
        -------
        Bio
            Structured biographical data such as name, birth details,
            physical attributes, position, and awards.
        """
        if self._bio:
            if _check_cache(self._cache, self._landing_key):
                return self._bio
        data = self._get_player_landing()
        self._bio = Bio.from_dict(data=data.data)
        self._logger.debug(f"{self._pid} bio retrieved")
        return self._bio 
    
    @property
    def stats(self) -> Stats:
        """
        Player statistical information.

        Returns
        -------
        Stats
            Structured access to career totals, season statistics,
            featured stats, and recent games.
        """
        if self._stats:
            if _check_cache(self._cache, self._landing_key):
                self._logger.info(f"Player: {self._pid} | Stats retrieved from cache")
                return self._stats
        data = self._get_player_landing()
        self._stats = Stats(pid=self._pid, data=data.data, client=self._client)
        self._logger.debug(f"{self._pid} stats retrieved")
        return self._stats
    
    def refresh(self) -> None:  
        """
        Refresh player data from the NHL API.

        Clears any cached data and immediately re-fetches the
        latest player information.
        """
        self._clear()
        self._logger.info(f"Refreshing data for Player {self._pid}")
        self._get_player_landing()    