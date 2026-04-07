"""
METHODS FOR RETRIEVING TEAM DATA FROM API.NHLE.COM/STATS/REST
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from ...core.config import LANG
from ...core.transport import APIResponse
from ._helpers import _build_stats_params

if TYPE_CHECKING:
    from ...core.transport import APICallStats


class CallNhlStatsTeams:
    def __init__(self, http: APICallStats):
        self._http = http

    # ==========================================================================
    # TEAM STATS REPORTS
    # ==========================================================================

    def get_team_stats(
        self,
        report: str,
        *,
        is_aggregate: bool | None = None,
        is_game: bool | None = None,
        fact_cayenne_exp: str | None = None,
        include: str | None = None,
        exclude: str | None = None,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> APIResponse:
        """
        Retrieve team stats for a specific report type.
        report: str - e.g. "summary"
        """
        params = _build_stats_params(
            is_aggregate=is_aggregate, is_game=is_game,
            fact_cayenne_exp=fact_cayenne_exp, include=include, exclude=exclude,
            cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
        )
        endpoint = f"/{LANG}/team/{report}"
        return self._http.get(endpoint=endpoint, params=params or None)

    # ==========================================================================
    # TEAM REFERENCE
    # ==========================================================================

    def get_teams(self) -> APIResponse:
        """
        Retrieve list of all teams.
        """
        endpoint = f"/{LANG}/team"
        return self._http.get(endpoint=endpoint)

    def get_team_by_id(self, team_id: int) -> APIResponse:
        """
        Retrieve data for a specific team by ID.
        team_id: int
        """
        endpoint = f"/{LANG}/team/id/{team_id}"
        return self._http.get(endpoint=endpoint)

    def get_franchise(self) -> APIResponse:
        """
        Retrieve list of all franchises.
        """
        endpoint = f"/{LANG}/franchise"
        return self._http.get(endpoint=endpoint)
