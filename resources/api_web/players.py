"""
FUNCTIONS FOR RETRIEVING PLAYER DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from nhl_stats.core.config import V
from ...core.transport import _call_api_get

# test:
player_id = 8477492 #manually checking Nathan MacKinnon for testing

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
    # print(player_info)
    return player_info


def _get_game_log(pid: int, season: int, g_type: int) -> dict:
    """
    Retrieve the game log for a specific player, season, and game type.
    """
    endpoint = f"{V}/player/{pid}/game-log/{season}/{g_type}"
    game_log: dict = _call_api_get(endpoint=endpoint)
    return game_log


def _get_game_log_now(pid: int) -> dict:
    """
    Retrieve the game log for a specific player as of the current moment.
    """
    endpoint = f"{V}/player/{pid}/game-log/now"
    game_log_now = _call_api_get(endpoint=endpoint)
    return game_log_now
    

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

def _get_skater_leaders(categories: Optional[str] = None, limit: Optional[int] = None) -> dict:
    """
    Retrieve current skater stats leaders.
    """
    params: dict = {}
    if categories is not None:
        params["categories"] = categories
    if limit is not None:
        params["limit"] = limit

    endpoint = f"{V}/skater-stats-leaders/current"
    skater_leaders: dict = _call_api_get(endpoint=endpoint, params=params)
    return skater_leaders


def _get_skater_leaders_by_season(season: int, g_type: int, 
                                 categories: Optional[str] = None, 
                                 limit: Optional[int] = None
                                 ) -> dict: 
    """
    Retrieve skater stats leaders for a specific season and game type.
    """
    params: dict = {}
    if categories is not None:
        params["categories"] = categories
    if limit is not None: 
        params["limit"] = limit
    endpoint = f"{V}/skater-stats-leaders/{season}/{g_type}"
    skater_leaders: dict = _call_api_get(endpoint=endpoint, params=params)
    return skater_leaders

# ==========================================================================
# GOALIES
# ==========================================================================

def _get_goalie_leaders(categories: Optional[str] = None, limit: Optional[int] = None) -> dict: 
    """
    Retrieve current goalie stats leaders
    """
    params: dict = {}
    if categories is not None:
        params["categories"] = categories
    if limit is not None: 
        params["limit"] = limit
    endpoint = f"{V}/goalie-stats-leaders/current"
    goalie_lead: dict = _call_api_get(endpoint=endpoint, params=params)
    return goalie_lead


# Update this to tests
def main() -> None:
    _get_game_log(pid=player_id, season=20252026, g_type=2)
    _get_player_info(player_id)
    _get_game_log_now(pid=player_id)
    _get_player_spotlight()
    _get_skater_leaders()
    _get_skater_leaders_by_season(season=20252026, g_type=2)
    _get_goalie_leaders()


if __name__ == "__main__":
    main()
