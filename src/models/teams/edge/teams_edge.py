"""
TEAMS EDGE STATS (LEAGUE-WIDE)
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .team_landing import TeamLanding
from .team_shot_location_10 import TeamShotLocation10
from .team_shot_speed_10 import TeamShotSpeed10
from .team_skating_distance_10 import TeamSkatingDistance10
from .team_skating_speed_10 import TeamSkatingSpeed10
from .team_zone_time_10 import TeamZoneTime10

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamsEdge:
    """
    Teams NHL Edge sub-resource (league-wide).

    Provides structured access to league-wide NHL Edge statistical data for teams.
    Each property returns a dedicated sub-resource with its own methods.

    Accessed via `client.teams.edge`.
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._logger = logging.getLogger("nhl_sdk.teams.edge")

        self._logger.debug("TeamsEdge initialized")

    @property
    def landing(self) -> TeamLanding:
        """
        Access team Edge landing leaders.

        Returns a TeamLanding sub-resource with methods for retrieving
        the league-leading team per Edge category and available seasons.
        """
        return TeamLanding(self._client)

    @property
    def skating_distance_top_10(self) -> TeamSkatingDistance10:
        """
        Access team skating distance top 10 leaderboard.

        Returns a TeamSkatingDistance10 sub-resource with methods for retrieving
        the top 10 teams by skating distance, filterable by position, strength, and sort.
        """
        return TeamSkatingDistance10(self._client)

    @property
    def skating_speed_top_10(self) -> TeamSkatingSpeed10:
        """
        Access team skating speed top 10 leaderboard.

        Returns a TeamSkatingSpeed10 sub-resource with methods for retrieving
        the top 10 teams by skating speed, filterable by position and sort.
        """
        return TeamSkatingSpeed10(self._client)

    @property
    def zone_time_top_10(self) -> TeamZoneTime10:
        """
        Access team zone time top 10 leaderboard.

        Returns a TeamZoneTime10 sub-resource with methods for retrieving
        the top 10 teams by zone time, filterable by strength and sort.
        """
        return TeamZoneTime10(self._client)

    @property
    def shot_speed_top_10(self) -> TeamShotSpeed10:
        """
        Access team shot speed top 10 leaderboard.

        Returns a TeamShotSpeed10 sub-resource with methods for retrieving
        the top 10 teams by shot speed, filterable by position and sort.
        """
        return TeamShotSpeed10(self._client)

    @property
    def shot_location_top_10(self) -> TeamShotLocation10:
        """
        Access team shot location top 10 leaderboard.

        Returns a TeamShotLocation10 sub-resource with methods for retrieving
        the top 10 teams by shot location, filterable by category and sort.
        """
        return TeamShotLocation10(self._client)
