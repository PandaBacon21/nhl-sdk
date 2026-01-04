"""
PLAYERS SPACE
"""

from typing import Optional, Literal
from datetime import datetime

from ..models.player import Player

class Players: 
    PlayerType = Literal["skater", "goalie"]
    StatType = Literal["goals", "goalsSh", "goalsPp", "assists", "points", "plusMinus", "faceOffLeaders", "penaltyMins", "toi"]
    
    def get(self, pid: int) -> "Player": 
        """Get player info for a specific player"""
        return Player(player_id=pid)


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