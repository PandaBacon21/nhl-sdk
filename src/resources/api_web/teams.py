"""
FUNCTIONS FOR RETRIEVING TEAM DATA FROM API-WEB.NHLE.COM/
"""

from typing import Any, Optional

from ...core.config import V
from ...core.transport import _call_api_get


# ==========================================================================
# STANDINGS
# ==========================================================================

def _get_standings(date: Optional[str] = None) -> dict:
    """ 
    Retrieve the standings as of the current moment a specific date
    date: YYYY-MM-DD
    """
    endpoint = f"{V}/standings/now"
    if date: 
        endpoint = f"{V}/standings/{date}"
    standings: dict = _call_api_get(endpoint=endpoint)
    # print(standings)
    return standings
    
def _get_standings_per_season() -> dict: 
    """
    Retrieves information for each season's standings
    """
    endpoint = f"{V}/standings-season"
    standings: dict = _call_api_get(endpoint=endpoint)
    # print(standings)
    return standings

# ==========================================================================
# STATS
# ==========================================================================

def _get_team_stats(team: str, season: Optional[int] = None, g_type: Optional[int] = None) -> dict:
    """
    Retrieve current statistics for a specific club
    team: three-letter team code
    """
    endpoint = f"{V}/club-stats/{team}/now"
    if season and g_type:
        endpoint = f"{V}/club-stats/{team}/{season}/{g_type}"
    team_stats: dict = _call_api_get(endpoint=endpoint)
    # print(team_stats)
    return team_stats

def _get_game_types_per_season(team: str) -> dict: 
    """
    Returns an overview of the stats for each season for a specific club
    Seems to only indicate the gametypes played in each season
    team: three-letter team code
    """
    endpoint = f"{V}/club-stats-season/{team}"
    game_types: dict = _call_api_get(endpoint=endpoint)
    # print(game_types)
    return game_types


def _get_team_scoreboard(team: str) -> dict: 
    """
    Retrieve the scoreboard for a specific team as of the current moment
    team: three-letter team code
    """
    endpoint = f"{V}/scoreboard/{team}/now"
    scoreboard: dict = _call_api_get(endpoint=endpoint)
    # print(scoreboard)
    return scoreboard

# ==========================================================================
# ROSTER
# ==========================================================================

def _get_team_roster(team: str, season: Optional[int] = None) -> dict: 
    """
    Retrieve the roster for a specific team as of the current moment or season
    team: three-letter team code
    season: YYYYYYYY
    """
    endpoint = f"{V}/roster/{team}/current"
    if season: 
        endpoint = f"{V}/roster/{team}/{season}"
    roster: dict[str, Any] = _call_api_get(endpoint=endpoint)
    # print(roster)
    return roster

def _get_roster_season_by_team(team: str) -> dict: 
    """
    Seems to just return a list of all of the seasons that the team played
    team: three-letter team code
    """
    endpoint = f"{V}/roster-season/{team}"
    seasons: dict = _call_api_get(endpoint=endpoint)
    # print(seasons)
    return seasons

def _get_team_prospects(team: str) -> dict: 
    """
    Retrieve prospects for a specific team
    team: three-letter team code
    """
    endpoint = f"{V}/prospects/{team}"
    prospects: dict = _call_api_get(endpoint=endpoint)
    # print(prospects)
    return prospects
    
# ==========================================================================
# SCHEDULE
# ==========================================================================

def _get_schedule(team: str, season: Optional[int] = None) -> dict: 
    """
    Retrieve the season schedule for a specific team at the current moment or season
    team: three-letter team code
    season: YYYYYYYY
    """
    endpoint = f"{V}/club-schedule-season/{team}/now"
    if season: 
        endpoint = f"{V}/club-schedule-season/{team}/{season}"
    schedule: dict[str, Any] = _call_api_get(endpoint=endpoint)
    # print(schedule)
    return schedule
    
def _get_schedule_month(team: str, month: Optional[str] = None) -> dict: 
    """
    Retrieve the monthly schedule for a specific team as of the current moment or month
    team: three-letter team code
    month: YYYY-MM

    """
    endpoint = f"{V}/club-schedule/{team}/month/now"
    if month: 
        endpoint = f"{V}/club-schedule/{team}/month/{month}"
    schedule: dict = _call_api_get(endpoint=endpoint)
    # print(schedule)
    return schedule

def _get_schedule_week(team: str, week: Optional[str] = None) -> dict: 
    """
    Retrieve the weekly schedule for a specific team as of the current moment or date
    team: three-letter team code
    week: YYYY-MM-DD
    """
    endpoint = f"{V}/club-schedule/{team}/week/now"
    if week: 
        endpoint = f"{V}/club-schedule/{team}/week/{week}"
    schedule: dict = _call_api_get(endpoint=endpoint)
    # print(schedule)
    return schedule

