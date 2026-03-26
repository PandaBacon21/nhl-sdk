"""
SKATER ZONE TIME TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import LeaderPlayer


@dataclass(slots=True, frozen=True)
class ZoneTimeLeaderEntry:
    """One player's entry in the zone time top 10 leaderboard."""
    player: LeaderPlayer
    offensive_zone_time: float | None
    neutral_zone_time: float | None
    defensive_zone_time: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneTimeLeaderEntry:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            offensive_zone_time = data.get("offensiveZoneTime"),
            neutral_zone_time = data.get("neutralZoneTime"),
            defensive_zone_time = data.get("defensiveZoneTime"),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "offensive_zone_time": self.offensive_zone_time,
            "neutral_zone_time": self.neutral_zone_time,
            "defensive_zone_time": self.defensive_zone_time,
        }


@dataclass(slots=True, frozen=True)
class SkaterZoneTimeTop10:
    """
    Top 10 skaters ranked by zone time percentage.

    Can be retrieved for the current season or a specific season/game type.

    Note: this is a league-wide leaderboard, not a per-player stat.
    """
    entries: list

    @classmethod
    def from_list(cls, data: list) -> SkaterZoneTimeTop10:
        return cls(
            entries = [ZoneTimeLeaderEntry.from_dict(e) for e in data or []],
        )

    def to_dict(self) -> dict:
        return {
            "entries": [e.to_dict() for e in self.entries],
        }
