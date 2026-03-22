"""
PLAYER EDGE STATS
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .skaters.skater_edge import SkaterEdge
from .goalies.goalie_edge import GoalieEdge
from .teams.team_edge import TeamEdge

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class EdgeStats:
    """
    Player NHL Edge statistical sub-resource.

    Provides structured access to NHL Edge data across skaters, goalies, and teams.

    Instances of this class are accessed via `Stats.edge`.

    Attributes
    ----------
    skater : SkaterEdge
        Per-player skater Edge stats (details, comparison, distance, speed, etc.)
    goalie : GoalieEdge
        Per-player goalie Edge stats.
    team : TeamEdge
        Team-level Edge stats. Methods require a `team_id` parameter.
    """
    def __init__(self, pid: int, client: NhlClient):
        self._pid = pid
        self._logger = logging.getLogger("nhl_sdk.player.stats.edge")

        self.skater: SkaterEdge = SkaterEdge(pid=pid, client=client)
        self.goalie: GoalieEdge = GoalieEdge(pid=pid, client=client)
        self.team: TeamEdge = TeamEdge(client=client)

        self._logger.debug(f"{self._pid} EdgeStats initialized")
