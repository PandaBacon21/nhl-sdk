"""
TEAMS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..models.teams.standings import Standings
from ..models.teams.team.team import Team, _NHL_TEAM_IDS
from ..models.teams.edge import TeamsEdge

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class Teams:
    """
    Teams Collection

    This is the primary interface for Team related data.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._logger = logging.getLogger("nhl_sdk.teams")

    def get(self, abbrev: str) -> Team:
        """
        Retrieve a team gateway object for the given abbreviation.

        Args:
            abbrev (str): Three-letter team code (e.g. ``"COL"``). Case-insensitive.

        Raises:
            ValueError: If the abbreviation is not recognized.
        """
        abbrev = abbrev.upper()
        team_id = _NHL_TEAM_IDS.get(abbrev)
        if team_id is None:
            raise ValueError(f"Unknown team abbreviation: {abbrev!r}")
        return Team(self._client, abbrev, team_id)

    @property
    def standings(self) -> Standings:
        """
        Access NHL standings data.

        Returns a Standings sub-resource with methods for current standings
        and per-season standings metadata.
        """
        return Standings(self._client)

    @property
    def edge(self) -> TeamsEdge:
        """
        Access league-wide team NHL Edge data.

        Returns a TeamsEdge sub-resource with methods for retrieving
        landing leaders and top-10 leaderboards across all NHL Edge categories.
        """
        return TeamsEdge(self._client)
