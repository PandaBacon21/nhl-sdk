"""
TEAM COMPARISON SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ......core.cache import get_cache
from ......core.utilities import CacheFetchMixin
from .team_comparison_result import TeamComparisonResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamComparison(CacheFetchMixin):
    """
    Team comparison NHL Edge sub-resource.

    Provides NHL Edge comparison data for a team, including shot speed
    and skating speed breakdowns, last 10 games of skating distance,
    season distance totals, shot location details, zone time comparisons,
    and shot differentials.

    Accessed via ``team.stats.edge.comparison`` on a ``Team`` object.
    """
    def __init__(self, client: NhlClient, team_id: int):
        self._client = client
        self._team_id = team_id
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.comparison")
        self._ttl: int = 60 * 60 * 1

    def get_comparison(self, season: int | None = None, game_type: int | None = None) -> TeamComparisonResult:
        """
        Retrieve NHL Edge comparison data for the team.

        Args:            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season). Required when ``season`` is provided.
        """
        team_id = self._team_id
        if season and game_type:
            key = f"teams:edge:comparison:{team_id}:{season}:{game_type}"
        else:
            key = f"teams:edge:comparison:{team_id}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_comparison(
                team_id=team_id, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            TeamComparisonResult.from_dict,
        )
