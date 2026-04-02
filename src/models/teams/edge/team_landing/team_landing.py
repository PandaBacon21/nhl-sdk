"""
TEAM EDGE LANDING SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_landing_result import TeamEdgeLandingResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamLanding(CacheFetchMixin):
    """
    Team Edge landing sub-resource.

    Returns the league-leading team for each NHL Edge category along with
    the list of seasons that have Edge data available.

    Accessed via `client.teams.edge.landing`.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.landing")
        self._ttl: int = 60 * 60 * 1

    def get_landing(self, season: int | None = None, game_type: int | None = None) -> TeamEdgeLandingResult:
        """
        Retrieve the team Edge landing leaders.

        Args:
            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season).
        """
        if season and game_type:
            key = f"teams:edge:landing:{season}:{game_type}"
        else:
            key = "teams:edge:landing:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_landing(
                season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            TeamEdgeLandingResult.from_dict,
        )
