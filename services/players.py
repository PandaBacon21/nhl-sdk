"""
PLAYERS COLLECTION
"""

from __future__ import annotations
from typing import Optional, Literal, TYPE_CHECKING
from datetime import datetime

from ..models.player import Player
from ..models.players import Spotlight, Leaders
from ..resources.api_web import _get_player_spotlight

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient

class Players: 
    """
    Players Collection

    This is the primary interface for player related data. 

    This interface exposes methods for retrieving individual Player
    objects and access player-related aggregates such as stat leaders.

    """
    def __init__(self, client:"NhlClient"):
        self._client = client
        self.leaders: Leaders = Leaders(self._client)
        self._spotlight_key = f"players:spotlight"
        self._ttl: int = 60 * 60 * 12

    PlayerType = Literal["s", "g"]
    StatType = Literal["goals", "goalsSh", "goalsPp", "assists", "points", "plusMinus", "faceOffLeaders", "penaltyMins", "toi"]
    
    def get(self, pid: int) -> "Player": 
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
        cached = self._client.cache.get(self._spotlight_key)
        if cached is not None: 
            return cached.data
        data = _get_player_spotlight()
        players = data["data"]
        print("Building Spotlight")
        spotlight = [Spotlight(player) for player in players or []]
        
        self._client.cache.set(key=self._spotlight_key, data=spotlight, ttl=self._ttl)
        print(f"spotlight cached: {datetime.now()}")
        return spotlight