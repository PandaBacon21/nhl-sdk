"""
TEAM SHOT LOCATION DETAIL RESULT
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ShotLocationEntry:
    """Shots on goal, goals, and shooting percentage for one rink area."""
    area: str | None
    sog: int | None
    sog_rank: int | None
    goals: int | None
    goals_rank: int | None
    shooting_pctg: float | None
    shooting_pctg_rank: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotLocationEntry:
        return cls(
            area = data.get("area"),
            sog = data.get("sog"),
            sog_rank = data.get("sogRank"),
            goals = data.get("goals"),
            goals_rank = data.get("goalsRank"),
            shooting_pctg = data.get("shootingPctg"),
            shooting_pctg_rank = data.get("shootingPctgRank"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "sog": self.sog,
            "sog_rank": self.sog_rank,
            "goals": self.goals,
            "goals_rank": self.goals_rank,
            "shooting_pctg": self.shooting_pctg,
            "shooting_pctg_rank": self.shooting_pctg_rank,
        }


@dataclass(slots=True, frozen=True)
class ShotLocationTotal:
    """Aggregated shot location stats for one location code × position group, with league averages."""
    location_code: str | None
    position: str | None
    sog: int | None
    sog_rank: int | None
    sog_league_avg: float | None
    goals: int | None
    goals_rank: int | None
    goals_league_avg: float | None
    shooting_pctg: float | None
    shooting_pctg_rank: int | None
    shooting_pctg_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotLocationTotal:
        return cls(
            location_code = data.get("locationCode"),
            position = data.get("position"),
            sog = data.get("sog"),
            sog_rank = data.get("sogRank"),
            sog_league_avg = data.get("sogLeagueAvg"),
            goals = data.get("goals"),
            goals_rank = data.get("goalsRank"),
            goals_league_avg = data.get("goalsLeagueAvg"),
            shooting_pctg = data.get("shootingPctg"),
            shooting_pctg_rank = data.get("shootingPctgRank"),
            shooting_pctg_league_avg = data.get("shootingPctgLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "position": self.position,
            "sog": self.sog,
            "sog_rank": self.sog_rank,
            "sog_league_avg": self.sog_league_avg,
            "goals": self.goals,
            "goals_rank": self.goals_rank,
            "goals_league_avg": self.goals_league_avg,
            "shooting_pctg": self.shooting_pctg,
            "shooting_pctg_rank": self.shooting_pctg_rank,
            "shooting_pctg_league_avg": self.shooting_pctg_league_avg,
        }


@dataclass(slots=True, frozen=True)
class TeamShotLocationResult:
    """
    Team shot location detail stats.

    Contains per-area breakdowns across 17 rink zones and aggregated
    totals by location code (all/high/long/mid) × position (all/F/D)
    with league averages and ranks.

    Instances of this class are accessed via `client.teams.stats.edge.shot_location`.
    """
    shot_location_details: list[ShotLocationEntry]
    shot_location_totals: list[ShotLocationTotal]

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotLocationResult:
        return cls(
            shot_location_details = [ShotLocationEntry.from_dict(e) for e in data.get("shotLocationDetails") or []],
            shot_location_totals = [ShotLocationTotal.from_dict(e) for e in data.get("shotLocationTotals") or []],
        )

    def to_dict(self) -> dict:
        return {
            "shot_location_details": [e.to_dict() for e in self.shot_location_details],
            "shot_location_totals": [e.to_dict() for e in self.shot_location_totals],
        }
