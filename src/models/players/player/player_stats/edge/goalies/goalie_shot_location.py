"""
GOALIE SHOT LOCATION MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import EdgeSeason
from .goalie_details import GoalieShotLocationAreaDetail


@dataclass(slots=True, frozen=True)
class GoalieShotLocationTotal:
    """Zone totals with full percentile rankings and league averages for all four stat types."""
    location_code: str | None
    shots_against: int | None
    goals_against: int | None
    saves: int | None
    save_pctg: float | None
    shots_against_percentile: float | None
    goals_against_percentile: float | None
    saves_percentile: float | None
    save_pctg_percentile: float | None
    shots_against_league_avg: float | None
    goals_against_league_avg: float | None
    saves_league_avg: float | None
    save_pctg_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieShotLocationTotal:
        return cls(
            location_code=data.get("locationCode"),
            shots_against=data.get("shotsAgainst"),
            goals_against=data.get("goalsAgainst"),
            saves=data.get("saves"),
            save_pctg=data.get("savePctg"),
            shots_against_percentile=data.get("shotsAgainstPercentile"),
            goals_against_percentile=data.get("goalsAgainstPercentile"),
            saves_percentile=data.get("savesPercentile"),
            save_pctg_percentile=data.get("savePctgPercentile"),
            shots_against_league_avg=data.get("shotsAgainstLeagueAvg"),
            goals_against_league_avg=data.get("goalsAgainstLeagueAvg"),
            saves_league_avg=data.get("savesLeagueAvg"),
            save_pctg_league_avg=data.get("savePctgLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "shots_against": self.shots_against,
            "goals_against": self.goals_against,
            "saves": self.saves,
            "save_pctg": self.save_pctg,
            "shots_against_percentile": self.shots_against_percentile,
            "goals_against_percentile": self.goals_against_percentile,
            "saves_percentile": self.saves_percentile,
            "save_pctg_percentile": self.save_pctg_percentile,
            "shots_against_league_avg": self.shots_against_league_avg,
            "goals_against_league_avg": self.goals_against_league_avg,
            "saves_league_avg": self.saves_league_avg,
            "save_pctg_league_avg": self.save_pctg_league_avg,
        }


@dataclass(slots=True, frozen=True)
class GoalieShotLocation:
    """
    Per-player goalie shot location detail.

    Provides shots against, goals against, saves, and save percentage broken
    down by specific rink area (shotLocationDetails) and by location zone
    (shotLocationTotals — all/high/long/mid), with percentile rankings and
    league averages.

    Instances of this class are accessed via `Stats.edge.goalie.shot_location()`.
    """
    seasons_with_edge: list
    area_details: list
    zone_totals: list

    @classmethod
    def from_dict(cls, data: dict) -> GoalieShotLocation:
        return cls(
            seasons_with_edge=[EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            area_details=[GoalieShotLocationAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
            zone_totals=[GoalieShotLocationTotal.from_dict(t) for t in data.get("shotLocationTotals") or []],
        )

    def to_dict(self) -> dict:
        return {
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "area_details": [d.to_dict() for d in self.area_details],
            "zone_totals": [t.to_dict() for t in self.zone_totals],
        }
