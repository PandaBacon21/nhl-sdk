"""
FUNCTIONS FOR RETRIEVING SEASON DATA FROM API-WEB.NHLE.COM/
"""

from ...core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# SEASONS
# ==========================================================================

def _get_seasons() -> dict:
    """
    Retrieve a list of all season IDs past & present in the NHL
    """ 
    endpoint = f"{V}/season"
    season: dict = _call_api_get(endpoint=endpoint)
    # print(season)
    return season
