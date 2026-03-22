"""
GOALIE EDGE STATS
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GoalieEdge:
    """
    Per-player goalie NHL Edge sub-resource.

    Provides structured access to a goalie's NHL Edge statistical data,
    including details, comparison, 5v5 save percentage, shot location,
    save percentage, and CAT details.

    Instances of this class are accessed via `Stats.edge.goalie`.
    """
    def __init__(self, pid: int, client: NhlClient):
        self._pid = pid
        self._client = client
        self._logger = logging.getLogger("nhl_sdk.player.stats.edge.goalie")

        self._logger.debug(f"{self._pid} GoalieEdge initialized")
