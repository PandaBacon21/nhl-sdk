"""
CAT SKATER DETAILS MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from .......core.utilities import LocalizedString
from ..player_edge_types import EdgeMeasurement, EdgeSeason
from .skater_details import SkatingSpeed, SogSummary, SogDetail, ZoneTimeDetails


@dataclass(slots=True, frozen=True)
class CatPlayerSummary:
    """Player summary included at the top level of the CAT skater details response."""
    id: int | None
    first_name: LocalizedString
    last_name: LocalizedString
    birth_date: str | None
    shoots_catches: str | None
    sweater_number: int | None
    position: str | None
    slug: str | None
    headshot: str | None
    goals: int | None
    assists: int | None
    points: int | None
    games_played: int | None
    team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> CatPlayerSummary:
        return cls(
            id = data.get("id"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            birth_date = data.get("birthDate"),
            shoots_catches = data.get("shootsCatches"),
            sweater_number = data.get("sweaterNumber"),
            position = data.get("position"),
            slug = data.get("slug"),
            headshot = data.get("headshot"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
            games_played = data.get("gamesPlayed"),
            team = data.get("team"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name.default,
            "last_name": self.last_name.default,
            "birth_date": self.birth_date,
            "shoots_catches": self.shoots_catches,
            "sweater_number": self.sweater_number,
            "position": self.position,
            "slug": self.slug,
            "headshot": self.headshot,
            "goals": self.goals,
            "assists": self.assists,
            "points": self.points,
            "games_played": self.games_played,
            "team": self.team,
        }


@dataclass(slots=True, frozen=True)
class CatSkaterDetails:
    """
    CAT endpoint NHL Edge rankings and stat summaries for a skater.

    Includes a player summary with current season stats, seasons with edge data,
    top shot speed, skating speed, total distance skated, shot on goal
    details, and zone time percentages.

    Instances of this class are accessed via `Stats.edge().cat_details()`.
    """
    player: CatPlayerSummary
    seasons_with_edge: list
    top_shot_speed: EdgeMeasurement
    skating_speed: SkatingSpeed
    total_distance_skated: EdgeMeasurement
    sog_summary: list
    sog_details: list
    zone_time: ZoneTimeDetails

    @classmethod
    def from_dict(cls, data: dict) -> CatSkaterDetails:
        return cls(
            player = CatPlayerSummary.from_dict(data.get("player") or {}),
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            top_shot_speed = EdgeMeasurement.from_dict(data.get("topShotSpeed") or {}),
            skating_speed = SkatingSpeed.from_dict(data.get("skatingSpeed") or {}),
            total_distance_skated = EdgeMeasurement.from_dict(data.get("totalDistanceSkated") or {}),
            sog_summary = [SogSummary.from_dict(s) for s in data.get("sogSummary") or []],
            sog_details = [SogDetail.from_dict(d) for d in data.get("sogDetails") or []],
            zone_time = ZoneTimeDetails.from_dict(data.get("zoneTimeDetails") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "top_shot_speed": self.top_shot_speed.to_dict(),
            "skating_speed": self.skating_speed.to_dict(),
            "total_distance_skated": self.total_distance_skated.to_dict(),
            "sog_summary": [s.to_dict() for s in self.sog_summary],
            "sog_details": [d.to_dict() for d in self.sog_details],
            "zone_time": self.zone_time.to_dict(),
        }
