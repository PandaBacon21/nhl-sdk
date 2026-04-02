"""
TEAM SKATING SPEED DETAIL SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ......core.cache import get_cache
from ......core.utilities import CacheFetchMixin
from .team_skating_speed_detail import TeamSkatingSpeedResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamSkatingSpeedDetails(CacheFetchMixin):
    """
    Team skating speed detail NHL Edge sub-resource.

    Provides top speed instances for the season and per-position breakdown
    with burst counts and league ranks.

    Accessed via `client.teams.stats.edge.skating_speed`.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.skating_speed")
        self._ttl: int = 60 * 60 * 1

    def get_skating_speed(self, team_id: int, season: int | None = None, game_type: int | None = None) -> TeamSkatingSpeedResult:
        """
        Retrieve skating speed detail stats for the team.

        Args:
            team_id (int): Numeric team ID.
            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season). Required when ``season`` is provided.
        """
        if season and game_type:
            key = f"teams:edge:skating_speed:{team_id}:{season}:{game_type}"
        else:
            key = f"teams:edge:skating_speed:{team_id}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_skating_speed(
                team_id=team_id, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            TeamSkatingSpeedResult.from_dict,
        )
