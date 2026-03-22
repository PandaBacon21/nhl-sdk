"""
SKATER SKATING DISTANCE MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..edge_types import EdgeValue, EdgeMeasurement


@dataclass(slots=True, frozen=True)
class SkatingDistanceGame:
    """Per-game skating distance breakdown by strength (all/even/power play/penalty kill)."""
    game_center_link: str | None
    game_date: str | None
    player_on_home_team: bool | None
    distance_skated_all: EdgeValue
    toi_all: int | None
    distance_skated_even: EdgeValue
    toi_even: int | None
    distance_skated_pp: EdgeValue
    toi_pp: int | None
    distance_skated_pk: EdgeValue
    toi_pk: int | None
    home_team: dict | None
    away_team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> SkatingDistanceGame:
        return cls(
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            player_on_home_team = data.get("playerOnHomeTeam"),
            distance_skated_all = EdgeValue.from_dict(data.get("distanceSkatedAll") or {}),
            toi_all = data.get("toiAll"),
            distance_skated_even = EdgeValue.from_dict(data.get("distanceSkatedEven") or {}),
            toi_even = data.get("toiEven"),
            distance_skated_pp = EdgeValue.from_dict(data.get("distanceSkatedPP") or {}),
            toi_pp = data.get("toiPP"),
            distance_skated_pk = EdgeValue.from_dict(data.get("distanceSkatedPK") or {}),
            toi_pk = data.get("toiPK"),
            home_team = data.get("homeTeam"),
            away_team = data.get("awayTeam"),
        )

    def to_dict(self) -> dict:
        return {
            "game_center_link": self.game_center_link,
            "game_date": self.game_date,
            "player_on_home_team": self.player_on_home_team,
            "distance_skated_all": self.distance_skated_all.to_dict(),
            "toi_all": self.toi_all,
            "distance_skated_even": self.distance_skated_even.to_dict(),
            "toi_even": self.toi_even,
            "distance_skated_pp": self.distance_skated_pp.to_dict(),
            "toi_pp": self.toi_pp,
            "distance_skated_pk": self.distance_skated_pk.to_dict(),
            "toi_pk": self.toi_pk,
            "home_team": self.home_team,
            "away_team": self.away_team,
        }


@dataclass(slots=True, frozen=True)
class SkatingDistanceStrength:
    """Season skating distance totals and peaks for a specific strength situation."""
    strength_code: str | None
    distance_total: EdgeMeasurement
    distance_per_60: EdgeMeasurement
    distance_max_game: EdgeMeasurement
    distance_max_period: EdgeMeasurement

    @classmethod
    def from_dict(cls, data: dict) -> SkatingDistanceStrength:
        return cls(
            strength_code = data.get("strengthCode"),
            distance_total = EdgeMeasurement.from_dict(data.get("distanceTotal") or {}),
            distance_per_60 = EdgeMeasurement.from_dict(data.get("distancePer60") or {}),
            distance_max_game = EdgeMeasurement.from_dict(data.get("distanceMaxGame") or {}),
            distance_max_period = EdgeMeasurement.from_dict(data.get("distanceMaxPeriod") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "strength_code": self.strength_code,
            "distance_total": self.distance_total.to_dict(),
            "distance_per_60": self.distance_per_60.to_dict(),
            "distance_max_game": self.distance_max_game.to_dict(),
            "distance_max_period": self.distance_max_period.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class SkatingDistance:
    """
    Per-player skating distance detail.

    Provides last 10 games of skating distance broken down by strength situation,
    plus season totals and peaks for all/even/power-play/penalty-kill situations.

    Instances of this class are accessed via `Stats.edge.skater.skating_distance()`.
    """
    last_10_games: list
    distance_by_strength: list

    @classmethod
    def from_dict(cls, data: dict) -> SkatingDistance:
        return cls(
            last_10_games = [SkatingDistanceGame.from_dict(g) for g in data.get("skatingDistanceLast10") or []],
            distance_by_strength = [SkatingDistanceStrength.from_dict(d) for d in data.get("skatingDistanceDetails") or []],
        )

    def to_dict(self) -> dict:
        return {
            "last_10_games": [g.to_dict() for g in self.last_10_games],
            "distance_by_strength": [d.to_dict() for d in self.distance_by_strength],
        }
