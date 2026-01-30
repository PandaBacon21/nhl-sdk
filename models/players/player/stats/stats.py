"""
PLAYER STATS OBJECT
"""
from typing import Optional, TYPE_CHECKING

from .featured_stats import Featured
from .career_stats import Career
from .season import Season, FeaturedGame
from .games import GameLogs
from .....resources.api_web import _get_game_log
from .....core.cache import CacheItem

if TYPE_CHECKING: 
    from nhl_stats.client import NhlClient

class Stats:
    """
    Player statistical sub-resource.

    Provides structured access to a player's statistical data,
    including featured stats, career totals, per-season statistics, 
    recent game performance (last 5 games), 
    and method for retreiving full season game logs. 


    Instances of this class are accessed via `Player.stats`.
    """
    def __init__(self, pid: int, data: dict, client: "NhlClient"):
        """
        Parameters
        ----------
        data : dict
            Raw player data as returned by the NHL API.
        """
        featured_stats: dict = data.get("featuredStats") or {}
        career_stats: dict = data.get("careerTotals") or {}

        self._pid = pid
        self._client = client
        self._game_key: str = f"player:{pid}:game-log"
        self._ttl: int = 60*60*4

        self.featured: Featured = Featured(featured_stats)
        self.career: Career = Career(career_stats)
        self.seasons = [Season(season) for season in data.get("seasonTotals") or []]
        self.last_5_games = [FeaturedGame(game) for game in data.get("last5Games") or []]

    def _check_cache(self, cache_key: str) -> CacheItem | None: 
        cache = self._client.cache
        cached = cache.get(cache_key)
        if cached is None:
            return None
        return cached

    def game_log(self, season: Optional[int] = None, game_type: Optional[int] = 2) -> GameLogs: 
        """  
        Retreive Game Logs by Season

        If no season or game_type specified, defaults to current or most recent season (if player not currently active).
        If season specified but not game_type, game_type defaults to 2 (regular season).
        """
        
        # Need to update caching
        
        if season and game_type:
            cache_key = f"{self._game_key}:{season}:{game_type}"
            cached = self._check_cache(cache_key=cache_key)
            if cached is None:
                print(f"{cache_key} no yet cached")
                res = _get_game_log(pid=self._pid, season=season, g_type=game_type)
                game_logs = GameLogs(data=res["data"])
                self._client.cache.set(key=cache_key, data=game_logs, ttl=self._ttl)
                return game_logs
            return cached.data
        else: 
            res = _get_game_log(pid=self._pid)
            key = f"{self._game_key}:{res["data"]["seasonId"]}:{res["data"]["gameTypeId"]}"
            game_logs = GameLogs(data=res["data"])
            self._client.cache.set(key=key, data=game_logs, ttl=self._ttl)
            return game_logs
            
        
