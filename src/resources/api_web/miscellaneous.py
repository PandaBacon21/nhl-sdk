"""
FUNCTIONS FOR RETRIEVING MISCELLANEOUS DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from ...core.config import V
from ...core.transport import APICallWeb, APIResponse


class CallNhlMisc:
    def __init__(self, http: APICallWeb): 
        self._http = http

    # ==========================================================================
    # META
    # ==========================================================================

    def get_meta(self, players: Optional[str] = None, teams: Optional[str] = None, season_states: Optional[str] = None) -> APIResponse: 
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

        endpoint = f"/{V}/meta"
        meta: APIResponse = self._http.get(endpoint=endpoint, params=params) 
        # print(meta)
        return meta

    def get_game_info(self, game_id:int) -> APIResponse: 
        """
        Retrieve information for a specific game
        game_id: int
        """
        endpoint = f"/{V}/meta/game/{game_id}"
        game_info: APIResponse = self._http.get(endpoint=endpoint)
        # print(game_info)
        return game_info

    def get_location(self) -> APIResponse: 
        """
        Returns country code that the webserver thinks the user is in
        """
        endpoint = f"/{V}/location"
        location: APIResponse = self._http.get(endpoint=endpoint)
        # print(location)
        return location

    def get_playoff_series_meta(self, year: int, series_letter: str) -> APIResponse: 
        """
        Retrieve metadata for a specific playoff series
        year: int - YYYY format
        series_letter: str - a, b, c, d, etc
        """
        endpoint = f"/{V}/meta/playoff-series/{year}/{series_letter}"
        series: APIResponse = self._http.get(endpoint=endpoint)
        # print(series)
        return series

    # ==========================================================================
    # POSTAL LOOKUP
    # ==========================================================================

    def get_postal_lookup(self, postal_code: str) -> APIResponse: 
        """
        Retrieves information based on a postal code
        postal_code: str
        """
        endpoint = f"/{V}/postal-lookup/{postal_code}"
        location: APIResponse = self._http.get(endpoint=endpoint)
        # print(location)
        return location

    # ==========================================================================
    # GAME REPLAYS
    # ==========================================================================

    def get_goal_replay(self, game_id: int, event_number: int) -> APIResponse: 
        """
        Retrieves goal replay information for a specific game and event
        game_id: int
        event_number: int
        """
        endpoint = f"/{V}/ppt-replay/goal/{game_id}/{event_number}"
        replay: APIResponse = self._http.get(endpoint=endpoint)
        # print(replay)
        return replay

    def get_play_replay(self, game_id: int, event_number: int) -> APIResponse: 
        """
        Retrieves replay information for a specific game and event
        game_id: int
        event_number: int
        """
        endpoint = f"/{V}/ppt-replay/{game_id}/{event_number}"
        replay: APIResponse = self._http.get(endpoint=endpoint)
        # print(replay)
        return replay

    # ==========================================================================
    # ADDITIONAL GAME CONTENT
    # ==========================================================================

    def get_game_rail(self, game_id: int) -> APIResponse: 
        """
        Retrieves sidebar content for the game center view
        game_id: int
        """
        endpoint = f"/{V}/gamecenter/{game_id}/right-rail"
        game_rail: APIResponse = self._http.get(endpoint=endpoint)
        # print(game_rail)
        return game_rail

    def get_wsc(self, game_id: int) -> APIResponse: 
        """
        Retrieves WSC (World Showcase) play-by-play information for a specific game
        game_id: int
        """
        endpoint = f"/{V}/gamecenter/{game_id}/right-rail"
        wsc: APIResponse = self._http.get(endpoint=endpoint)
        # print(wsc)
        return wsc

    # ==========================================================================
    # OPENAPI SPEC
    # ==========================================================================

    def get_openapi(self) -> APIResponse: 
        """
        Retrieve the OpenAPI specification. (Seems to return 404 currently)
        """
        endpoint = f"/model/{V}/openapi.json"
        openapi: APIResponse = self._http.get(endpoint=endpoint)
        # print(openapi)
        return openapi

