"""
FUNCTIONS FOR RETRIEVING PLAYER DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from nhl_stats.core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# PLAYER INFORMATION
# ==========================================================================

# ==========================================================================
# PLAYERS
# ==========================================================================

def _get_player_info(pid: int) -> dict: 
    """
    Retrieve information for a specific player.
    """
    endpoint = f"{V}/player/{pid}/landing"
    player_info: dict = _call_api_get(endpoint=endpoint)
    return player_info


def _get_game_log(pid: int, season: Optional[int] = None, g_type: Optional[int] = None) -> dict:
    """
    Retrieve the game log for a specific player, season, and game type.
    """
    endpoint = f"{V}/player/{pid}/game-log/now"
    if season and g_type:
        endpoint = f"{V}/player/{pid}/game-log/{season}/{g_type}"
    game_log: dict = _call_api_get(endpoint=endpoint)
    return game_log


def _get_player_spotlight() -> dict:
    """
    Retrieve information about players in the "spotlight".
    """
    endpoint = f"{V}/player-spotlight"
    spotlight: dict= _call_api_get(endpoint=endpoint)
    # print(spotlight)
    return spotlight
    
# ==========================================================================
# SKATERS
# ==========================================================================

def _get_skater_leaders(season: Optional[int] = None, g_type: Optional[int] = None, categories: Optional[str] = None, 
                        limit: Optional[int] = None) -> dict:
    """
    Retrieve current skater stats leaders.
    """
    params: dict = {}
    endpoint = f"{V}/skater-stats-leaders/current"

    if season and g_type: 
        endpoint = f"{V}/skater-stats-leaders/{season}/{g_type}"

    if categories is not None:
        params["categories"] = categories
    if limit is not None:
        params["limit"] = limit

    skater_leaders: dict = _call_api_get(endpoint=endpoint, params=params)
    return skater_leaders

# ==========================================================================
# GOALIES
# ==========================================================================

def _get_goalie_leaders(season: Optional[int] = None, g_type: Optional[int] = None, 
                        categories: Optional[str] = None, limit: Optional[int] = None) -> dict: 
    """
    Retrieve current goalie stats leaders
    """
    params: dict = {}
    endpoint = f"{V}/goalie-stats-leaders/current"

    if season and g_type: 
        endpoint = f"{V}/goalie-stats-leaders/{season}/{g_type}"

    if categories is not None:
        params["categories"] = categories
    if limit is not None: 
        params["limit"] = limit

    goalie_lead: dict = _call_api_get(endpoint=endpoint, params=params)
    return goalie_lead
