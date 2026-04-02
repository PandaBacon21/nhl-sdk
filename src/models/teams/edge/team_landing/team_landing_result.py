"""
TEAM EDGE LANDING RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString
from ....players.player.player_stats.edge.player_edge_types import EdgeSeason, EdgeValue


@dataclass(slots=True, frozen=True)
class TeamEdgeLeaderTeam:
    """Lite team reference included in each Edge leader entry."""
    id: int | None
    common_name: LocalizedString
    place_name_with_preposition: LocalizedString
    abbrev: str | None
    logo_light: str | None
    logo_dark: str | None
    slug: str | None
    wins: int | None
    losses: int | None
    ot_losses: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgeLeaderTeam:
        logo = data.get("teamLogo") or {}
        return cls(
            id = data.get("id"),
            common_name = LocalizedString(data.get("commonName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            abbrev = data.get("abbrev"),
            logo_light = logo.get("light"),
            logo_dark = logo.get("dark"),
            slug = data.get("slug"),
            wins = data.get("wins"),
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "common_name": self.common_name.default,
            "place_name_with_preposition": self.place_name_with_preposition.default,
            "abbrev": self.abbrev,
            "logo_light": self.logo_light,
            "logo_dark": self.logo_dark,
            "slug": self.slug,
            "wins": self.wins,
            "losses": self.losses,
            "ot_losses": self.ot_losses,
        }


@dataclass(slots=True, frozen=True)
class LandingSogAreaDetail:
    """Shot on goal count and rank for one rink area."""
    area: str | None
    sog: int | None
    rank: int | None

    @classmethod
    def from_dict(cls, data: dict) -> LandingSogAreaDetail:
        return cls(
            area = data.get("area"),
            sog = data.get("sog"),
            rank = data.get("rank"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "sog": self.sog,
            "rank": self.rank,
        }


@dataclass(slots=True, frozen=True)
class TeamShotAttemptLeader:
    """Leader entry for shot attempts over a speed threshold (e.g. over 90 mph)."""
    team: TeamEdgeLeaderTeam
    attempts: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotAttemptLeader:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            attempts = data.get("attempts"),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "attempts": self.attempts,
        }


@dataclass(slots=True, frozen=True)
class TeamBurstsLeader:
    """Leader entry for skating speed bursts over 22 mph."""
    team: TeamEdgeLeaderTeam
    bursts: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamBurstsLeader:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            bursts = data.get("bursts"),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "bursts": self.bursts,
        }


@dataclass(slots=True, frozen=True)
class TeamDistanceLeader:
    """Leader entry for skating distance per 60 minutes."""
    team: TeamEdgeLeaderTeam
    distance_skated: EdgeValue

    @classmethod
    def from_dict(cls, data: dict) -> TeamDistanceLeader:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            distance_skated = EdgeValue.from_dict(data.get("distanceSkated") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "distance_skated": self.distance_skated.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamHighDangerSOGLeader:
    """Leader entry for high danger shots on goal with per-area breakdown."""
    team: TeamEdgeLeaderTeam
    sog: int | None
    shot_location_details: list[LandingSogAreaDetail]

    @classmethod
    def from_dict(cls, data: dict) -> TeamHighDangerSOGLeader:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            sog = data.get("sog"),
            shot_location_details = [LandingSogAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "sog": self.sog,
            "shot_location_details": [d.to_dict() for d in self.shot_location_details],
        }


@dataclass(slots=True, frozen=True)
class TeamZoneTimeLeader:
    """Leader entry for offensive, neutral, or defensive zone time percentage."""
    team: TeamEdgeLeaderTeam
    zone_time: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamZoneTimeLeader:
        return cls(
            team = TeamEdgeLeaderTeam.from_dict(data.get("team") or {}),
            zone_time = data.get("zoneTime"),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "zone_time": self.zone_time,
        }


@dataclass(slots=True, frozen=True)
class TeamEdgeLandingLeaders:
    """All leader categories from the team Edge landing page."""
    shot_attempts_over_90: TeamShotAttemptLeader
    bursts_over_22: TeamBurstsLeader
    distance_per_60: TeamDistanceLeader
    high_danger_sog: TeamHighDangerSOGLeader
    offensive_zone_time: TeamZoneTimeLeader
    neutral_zone_time: TeamZoneTimeLeader
    defensive_zone_time: TeamZoneTimeLeader

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgeLandingLeaders:
        return cls(
            shot_attempts_over_90 = TeamShotAttemptLeader.from_dict(data.get("shotAttemptsOver90") or {}),
            bursts_over_22 = TeamBurstsLeader.from_dict(data.get("burstsOver22") or {}),
            distance_per_60 = TeamDistanceLeader.from_dict(data.get("distancePer60") or {}),
            high_danger_sog = TeamHighDangerSOGLeader.from_dict(data.get("highDangerSOG") or {}),
            offensive_zone_time = TeamZoneTimeLeader.from_dict(data.get("offensiveZoneTime") or {}),
            neutral_zone_time = TeamZoneTimeLeader.from_dict(data.get("neutralZoneTime") or {}),
            defensive_zone_time = TeamZoneTimeLeader.from_dict(data.get("defensiveZoneTime") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "shot_attempts_over_90": self.shot_attempts_over_90.to_dict(),
            "bursts_over_22": self.bursts_over_22.to_dict(),
            "distance_per_60": self.distance_per_60.to_dict(),
            "high_danger_sog": self.high_danger_sog.to_dict(),
            "offensive_zone_time": self.offensive_zone_time.to_dict(),
            "neutral_zone_time": self.neutral_zone_time.to_dict(),
            "defensive_zone_time": self.defensive_zone_time.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamEdgeLandingResult:
    """Top-level model for the team Edge landing page response."""
    seasons_with_edge: list[EdgeSeason]
    leaders: TeamEdgeLandingLeaders

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgeLandingResult:
        return cls(
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            leaders = TeamEdgeLandingLeaders.from_dict(data.get("leaders") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "leaders": self.leaders.to_dict(),
        }
