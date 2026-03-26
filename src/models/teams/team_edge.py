"""
TEAM EDGE STATS
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamEdge:
    """
    Team NHL Edge sub-resource.

    Provides structured access to a team's NHL Edge statistical data,
    including details, comparison, skating distance/speed,
    zone time, shot speed, and shot location.

    Instances of this class are accessed via `Stats.edge.team`.
    Methods require a `team_id` parameter.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._logger = logging.getLogger("nhl_sdk.player.stats.edge.team")

        self._logger.debug("TeamEdge initialized")
