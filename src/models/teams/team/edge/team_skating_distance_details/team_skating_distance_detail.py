"""
TEAM SKATING DISTANCE DETAIL RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ......core.utilities import LocalizedString
from ......models.players.player.player_stats.edge.player_edge_types import EdgeValue
from ..team_edge_types import TeamEdgeLogo, TeamEdgeMeasurement


@dataclass(slots=True, frozen=True)
class TeamDistanceTeamRef:
    """Compact team reference used in skating distance last-10 game entries."""
    common_name: LocalizedString
    place_name_with_preposition: LocalizedString
    team_logo: TeamEdgeLogo

    @classmethod
    def from_dict(cls, data: dict) -> TeamDistanceTeamRef:
        return cls(
            common_name = LocalizedString(data.get("commonName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            team_logo = TeamEdgeLogo.from_dict(data.get("teamLogo") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "common_name": self.common_name.default,
            "place_name_with_preposition": self.place_name_with_preposition.default,
            "team_logo": self.team_logo.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamDistanceLast10Game:
    """Per-game skating distance by situation (all/even/PP/PK) for last-10 entries."""
    game_center_link: str | None
    game_date: str | None
    is_home_team: bool | None
    toi_all: int | None
    distance_skated_all: EdgeValue
    toi_even: int | None
    distance_skated_even: EdgeValue
    toi_pp: int | None
    distance_skated_pp: EdgeValue
    toi_pk: int | None
    distance_skated_pk: EdgeValue
    home_team: TeamDistanceTeamRef
    away_team: TeamDistanceTeamRef

    @classmethod
    def from_dict(cls, data: dict) -> TeamDistanceLast10Game:
        return cls(
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            is_home_team = data.get("isHomeTeam"),
            toi_all = data.get("toiAll"),
            distance_skated_all = EdgeValue.from_dict(data.get("distanceSkatedAll") or {}),
            toi_even = data.get("toiEven"),
            distance_skated_even = EdgeValue.from_dict(data.get("distanceSkatedEven") or {}),
            toi_pp = data.get("toiPP"),
            distance_skated_pp = EdgeValue.from_dict(data.get("distanceSkatedPP") or {}),
            toi_pk = data.get("toiPK"),
            distance_skated_pk = EdgeValue.from_dict(data.get("distanceSkatedPK") or {}),
            home_team = TeamDistanceTeamRef.from_dict(data.get("homeTeam") or {}),
            away_team = TeamDistanceTeamRef.from_dict(data.get("awayTeam") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "game_center_link": self.game_center_link,
            "game_date": self.game_date,
            "is_home_team": self.is_home_team,
            "toi_all": self.toi_all,
            "distance_skated_all": self.distance_skated_all.to_dict(),
            "toi_even": self.toi_even,
            "distance_skated_even": self.distance_skated_even.to_dict(),
            "toi_pp": self.toi_pp,
            "distance_skated_pp": self.distance_skated_pp.to_dict(),
            "toi_pk": self.toi_pk,
            "distance_skated_pk": self.distance_skated_pk.to_dict(),
            "home_team": self.home_team.to_dict(),
            "away_team": self.away_team.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamDistanceEntry:
    """Skating distance stats for one strength/position combination (with ranks and league averages)."""
    strength_code: str | None
    position_code: str | None
    distance_total: TeamEdgeMeasurement
    distance_per_60: TeamEdgeMeasurement
    distance_max_game: TeamEdgeMeasurement
    distance_max_period: TeamEdgeMeasurement

    @classmethod
    def from_dict(cls, data: dict) -> TeamDistanceEntry:
        return cls(
            strength_code = data.get("strengthCode"),
            position_code = data.get("positionCode"),
            distance_total = TeamEdgeMeasurement.from_dict(data.get("distanceTotal") or {}),
            distance_per_60 = TeamEdgeMeasurement.from_dict(data.get("distancePer60") or {}),
            distance_max_game = TeamEdgeMeasurement.from_dict(data.get("distanceMaxGame") or {}),
            distance_max_period = TeamEdgeMeasurement.from_dict(data.get("distanceMaxPeriod") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "strength_code": self.strength_code,
            "position_code": self.position_code,
            "distance_total": self.distance_total.to_dict(),
            "distance_per_60": self.distance_per_60.to_dict(),
            "distance_max_game": self.distance_max_game.to_dict(),
            "distance_max_period": self.distance_max_period.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamSkatingDistanceResult:
    """
    Team skating distance detail stats by strength and position.

    Provides last-10-game per-situation breakdowns (all/even/PP/PK) and
    season summaries across strength codes (all/pp/pk/es) x position codes
    (all/F/D), each with ranks and league averages.

    Instances of this class are accessed via `client.teams.stats.edge.skating_distance`.
    """
    skating_distance_last_10: list[TeamDistanceLast10Game]
    skating_distance_details: list[TeamDistanceEntry]

    @classmethod
    def from_dict(cls, data: dict) -> TeamSkatingDistanceResult:
        return cls(
            skating_distance_last_10 = [TeamDistanceLast10Game.from_dict(g) for g in data.get("skatingDistanceLast10") or []],
            skating_distance_details = [TeamDistanceEntry.from_dict(e) for e in data.get("skatingDistanceDetails") or []],
        )

    def to_dict(self) -> dict:
        return {
            "skating_distance_last_10": [g.to_dict() for g in self.skating_distance_last_10],
            "skating_distance_details": [e.to_dict() for e in self.skating_distance_details],
        }
