"""
SKATER SHOT SPEED MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..edge_types import EdgeValue, EdgeMeasurement, EdgeCount, OverlayPeriodDescriptor


@dataclass(slots=True, frozen=True)
class ShotSpeedGame:
    """A single hardest-shot instance for the player, with game and period context."""
    game_center_link: str | None
    game_date: str | None
    game_type: int | None
    player_on_home_team: bool | None
    shot_speed: EdgeValue
    time_in_period: str | None
    period_descriptor: OverlayPeriodDescriptor
    home_team: dict | None
    away_team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> ShotSpeedGame:
        return cls(
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            game_type = data.get("gameType"),
            player_on_home_team = data.get("playerOnHomeTeam"),
            shot_speed = EdgeValue.from_dict(data.get("shotSpeed") or {}),
            time_in_period = data.get("timeInPeriod"),
            period_descriptor = OverlayPeriodDescriptor.from_dict(data.get("periodDescriptor") or {}),
            home_team = data.get("homeTeam"),
            away_team = data.get("awayTeam"),
        )

    def to_dict(self) -> dict:
        return {
            "game_center_link": self.game_center_link,
            "game_date": self.game_date,
            "game_type": self.game_type,
            "player_on_home_team": self.player_on_home_team,
            "shot_speed": self.shot_speed.to_dict(),
            "time_in_period": self.time_in_period,
            "period_descriptor": self.period_descriptor.to_dict(),
            "home_team": self.home_team,
            "away_team": self.away_team,
        }


@dataclass(slots=True, frozen=True)
class ShotSpeedSummary:
    """Season shot speed summary with rankings and league averages."""
    top_shot_speed: EdgeMeasurement
    avg_shot_speed: EdgeMeasurement
    shot_attempts_over_100: EdgeCount
    shot_attempts_90_100: EdgeCount
    shot_attempts_80_90: EdgeCount
    shot_attempts_70_80: EdgeCount

    @classmethod
    def from_dict(cls, data: dict) -> ShotSpeedSummary:
        return cls(
            top_shot_speed = EdgeMeasurement.from_dict(data.get("topShotSpeed") or {}),
            avg_shot_speed = EdgeMeasurement.from_dict(data.get("avgShotSpeed") or {}),
            shot_attempts_over_100 = EdgeCount.from_dict(data.get("shotAttemptsOver100") or {}),
            shot_attempts_90_100 = EdgeCount.from_dict(data.get("shotAttempts90To100") or {}),
            shot_attempts_80_90 = EdgeCount.from_dict(data.get("shotAttempts80To90") or {}),
            shot_attempts_70_80 = EdgeCount.from_dict(data.get("shotAttempts70To80") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "top_shot_speed": self.top_shot_speed.to_dict(),
            "avg_shot_speed": self.avg_shot_speed.to_dict(),
            "shot_attempts_over_100": self.shot_attempts_over_100.to_dict(),
            "shot_attempts_90_100": self.shot_attempts_90_100.to_dict(),
            "shot_attempts_80_90": self.shot_attempts_80_90.to_dict(),
            "shot_attempts_70_80": self.shot_attempts_70_80.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class ShotSpeed:
    """
    Per-player shot speed detail.

    Provides the player's hardest shot instances across the season,
    plus a season summary including top/average speed rankings and shot attempt bucket counts.

    Instances of this class are accessed via `Stats.edge.skater.shot_speed()`.
    """
    hardest_shots: list
    speed_summary: ShotSpeedSummary

    @classmethod
    def from_dict(cls, data: dict) -> ShotSpeed:
        return cls(
            hardest_shots = [ShotSpeedGame.from_dict(g) for g in data.get("hardestShots") or []],
            speed_summary = ShotSpeedSummary.from_dict(data.get("shotSpeedDetails") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "hardest_shots": [g.to_dict() for g in self.hardest_shots],
            "speed_summary": self.speed_summary.to_dict(),
        }
