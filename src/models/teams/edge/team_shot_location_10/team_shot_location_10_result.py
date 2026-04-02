"""
TEAM SHOT LOCATION TOP 10 RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ..team_landing.team_landing_result import TeamEdgeLeaderTeam


@dataclass(slots=True, frozen=True)
class TeamShotLocationLeaderEntry:
    """One team's entry in the shot location top 10 leaderboard."""
    team: TeamEdgeLeaderTeam
    all: float | None
    high_danger: float | None
    mid_range: float | None
    long_range: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotLocationLeaderEntry:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            all = data.get("all"),
            high_danger = data.get("highDanger"),
            mid_range = data.get("midRange"),
            long_range = data.get("longRange"),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "all": self.all,
            "high_danger": self.high_danger,
            "mid_range": self.mid_range,
            "long_range": self.long_range,
        }
