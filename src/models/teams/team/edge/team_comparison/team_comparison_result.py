"""
TEAM COMPARISON RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ......core.utilities import LocalizedString
from ......models.players.player.player_stats.edge.player_edge_types import (
    EdgeSeason, EdgeValue, EdgePeak,
)
from ..team_edge_types import TeamEdgeLogo, TeamDetailTeam


@dataclass(slots=True, frozen=True)
class TeamCompShotSpeed:
    """Team shot speed breakdown: top/avg speed and attempt counts by speed bucket."""
    top_shot_speed: EdgePeak
    avg_shot_speed: EdgeValue
    shot_attempts_over_100: int | None
    shot_attempts_90_100: int | None
    shot_attempts_80_90: int | None
    shot_attempts_70_80: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompShotSpeed:
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
class TeamCompSkatingSpeed:
    """Team skating speed breakdown: max speed and burst counts by speed range."""
    max_skating_speed: EdgePeak
    bursts_over_22: int | None
    bursts_20_22: int | None
    bursts_18_20: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompSkatingSpeed:
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
class TeamCompTeamRef:
    """Compact team reference used in skating distance game entries."""
    common_name: LocalizedString
    place_name_with_preposition: LocalizedString
    abbrev: str | None
    team_logo: TeamEdgeLogo
    slug: str | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompTeamRef:
        return cls(
            common_name = LocalizedString(data.get("commonName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            abbrev = data.get("abbrev"),
            team_logo = TeamEdgeLogo.from_dict(data.get("teamLogo") or {}),
            slug = data.get("slug"),
        )

    def to_dict(self) -> dict:
        return {
            "common_name": self.common_name.default,
            "place_name_with_preposition": self.place_name_with_preposition.default,
            "abbrev": self.abbrev,
            "team_logo": self.team_logo.to_dict(),
            "slug": self.slug,
        }


@dataclass(slots=True, frozen=True)
class TeamCompDistanceGame:
    """Skating distance and game context for a single game (last-10 entries)."""
    game_center_link: str | None
    game_date: str | None
    is_home_team: bool | None
    distance_skated: EdgeValue
    home_team: TeamCompTeamRef
    away_team: TeamCompTeamRef

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompDistanceGame:
        return cls(
            game_center_link = data.get("gameCenterLink"),
            game_date = data.get("gameDate"),
            is_home_team = data.get("isHomeTeam"),
            distance_skated = EdgeValue.from_dict(data.get("distanceSkated") or {}),
            home_team = TeamCompTeamRef.from_dict(data.get("homeTeam") or {}),
            away_team = TeamCompTeamRef.from_dict(data.get("awayTeam") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "game_center_link": self.game_center_link,
            "game_date": self.game_date,
            "is_home_team": self.is_home_team,
            "distance_skated": self.distance_skated.to_dict(),
            "home_team": self.home_team.to_dict(),
            "away_team": self.away_team.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamCompDistance:
    """Season skating distance totals and peak game/period performances."""
    distance_total: EdgeValue
    distance_per_60: EdgeValue
    distance_max_game: EdgePeak
    distance_max_period: EdgePeak

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompDistance:
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
class TeamCompShotLocationDetail:
    """Shot location data for a specific rink area."""
    area: str | None
    sog: int | None
    goals: int | None
    shooting_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompShotLocationDetail:
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
class TeamCompShotLocationTotal:
    """Shot location totals rolled up by zone (all/high/long/mid)."""
    location_code: str | None
    sog: int | None
    goals: int | None
    shooting_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompShotLocationTotal:
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
class TeamCompZoneTime:
    """Zone time comparison with league averages (no ranks, no EV split)."""
    offensive_zone_pctg: float | None
    offensive_zone_league_avg: float | None
    neutral_zone_pctg: float | None
    neutral_zone_league_avg: float | None
    defensive_zone_pctg: float | None
    defensive_zone_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamCompZoneTime:
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
class TeamShotDifferential:
    """Team shot differential metrics (shot attempts and shots on goal)."""
    shot_attempt_differential: float | None
    sog_differential: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotDifferential:
        return cls(
            shot_attempt_differential = data.get("shotAttemptDifferential"),
            sog_differential = data.get("sogDifferential"),
        )

    def to_dict(self) -> dict:
        return {
            "shot_attempt_differential": self.shot_attempt_differential,
            "sog_differential": self.sog_differential,
        }


@dataclass(slots=True, frozen=True)
class TeamComparisonResult:
    """
    NHL Edge comparison data for a team.

    Provides shot speed and skating speed breakdowns, last 10 games of
    skating distance, season distance details, shot location data by
    rink area and zone, zone time comparisons, and shot differentials.

    Instances of this class are accessed via `client.teams.stats.edge.comparison`.
    """
    team: TeamDetailTeam
    seasons_with_edge: list[EdgeSeason]
    shot_speed: TeamCompShotSpeed
    skating_speed: TeamCompSkatingSpeed
    skating_distance_last_10: list[TeamCompDistanceGame]
    distance: TeamCompDistance
    shot_location_details: list[TeamCompShotLocationDetail]
    shot_location_totals: list[TeamCompShotLocationTotal]
    zone_time: TeamCompZoneTime
    shot_differential: TeamShotDifferential

    @classmethod
    def from_dict(cls, data: dict) -> TeamComparisonResult:
        return cls(
            team = TeamDetailTeam.from_dict(data.get("team") or {}),
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            shot_speed = TeamCompShotSpeed.from_dict(data.get("shotSpeedDetails") or {}),
            skating_speed = TeamCompSkatingSpeed.from_dict(data.get("skatingSpeedDetails") or {}),
            skating_distance_last_10 = [TeamCompDistanceGame.from_dict(g) for g in data.get("skatingDistanceLast10") or []],
            distance = TeamCompDistance.from_dict(data.get("skatingDistanceDetails") or {}),
            shot_location_details = [TeamCompShotLocationDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
            shot_location_totals = [TeamCompShotLocationTotal.from_dict(t) for t in data.get("shotLocationTotals") or []],
            zone_time = TeamCompZoneTime.from_dict(data.get("zoneTimeDetails") or {}),
            shot_differential = TeamShotDifferential.from_dict(data.get("shotDifferential") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "shot_speed": self.shot_speed.to_dict(),
            "skating_speed": self.skating_speed.to_dict(),
            "skating_distance_last_10": [g.to_dict() for g in self.skating_distance_last_10],
            "distance": self.distance.to_dict(),
            "shot_location_details": [d.to_dict() for d in self.shot_location_details],
            "shot_location_totals": [t.to_dict() for t in self.shot_location_totals],
            "zone_time": self.zone_time.to_dict(),
            "shot_differential": self.shot_differential.to_dict(),
        }
