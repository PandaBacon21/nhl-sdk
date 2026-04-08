"""
METHODS FOR RETRIEVING SEASON DATA FROM API.NHLE.COM/STATS/REST
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from ...core.config import LANG
from ...core.transport import APIResponse

if TYPE_CHECKING:
    from ...core.transport import APICallStats


class CallNhlStatsSeasons:
    def __init__(self, http: APICallStats):
        self._http = http

    def get_season(self) -> APIResponse:
        """
        Retrieve season data.
        """
        endpoint = f"/{LANG}/season"
        return self._http.get(endpoint=endpoint)

    def get_component_season(self) -> APIResponse:
        """
        Retrieve component season information.
        """
        endpoint = f"/{LANG}/componentSeason"
        return self._http.get(endpoint=endpoint)
