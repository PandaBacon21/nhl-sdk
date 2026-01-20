"""
FUNCTIONS FOR RETRIEVING NHLEDGE SKATER DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from nhl_stats.core.config import V
from ....core.transport import _call_api_get


# ==========================================================================
# SKATERS
# ==========================================================================

def _get_skater_details(pid: int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict:
    """
    Retrieve player rankings for NHL Edge data. 
    Includes top shot speed, skating speed, distance skated, 
    shot on goal summary/details, zone time percentages.
    
    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together. 
    """
    endpoint = f"/{V}/edge/skater-detail/{pid}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/skater-detail/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater

def _get_skater_comparison(pid: int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Retrieve NHL Edge data for the specified player. 
    Includes skating distance and speed data, 
    shot location and speed data, zone time details and zone starts.

    Parameters: 
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"{V}/edge/skater-comparison/{pid}/now"
    if season and game_type:
        endpoint = f"{V}/edge/skater-comparison/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater

def _get_skating_distance(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Skating Distance Details for a specific player

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-skating-distance-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/skater-skating-distance-detail/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater

def _get_skating_speed(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Skating Speed Details for a specific player

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-skating-speed-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/skater-skating-speed-detail/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater

def _get_zone_time(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Zone time details by situation (All Situations/Even Strength/Power Play/Penalty Kill). Includes zone starts.

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-zone-time/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/skater-zone-time/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater

def _get_shot_speed(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Provides the 10 hardest shots for a specified player. Includes top shot speed, 
    average shot speed, shot attempts in the following groups: 100+, 90-100, 80-90, 70-80.

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-shot-speed-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/skater-shot-speed-detail/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater

def _get_shot_location(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Provides information on shot location

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-shot-location-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/skater-shot-location-detail/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater

def _get_cat_skater_details(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Provides information on top shot speed, skating speed/distance, shots on goal summary/details and zone time details.

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/cat/edge/skater-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/cat/edge/skater-detail/{pid}/{season}/{game_type}"
    skater = _call_api_get(endpoint=endpoint)
    return skater


# ==========================================================================
# SKATER LEADERS
# ==========================================================================


def _get_skater_landing(season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Retrieve leading player for NHL Edge data. 
    Includes top shot speed, skating speed, 
    distance skated, high danger SOG, zone time percentages.

    Parameters: 
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together. 
    """
    endpoint = f"/{V}/edge/skater-landing/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/skater-landing/{season}/{game_type}"
    landing = _call_api_get(endpoint=endpoint)
    return landing

def _get_skater_distance_10(pos: str, strength: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Retrieve top 10 skaters in skating distance based on the provided filters

    Parameters:
    pos - str
    strength - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-distance-top-10/{pos}/{strength}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/skater-distance-top-10/{pos}/{strength}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_skating_speed_10(pos: str, sort: str, season: Optional[int] = None, 
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
    endpoint = f"/{V}/edge/skater-speed-top-10/{pos}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/skater-speed-top-10/{pos}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_skater_zone_time_10(pos: str, strength: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Retrieve top 10 skaters in zone time based on the provided filters

    Parameters:
    pos - str
    strength - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-zone-time-top-10/{pos}/{strength}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/skater-zone-time-top-10/{pos}/{strength}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_skater_shot_speed_10(pos: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Retrieve 10 fastest shots based on the provided filters.
    
    Parameters:
    pos - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-shot-speed-top-10/{pos}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/skater-shot-speed-top-10/{pos}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_skater_shot_location_10(pos: str, category: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Top 10 skaters based on the specified filters.
    
    Parameters:
    pos - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/skater-shot-location-top-10/{pos}/{category}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/skater-shot-location-top-10/{pos}/{category}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

