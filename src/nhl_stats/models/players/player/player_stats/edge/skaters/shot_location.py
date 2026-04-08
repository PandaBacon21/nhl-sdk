"""
SKATER SHOT LOCATION MODEL
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ShotAreaDetail:
    """Shots on goal, goals, and shooting percentage with percentile rankings for a specific rink area."""
    area: str | None
    sog: int | None
    goals: int | None
    shooting_pctg: float | None
    sog_percentile: float | None
    goals_percentile: float | None
    shooting_pctg_percentile: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotAreaDetail:
        return cls(
            area = data.get("area"),
            sog = data.get("sog"),
            goals = data.get("goals"),
            shooting_pctg = data.get("shootingPctg"),
            sog_percentile = data.get("sogPercentile"),
            goals_percentile = data.get("goalsPercentile"),
            shooting_pctg_percentile = data.get("shootingPctgPercentile"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "sog": self.sog,
            "goals": self.goals,
            "shooting_pctg": self.shooting_pctg,
            "sog_percentile": self.sog_percentile,
            "goals_percentile": self.goals_percentile,
            "shooting_pctg_percentile": self.shooting_pctg_percentile,
        }


@dataclass(slots=True, frozen=True)
class ShotZoneTotal:
    """Shots on goal, goals, and shooting percentage with percentile rankings and league averages for a location zone."""
    location_code: str | None
    sog: int | None
    goals: int | None
    shooting_pctg: float | None
    sog_percentile: float | None
    goals_percentile: float | None
    shooting_pctg_percentile: float | None
    sog_league_avg: float | None
    goals_league_avg: float | None
    shooting_pctg_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotZoneTotal:
        return cls(
            location_code = data.get("locationCode"),
            sog = data.get("sog"),
            goals = data.get("goals"),
            shooting_pctg = data.get("shootingPctg"),
            sog_percentile = data.get("sogPercentile"),
            goals_percentile = data.get("goalsPercentile"),
            shooting_pctg_percentile = data.get("shootingPctgPercentile"),
            sog_league_avg = data.get("sogLeagueAvg"),
            goals_league_avg = data.get("goalsLeagueAvg"),
            shooting_pctg_league_avg = data.get("shootingPctgLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "sog": self.sog,
            "goals": self.goals,
            "shooting_pctg": self.shooting_pctg,
            "sog_percentile": self.sog_percentile,
            "goals_percentile": self.goals_percentile,
            "shooting_pctg_percentile": self.shooting_pctg_percentile,
            "sog_league_avg": self.sog_league_avg,
            "goals_league_avg": self.goals_league_avg,
            "shooting_pctg_league_avg": self.shooting_pctg_league_avg,
        }


@dataclass(slots=True, frozen=True)
class ShotLocation:
    """
    Per-player shot location detail.

    Provides shots on goal, goals, and shooting percentage broken down by
    specific rink area and by location zone (all/high/long/mid), with
    percentile rankings and league averages.

    Instances of this class are accessed via `Stats.edge().shot_location()`.
    """
    area_details: list
    zone_totals: list

    @classmethod
    def from_dict(cls, data: dict) -> ShotLocation:
        return cls(
            area_details = [ShotAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
            zone_totals = [ShotZoneTotal.from_dict(t) for t in data.get("shotLocationTotals") or []],
        )

    def to_dict(self) -> dict:
        return {
            "area_details": [d.to_dict() for d in self.area_details],
            "zone_totals": [t.to_dict() for t in self.zone_totals],
        }
