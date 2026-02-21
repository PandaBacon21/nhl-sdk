"""
PLAYERS COLLECTION
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

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
        self._ttl: int = 60 * 60 * 6

    def get(self, pid: int) -> Player: 
        """
        Return a Player object for the given NHL player ID.
        
        Parameters
        ----------
        data : int
            Unique player Id
        """
        return Player(player_id=pid, client=self._client)

    @property
    def spotlight(self) -> list[Spotlight]:
        """
        Return a list of currently Spotlighted Players 
        """
        spotlight_key: str = f"players:spotlight"
        
        cached = self._client.cache.get(spotlight_key)
        if cached is not None: 
            return cached.data
        data = self._client._api.api_web.call_nhl_players.get_player_spotlight()
        players = data.data
        print("Building Spotlight")
        spotlight = [Spotlight(player) for player in players or []]

        self._client.cache.set(key=spotlight_key, data=spotlight, ttl=self._ttl)
        print(f"{spotlight_key} cached: {datetime.now()}")
        return spotlight
    
    @property
    def leaders(self) -> Leaders: 
        """
        Return leaders of various statistics for skaters and goalies
        """
        return Leaders(self._client)

