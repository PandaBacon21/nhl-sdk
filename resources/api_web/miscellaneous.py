"""
FUNCTIONS FOR RETRIEVING MISCELLANEOUS DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from nhl_stats.core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# META
# ==========================================================================

def _get_meta(players: Optional[str] = None, teams: Optional[str] = None, season_states: Optional[str] = None) -> dict: 
    """
    Retrieve meta information
    Query Params (Optional): 
    players: str - player ID
    teams: str - three-letter team code
    season_states: str - Unsure what the options might be here
    """
    params: dict = {}
    if players is not None:
        params["players"] = players
    if teams is not None:
        params["teams"] = teams
    if season_states is not None:
        params["seasonStates"] = season_states

    endpoint = f"{V}/meta"
    meta: dict = _call_api_get(endpoint=endpoint, params=params) 
    # print(meta)
    return meta

def _get_game_info(game_id:int) -> dict: 
    """
    Retrieve information for a specific game
    game_id: int
    """
    endpoint = f"{V}/meta/game/{game_id}"
    game_info: dict = _call_api_get(endpoint=endpoint)
    # print(game_info)
    return game_info

def _get_location() -> dict: 
    """
    Returns country code that the webserver thinks the user is in
    """
    endpoint = f"{V}/location"
    location: dict = _call_api_get(endpoint=endpoint)
    # print(location)
    return location

def _get_playoff_series_meta(year: int, series_letter: str) -> dict: 
    """
    Retrieve metadata for a specific playoff series
    year: int - YYYY format
    series_letter: str - a, b, c, d, etc
    """
    endpoint = f"{V}/meta/playoff-series/{year}/{series_letter}"
    series: dict = _call_api_get(endpoint=endpoint)
    # print(series)
    return series

# ==========================================================================
# POSTAL LOOKUP
# ==========================================================================

def _get_postal_lookup(postal_code: str) -> dict: 
    """
    Retrieves information based on a postal code
    postal_code: str
    """
    endpoint = f"{V}/postal-lookup/{postal_code}"
    location: dict = _call_api_get(endpoint=endpoint)
    # print(location)
    return location

# ==========================================================================
# GAME REPLAYS
# ==========================================================================

def _get_goal_replay(game_id: int, event_number: int) -> dict: 
    """
    Retrieves goal replay information for a specific game and event
    game_id: int
    event_number: int
    """
    endpoint = f"{V}/ppt-replay/goal/{game_id}/{event_number}"
    replay: dict = _call_api_get(endpoint=endpoint)
    # print(replay)
    return replay

def _get_play_replay(game_id: int, event_number: int) -> dict: 
    """
    Retrieves replay information for a specific game and event
    game_id: int
    event_number: int
    """
    endpoint = f"{V}/ppt-replay/{game_id}/{event_number}"
    replay: dict = _call_api_get(endpoint=endpoint)
    # print(replay)
    return replay

# ==========================================================================
# ADDITIONAL GAME CONTENT
# ==========================================================================

def _get_game_rail(game_id: int) -> dict: 
    """
    Retrieves sidebar content for the game center view
    game_id: int
    """
    endpoint = f"{V}/gamecenter/{game_id}/right-rail"
    game_rail: dict = _call_api_get(endpoint=endpoint)
    # print(game_rail)
    return game_rail

def _get_wsc(game_id: int) -> dict: 
    """
    Retrieves WSC (World Showcase) play-by-play information for a specific game
    game_id: int
    """
    endpoint = f"{V}/gamecenter/{game_id}/right-rail"
    wsc: dict = _call_api_get(endpoint=endpoint)
    # print(wsc)
    return wsc

# ==========================================================================
# OPENAPI SPEC
# ==========================================================================

def _get_openapi() -> dict: 
    """
    Retrieve the OpenAPI specification. (Seems to return 404 currently)
    """
    endpoint = f"model/{V}/openapi.json"
    openapi: dict = _call_api_get(endpoint=endpoint)
    # print(openapi)
    return openapi

