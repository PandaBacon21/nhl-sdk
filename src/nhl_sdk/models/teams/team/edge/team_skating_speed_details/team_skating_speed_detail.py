"""
TEAM SKATING SPEED DETAIL RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ......core.utilities import LocalizedString
from ......models.players.player.player_stats.edge.player_edge_types import (
    EdgeValue, OverlayPeriodDescriptor,
)
from ..team_edge_types import TeamEdgeMeasurement, TeamEdgeCount
from ..team_skating_distance_details.team_skating_distance_detail import TeamDistanceTeamRef


@dataclass(slots=True, frozen=True)
class TopSpeedPlayer:
    """Player reference in a top skating speed entry."""
    id: int | None
    first_name: LocalizedString
    last_name: LocalizedString
    slug: str | None

    @classmethod
    def from_dict(cls, data: dict) -> TopSpeedPlayer:
        return cls(
            id = data.get("id"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            slug = data.get("slug"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name.default,
            "last_name": self.last_name.default,
            "slug": self.slug,
        }


@dataclass(slots=True, frozen=True)
class TeamTopSpeedEntry:
    """A single top skating speed instance (player, game context, speed, period info, teams)."""
    player: TopSpeedPlayer
    game_center_link: str | None
    game_date: str | None
    game_type: int | None
    is_home_team: bool | None
    skating_speed: EdgeValue
    time_in_period: str | None
    period_descriptor: OverlayPeriodDescriptor
    home_team: TeamDistanceTeamRef
    away_team: TeamDistanceTeamRef

    @classmethod
    def from_dict(cls, data: dict) -> TeamTopSpeedEntry:
        return cls(
            player = TopSpeedPlayer.from_dict(data.get("player") or {}),
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            game_type = data.get("gameType"),
            is_home_team = data.get("isHomeTeam"),
            skating_speed = EdgeValue.from_dict(data.get("skatingSpeed") or {}),
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
            "skating_speed": self.skating_speed.to_dict(),
            "time_in_period": self.time_in_period,
            "period_descriptor": self.period_descriptor.to_dict(),
            "home_team": self.home_team.to_dict(),
            "away_team": self.away_team.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamSpeedDetail:
    """Skating speed stats for one position group (all/F/D) with rank and league averages."""
    position_code: str | None
    max_skating_speed: TeamEdgeMeasurement
    bursts_over_22: TeamEdgeCount
    bursts_20_to_22: TeamEdgeCount
    bursts_18_to_20: TeamEdgeCount

    @classmethod
    def from_dict(cls, data: dict) -> TeamSpeedDetail:
        return cls(
            position_code = data.get("positionCode"),
            max_skating_speed = TeamEdgeMeasurement.from_dict(data.get("maxSkatingSpeed") or {}),
            bursts_over_22 = TeamEdgeCount.from_dict(data.get("burstsOver22") or {}),
            bursts_20_to_22 = TeamEdgeCount.from_dict(data.get("bursts20To22") or {}),
            bursts_18_to_20 = TeamEdgeCount.from_dict(data.get("bursts18To20") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "position_code": self.position_code,
            "max_skating_speed": self.max_skating_speed.to_dict(),
            "bursts_over_22": self.bursts_over_22.to_dict(),
            "bursts_20_to_22": self.bursts_20_to_22.to_dict(),
            "bursts_18_to_20": self.bursts_18_to_20.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamSkatingSpeedResult:
    """
    Team skating speed detail stats.

    Contains the top speed instances for the season and per-position breakdowns
    with burst counts and league ranks.

    Accessed via ``team.stats.edge.skating_speed`` on a ``Team`` object.
    """
    top_skating_speeds: list[TeamTopSpeedEntry]
    skating_speed_details: list[TeamSpeedDetail]

    @classmethod
    def from_dict(cls, data: dict) -> TeamSkatingSpeedResult:
        return cls(
            top_skating_speeds = [TeamTopSpeedEntry.from_dict(e) for e in data.get("topSkatingSpeeds") or []],
            skating_speed_details = [TeamSpeedDetail.from_dict(e) for e in data.get("skatingSpeedDetails") or []],
        )

    def to_dict(self) -> dict:
        return {
            "top_skating_speeds": [e.to_dict() for e in self.top_skating_speeds],
            "skating_speed_details": [e.to_dict() for e in self.skating_speed_details],
        }
