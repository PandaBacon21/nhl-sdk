"""
METHODS FOR RETRIEVING PLAYER DATA FROM API.NHLE.COM/STATS/REST
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from ...core.config import LANG
from ...core.transport import APIResponse
from ._helpers import _build_stats_params

if TYPE_CHECKING:
    from ...core.transport import APICallStats


class CallNhlStatsPlayers:
    def __init__(self, http: APICallStats):
        self._http = http

    # ==========================================================================
    # SKATERS
    # ==========================================================================

    def get_skater_stats(
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
        Retrieve skater stats for a specific report type.
        report: str - e.g. "summary"
        """
        params = _build_stats_params(
            is_aggregate=is_aggregate, is_game=is_game,
            fact_cayenne_exp=fact_cayenne_exp, include=include, exclude=exclude,
            cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
        )
        endpoint = f"/{LANG}/skater/{report}"
        return self._http.get(endpoint=endpoint, params=params or None)

    def get_skater_leaders(self, attribute: str) -> APIResponse:
        """
        Retrieve skater leaders for a specific attribute.
        attribute: str - e.g. "goals", "assists", "points"
        """
        endpoint = f"/{LANG}/leaders/skaters/{attribute}"
        return self._http.get(endpoint=endpoint)

    def get_skater_milestones(
        self,
        *,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> APIResponse:
        """
        Retrieve upcoming milestone data for skaters.
        """
        params = _build_stats_params(
            cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
        )
        endpoint = f"/{LANG}/milestones/skaters"
        return self._http.get(endpoint=endpoint, params=params or None)

    # ==========================================================================
    # GOALIES
    # ==========================================================================

    def get_goalie_stats(
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
        Retrieve goalie stats for a specific report type.
        report: str - e.g. "summary"
        """
        params = _build_stats_params(
            is_aggregate=is_aggregate, is_game=is_game,
            fact_cayenne_exp=fact_cayenne_exp, include=include, exclude=exclude,
            cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
        )
        endpoint = f"/{LANG}/goalie/{report}"
        return self._http.get(endpoint=endpoint, params=params or None)

    def get_goalie_leaders(self, attribute: str) -> APIResponse:
        """
        Retrieve goalie leaders for a specific attribute.
        attribute: str - e.g. "wins", "gaa", "savePct"
        """
        endpoint = f"/{LANG}/leaders/goalies/{attribute}"
        return self._http.get(endpoint=endpoint)

    def get_goalie_milestones(
        self,
        *,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> APIResponse:
        """
        Retrieve upcoming milestone data for goalies.
        """
        params = _build_stats_params(
            cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
        )
        endpoint = f"/{LANG}/milestones/goalies"
        return self._http.get(endpoint=endpoint, params=params or None)

    # ==========================================================================
    # PLAYERS
    # ==========================================================================

    def get_players(
        self,
        *,
        include: str | None = None,
        exclude: str | None = None,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> APIResponse:
        """
        Retrieve basic player information.
        Note: responses limited to 5 results by default.
        """
        params = _build_stats_params(
            include=include, exclude=exclude, cayenne_exp=cayenne_exp,
            sort=sort, dir=dir, start=start, limit=limit,
        )
        endpoint = f"/{LANG}/players"
        return self._http.get(endpoint=endpoint, params=params or None)
