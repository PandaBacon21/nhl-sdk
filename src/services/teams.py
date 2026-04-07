"""
TEAMS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache import get_cache
from ..core.utilities import CacheFetchMixin
from ..models.teams.standings import Standings
from ..models.teams.team.team import Team, _NHL_TEAM_IDS
from ..models.teams.edge import TeamsEdge
from ..models.teams.team.team_stats.team_ref import TeamRef

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class Teams(CacheFetchMixin):
    """
    Teams Collection

    This is the primary interface for Team related data.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams")
        self._ttl: int = 60 * 60 * 24

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

    def all(self) -> list[TeamRef]:
        """
        Return all NHL teams from the NHL Stats API reference endpoint.

        Includes historical teams. For only active rosters use
        the known abbreviations via ``get(abbrev)``.
        """
        return self._fetch(
            "teams:all",
            lambda: self._client._api.api_stats.call_nhl_stats_teams.get_teams(),
            self._logger, self._cache, self._ttl,
            lambda d: [TeamRef.from_dict(t) for t in (d.get("data") or [])],
        )
