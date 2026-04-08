"""
GOALIE SHOT LOCATION TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ....player.player_stats.edge.player_edge_types import LeaderPlayer


@dataclass(slots=True, frozen=True)
class GoalieShotLocationLeaderEntry:
    """One goalie's entry in the shot location top 10 leaderboard."""
    player: LeaderPlayer
    all: int | None
    high_danger: int | None
    mid_range: int | None
    long_range: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieShotLocationLeaderEntry:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            all = data.get("all"),
            high_danger = data.get("highDanger"),
            mid_range = data.get("midRange"),
            long_range = data.get("longRange"),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "all": self.all,
            "high_danger": self.high_danger,
            "mid_range": self.mid_range,
            "long_range": self.long_range,
        }
