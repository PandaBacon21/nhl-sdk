"""
TEAM ZONE TIME TOP 10 RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ..team_landing.team_landing_result import TeamEdgeLeaderTeam


@dataclass(slots=True, frozen=True)
class TeamZoneTimeLeaderEntry:
    """One team's entry in the zone time top 10 leaderboard."""
    team: TeamEdgeLeaderTeam
    offensive_zone_time: float | None
    neutral_zone_time: float | None
    defensive_zone_time: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamZoneTimeLeaderEntry:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            offensive_zone_time = data.get("offensiveZoneTime"),
            neutral_zone_time = data.get("neutralZoneTime"),
            defensive_zone_time = data.get("defensiveZoneTime"),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "offensive_zone_time": self.offensive_zone_time,
            "neutral_zone_time": self.neutral_zone_time,
            "defensive_zone_time": self.defensive_zone_time,
        }
