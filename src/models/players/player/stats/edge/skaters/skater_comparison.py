"""
SKATER COMPARISON MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..edge_types import EdgeValue, EdgePeak, EdgeSeason


@dataclass(slots=True, frozen=True)
class ShotSpeedDetails:
    """Shot speed breakdown: peak, average, and attempt counts by speed range."""
    top_shot_speed: EdgePeak
    avg_shot_speed: EdgeValue
    shot_attempts_over_100: int | None
    shot_attempts_90_100: int | None
    shot_attempts_80_90: int | None
    shot_attempts_70_80: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotSpeedDetails:
        return cls(
            top_shot_speed = EdgePeak.from_dict(data.get("topShotSpeed") or {}),
            avg_shot_speed = EdgeValue.from_dict(data.get("avgShotSpeed") or {}),
            shot_attempts_over_100 = data.get("shotAttemptsOver100"),
            shot_attempts_90_100 = data.get("shotAttempts90To100"),
            shot_attempts_80_90 = data.get("shotAttempts80To90"),
            shot_attempts_70_80 = data.get("shotAttempts70To80"),
        )

    def to_dict(self) -> dict:
        return {
            "top_shot_speed": self.top_shot_speed.to_dict(),
            "avg_shot_speed": self.avg_shot_speed.to_dict(),
            "shot_attempts_over_100": self.shot_attempts_over_100,
            "shot_attempts_90_100": self.shot_attempts_90_100,
            "shot_attempts_80_90": self.shot_attempts_80_90,
            "shot_attempts_70_80": self.shot_attempts_70_80,
        }


@dataclass(slots=True, frozen=True)
class SkatingSpeedDetails:
    """Skating speed breakdown: peak speed and burst counts by speed range."""
    max_skating_speed: EdgePeak
    bursts_over_22: int | None
    bursts_20_22: int | None
    bursts_18_20: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SkatingSpeedDetails:
        return cls(
            max_skating_speed = EdgePeak.from_dict(data.get("maxSkatingSpeed") or {}),
            bursts_over_22 = data.get("burstsOver22"),
            bursts_20_22 = data.get("bursts20To22"),
            bursts_18_20 = data.get("bursts18To20"),
        )

    def to_dict(self) -> dict:
        return {
            "max_skating_speed": self.max_skating_speed.to_dict(),
            "bursts_over_22": self.bursts_over_22,
            "bursts_20_22": self.bursts_20_22,
            "bursts_18_20": self.bursts_18_20,
        }


@dataclass(slots=True, frozen=True)
class DistanceGame:
    """Skating distance and TOI for a single game."""
    game_center_link: str | None
    game_date: str | None
    player_on_home_team: bool | None
    distance_skated: EdgeValue
    toi: float | None
    home_team: dict | None
    away_team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> DistanceGame:
        return cls(
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            player_on_home_team = data.get("playerOnHomeTeam"),
            distance_skated = EdgeValue.from_dict(data.get("distanceSkated") or {}),
            toi = data.get("toi"),
            home_team = data.get("homeTeam"),
            away_team = data.get("awayTeam"),
        )

    def to_dict(self) -> dict:
        return {
            "game_center_link": self.game_center_link,
            "game_date": self.game_date,
            "player_on_home_team": self.player_on_home_team,
            "distance_skated": self.distance_skated.to_dict(),
            "toi": self.toi,
            "home_team": self.home_team,
            "away_team": self.away_team,
        }


@dataclass(slots=True, frozen=True)
class SkatingDistanceDetails:
    """Season skating distance totals and peak game/period performances."""
    distance_total: EdgeValue
    distance_per_60: EdgeValue
    distance_max_game: EdgePeak
    distance_max_period: EdgePeak

    @classmethod
    def from_dict(cls, data: dict) -> SkatingDistanceDetails:
        return cls(
            distance_total = EdgeValue.from_dict(data.get("distanceTotal") or {}),
            distance_per_60 = EdgeValue.from_dict(data.get("distancePer60") or {}),
            distance_max_game = EdgePeak.from_dict(data.get("distanceMaxGame") or {}),
            distance_max_period = EdgePeak.from_dict(data.get("distanceMaxPeriod") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "distance_total": self.distance_total.to_dict(),
            "distance_per_60": self.distance_per_60.to_dict(),
            "distance_max_game": self.distance_max_game.to_dict(),
            "distance_max_period": self.distance_max_period.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class ShotLocationDetail:
    """Goals, shots on goal, and shooting percentage for a specific rink area."""
    area: str | None
    sog: int | None
    goals: int | None
    shooting_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotLocationDetail:
        return cls(
            area = data.get("area"),
            sog = data.get("sog"),
            goals = data.get("goals"),
            shooting_pctg = data.get("shootingPctg"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "sog": self.sog,
            "goals": self.goals,
            "shooting_pctg": self.shooting_pctg,
        }


@dataclass(slots=True, frozen=True)
class ShotLocationTotal:
    """Goals, shots on goal, and shooting percentage rolled up by location zone."""
    location_code: str | None
    sog: int | None
    goals: int | None
    shooting_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotLocationTotal:
        return cls(
            location_code = data.get("locationCode"),
            sog = data.get("sog"),
            goals = data.get("goals"),
            shooting_pctg = data.get("shootingPctg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "sog": self.sog,
            "goals": self.goals,
            "shooting_pctg": self.shooting_pctg,
        }


@dataclass(slots=True, frozen=True)
class ZoneTimeComparison:
    """Zone time percentages with league averages (no percentile rankings)."""
    offensive_zone_pctg: float | None
    offensive_zone_league_avg: float | None
    neutral_zone_pctg: float | None
    neutral_zone_league_avg: float | None
    defensive_zone_pctg: float | None
    defensive_zone_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneTimeComparison:
        return cls(
            offensive_zone_pctg = data.get("offensiveZonePctg"),
            offensive_zone_league_avg = data.get("offensiveZoneLeagueAvg"),
            neutral_zone_pctg = data.get("neutralZonePctg"),
            neutral_zone_league_avg = data.get("neutralZoneLeagueAvg"),
            defensive_zone_pctg = data.get("defensiveZonePctg"),
            defensive_zone_league_avg = data.get("defensiveZoneLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "offensive_zone_pctg": self.offensive_zone_pctg,
            "offensive_zone_league_avg": self.offensive_zone_league_avg,
            "neutral_zone_pctg": self.neutral_zone_pctg,
            "neutral_zone_league_avg": self.neutral_zone_league_avg,
            "defensive_zone_pctg": self.defensive_zone_pctg,
            "defensive_zone_league_avg": self.defensive_zone_league_avg,
        }


@dataclass(slots=True, frozen=True)
class ZoneStarts:
    """Zone start percentages (where faceoffs begin relative to total zone starts)."""
    offensive_zone_starts: float | None
    neutral_zone_starts: float | None
    defensive_zone_starts: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneStarts:
        return cls(
            offensive_zone_starts = data.get("offensiveZoneStarts"),
            neutral_zone_starts = data.get("neutralZoneStarts"),
            defensive_zone_starts = data.get("defensiveZoneStarts"),
        )

    def to_dict(self) -> dict:
        return {
            "offensive_zone_starts": self.offensive_zone_starts,
            "neutral_zone_starts": self.neutral_zone_starts,
            "defensive_zone_starts": self.defensive_zone_starts,
        }


@dataclass(slots=True, frozen=True)
class SkaterComparison:
    """
    NHL Edge drill-down comparison data for a skater.

    Provides shot speed and skating speed breakdowns, last 10 games of
    skating distance, season distance details, shot location data,
    and zone time/starts.

    Instances of this class are accessed via `Stats.edge.skater.comparison()`.
    """
    seasons_with_edge: list
    shot_speed: ShotSpeedDetails
    skating_speed: SkatingSpeedDetails
    skating_distance_last_10: list
    skating_distance: SkatingDistanceDetails
    shot_location_details: list
    shot_location_totals: list
    zone_time: ZoneTimeComparison
    zone_starts: ZoneStarts

    @classmethod
    def from_dict(cls, data: dict) -> SkaterComparison:
        return cls(
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            shot_speed = ShotSpeedDetails.from_dict(data.get("shotSpeedDetails") or {}),
            skating_speed = SkatingSpeedDetails.from_dict(data.get("skatingSpeedDetails") or {}),
            skating_distance_last_10 = [DistanceGame.from_dict(g) for g in data.get("skatingDistanceLast10") or []],
            skating_distance = SkatingDistanceDetails.from_dict(data.get("skatingDistanceDetails") or {}),
            shot_location_details = [ShotLocationDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
            shot_location_totals = [ShotLocationTotal.from_dict(t) for t in data.get("shotLocationTotals") or []],
            zone_time = ZoneTimeComparison.from_dict(data.get("zoneTimeDetails") or {}),
            zone_starts = ZoneStarts.from_dict(data.get("zoneStarts") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "shot_speed": self.shot_speed.to_dict(),
            "skating_speed": self.skating_speed.to_dict(),
            "skating_distance_last_10": [g.to_dict() for g in self.skating_distance_last_10],
            "skating_distance": self.skating_distance.to_dict(),
            "shot_location_details": [d.to_dict() for d in self.shot_location_details],
            "shot_location_totals": [t.to_dict() for t in self.shot_location_totals],
            "zone_time": self.zone_time.to_dict(),
            "zone_starts": self.zone_starts.to_dict(),
        }
