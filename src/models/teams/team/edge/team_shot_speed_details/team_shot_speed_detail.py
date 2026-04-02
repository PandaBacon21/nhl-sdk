"""
TEAM SHOT SPEED DETAIL RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ......models.players.player.player_stats.edge.player_edge_types import (
    EdgeValue, OverlayPeriodDescriptor,
)
from ..team_edge_types import TeamEdgeMeasurement, TeamEdgeCount
from ..team_skating_distance_details.team_skating_distance_detail import TeamDistanceTeamRef
from ..team_skating_speed_details.team_skating_speed_detail import TopSpeedPlayer


@dataclass(slots=True, frozen=True)
class TeamHardestShotEntry:
    """A single hardest shot instance (player, game context, shot speed, period info, teams)."""
    player: TopSpeedPlayer
    game_center_link: str | None
    game_date: str | None
    game_type: int | None
    is_home_team: bool | None
    shot_speed: EdgeValue
    time_in_period: str | None
    period_descriptor: OverlayPeriodDescriptor
    home_team: TeamDistanceTeamRef
    away_team: TeamDistanceTeamRef

    @classmethod
    def from_dict(cls, data: dict) -> TeamHardestShotEntry:
        return cls(
            player = TopSpeedPlayer.from_dict(data.get("player") or {}),
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            game_type = data.get("gameType"),
            is_home_team = data.get("isHomeTeam"),
            shot_speed = EdgeValue.from_dict(data.get("shotSpeed") or {}),
            time_in_period = data.get("timeInPeriod"),
            period_descriptor = OverlayPeriodDescriptor.from_dict(data.get("periodDescriptor") or {}),
            home_team = TeamDistanceTeamRef.from_dict(data.get("homeTeam") or {}),
            away_team = TeamDistanceTeamRef.from_dict(data.get("awayTeam") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "game_center_link": self.game_center_link,
            "game_date": self.game_date,
            "game_type": self.game_type,
            "is_home_team": self.is_home_team,
            "shot_speed": self.shot_speed.to_dict(),
            "time_in_period": self.time_in_period,
            "period_descriptor": self.period_descriptor.to_dict(),
            "home_team": self.home_team.to_dict(),
            "away_team": self.away_team.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamShotSpeedDetail:
    """Shot speed stats for one position group (all/D/F) with ranks and league averages."""
    position: str | None
    top_shot_speed: TeamEdgeMeasurement
    avg_shot_speed: TeamEdgeMeasurement
    shot_attempts_over_100: TeamEdgeCount
    shot_attempts_90_to_100: TeamEdgeCount
    shot_attempts_80_to_90: TeamEdgeCount
    shot_attempts_70_to_80: TeamEdgeCount

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotSpeedDetail:
        return cls(
            position = data.get("position"),
            top_shot_speed = TeamEdgeMeasurement.from_dict(data.get("topShotSpeed") or {}),
            avg_shot_speed = TeamEdgeMeasurement.from_dict(data.get("avgShotSpeed") or {}),
            shot_attempts_over_100 = TeamEdgeCount.from_dict(data.get("shotAttemptsOver100") or {}),
            shot_attempts_90_to_100 = TeamEdgeCount.from_dict(data.get("shotAttempts90To100") or {}),
            shot_attempts_80_to_90 = TeamEdgeCount.from_dict(data.get("shotAttempts80To90") or {}),
            shot_attempts_70_to_80 = TeamEdgeCount.from_dict(data.get("shotAttempts70To80") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "position": self.position,
            "top_shot_speed": self.top_shot_speed.to_dict(),
            "avg_shot_speed": self.avg_shot_speed.to_dict(),
            "shot_attempts_over_100": self.shot_attempts_over_100.to_dict(),
            "shot_attempts_90_to_100": self.shot_attempts_90_to_100.to_dict(),
            "shot_attempts_80_to_90": self.shot_attempts_80_to_90.to_dict(),
            "shot_attempts_70_to_80": self.shot_attempts_70_to_80.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamShotSpeedResult:
    """
    Team shot speed detail stats.

    Contains the hardest shot instances for the season and per-position
    breakdowns with shot speed ranks and attempt buckets.

    Instances of this class are accessed via `client.teams.stats.edge.shot_speed`.
    """
    hardest_shots: list[TeamHardestShotEntry]
    shot_speed_details: list[TeamShotSpeedDetail]

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotSpeedResult:
        return cls(
            hardest_shots = [TeamHardestShotEntry.from_dict(e) for e in data.get("hardestShots") or []],
            shot_speed_details = [TeamShotSpeedDetail.from_dict(e) for e in data.get("shotSpeedDetails") or []],
        )

    def to_dict(self) -> dict:
        return {
            "hardest_shots": [e.to_dict() for e in self.hardest_shots],
            "shot_speed_details": [e.to_dict() for e in self.shot_speed_details],
        }
