"""
TEAM SHOT LOCATION TOP 10 SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_shot_location_10_result import TeamShotLocationLeaderEntry

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class TeamShotLocation10(CacheFetchMixin):
    """
    Team shot location top 10 sub-resource.

    Returns the top 10 teams by shot location metric, filterable by category and sort.

    Accessed via `client.teams.edge.shot_location_top_10`.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.edge.shot_location_10")
        self._ttl: int = 60 * 60 * 1

    def get_top_10(
        self,
        category: str,
        sort: str,
        season: int | None = None,
        game_type: int | None = None,
    ) -> list[TeamShotLocationLeaderEntry]:
        """
        Retrieve the top 10 teams by shot location.

        Args:
            category (str): Stat category (``"sog"``, ``"goals"``, ``"shooting-pctg"``).
            sort (str): Sort metric (``"all"``, ``"high"``, ``"mid"``, ``"long"``).
            season (int, optional): Season in YYYYYYYY format.
            game_type (int, optional): Game type (e.g. ``2`` for regular season).
        """
        if season and game_type:
            key = f"teams:edge:shot_location_10:{category}:{sort}:{season}:{game_type}"
        else:
            key = f"teams:edge:shot_location_10:{category}:{sort}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_team.get_team_shot_location_10(
                category=category, sort=sort, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            lambda d: [TeamShotLocationLeaderEntry.from_dict(e) for e in (d or [])],
        )
