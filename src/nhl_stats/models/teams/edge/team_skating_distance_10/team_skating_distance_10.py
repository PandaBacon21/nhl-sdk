"""
TEAM SKATING DISTANCE TOP 10 SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_skating_distance_10_result import TeamDistanceLeaderEntry

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class TeamSkatingDistance10(CacheFetchMixin):
    """
    Team skating distance top 10 sub-resource.

    Returns the top 10 teams by skating distance, filterable by position,
    strength situation, and sort metric.

    Accessed via `client.teams.edge.skating_distance_top_10`.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.skating_distance_10")
        self._ttl: int = 60 * 60 * 1

    def get_top_10(
        self,
        strength: str,
        sort: str,
        pos: str = "all",
        season: int | None = None,
        game_type: int | None = None,
    ) -> list[TeamDistanceLeaderEntry]:
        """
        Retrieve the top 10 teams by skating distance.

        Args:
            strength (str): Strength situation (``"all"``, ``"es"``, ``"pp"``, ``"pk"``).
            sort (str): Sort metric (``"total"``, ``"per-60"``, ``"max-game"``, ``"max-period"``).
            pos (str): Position filter (``"all"``, ``"F"``, ``"D"``). Defaults to ``"all"``.
            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season).
        """
        if season and game_type:
            key = f"teams:edge:skating_distance_10:{pos}:{strength}:{sort}:{season}:{game_type}"
        else:
            key = f"teams:edge:skating_distance_10:{pos}:{strength}:{sort}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10(
                strength=strength, sort=sort, pos=pos, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            lambda d: [TeamDistanceLeaderEntry.from_dict(e) for e in (d or [])],
        )
