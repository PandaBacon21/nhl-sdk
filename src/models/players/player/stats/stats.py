"""
PLAYER STATS OBJECT
"""
from __future__ import annotations
import logging
from typing import Optional, TYPE_CHECKING

from .featured_stats import Featured
from .career_stats import Career
from .season import Season, FeaturedGame
from .games import GameLogs
from .edge import EdgeStats
from .....core.cache import get_cache
from .....core.utilities import _check_cache

if TYPE_CHECKING: 
    from nhl_stats.src.client import NhlClient

class Stats:
    """
    Player statistical sub-resource.

    Provides structured access to a player's statistical data,
    including featured stats, career totals, per-season statistics, 
    recent game performance (last 5 games), 
    and method for retreiving full season game logs. 


    Instances of this class are accessed via `Player.stats`.
    """
    def __init__(self, pid: int, data: dict, client: NhlClient):
        """
        Parameters
        ----------
        data : dict
            Raw player landing data as returned by the NHL API.
        """
        featured_stats: dict = data.get("featuredStats") or {}
        career_stats: dict = data.get("careerTotals") or {}

        self._pid = pid
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.player.stats")
        
        self._game_key: str = f"player:{pid}:game-log"
        self._ttl: int = 60 * 60 * 1

        self.featured: Featured = Featured.from_dict(featured_stats)
        self.career: Career = Career.from_dict(career_stats)
        self.seasons = [Season.from_dict(season) for season in data.get("seasonTotals") or []]
        self.last_5_games = [FeaturedGame.from_dict(game) for game in data.get("last5Games") or []]
        self.edge: EdgeStats = EdgeStats(pid=pid, client=client)

        self._logger.debug(f"{self._pid} Stats initialized")

    def game_log(self, season: Optional[int] = None, game_type: Optional[int] = 2) -> GameLogs: 
        """  
        Retreive Game Logs by Season

        If no season or game_type specified, defaults to current or most recent season (if player not currently active).
        If season specified but not game_type, game_type defaults to 2 (regular season).
        """

        if season and game_type:
            cache_key = f"{self._game_key}:{season}:{game_type}"
            cached = _check_cache(cache=self._cache, cache_key=cache_key)
            if cached is None:
                self._logger.debug(f"{cache_key}: Cache Miss")
                res = self._client._api.api_web.call_nhl_players.get_game_log(pid=self._pid, season=season, g_type=game_type)
                game_logs = GameLogs.from_dict(data=res.data)
                self._cache.set(key=cache_key, data=game_logs, ttl=self._ttl)
                self._logger.debug(f"{cache_key}: Cached | ttl: {self._ttl}")
                return game_logs
            self._logger.debug(f"{cache_key}: Cache Hit")
            return cached.data
        else:
            self._logger.debug(f"{self._game_key}:now: Cache Miss")
            res = self._client._api.api_web.call_nhl_players.get_game_log(pid=self._pid)
            cache_key = f"{self._game_key}:{res.data["seasonId"]}:{res.data["gameTypeId"]}"
            game_logs = GameLogs.from_dict(data=res.data)
            self._cache.set(key=cache_key, data=game_logs, ttl=self._ttl)
            self._logger.debug(f"{cache_key}: Cached | ttl: {self._ttl}")
            return game_logs
            
        
