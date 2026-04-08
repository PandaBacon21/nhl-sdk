"""
SKATER DETAILS MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import EdgeMeasurement, EdgeCount, EdgeSeason


@dataclass(slots=True, frozen=True)
class SkatingSpeed:
    """Skating speed stats: peak speed and bursts above 20 mph."""
    speed_max: EdgeMeasurement
    bursts_over_20: EdgeCount

    @classmethod
    def from_dict(cls, data: dict) -> SkatingSpeed:
        return cls(
            speed_max = EdgeMeasurement.from_dict(data.get("speedMax") or {}),
            bursts_over_20 = EdgeCount.from_dict(data.get("burstsOver20") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "speed_max": self.speed_max.to_dict(),
            "bursts_over_20": self.bursts_over_20.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class SogSummary:
    """Shot on goal summary for a specific location zone (all/high/long/mid)."""
    location_code: str | None
    shots: int | None
    shots_percentile: float | None
    shots_league_avg: float | None
    goals: int | None
    goals_percentile: float | None
    goals_league_avg: float | None
    shooting_pctg: float | None
    shooting_pctg_percentile: float | None
    shooting_pctg_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SogSummary:
        return cls(
            location_code = data.get("locationCode"),
            shots = data.get("shots"),
            shots_percentile = data.get("shotsPercentile"),
            shots_league_avg = data.get("shotsLeagueAvg"),
            goals = data.get("goals"),
            goals_percentile = data.get("goalsPercentile"),
            goals_league_avg = data.get("goalsLeagueAvg"),
            shooting_pctg = data.get("shootingPctg"),
            shooting_pctg_percentile = data.get("shootingPctgPercentile"),
            shooting_pctg_league_avg = data.get("shootingPctgLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "shots": self.shots,
            "shots_percentile": self.shots_percentile,
            "shots_league_avg": self.shots_league_avg,
            "goals": self.goals,
            "goals_percentile": self.goals_percentile,
            "goals_league_avg": self.goals_league_avg,
            "shooting_pctg": self.shooting_pctg,
            "shooting_pctg_percentile": self.shooting_pctg_percentile,
            "shooting_pctg_league_avg": self.shooting_pctg_league_avg,
        }


@dataclass(slots=True, frozen=True)
class SogDetail:
    """Shot on goal count and percentile for a specific rink area."""
    area: str | None
    shots: int | None
    shots_percentile: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SogDetail:
        return cls(
            area = data.get("area"),
            shots = data.get("shots"),
            shots_percentile = data.get("shotsPercentile"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "shots": self.shots,
            "shots_percentile": self.shots_percentile,
        }


@dataclass(slots=True, frozen=True)
class ZoneTimeDetails:
    """
    Zone time percentages and league rankings across offensive (total and even strength), 
    neutral, and defensive zones.
    """
    offensive_zone_pctg: float | None
    offensive_zone_percentile: float | None
    offensive_zone_league_avg: float | None
    offensive_zone_ev_pctg: float | None
    offensive_zone_ev_percentile: float | None
    offensive_zone_ev_league_avg: float | None
    neutral_zone_pctg: float | None
    neutral_zone_percentile: float | None
    neutral_zone_league_avg: float | None
    defensive_zone_pctg: float | None
    defensive_zone_percentile: float | None
    defensive_zone_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneTimeDetails:
        return cls(
            offensive_zone_pctg = data.get("offensiveZonePctg"),
            offensive_zone_percentile = data.get("offensiveZonePercentile"),
            offensive_zone_league_avg = data.get("offensiveZoneLeagueAvg"),
            offensive_zone_ev_pctg = data.get("offensiveZoneEvPctg"),
            offensive_zone_ev_percentile = data.get("offensiveZoneEvPercentile"),
            offensive_zone_ev_league_avg = data.get("offensiveZoneEvLeagueAvg"),
            neutral_zone_pctg = data.get("neutralZonePctg"),
            neutral_zone_percentile = data.get("neutralZonePercentile"),
            neutral_zone_league_avg = data.get("neutralZoneLeagueAvg"),
            defensive_zone_pctg = data.get("defensiveZonePctg"),
            defensive_zone_percentile = data.get("defensiveZonePercentile"),
            defensive_zone_league_avg = data.get("defensiveZoneLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "offensive_zone_pctg": self.offensive_zone_pctg,
            "offensive_zone_percentile": self.offensive_zone_percentile,
            "offensive_zone_league_avg": self.offensive_zone_league_avg,
            "offensive_zone_ev_pctg": self.offensive_zone_ev_pctg,
            "offensive_zone_ev_percentile": self.offensive_zone_ev_percentile,
            "offensive_zone_ev_league_avg": self.offensive_zone_ev_league_avg,
            "neutral_zone_pctg": self.neutral_zone_pctg,
            "neutral_zone_percentile": self.neutral_zone_percentile,
            "neutral_zone_league_avg": self.neutral_zone_league_avg,
            "defensive_zone_pctg": self.defensive_zone_pctg,
            "defensive_zone_percentile": self.defensive_zone_percentile,
            "defensive_zone_league_avg": self.defensive_zone_league_avg,
        }


@dataclass(slots=True, frozen=True)
class SkaterDetails:
    """
    NHL Edge rankings and stat summaries for a skater.

    Provides a full per-category summary including shot speed, skating speed,
    distance skated, shot on goal details, and zone time percentages.

    Instances of this class are accessed via `Stats.edge().details()`.
    """
    seasons_with_edge: list
    top_shot_speed: EdgeMeasurement
    skating_speed: SkatingSpeed
    total_distance_skated: EdgeMeasurement
    distance_max_game: EdgeMeasurement
    sog_summary: list
    sog_details: list
    zone_time: ZoneTimeDetails

    @classmethod
    def from_dict(cls, data: dict) -> SkaterDetails:
        return cls(
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            top_shot_speed = EdgeMeasurement.from_dict(data.get("topShotSpeed") or {}),
            skating_speed = SkatingSpeed.from_dict(data.get("skatingSpeed") or {}),
            total_distance_skated = EdgeMeasurement.from_dict(data.get("totalDistanceSkated") or {}),
            distance_max_game = EdgeMeasurement.from_dict(data.get("distanceMaxGame") or {}),
            sog_summary = [SogSummary.from_dict(s) for s in data.get("sogSummary") or []],
            sog_details = [SogDetail.from_dict(d) for d in data.get("sogDetails") or []],
            zone_time = ZoneTimeDetails.from_dict(data.get("zoneTimeDetails") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "top_shot_speed": self.top_shot_speed.to_dict(),
            "skating_speed": self.skating_speed.to_dict(),
            "total_distance_skated": self.total_distance_skated.to_dict(),
            "distance_max_game": self.distance_max_game.to_dict(),
            "sog_summary": [s.to_dict() for s in self.sog_summary],
            "sog_details": [d.to_dict() for d in self.sog_details],
            "zone_time": self.zone_time.to_dict(),
        }
