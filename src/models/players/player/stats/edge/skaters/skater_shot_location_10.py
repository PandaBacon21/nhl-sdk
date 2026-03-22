"""
SKATER SHOT LOCATION TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..edge_types import LeaderPlayer


@dataclass(slots=True, frozen=True)
class ShotLocationLeaderEntry:
    """One player's entry in the shot location top 10 leaderboard."""
    player: LeaderPlayer
    all: int | None
    high_danger: int | None
    mid_range: int | None
    long_range: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotLocationLeaderEntry:
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


@dataclass(slots=True, frozen=True)
class SkaterShotLocationTop10:
    """
    Top 10 skaters ranked by shot location category.

    Can be retrieved for the current season or a specific season/game type.

    Note: this is a league-wide leaderboard, not a per-player stat.
    """
    entries: list

    @classmethod
    def from_list(cls, data: list) -> SkaterShotLocationTop10:
        return cls(
            entries = [ShotLocationLeaderEntry.from_dict(e) for e in data or []],
        )

    def to_dict(self) -> dict:
        return {
            "entries": [e.to_dict() for e in self.entries],
        }
