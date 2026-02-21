"""
FUNCTIONS FOR RETRIEVING GAME DATA FROM API-WEB.NHLE.COM/
"""
from typing import Optional

from ...core.config import V
from ...core.transport import APICallWeb, APIResponse

# ==========================================================================
# SCHEDULE
# ==========================================================================


class CallNhlGames:
    def __init__(self, http: APICallWeb): 
        self._http = http

    def get_daily_scores(self, date: Optional[str] = None) -> APIResponse: 
        """
        Retrieve daily scores as of the current moment or by date
        date: YYYY-MM-DD
        """
        endpoint = f"/{V}/score/now"
        if date:
            endpoint = f"/{V}/score/{date}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def get_scoreboard_now(self) -> APIResponse: 
        """
        Retrieve the overall scoreboard as of the current moment
        """
        endpoint = f"/{V}/scoreboard/now"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    # ==========================================================================
    # WHERE TO WATCH
    # ==========================================================================

    def get_streams(self) -> APIResponse: 
        """
        Retrieve information about streaming options
        """
        endpoint = f"/{V}/where-to-watch"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    # ==========================================================================
    # GAME EVENTS
    # ==========================================================================

    def get_play_by_play(self, game_id: int) -> APIResponse: 
        """
        Retrieve play-by-play information for a specific game
        game_id: unique game ID
        """
        endpoint = f"/{V}/gamecenter/{game_id}/play-by-play"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def get_game_landing(self, game_id: int) -> APIResponse: 
        """
        Retrieve landing information for a specific game
        game_id: unique game ID
        """
        endpoint = f"/{V}/gamecenter/{game_id}/landing"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def get_boxscore(self, game_id: int) -> APIResponse: 
        """
        Retrieve boxscore information for a specific game
        game_id: unique game ID
        """
        endpoint = f"/{V}/gamecenter/{game_id}/boxscore"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res
        
    def get_game_story(self, game_id: int) -> APIResponse:
        """
        Retrieve game story information for a specific game
        game_id: unique game ID
        """
        endpoint = f"/{V}/wsc/game-story/{game_id}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    # ==========================================================================
    # NETWORK
    # ==========================================================================

    def get_tv_schedule(self, date: Optional[str] = None) -> APIResponse:
        """
        Retrieve the TV current schedule or for a specific date
        date: YYYY-MM-DD
        """
        endpoint = f"/{V}/network/tv-schedule/now"
        if date: 
            endpoint = f"/{V}/network/tv-schedule/{date}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res
        
    # ==========================================================================
    # PARTNER ODDS
    # ==========================================================================

    def get_odds(self, country_code: str) -> APIResponse:
        """
        Retrieve odds for games in a specific country as of the current moment
        country_code: official country code
        """
        endpoint = f"/{V}/partner-game/{country_code}/now"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res



