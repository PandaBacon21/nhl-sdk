"""
SKATER DISTANCE TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import LeaderPlayer, EdgeValue, EdgePeak


@dataclass(slots=True, frozen=True)
class DistanceLeaderEntry:
    """One player's entry in the skating distance top 10 leaderboard."""
    player: LeaderPlayer
    distance_total: EdgeValue
    distance_per_60: EdgeValue
    distance_max_per_game: EdgePeak
    distance_max_per_period: EdgePeak

    @classmethod
    def from_dict(cls, data: dict) -> DistanceLeaderEntry:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            distance_total = EdgeValue.from_dict(data.get("distanceTotal") or {}),
            distance_per_60 = EdgeValue.from_dict(data.get("distancePer60") or {}),
            distance_max_per_game = EdgePeak.from_dict(data.get("distanceMaxPerGame") or {}),
            distance_max_per_period = EdgePeak.from_dict(data.get("distanceMaxPerPeriod") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "distance_total": self.distance_total.to_dict(),
            "distance_per_60": self.distance_per_60.to_dict(),
            "distance_max_per_game": self.distance_max_per_game.to_dict(),
            "distance_max_per_period": self.distance_max_per_period.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class SkaterDistanceTop10:
    """
    Top 10 skaters ranked by skating distance.

    Can be retrieved for the current season or a specific season/game type.

    Note: this is a league-wide leaderboard, not a per-player stat.
    """
    entries: list

    @classmethod
    def from_list(cls, data: list) -> SkaterDistanceTop10:
        return cls(
            entries = [DistanceLeaderEntry.from_dict(e) for e in data or []],
        )

    def to_dict(self) -> dict:
        return {
            "entries": [e.to_dict() for e in self.entries],
        }
