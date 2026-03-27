"""
GOALIE COMPARISON MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import EdgeSeason
from .goalie_save_pctg import GoalieSavePctgGame, GoalieSavePctgSummary
from .goalie_5v5 import GoalieFiveVFiveSummary


@dataclass(slots=True, frozen=True)
class GoalieComparisonShotSummary:
    """Shot summary by location zone — no percentile rankings."""
    location_code: str | None
    shots_against: int | None
    goals_against: int | None
    saves: int | None
    save_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieComparisonShotSummary:
        return cls(
            location_code=data.get("locationCode"),
            shots_against=data.get("shotsAgainst"),
            goals_against=data.get("goalsAgainst"),
            saves=data.get("saves"),
            save_pctg=data.get("savePctg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "shots_against": self.shots_against,
            "goals_against": self.goals_against,
            "saves": self.saves,
            "save_pctg": self.save_pctg,
        }


@dataclass(slots=True, frozen=True)
class GoalieComparisonShotDetail:
    """Shot detail by rink area — no percentile rankings."""
    area: str | None
    goals_against: int | None
    shots_against: int | None
    saves: int | None
    save_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieComparisonShotDetail:
        return cls(
            area=data.get("area"),
            goals_against=data.get("goalsAgainst"),
            shots_against=data.get("shotsAgainst"),
            saves=data.get("saves"),
            save_pctg=data.get("savePctg"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "goals_against": self.goals_against,
            "shots_against": self.shots_against,
            "saves": self.saves,
            "save_pctg": self.save_pctg,
        }


@dataclass(slots=True, frozen=True)
class GoalieComparison:
    """
    NHL Edge drill-down comparison data for a goalie.

    Provides shot location breakdowns (no percentile rankings), 5v5 save
    percentage (last 10 games and season summary), and overall save percentage
    (last 10 games and season summary).

    Instances of this class are accessed via `Stats.edge().comparison()`.
    """
    seasons_with_edge: list
    shot_location_summary: list
    shot_location_details: list
    save_pctg_5v5_last_10: list
    save_pctg_5v5_summary: GoalieFiveVFiveSummary
    save_pctg_last_10: list
    save_pctg_summary: GoalieSavePctgSummary

    @classmethod
    def from_dict(cls, data: dict) -> GoalieComparison:
        return cls(
            seasons_with_edge=[EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            shot_location_summary=[GoalieComparisonShotSummary.from_dict(s) for s in data.get("shotLocationSummary") or []],
            shot_location_details=[GoalieComparisonShotDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
            save_pctg_5v5_last_10=[GoalieSavePctgGame.from_dict(g) for g in data.get("savePctg5v5Last10") or []],
            save_pctg_5v5_summary=GoalieFiveVFiveSummary.from_dict(data.get("savePctg5v5Details") or {}),
            save_pctg_last_10=[GoalieSavePctgGame.from_dict(g) for g in data.get("savePctgLast10") or []],
            save_pctg_summary=GoalieSavePctgSummary.from_dict(data.get("savePctgDetails") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "shot_location_summary": [s.to_dict() for s in self.shot_location_summary],
            "shot_location_details": [d.to_dict() for d in self.shot_location_details],
            "save_pctg_5v5_last_10": [g.to_dict() for g in self.save_pctg_5v5_last_10],
            "save_pctg_5v5_summary": self.save_pctg_5v5_summary.to_dict(),
            "save_pctg_last_10": [g.to_dict() for g in self.save_pctg_last_10],
            "save_pctg_summary": self.save_pctg_summary.to_dict(),
        }
