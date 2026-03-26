"""
GOALIE 5V5 SAVE PERCENTAGE MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import EdgeCount, EdgeSeason
from .goalie_save_pctg import GoalieSavePctgGame


@dataclass(slots=True, frozen=True)
class GoalieFiveVFiveSummary:
    """Season 5v5 save percentage summary with percentile rankings and league averages."""
    save_pctg: EdgeCount
    save_pctg_close: EdgeCount
    shots: EdgeCount
    shots_per_60: EdgeCount

    @classmethod
    def from_dict(cls, data: dict) -> GoalieFiveVFiveSummary:
        return cls(
            save_pctg=EdgeCount.from_dict(data.get("savePctg") or {}),
            save_pctg_close=EdgeCount.from_dict(data.get("savePctgClose") or {}),
            shots=EdgeCount.from_dict(data.get("shots") or {}),
            shots_per_60=EdgeCount.from_dict(data.get("shotsPer60") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "save_pctg": self.save_pctg.to_dict(),
            "save_pctg_close": self.save_pctg_close.to_dict(),
            "shots": self.shots.to_dict(),
            "shots_per_60": self.shots_per_60.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class GoalieFiveVFive:
    """
    Per-player 5v5 save percentage detail.

    Provides the last 10 games of 5v5 save percentage, plus a season
    summary of 5v5 save percentage, close-game save percentage, shots faced,
    and shots per 60 — each with percentile rankings and league averages.

    Instances of this class are accessed via `Stats.edge.goalie.five_v_five()`.
    """
    seasons_with_edge: list
    last_10_games: list
    save_pctg_5v5_summary: GoalieFiveVFiveSummary

    @classmethod
    def from_dict(cls, data: dict) -> GoalieFiveVFive:
        return cls(
            seasons_with_edge=[EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            last_10_games=[GoalieSavePctgGame.from_dict(g) for g in data.get("savePctg5v5Last10") or []],
            save_pctg_5v5_summary=GoalieFiveVFiveSummary.from_dict(data.get("savePctg5v5Details") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "last_10_games": [g.to_dict() for g in self.last_10_games],
            "save_pctg_5v5_summary": self.save_pctg_5v5_summary.to_dict(),
        }
