"""
FUNCTIONS FOR RETRIEVING PLAYER DATA FROM API-WEB.NHLE.COM/
"""

from __future__ import annotations
from typing import Optional

from ...core.config import V
from ...core.transport import APICallWeb, APIResponse

# ==========================================================================
# PLAYER INFORMATION
# ==========================================================================

class CallNhlPlayers:
    def __init__(self, http: APICallWeb): 
        self._http = http

    # ==========================================================================
    # PLAYERS
    # ==========================================================================

    def get_player_landing(self, pid: int) -> APIResponse: 
        """
        Retrieve information for a specific player.
        """
        endpoint = f"/{V}/player/{pid}/landing"
        # player_info: dict = _call_apiget(endpoint=endpoint)
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res


    def get_game_log(self, pid: int, season: Optional[int] = None, g_type: Optional[int] = None) -> APIResponse:
        """
        Retrieve the game log for a specific player, season, and game type.
        """
        endpoint = f"/{V}/player/{pid}/game-log/now"
        if season and g_type:
            endpoint = f"/{V}/player/{pid}/game-log/{season}/{g_type}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res


    def get_player_spotlight(self) -> APIResponse:
        """
        Retrieve information about players in the "spotlight".
        """
        endpoint = f"/{V}/player-spotlight"
        res: APIResponse= self._http.get(endpoint=endpoint)
        # print(spotlight)
        return res
        
    # ==========================================================================
    # SKATERS
    # ==========================================================================

    def get_skater_leaders(self, season: Optional[int] = None, g_type: Optional[int] = None, categories: Optional[str] = None, 
                            limit: Optional[int] = None) -> APIResponse:
        """
        Retrieve current skater stats leaders.
        """
        params: dict = {}
        endpoint = f"/{V}/skater-stats-leaders/current"

        if season and g_type: 
            endpoint = f"/{V}/skater-stats-leaders/{season}/{g_type}"

        if categories is not None:
            params["categories"] = categories
        if limit is not None:
            params["limit"] = limit

        res: APIResponse = self._http.get(endpoint=endpoint, params=params)
        return res

    # ==========================================================================
    # GOALIES
    # ==========================================================================

    def get_goalie_leaders(self, season: Optional[int] = None, g_type: Optional[int] = None, 
                            categories: Optional[str] = None, limit: Optional[int] = None) -> APIResponse: 
        """
        Retrieve current goalie stats leaders
        """
        params: dict = {}
        endpoint = f"/{V}/goalie-stats-leaders/current"

        if season and g_type: 
            endpoint = f"/{V}/goalie-stats-leaders/{season}/{g_type}"

        if categories is not None:
            params["categories"] = categories
        if limit is not None: 
            params["limit"] = limit

        res: APIResponse = self._http.get(endpoint=endpoint, params=params)
        return res
