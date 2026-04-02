"""
TEAM SKATING SPEED TOP 10 RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ....players.player.player_stats.edge.player_edge_types import EdgePeak
from ..team_landing.team_landing_result import TeamEdgeLeaderTeam


@dataclass(slots=True, frozen=True)
class TeamSpeedLeaderEntry:
    """One team's entry in the skating speed top 10 leaderboard."""
    team: TeamEdgeLeaderTeam
    max_skating_speed: EdgePeak
    bursts_over_22: int | None
    bursts_20_to_22: int | None
    bursts_18_to_20: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamSpeedLeaderEntry:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            max_skating_speed = EdgePeak.from_dict(data.get("maxSkatingSpeed") or {}),
            bursts_over_22 = data.get("burstsOver22"),
            bursts_20_to_22 = data.get("bursts20To22"),
            bursts_18_to_20 = data.get("bursts18To20"),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "max_skating_speed": self.max_skating_speed.to_dict(),
            "bursts_over_22": self.bursts_over_22,
            "bursts_20_to_22": self.bursts_20_to_22,
            "bursts_18_to_20": self.bursts_18_to_20,
        }
