"""
PLAYERS COLLECTION
"""

from __future__ import annotations
from typing import Optional, Literal, TYPE_CHECKING

from ..models.player import Player

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

    PlayerType = Literal["skater", "goalie"]
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


    # def get_stat_leaders(self, player_type: PlayerType, category: StatType | None = None, season: Optional[int] = None, 
    #                   game_type: Optional[int] = None, limit: Optional[int] = None) -> dict: 
    #     """
    #     Get stat leaders
        
    #     If 'season' is included, 'gametype' must also be included, and vice versa. 
    #     player_type: PlayerType
    #     category: Optional[str] = StatType
    #     season: Optional[int] = YYYYYYYY format
    #     game_type: Optional[int] = 2 (regular season), 3 (playoff)
    #     limit: Optional[int] = default = top 5, -1 returns all
    #     """
    #     if (season is None) ^ (game_type is None):
    #         raise ValueError(f"season and game_type must be either provided together or omitted together")