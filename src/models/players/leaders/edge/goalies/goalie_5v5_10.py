"""
GOALIE 5V5 TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ....player.player_stats.edge.player_edge_types import LeaderPlayer


@dataclass(slots=True, frozen=True)
class GoalieFiveVFiveLeaderEntry:
    """One goalie's entry in the 5v5 save percentage top 10 leaderboard."""
    player: LeaderPlayer
    save_pctg: float | None
    save_pctg_close: float | None
    shots: int | None
    shots_per_60: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieFiveVFiveLeaderEntry:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            save_pctg = data.get("savePctg"),
            save_pctg_close = data.get("savePctgClose"),
            shots = data.get("shots"),
            shots_per_60 = data.get("shotsPer60"),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "save_pctg": self.save_pctg,
            "save_pctg_close": self.save_pctg_close,
            "shots": self.shots,
            "shots_per_60": self.shots_per_60,
        }
