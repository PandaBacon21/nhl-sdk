"""
TEAM EDGE STATS
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .team_details import TeamDetails
from .team_comparison import TeamComparison
from .team_skating_distance_details import TeamSkatingDistance
from .team_skating_speed_details import TeamSkatingSpeedDetails
from .team_zone_details import TeamZoneDetails
from .team_shot_speed_details import TeamShotSpeedDetails
from .team_shot_location_details import TeamShotLocationDetails

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class TeamEdge:
    """
    Team NHL Edge sub-resource.

    Provides structured access to a team's NHL Edge statistical data.
    Each property returns a dedicated sub-resource with the team ID baked in.

    Accessed via ``team.stats.edge`` on a ``Team`` object.
    """
    def __init__(self, client: NhlClient, team_id: int):
        self._client = client
        self._team_id = team_id
        self._logger = logging.getLogger("nhl_sdk.teams.edge.team")

        self._logger.debug("TeamEdge initialized (team_id=%d)", team_id)

    @property
    def details(self) -> TeamDetails:
        """
        Access team NHL Edge detail stats.

        Returns a TeamDetails sub-resource with methods for retrieving
        a team's full Edge stat summary.
        """
        return TeamDetails(self._client, self._team_id)

    @property
    def comparison(self) -> TeamComparison:
        """
        Access team NHL Edge comparison data.

        Returns a TeamComparison sub-resource with methods for retrieving
        shot speed/skating speed breakdowns, last-10 skating distance,
        shot location data, zone time comparisons, and shot differentials.
        """
        return TeamComparison(self._client, self._team_id)

    @property
    def skating_distance(self) -> TeamSkatingDistance:
        """
        Access team NHL Edge skating distance detail stats.

        Returns a TeamSkatingDistance sub-resource with methods for retrieving
        per-situation distance breakdowns by strength and position.
        """
        return TeamSkatingDistance(self._client, self._team_id)

    @property
    def skating_speed(self) -> TeamSkatingSpeedDetails:
        """
        Access team NHL Edge skating speed detail stats.

        Returns a TeamSkatingSpeedDetails sub-resource with methods for retrieving
        top speed instances and per-position burst count breakdowns.
        """
        return TeamSkatingSpeedDetails(self._client, self._team_id)

    @property
    def zone_time(self) -> TeamZoneDetails:
        """
        Access team NHL Edge zone time detail stats.

        Returns a TeamZoneDetails sub-resource with methods for retrieving
        zone time percentages by strength code and shot differentials with ranks.
        """
        return TeamZoneDetails(self._client, self._team_id)

    @property
    def shot_speed(self) -> TeamShotSpeedDetails:
        """
        Access team NHL Edge shot speed detail stats.

        Returns a TeamShotSpeedDetails sub-resource with methods for retrieving
        hardest shot instances and per-position attempt bucket breakdowns.
        """
        return TeamShotSpeedDetails(self._client, self._team_id)

    @property
    def shot_location(self) -> TeamShotLocationDetails:
        """
        Access team NHL Edge shot location detail stats.

        Returns a TeamShotLocationDetails sub-resource with methods for retrieving
        per-area breakdowns and aggregated totals by location code and position.
        """
        return TeamShotLocationDetails(self._client, self._team_id)
