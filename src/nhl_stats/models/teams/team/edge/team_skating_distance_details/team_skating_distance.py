"""
TEAM SKATING DISTANCE DETAIL SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ......core.cache import get_cache
from ......core.utilities import CacheFetchMixin
from .team_skating_distance_detail import TeamSkatingDistanceResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class TeamSkatingDistance(CacheFetchMixin):
    """
    Team skating distance detail NHL Edge sub-resource.

    Provides last-10-game per-situation skating distance breakdowns and
    season summaries across strength codes and position codes, each with
    ranks and league averages.

    Accessed via ``team.stats.edge.skating_distance`` on a ``Team`` object.
    """
    def __init__(self, client: NhlClient, team_id: int):
        self._client = client
        self._team_id = team_id
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.skating_distance")
        self._ttl: int = 60 * 60 * 1

    def get_skating_distance(self, season: int | None = None, game_type: int | None = None) -> TeamSkatingDistanceResult:
        """
        Retrieve skating distance detail stats for the team.

        Args:            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season). Required when ``season`` is provided.
        """
        team_id = self._team_id
        if season and game_type:
            key = f"teams:edge:skating_distance:{team_id}:{season}:{game_type}"
        else:
            key = f"teams:edge:skating_distance:{team_id}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_distance(
                team_id=team_id, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            TeamSkatingDistanceResult.from_dict,
        )
