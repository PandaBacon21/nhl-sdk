"""
TEAM ROSTER SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_prospects import ProspectsResult
from .team_roster_result import TeamRosterResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamRoster(CacheFetchMixin):
    """
    TeamRoster sub-resource.

    Provides access to team roster data including current/historical rosters,
    season availability, and prospects.

    Accessed via ``team.roster`` on a ``Team`` object.
    """
    def __init__(self, client: NhlClient, abbrev: str) -> None:
        self._client = client
        self._abbrev = abbrev
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.roster")
        self._ttl: int = 60 * 60 * 6

    def get_team_prospects(self) -> ProspectsResult:
        """
        Retrieve the prospect list for the team.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:roster:{team}:prospects",
            lambda: self._client._api.api_web.call_nhl_teams.get_team_prospects(team=team),
            self._logger, self._cache, self._ttl,
            ProspectsResult.from_dict,
        )

    def get_team_roster(self, season: int | None = None) -> TeamRosterResult:
        """
        Retrieve the roster for the team.

        Args:
            season (int, optional): Eight-digit season identifier (e.g. ``20242025``).
                Defaults to the current roster.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:roster:{team}:{season or 'now'}",
            lambda: self._client._api.api_web.call_nhl_teams.get_team_roster(team=team, season=season),
            self._logger, self._cache, self._ttl,
            TeamRosterResult.from_dict,
        )

    def get_roster_seasons(self) -> list[int]:
        """
        Retrieve the list of seasons for which the team has roster data.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:roster:{team}:seasons",
            lambda: self._client._api.api_web.call_nhl_teams.get_roster_season_by_team(team=team),
            self._logger, self._cache, self._ttl,
            lambda d: d or [],
        )
