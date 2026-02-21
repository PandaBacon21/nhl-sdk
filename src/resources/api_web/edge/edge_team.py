"""
FUNCTIONS FOR RETRIEVING NHLEDGE TEAM DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from ....core.config import V
from ....core.transport import APICallWeb, APIResponse


# ==========================================================================
# TEAM
# ==========================================================================

class CallNhlEdgeTeam:
    def __init__(self, http: APICallWeb): 
        self._http = http

    def get_team_details(self, team_id: int, season: Optional[int] = None, game_type: Optional[int] = None) -> APIResponse:
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
        team = self._http.get(endpoint=endpoint)
        return team

    def get_team_comparison(self, team_id: int, season: Optional[int] = None, game_type: Optional[int] = None) -> APIResponse: 
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
        team = self._http.get(endpoint=endpoint)
        return team

    def get_team_distance(self, team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> APIResponse: 
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
        team = self._http.get(endpoint=endpoint)
        return team

    def get_team_skating_speed(self, team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> APIResponse: 
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
        team = self._http.get(endpoint=endpoint)
        return team

    def get_team_zone_time(self, team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> APIResponse: 
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
        team = self._http.get(endpoint=endpoint)
        return team

    def get_team_shot_speed(self, team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> APIResponse: 
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
        team = self._http.get(endpoint=endpoint)
        return team

    def get_team_shot_location(self, team_id:int, season: Optional[int] = None, game_type: Optional[int] = None) -> APIResponse: 
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
        team = self._http.get(endpoint=endpoint)
        return team


    # ==========================================================================
    # TEAM LEADERS
    # ==========================================================================


    def get_team_skating_distance_10(self,  strength: str, sort: str, pos: str = "all", season: Optional[int] = None, 
                                game_type: Optional[int] = None) -> APIResponse: 
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
        top_10 = self._http.get(endpoint=endpoint)
        return top_10

    def get_team_skating_speed_10(self, sort: str, pos: str = "all", season: Optional[int] = None, 
                                game_type: Optional[int] = None) -> APIResponse: 
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
        top_10 = self._http.get(endpoint=endpoint)
        return top_10

    def get_team_zone_time_10(self, strength: str, sort: str, season: Optional[int] = None, 
                                game_type: Optional[int] = None) -> APIResponse: 
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
        top_10 = self._http.get(endpoint=endpoint)
        return top_10

    def get_team_shot_speed_10(self, sort: str, pos: str = "all", season: Optional[int] = None, 
                                game_type: Optional[int] = None) -> APIResponse: 
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
        top_10 = self._http.get(endpoint=endpoint)
        return top_10

    def get_team_shot_location_10(self, category: str, sort: str, season: Optional[int] = None, 
                                game_type: Optional[int] = None) -> APIResponse: 
        """
        Top 10 teams based on the specified filters.
        
        Parameters:
        pos - str
        sort - str
        season - Optional - int
        game_type - Optional - int

        Both season and game_type are required to be included or omitted together.
        """
        pos: str = "all"
        
        endpoint = f"/{V}/edge/team-shot-location-top-10/{pos}/{category}/{sort}/now"
        if season and game_type: 
            endpoint = f"/{V}/edge/team-shot-location-top-10/{pos}/{category}/{sort}/{season}/{game_type}"
        top_10 = self._http.get(endpoint=endpoint)
        return top_10

