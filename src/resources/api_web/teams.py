"""
FUNCTIONS FOR RETRIEVING TEAM DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from ...core.config import V
from ...core.transport import APICallWeb, APIResponse



class CallNhlTeams:
    def __init__(self, http: APICallWeb): 
        self._http = http

    # ==========================================================================
    # STANDINGS
    # ==========================================================================

    def get_standings(self, date: Optional[str] = None) -> APIResponse:
        """ 
        Retrieve the standings as of the current moment a specific date
        date: YYYY-MM-DD
        """
        endpoint = f"/{V}/standings/now"
        if date: 
            endpoint = f"/{V}/standings/{date}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res
        
    def get_standings_per_season(self,) -> APIResponse: 
        """
        Retrieves information for each season's standings
        """
        endpoint = f"/{V}/standings-season"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    # ==========================================================================
    # STATS
    # ==========================================================================

    def get_team_stats(self, team: str, season: Optional[int] = None, g_type: Optional[int] = None) -> APIResponse:
        """
        Retrieve current statistics for a specific club
        team: three-letter team code
        """
        endpoint = f"/{V}/club-stats/{team}/now"
        if season and g_type:
            endpoint = f"/{V}/club-stats/{team}/{season}/{g_type}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    def get_game_types_per_season(self, team: str) -> APIResponse: 
        """
        Returns an overview of the stats for each season for a specific club
        Seems to only indicate the gametypes played in each season
        team: three-letter team code
        """
        endpoint = f"/{V}/club-stats-season/{team}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res


    def get_team_scoreboard(self, team: str) -> APIResponse: 
        """
        Retrieve the scoreboard for a specific team as of the current moment
        team: three-letter team code
        """
        endpoint = f"/{V}/scoreboard/{team}/now"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    # ==========================================================================
    # ROSTER
    # ==========================================================================

    def get_team_roster(self, team: str, season: Optional[int] = None) -> APIResponse: 
        """
        Retrieve the roster for a specific team as of the current moment or season
        team: three-letter team code
        season: YYYYYYYY
        """
        endpoint = f"/{V}/roster/{team}/current"
        if season: 
            endpoint = f"/{V}/roster/{team}/{season}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    def get_roster_season_by_team(self, team: str) -> APIResponse: 
        """
        Seems to just return a list of all of the seasons that the team played
        team: three-letter team code
        """
        endpoint = f"/{V}/roster-season/{team}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    def get_team_prospects(self, team: str) -> APIResponse: 
        """
        Retrieve prospects for a specific team
        team: three-letter team code
        """
        endpoint = f"/{V}/prospects/{team}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res
        
    # ==========================================================================
    # SCHEDULE
    # ==========================================================================

    def get_schedule(self, team: str, season: Optional[int] = None) -> APIResponse: 
        """
        Retrieve the season schedule for a specific team at the current moment or season
        team: three-letter team code
        season: YYYYYYYY
        """
        endpoint = f"/{V}/club-schedule-season/{team}/now"
        if season: 
            endpoint = f"/{V}/club-schedule-season/{team}/{season}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res
        
    def get_schedule_month(self, team: str, month: Optional[str] = None) -> APIResponse: 
        """
        Retrieve the monthly schedule for a specific team as of the current moment or month
        team: three-letter team code
        month: YYYY-MM

        """
        endpoint = f"/{V}/club-schedule/{team}/month/now"
        if month: 
            endpoint = f"/{V}/club-schedule/{team}/month/{month}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    def get_schedule_week(self, team: str, week: Optional[str] = None) -> APIResponse: 
        """
        Retrieve the weekly schedule for a specific team as of the current moment or date
        team: three-letter team code
        week: YYYY-MM-DD
        """
        endpoint = f"/{V}/club-schedule/{team}/week/now"
        if week: 
            endpoint = f"/{V}/club-schedule/{team}/week/{week}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

