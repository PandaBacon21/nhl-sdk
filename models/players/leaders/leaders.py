"""
LEADERS OBJECT
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .player_leaders import SkaterLeaders, GoalieLeaders
from ....resources.api_web import _get_skater_leaders, _get_goalie_leaders

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class Leaders:
    def __init__(self, client: "NhlClient"):
        self._client = client

    # Add caching 
    def goalies(self, season: Optional[int] = None, game_type: Optional[int] = None, 
                categories: Optional[str] = None, limit: Optional[int] = None) -> GoalieLeaders:
        data = _get_goalie_leaders(season=season, g_type=game_type, categories=categories, limit=limit)
        leaders = data["data"]    
        return GoalieLeaders(leaders)
    
    # Add caching
    def skaters(self, season: Optional[int] = None, game_type: Optional[int] = None, 
                categories: Optional[str] = None, limit: Optional[int] = None) -> SkaterLeaders:
        data = _get_skater_leaders(season=season, g_type=game_type, categories=categories, limit=limit)
        leaders = data["data"]    
        return SkaterLeaders(leaders)