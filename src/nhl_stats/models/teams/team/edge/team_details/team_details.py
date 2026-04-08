"""
TEAM DETAILS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ......core.cache import get_cache
from ......core.utilities import CacheFetchMixin
from .team_details_result import TeamDetailResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class TeamDetails(CacheFetchMixin):
    """
    Team details NHL Edge sub-resource.

    Provides NHL Edge rankings and stat summaries for a team,
    including shot speed, skating speed, distance skated,
    shot on goal details, and zone time percentages.

    Accessed via ``team.stats.edge.details`` on a ``Team`` object.
    """
    def __init__(self, client: NhlClient, team_id: int):
        self._client = client
        self._team_id = team_id
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.details")
        self._ttl: int = 60 * 60 * 1

    def get_details(self, season: int | None = None, game_type: int | None = None) -> TeamDetailResult:
        """
        Retrieve NHL Edge rankings and stat summaries for the team.

        Args:
            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season). Required when ``season`` is provided.
        """
        team_id = self._team_id
        if season and game_type:
            key = f"teams:edge:details:{team_id}:{season}:{game_type}"
        else:
            key = f"teams:edge:details:{team_id}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_details(
                team_id=team_id, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            TeamDetailResult.from_dict,
        )
