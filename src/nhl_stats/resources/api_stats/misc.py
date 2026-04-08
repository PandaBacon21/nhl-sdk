"""
METHODS FOR RETRIEVING MISCELLANEOUS DATA FROM API.NHLE.COM/STATS/REST
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from ...core.config import LANG
from ...core.transport import APIResponse

if TYPE_CHECKING:
    from ...core.transport import APICallStats


class CallNhlStatsMisc:
    def __init__(self, http: APICallStats):
        self._http = http

    def get_shift_charts(self, game_id: int) -> APIResponse:
        """
        Retrieve shift chart data for a specific game.
        game_id: int
        """
        endpoint = f"/{LANG}/shiftcharts"
        params = {"cayenneExp": f"gameId={game_id}"}
        res: APIResponse = self._http.get(endpoint=endpoint, params=params)
        return res

    def get_countries(self) -> APIResponse:
        """
        Retrieve list of all countries with a hockey presence.
        """
        endpoint = f"/{LANG}/country"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def get_glossary(self) -> APIResponse:
        """
        Retrieve statistical term definitions.
        """
        endpoint = f"/{LANG}/glossary"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def get_config(self) -> APIResponse:
        """
        Retrieve API configuration details.
        """
        endpoint = f"/{LANG}/config"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def get_content_module(self, template_key: str) -> APIResponse:
        """
        Retrieve content module data for a given template key.
        template_key: str

        NOTE: Service and model layers are intentionally not implemented —
        valid templateKey values are unknown. Returns raw APIResponse.
        """
        
        endpoint = f"/{LANG}/content/module/{template_key}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def ping(self) -> APIResponse:
        """
        Check server connectivity.
        """
        res: APIResponse = self._http.get(endpoint="/ping")
        return res
