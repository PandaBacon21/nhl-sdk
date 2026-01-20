"""
FUNCTIONS FOR RETRIEVING NHLEDGE GOALIE DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from nhl_stats.core.config import V
from ....core.transport import _call_api_get


# ==========================================================================
# GOALIES
# ==========================================================================

def _get_goalie_details(pid: int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict:
    """
    Retrieve goalie rankings for NHL Edge data. 
    Includes GAA, games above .900, goal differential per 60, average goal support, 
    point percentage, shot location summary/details.
    
    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together. 
    """
    endpoint = f"/{V}/edge/goalie-detail/{pid}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/goalie-detail/{pid}/{season}/{game_type}"
    goalie = _call_api_get(endpoint=endpoint)
    return goalie

def _get_goalie_comparison(pid: int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Retrieve NHL Edge data for the specified player. 
    Includes shot location summary/details, 5v5 save percentage in the last 10 games/details, 
    overall save percentage in the last 10 games, and overall save percentage details.

    Parameters: 
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"{V}/edge/goalie-comparison/{pid}/now"
    if season and game_type:
        endpoint = f"{V}/edge/goalie-comparison/{pid}/{season}/{game_type}"
    goalie = _call_api_get(endpoint=endpoint)
    return goalie

def _get_goalie_5v5(pid: int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    5v5 save percentage details for the specified player.

    Parameters: 
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"{V}/edge/goalie-5v5-detail/{pid}/now"
    if season and game_type:
        endpoint = f"{V}/edge/goalie-5v5-detail/{pid}/{season}/{game_type}"
    goalie = _call_api_get(endpoint=endpoint)
    return goalie

def _get_shot_location(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Goalie shot location details for the specified player.

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/goalie-shot-location-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/goalie-shot-location-detail/{pid}/{season}/{game_type}"
    goalie = _call_api_get(endpoint=endpoint)
    return goalie

def _get_save_pctg(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Goalie save percentage details for the specified player. 
    Contains save percentage in last 10 games, games above .900 and percentage of games above .900.

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/goalie-save-percentage-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/goalie-save-percentage-detail/{pid}/{season}/{game_type}"
    goalie = _call_api_get(endpoint=endpoint)
    return goalie

def _get_cat_goalie_details(pid:int, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Provides information on GAA, games above .900, goal differential per 60, 
    goal support average, point percentage, shot location summary/details.

    Parameters:
    pid - int
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/cat/edge/goalie-detail/{pid}/now"
    if season and game_type:
        endpoint = f"/{V}/cat/edge/goalie-detail/{pid}/{season}/{game_type}"
    goalie = _call_api_get(endpoint=endpoint)
    return goalie




# ==========================================================================
# GOALIE LEADERS
# ==========================================================================

def _get_goalie_landing(season: Optional[int] = None, game_type: Optional[int] = None) -> dict:
    """
    Retrieve leading goalie for NHL Edge data. 
    Includes high-danger save percentage/saves/goals against, 
    save percentage at 5v5, games above .900.
    
    Parameters:
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together. 
    """
    endpoint = f"/{V}/edge/goalie-landing/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/goalie-landing/{season}/{game_type}"
    goalies = _call_api_get(endpoint=endpoint)
    return goalies

def _get_goalies_5v5_10(sort: str, season: Optional[int] = None, game_type: Optional[int] = None) -> dict: 
    """
    Top 10 goalies based on the specified filters.
    
    Parameters:
    sort - str

    Both season and game_type are required to be included or omitted together. 
    """
    endpoint = f"/{V}/edge/goalie-5v5-top-10/{sort}/now"
    if season and game_type:
        endpoint = f"/{V}/edge/goalie-5v5-top-10/{sort}/{season}/{game_type}"
    goalies = _call_api_get(endpoint=endpoint)
    return goalies

def _get_goalie_shot_location_10(category: str, sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Top 10 goalie based on the specified filters.
    
    Parameters:
    pos - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/goalie-shot-location-top-10/{category}/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/goalie-shot-location-top-10/{category}/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10

def _get_goalie_save_pctg_10(sort: str, season: Optional[int] = None, 
                            game_type: Optional[int] = None) -> dict: 
    """
    Top 10 goalies based on the available filters. 
    Contains games above .900 and percentage of games above .900.
    
    Parameters:
    pos - str
    sort - str
    season - Optional - int
    game_type - Optional - int

    Both season and game_type are required to be included or omitted together.
    """
    endpoint = f"/{V}/edge/goalie-edge-save-pctg-top-10/{sort}/now"
    if season and game_type: 
        endpoint = f"/{V}/edge/goalie-edge-save-pctg-top-10/{sort}/{season}/{game_type}"
    top_10 = _call_api_get(endpoint=endpoint)
    return top_10
