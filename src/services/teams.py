"""
TEAMS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache import get_cache
from ..models.teams.standings import Standings
from ..models.teams.team.team_stats import TeamStats

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class Teams:
    """
    Teams Collection

    This is the primary interface for Team related data.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams")

    @property
    def standings(self) -> Standings:
        """
        Access NHL standings data.

        Returns a Standings sub-resource with methods for current standings
        and per-season standings metadata.
        """
        return Standings(self._client)

    @property
    def stats(self) -> TeamStats:
        """
        Access per-team stats data.

        Returns a TeamStats sub-resource with methods for club skater/goalie
        stats, season/game-type metadata, and the current scoreboard.
        """
        return TeamStats(self._client)
