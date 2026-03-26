"""
SKATER SHOT SPEED TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import LeaderPlayer, EdgePeak


@dataclass(slots=True, frozen=True)
class ShotSpeedLeaderEntry:
    """One player's entry in the shot speed top 10 leaderboard."""
    player: LeaderPlayer
    hardest_shot: EdgePeak
    shot_attempts_over_100: int | None
    shot_attempts_90_100: int | None
    shot_attempts_80_90: int | None
    shot_attempts_70_80: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotSpeedLeaderEntry:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            hardest_shot = EdgePeak.from_dict(data.get("hardestShot") or {}),
            shot_attempts_over_100 = data.get("shotAttemptsOver100"),
            shot_attempts_90_100 = data.get("shotAttempts90To100"),
            shot_attempts_80_90 = data.get("shotAttempts80To90"),
            shot_attempts_70_80 = data.get("shotAttempts70To80"),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "hardest_shot": self.hardest_shot.to_dict(),
            "shot_attempts_over_100": self.shot_attempts_over_100,
            "shot_attempts_90_100": self.shot_attempts_90_100,
            "shot_attempts_80_90": self.shot_attempts_80_90,
            "shot_attempts_70_80": self.shot_attempts_70_80,
        }


@dataclass(slots=True, frozen=True)
class SkaterShotSpeedTop10:
    """
    Top 10 skaters ranked by shot speed.

    Can be retrieved for the current season or a specific season/game type.

    Note: this is a league-wide leaderboard, not a per-player stat.
    """
    entries: list

    @classmethod
    def from_list(cls, data: list) -> SkaterShotSpeedTop10:
        return cls(
            entries = [ShotSpeedLeaderEntry.from_dict(e) for e in data or []],
        )

    def to_dict(self) -> dict:
        return {
            "entries": [e.to_dict() for e in self.entries],
        }
