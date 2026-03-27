"""
SKATER SKATING SPEED MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import EdgeValue, EdgeMeasurement, EdgeCount, OverlayPeriodDescriptor


@dataclass(slots=True, frozen=True)
class SkatingSpeedGame:
    """A single top-speed instance for the player, with game and period context."""
    game_center_link: str | None
    game_date: str | None
    game_type: int | None
    player_on_home_team: bool | None
    skating_speed: EdgeValue
    time_in_period: str | None
    period_descriptor: OverlayPeriodDescriptor
    home_team: dict | None
    away_team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> SkatingSpeedGame:
        return cls(
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            game_type = data.get("gameType"),
            player_on_home_team = data.get("playerOnHomeTeam"),
            skating_speed = EdgeValue.from_dict(data.get("skatingSpeed") or {}),
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
            "skating_speed": self.skating_speed.to_dict(),
            "time_in_period": self.time_in_period,
            "period_descriptor": self.period_descriptor.to_dict(),
            "home_team": self.home_team,
            "away_team": self.away_team,
        }


@dataclass(slots=True, frozen=True)
class SkatingSpeedSummary:
    """Season skating speed summary with rankings and league averages."""
    max_skating_speed: EdgeMeasurement
    bursts_over_22: EdgeCount
    bursts_20_22: EdgeCount
    bursts_18_20: EdgeCount

    @classmethod
    def from_dict(cls, data: dict) -> SkatingSpeedSummary:
        return cls(
            max_skating_speed = EdgeMeasurement.from_dict(data.get("maxSkatingSpeed") or {}),
            bursts_over_22 = EdgeCount.from_dict(data.get("burstsOver22") or {}),
            bursts_20_22 = EdgeCount.from_dict(data.get("bursts20To22") or {}),
            bursts_18_20 = EdgeCount.from_dict(data.get("bursts18To20") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "max_skating_speed": self.max_skating_speed.to_dict(),
            "bursts_over_22": self.bursts_over_22.to_dict(),
            "bursts_20_22": self.bursts_20_22.to_dict(),
            "bursts_18_20": self.bursts_18_20.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class SkatingSpeed:
    """
    Per-player skating speed detail.

    Provides the player's top speed instances across the season,
    plus a season summary including max speed ranking and burst counts.

    Instances of this class are accessed via `Stats.edge().skating_speed()`.
    """
    top_speeds: list
    speed_summary: SkatingSpeedSummary

    @classmethod
    def from_dict(cls, data: dict) -> SkatingSpeed:
        return cls(
            top_speeds = [SkatingSpeedGame.from_dict(g) for g in data.get("topSkatingSpeeds") or []],
            speed_summary = SkatingSpeedSummary.from_dict(data.get("skatingSpeedDetails") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "top_speeds": [g.to_dict() for g in self.top_speeds],
            "speed_summary": self.speed_summary.to_dict(),
        }
