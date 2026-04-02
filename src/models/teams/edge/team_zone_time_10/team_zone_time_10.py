"""
TEAM ZONE TIME TOP 10 SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_zone_time_10_result import TeamZoneTimeLeaderEntry

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamZoneTime10(CacheFetchMixin):
    """
    Team zone time top 10 sub-resource.

    Returns the top 10 teams by zone time, filterable by strength and sort metric.

    Accessed via `client.teams.edge.zone_time_top_10`.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.zone_time_10")
        self._ttl: int = 60 * 60 * 1

    def get_top_10(
        self,
        strength: str,
        sort: str,
        season: int | None = None,
        game_type: int | None = None,
    ) -> list[TeamZoneTimeLeaderEntry]:
        """
        Retrieve the top 10 teams by zone time.

        Args:
            strength (str): Strength filter (``"all"``, ``"pp"``, ``"pk"``, ``"es"``).
            sort (str): Sort metric (``"offensive"``, ``"neutral"``, ``"defensive"``).
            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season).
        """
        if season and game_type:
            key = f"teams:edge:zone_time_10:{strength}:{sort}:{season}:{game_type}"
        else:
            key = f"teams:edge:zone_time_10:{strength}:{sort}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_zone_time_10(
                strength=strength, sort=sort, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            lambda d: [TeamZoneTimeLeaderEntry.from_dict(e) for e in (d or [])],
        )
