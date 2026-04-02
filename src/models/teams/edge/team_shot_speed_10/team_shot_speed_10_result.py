"""
TEAM SHOT SPEED TOP 10 RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ....players.player.player_stats.edge.player_edge_types import EdgePeak
from ..team_landing.team_landing_result import TeamEdgeLeaderTeam


@dataclass(slots=True, frozen=True)
class TeamShotSpeedLeaderEntry:
    """One team's entry in the shot speed top 10 leaderboard."""
    team: TeamEdgeLeaderTeam
    hardest_shot: EdgePeak
    shot_attempts_over_100: int | None
    shot_attempts_90_to_100: int | None
    shot_attempts_80_to_90: int | None
    shot_attempts_70_to_80: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotSpeedLeaderEntry:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            hardest_shot = EdgePeak.from_dict(data.get("hardestShot") or {}),
            shot_attempts_over_100 = data.get("shotAttemptsOver100"),
            shot_attempts_90_to_100 = data.get("shotAttempts90To100"),
            shot_attempts_80_to_90 = data.get("shotAttempts80To90"),
            shot_attempts_70_to_80 = data.get("shotAttempts70To80"),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "hardest_shot": self.hardest_shot.to_dict(),
            "shot_attempts_over_100": self.shot_attempts_over_100,
            "shot_attempts_90_to_100": self.shot_attempts_90_to_100,
            "shot_attempts_80_to_90": self.shot_attempts_80_to_90,
            "shot_attempts_70_to_80": self.shot_attempts_70_to_80,
        }
