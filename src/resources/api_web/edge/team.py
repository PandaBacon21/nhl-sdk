"""
FUNCTIONS FOR RETRIEVING NHLEDGE TEAM DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from ....core.config import V
from ....core.transport import _call_api_get


# ==========================================================================
# TEAM
# ==========================================================================

def _get_team_details(team_id: int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict:
    """
    Retrieve team-based ranking for NHL Edge data
    
    Parameters:
    team_id - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together. 
    """
    endpoint = f"/{V}/edge/team-detail/{team_id}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/team-detail/{team_id}/{season}/{game_type}"
    team = _call_api_get(endpoint=endpoint)
    return team

def _get_team_comparison(team_id: int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    General information and comparison to league average for NHL Edge datapoints. 
    Includes shots by location and shooting percentage by location.

    Parameters: 
    team_id - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"{V}/edge/team-comparison/{team_id}/now"
    if season and game_type:
        endpoint = f"{V}/edge/team-comparison/{team_id}/{season}/{game_type}"
    team = _call_api_get(endpoint=endpoint)
    return team

def _get_team_distance(team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Skating distance details for all situations and positions, both in last 10 games and in the season.

    Parameters:
    team_id - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-skating-distance-detail/{team_id}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/team-skating-distance-detail/{team_id}/{season}/{game_type}"
    team = _call_api_get(endpoint=endpoint)
    return team

def _get_skating_speed(team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Skating Speed Details for a specific player

    Parameters:
    team_id - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-skating-speed-detail/{team_id}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/team-skating-speed-detail/{team_id}/{season}/{game_type}"
    team = _call_api_get(endpoint=endpoint)
    return team

def _get_zone_time(team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Zone time details by situation (All Situations/Even Strength/Power Play/Penalty Kill)

    Parameters:
    team_id - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-zone-time-details/{team_id}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/team-zone-time-details/{team_id}/{season}/{game_type}"
    team = _call_api_get(endpoint=endpoint)
    return team

def _get_shot_speed(team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Team shots speed details

    Parameters:
    team_id - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-shot-speed-detail/{team_id}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/team-shot-speed-detail/{team_id}/{season}/{game_type}"
    team = _call_api_get(endpoint=endpoint)
    return team

def _get_shot_location(team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Provides information on shot location

    Parameters:
    team_id - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-shot-location-detail/{team_id}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/team-shot-location-detail/{team_id}/{season}/{game_type}"
    team = _call_api_get(endpoint=endpoint)
    return team


# ==========================================================================
# TEAM LEADERS
# ==========================================================================


def _get_team_skating_distance_10(pos: str, strength: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Retrieve team-based ranking for NHL Edge data

    Parameters:
    pos - str
    strength - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-skating-distance-top-10/{pos}/{strength}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/team-skating-distance-top-10/{pos}/{strength}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_team_skating_speed_10(pos: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Retrieve 10 fastest skaters based on the provided filters.
    
    Parameters:
    pos - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-skating-speed-top-10/{pos}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/team-skating-speed-top-10/{pos}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_team_zone_time_10(strength: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Top 10 teams by specified zone time

    Parameters:
    pos - str
    strength - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-zone-time-top-10/{strength}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/team-zone-time-top-10/{strength}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_team_shot_speed_10(pos: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Retrieve team-based ranking for NHL Edge data 
    
    Parameters:
    pos - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-shot-speed-top-10/{pos}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/team-shot-speed-top-10/{pos}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_team_shot_location_10(pos: str, category: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Top 10 teams based on the specified filters.
    
    Parameters:
    pos - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/team-shot-location-top-10/{pos}/{category}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/team-shot-location-top-10/{pos}/{category}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

