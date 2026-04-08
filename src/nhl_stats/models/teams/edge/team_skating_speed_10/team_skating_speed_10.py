"""
TEAM SKATING SPEED TOP 10 SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_skating_speed_10_result import TeamSpeedLeaderEntry

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class TeamSkatingSpeed10(CacheFetchMixin):
    """
    Team skating speed top 10 sub-resource.

    Returns the top 10 teams by skating speed, filterable by position and sort metric.

    Accessed via `client.teams.edge.skating_speed_top_10`.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.skating_speed_10")
        self._ttl: int = 60 * 60 * 1

    def get_top_10(
        self,
        sort: str,
        pos: str = "all",
        season: int | None = None,
        game_type: int | None = None,
    ) -> list[TeamSpeedLeaderEntry]:
        """
        Retrieve the top 10 teams by skating speed.

        Args:
            sort (str): Sort metric (``"max"``, ``"over-22"``, ``"20-22"``, ``"18-20"``).
            pos (str): Position filter (``"all"``, ``"F"``, ``"D"``). Defaults to ``"all"``.
            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season).
        """
        if season and game_type:
            key = f"teams:edge:skating_speed_10:{pos}:{sort}:{season}:{game_type}"
        else:
            key = f"teams:edge:skating_speed_10:{pos}:{sort}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10(
                sort=sort, pos=pos, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            lambda d: [TeamSpeedLeaderEntry.from_dict(e) for e in (d or [])],
        )
