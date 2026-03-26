"""
SKATER SPEED TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import LeaderPlayer, EdgePeak


@dataclass(slots=True, frozen=True)
class SpeedLeaderEntry:
    """One player's entry in the skating speed top 10 leaderboard."""
    player: LeaderPlayer
    max_speed: EdgePeak
    bursts_over_22: int | None
    bursts_20_22: int | None
    bursts_18_20: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SpeedLeaderEntry:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            max_speed = EdgePeak.from_dict(data.get("maxSpeed") or {}),
            bursts_over_22 = data.get("burstsOver22"),
            bursts_20_22 = data.get("bursts20To22"),
            bursts_18_20 = data.get("bursts18To20"),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "max_speed": self.max_speed.to_dict(),
            "bursts_over_22": self.bursts_over_22,
            "bursts_20_22": self.bursts_20_22,
            "bursts_18_20": self.bursts_18_20,
        }


@dataclass(slots=True, frozen=True)
class SkaterSpeedTop10:
    """
    Top 10 skaters ranked by skating speed.

    Can be retrieved for the current season or a specific season/game type.

    Note: this is a league-wide leaderboard, not a per-player stat.
    """
    entries: list

    @classmethod
    def from_list(cls, data: list) -> SkaterSpeedTop10:
        return cls(
            entries = [SpeedLeaderEntry.from_dict(e) for e in data or []],
        )

    def to_dict(self) -> dict:
        return {
            "entries": [e.to_dict() for e in self.entries],
        }
