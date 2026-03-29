"""
LEADERS OBJECT
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from .player_leaders import SkaterLeaders, GoalieLeaders

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class Leaders:
    """
    Access NHL statistical leaders.

    Provides namespace access to skater and goalie leader data, including
    both stat leaders and NHL Edge leaderboards.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._logger = logging.getLogger("nhl_sdk.leaders")

    @property
    def skaters(self) -> SkaterLeaders:
        """
        Access skater stat leaders and Edge leaderboards.

        Returns a SkaterLeaders namespace with:
          - `.get_stat_leaders(season, game_type, categories, limit)` — stat leader lists
          - `.edge_landing(season, game_type)` — Edge landing leaders
          - `.edge_distance_top_10(...)`, `.edge_speed_top_10(...)`, etc. — Edge leaderboards
        """
        self._logger.debug("Retrieve SkaterLeaders")
        return SkaterLeaders(self._client)

    @property
    def goalies(self) -> GoalieLeaders:
        """
        Access goalie stat leaders and Edge leaderboards.

        Returns a GoalieLeaders namespace with:
          - `.get_stat_leaders(season, game_type, categories, limit)` — stat leader lists
          - `.edge_landing(season, game_type)` — Edge landing leaders
          - `.edge_five_v_five_top_10(...)`, `.edge_shot_location_top_10(...)`, etc. — Edge leaderboards
        """
        self._logger.debug("Retrieve GoalieLeaders")
        return GoalieLeaders(self._client)
