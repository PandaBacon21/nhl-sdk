"""
FUNCTIONS FOR RETRIEVING PLAYOFF DATA FROM API-WEB.NHLE.COM/
"""

from nhl_stats.core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# OVERVIEW
# ==========================================================================

def _get_carousel(season: int) -> dict:
    """
    Retrieve an overview of each playoff series
    season: int - YYYYYYYY format
    """ 
    endpoint = f"{V}/playoff-series/carousel/{season}/"
    carousel: dict = _call_api_get(endpoint=endpoint)
    # print(carousel)
    return carousel

# ==========================================================================
# SCHEDULE
# ==========================================================================

def _get_series_schedule(season: int, series_letter: str) -> dict:
    """
    Retrieve the schedule for a specific playoff series
    season: int - YYYYYYYY format
    series_letter: str - Single letter indicating which series to retrieve. Is sequential in alphabetical order.
    """ 
    endpoint = f"{V}/schedule/playoff-series/{season}/{series_letter}/"
    series: dict = _call_api_get(endpoint=endpoint)
    # print(series)
    return series

# ==========================================================================
# BRACKET
# ==========================================================================

# Need to add handling for empty bracket 
def _get_bracket(year: int) -> dict:
    """
    Retrieve the current bracket for a specific year's playoffs
    season: int - YYYY format
    """ 
    endpoint = f"{V}/playoff-bracket/{year}"
    bracket: dict = _call_api_get(endpoint=endpoint)
    # print(bracket)
    return bracket
