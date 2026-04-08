"""
TEAM SKATING DISTANCE TOP 10 RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ....players.player.player_stats.edge.player_edge_types import EdgeValue
from ..team_landing.team_landing_result import TeamEdgeLeaderTeam
from ..team_edge_types import TeamEdgePeak


@dataclass(slots=True, frozen=True)
class TeamDistanceLeaderEntry:
    """One team's entry in the skating distance top 10 leaderboard."""
    team: TeamEdgeLeaderTeam
    distance_total: EdgeValue
    distance_per_60: EdgeValue
    distance_max_per_game: TeamEdgePeak
    distance_max_per_period: TeamEdgePeak

    @classmethod
    def from_dict(cls, data: dict) -> TeamDistanceLeaderEntry:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            distance_total = EdgeValue.from_dict(data.get("distanceTotal") or {}),
            distance_per_60 = EdgeValue.from_dict(data.get("distancePer60") or {}),
            distance_max_per_game = TeamEdgePeak.from_dict(data.get("distanceMaxPerGame") or {}),
            distance_max_per_period = TeamEdgePeak.from_dict(data.get("distanceMaxPerPeriod") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "distance_total": self.distance_total.to_dict(),
            "distance_per_60": self.distance_per_60.to_dict(),
            "distance_max_per_game": self.distance_max_per_game.to_dict(),
            "distance_max_per_period": self.distance_max_per_period.to_dict(),
        }
