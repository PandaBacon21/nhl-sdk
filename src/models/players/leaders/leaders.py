"""
LEADERS OBJECT
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from datetime import datetime

from .player_leaders import SkaterLeaders, GoalieLeaders
from ....core.utilities import _check_cache

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Leaders:
    """
    Access NHL statistical leaders.

    This class provides helper methods for retrieving league leaders
    for both skaters and goalies, with optional season, game type,
    category filtering, and result limits.
    """
    def __init__(self, client: NhlClient):
        """
        Initialize the Leaders API helper.

        Args:
            client (NhlClient): Shared NHL API client instance used for accessing the cache.
        """
        self._client = client
        self._ttl: int = 60*60*2

    def _cache_key(self, position: str, season: Optional[int] = None, game_type: Optional[int] = None, 
                categories: Optional[str] = None, limit: Optional[int] = None) -> str: 
        """
        Generate a cache key for leader queries.
        
        For internal use only
        """
        if season and game_type and categories and limit: 
            return f"leaders:{season}:{position}:{game_type}:{categories}:{limit}"
        if season and game_type and categories: 
            return f"leaders:{season}:{position}:{game_type}:{categories}"
        if season and game_type:
            return f"leaders:{season}:{position}:{game_type}"
        if season:
            return f"leaders:{season}:{position}:now"
        return f"leaders:{position}:now"


    def goalies(self, season: Optional[int] = None, game_type: Optional[int] = None, 
                categories: Optional[str] = None, limit: Optional[int] = None) -> GoalieLeaders:
        """
        Retrieve goalie statistical leaders.
        No season and game_type retreives current leaders

        Args:
            season (int, optional): NHL season (e.g. 20232024).
            game_type (int, optional): 2 - regular season, 3 - playoffs.
            categories (str, optional): example, wins.
            limit (int, optional): Maximum number of goalies to return.
        """
        cache_key = self._cache_key("g", season, game_type, categories, limit)
        cached = _check_cache(cache=self._client.cache, cache_key=cache_key)
        if cached is None: 
            print(f"{cache_key} not in cache or expired")
            data = self._client._api.api_web.call_nhl_players.get_goalie_leaders(season=season, g_type=game_type, categories=categories, limit=limit)
            leaders = GoalieLeaders(data.data, client=self._client)
            self._client.cache.set(cache_key, leaders, self._ttl)
            print(f"{cache_key} cached: {datetime.now()}")
            return leaders  
        print(f"{cache_key} returned from cache")
        return cached.data


    def skaters(self, season: Optional[int] = None, game_type: Optional[int] = None, 
                categories: Optional[str] = None, limit: Optional[int] = None) -> SkaterLeaders:
        """
        Retrieve skater statistical leaders. 
        No season and game_type retreives current leaders

        Args:
            season (int, optional): NHL season (e.g. 20232024).
            game_type (int, optional): 2 - regular season, 3 - playoffs.
            categories (str, optional): example, goals
            limit (int, optional): Maximum number of skaters to return.
        """
        cache_key = self._cache_key("s", season, game_type, categories, limit)
        cached = _check_cache(cache=self._client.cache, cache_key=cache_key)
        if cached is None:
            print(f"{cache_key} not in cache or expired")
            data = self._client._api.api_web.call_nhl_players.get_skater_leaders(season=season, g_type=game_type, categories=categories, limit=limit)
            leaders = SkaterLeaders(data.data, client=self._client)
            self._client.cache.set(cache_key, leaders, self._ttl)
            print(f"{cache_key} cached: {datetime.now()}")
            return leaders  
        print(f"{cache_key} returned from cache")
        return cached.data