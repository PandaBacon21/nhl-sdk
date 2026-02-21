"""
FUNCTIONS FOR RETRIEVING PLAYOFF DATA FROM API-WEB.NHLE.COM/
"""

from __future__ import annotations
from ...core.config import V
from ...core.transport import APICallWeb, APIResponse



class CallNhlPlayoffs:
    def __init__(self, http: APICallWeb): 
        self._http = http

    # ==========================================================================
    # OVERVIEW
    # ==========================================================================

    def get_carousel(self, season: int) -> APIResponse:
        """
        Retrieve an overview of each playoff series
        season: int - YYYYYYYY format
        """ 
        endpoint = f"/{V}/playoff-series/carousel/{season}/"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    # ==========================================================================
    # SCHEDULE
    # ==========================================================================

    def get_series_schedule(self, season: int, series_letter: str) -> APIResponse:
        """
        Retrieve the schedule for a specific playoff series
        season: int - YYYYYYYY format
        series_letter: str - Single letter indicating which series to retrieve. Is sequential in alphabetical order.
        """ 
        endpoint = f"/{V}/schedule/playoff-series/{season}/{series_letter}/"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

    # ==========================================================================
    # BRACKET
    # ==========================================================================

    # Need to add handling for empty bracket 
    def get_bracket(self, year: int) -> APIResponse:
        """
        Retrieve the current bracket for a specific year's playoffs
        season: int - YYYY format
        """ 
        endpoint = f"/{V}/playoff-bracket/{year}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res
