"""
FUNCTIONS FOR RETRIEVING DRAFT DATA FROM API-WEB.NHLE.COM/
"""

from nhl_stats.core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# DRAFT
# ==========================================================================

def _get_rankings_now() -> dict: 
    """
    Retrieve a list of all draft prospects by category of prospect as of the current moment
    """
    endpoint = f"{V}/draft/rankings/now"
    rankings: dict = _call_api_get(endpoint=endpoint)
    # print(rankings)
    return rankings

def _get_rankings(season: int, category: str) -> dict: 
    """
    Retrieve a list of all draft prospects by category of prospect for a specific season
    season: int - YYYY
    category: str - Prospect Category (1 - North American Skater, 2 - International Skater, 
    3 - North American Goalie, 4 - International Goalie)
    """
    endpoint = f"{V}/draft/rankings/{season}/{category}"
    rankings: dict = _call_api_get(endpoint=endpoint)
    # print(rankings)
    return rankings

def _get_tracker_now() -> dict: 
    """
    Retrieve current draft tracker information with the most recent draft picks.
    """
    endpoint = f"{V}/draft-tracker/picks/now"
    tracker: dict = _call_api_get(endpoint=endpoint)
    # print(tracker)
    return tracker

def _get_picks_now() -> dict: 
    """
    Retrieve the most recent draft picks information
    """
    endpoint = f"{V}/draft/picks/now"
    picks: dict = _call_api_get(endpoint=endpoint)
    # print(picks)
    return picks

def _get_picks(season: int, round: str) -> dict: 
    """
    Retrieve a list of draft picks for a specific season
    season: int - YYYY
    round: str - Selectable round (1-7, 1 for round 1 etc.) or all for all selectable rounds
    """
    endpoint = f"{V}/draft/picks/{season}/{round}"
    picks: dict = _call_api_get(endpoint=endpoint)
    # print(picks)
    return picks
