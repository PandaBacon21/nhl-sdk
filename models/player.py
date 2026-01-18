"""
PLAYER CLASS
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from ..resources.api_web import _get_player_info
from .bio import Bio
from .stats import Stats
from ..core.cache import CacheItem

if TYPE_CHECKING: 
    from nhl_stats.client import NhlClient

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
    def __init__(self, player_id: int, client: "NhlClient"): 
        """
        Parameters
        ----------
        data : int
            Unique player Id
        """
        self._client = client
        self._pid: int = player_id
        self._cache_key: str = f"player:{self._pid}:landing"
        self._cache_version: datetime | None = None
        self._bio: Bio | None = None
        self._stats: Stats | None = None

    def __repr__(self): 
        return f"Player(pid: {self._pid})"
    
    def __str__(self): 
        if self._bio:
            return f"{self.bio.first_name} {self.bio.last_name}, Player Id: {self._pid}" 
        else: 
            return f"Player Id: {self._pid}. Bio not yet fetched."

    def _fetch_player_landing(self) -> CacheItem:
        cached = self._check_cache(self._cache_key)
        if cached is not None:
            return cached
        
        res = _get_player_info(pid=self._pid)
        if not res["ok"]:
            raise RuntimeError(res.get("error", f"Failed to fetch player: {self._pid}"))      
        cache_item = self._client.cache.set(self._cache_key, res["data"], ttl=60 * 60 * 4)
        self._cache_version = cache_item.created_at 
        return cache_item

    def _clear(self) -> None: 
        print(f"Clearing Player {self._pid} data")
        self._cache_version = None
        self._bio = None
        self._stats = None
        print(f"Player {self._pid} data cleared")

    def _check_cache(self, cache_key: str) -> CacheItem | None: 
        cache = self._client.cache
        cached = cache.get(cache_key)
        if (cached is None) or (self._cache_version != cached.created_at): 
            return None
        return cached
    
    def refresh(self) -> None:  
        """
        Refresh player data from the NHL API.

        Clears any cached data and immediately re-fetches the
        latest player information.
        """
        self._clear()
        print(f"Refreshing data for Player {self._pid}")
        self._fetch_player_landing()    

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
            if self._check_cache(self._cache_key):
                return self._bio
        print(f"Building Bio: Player {self._pid}")
        data = self._fetch_player_landing()
        self._bio = Bio(data=data.data)
        print(f"Bio built: Player {self._pid} ")
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
            if self._check_cache(self._cache_key):
                return self._stats
        print(f"Building Stats: Player {self._pid}")
        data = self._fetch_player_landing()
        print(f"Stats built: Player {self._pid}")
        self._stats = Stats(data=data.data)
        return self._stats
    
    def raw(self) -> dict: 
        """
        Return the raw NHL API response for this player.

        This mirrors the underlying NHL endpoint response for: 
        https://api-web.nhle.com/v1/player/{playerId}/landing 
        
        Contains all fields returned by the API without additional processing.

        Returns
        -------
        dict
            Raw player data.
        """
        res = self._fetch_player_landing()
        return res.data