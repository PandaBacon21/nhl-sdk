"""
TEAM DETAIL RESULT
"""
from __future__ import annotations
from dataclasses import dataclass

from ......models.players.player.player_stats.edge.player_edge_types import EdgeSeason
from ..team_edge_types import TeamEdgeMeasurement, TeamEdgeCount, TeamEdgeLogo, TeamDetailTeam


@dataclass(slots=True, frozen=True)
class TeamShotSpeed:
    """Team shot speed stats: attempts over 90 mph and top shot speed."""
    shot_attempts_over_90: TeamEdgeCount
    top_shot_speed: TeamEdgeMeasurement

    @classmethod
    def from_dict(cls, data: dict) -> TeamShotSpeed:
        return cls(
            shot_attempts_over_90 = TeamEdgeCount.from_dict(data.get("shotAttemptsOver90") or {}),
            top_shot_speed = TeamEdgeMeasurement.from_dict(data.get("topShotSpeed") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "shot_attempts_over_90": self.shot_attempts_over_90.to_dict(),
            "top_shot_speed": self.top_shot_speed.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamSkatingSpeed:
    """Team skating speed stats: peak speed and bursts above 20 and 22 mph."""
    bursts_over_22: TeamEdgeCount
    bursts_over_20: TeamEdgeCount
    speed_max: TeamEdgeMeasurement

    @classmethod
    def from_dict(cls, data: dict) -> TeamSkatingSpeed:
        return cls(
            bursts_over_22 = TeamEdgeCount.from_dict(data.get("burstsOver22") or {}),
            bursts_over_20 = TeamEdgeCount.from_dict(data.get("burstsOver20") or {}),
            speed_max = TeamEdgeMeasurement.from_dict(data.get("speedMax") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "bursts_over_22": self.bursts_over_22.to_dict(),
            "bursts_over_20": self.bursts_over_20.to_dict(),
            "speed_max": self.speed_max.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamDistanceSkated:
    """Team skating distance for the season."""
    total: TeamEdgeMeasurement

    @classmethod
    def from_dict(cls, data: dict) -> TeamDistanceSkated:
        return cls(
            total = TeamEdgeMeasurement.from_dict(data.get("total") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "total": self.total.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class TeamSogSummary:
    """Shot on goal summary for a specific location zone (all/high/long/mid)."""
    location_code: str | None
    shots: int | None
    shots_rank: int | None
    shots_league_avg: float | None
    shooting_pctg: float | None
    shooting_pctg_rank: int | None
    shooting_pctg_league_avg: float | None
    goals: int | None
    goals_rank: int | None
    goals_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamSogSummary:
        return cls(
            location_code = data.get("locationCode"),
            shots = data.get("shots"),
            shots_rank = data.get("shotsRank"),
            shots_league_avg = data.get("shotsLeagueAvg"),
            shooting_pctg = data.get("shootingPctg"),
            shooting_pctg_rank = data.get("shootingPctgRank"),
            shooting_pctg_league_avg = data.get("shootingPctgLeagueAvg"),
            goals = data.get("goals"),
            goals_rank = data.get("goalsRank"),
            goals_league_avg = data.get("goalsLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "shots": self.shots,
            "shots_rank": self.shots_rank,
            "shots_league_avg": self.shots_league_avg,
            "shooting_pctg": self.shooting_pctg,
            "shooting_pctg_rank": self.shooting_pctg_rank,
            "shooting_pctg_league_avg": self.shooting_pctg_league_avg,
            "goals": self.goals,
            "goals_rank": self.goals_rank,
            "goals_league_avg": self.goals_league_avg,
        }


@dataclass(slots=True, frozen=True)
class TeamSogDetail:
    """Shot on goal count and rank for a specific rink area."""
    area: str | None
    shots: int | None
    shots_rank: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamSogDetail:
        return cls(
            area = data.get("area"),
            shots = data.get("shots"),
            shots_rank = data.get("shotsRank"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "shots": self.shots,
            "shots_rank": self.shots_rank,
        }


@dataclass(slots=True, frozen=True)
class TeamZoneTimeDetails:
    """
    Zone time percentages and league ranks across offensive (total and even strength),
    neutral, and defensive zones.
    """
    offensive_zone_pctg: float | None
    offensive_zone_rank: int | None
    offensive_zone_league_avg: float | None
    offensive_zone_ev_pctg: float | None
    offensive_zone_ev_rank: int | None
    offensive_zone_ev_league_avg: float | None
    neutral_zone_pctg: float | None
    neutral_zone_rank: int | None
    neutral_zone_league_avg: float | None
    defensive_zone_pctg: float | None
    defensive_zone_rank: int | None
    defensive_zone_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamZoneTimeDetails:
        return cls(
            offensive_zone_pctg = data.get("offensiveZonePctg"),
            offensive_zone_rank = data.get("offensiveZoneRank"),
            offensive_zone_league_avg = data.get("offensiveZoneLeagueAvg"),
            offensive_zone_ev_pctg = data.get("offensiveZoneEvPctg"),
            offensive_zone_ev_rank = data.get("offensiveZoneEvRank"),
            offensive_zone_ev_league_avg = data.get("offensiveZoneEvLeagueAvg"),
            neutral_zone_pctg = data.get("neutralZonePctg"),
            neutral_zone_rank = data.get("neutralZoneRank"),
            neutral_zone_league_avg = data.get("neutralZoneLeagueAvg"),
            defensive_zone_pctg = data.get("defensiveZonePctg"),
            defensive_zone_rank = data.get("defensiveZoneRank"),
            defensive_zone_league_avg = data.get("defensiveZoneLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "offensive_zone_pctg": self.offensive_zone_pctg,
            "offensive_zone_rank": self.offensive_zone_rank,
            "offensive_zone_league_avg": self.offensive_zone_league_avg,
            "offensive_zone_ev_pctg": self.offensive_zone_ev_pctg,
            "offensive_zone_ev_rank": self.offensive_zone_ev_rank,
            "offensive_zone_ev_league_avg": self.offensive_zone_ev_league_avg,
            "neutral_zone_pctg": self.neutral_zone_pctg,
            "neutral_zone_rank": self.neutral_zone_rank,
            "neutral_zone_league_avg": self.neutral_zone_league_avg,
            "defensive_zone_pctg": self.defensive_zone_pctg,
            "defensive_zone_rank": self.defensive_zone_rank,
            "defensive_zone_league_avg": self.defensive_zone_league_avg,
        }


@dataclass(slots=True, frozen=True)
class TeamDetailResult:
    """
    NHL Edge rankings and stat summaries for a team.

    Provides a full per-category summary including shot speed, skating speed,
    distance skated, shot on goal details, and zone time percentages.

    Instances of this class are accessed via `client.teams.stats.edge.details(team_id)`.
    """
    team: TeamDetailTeam
    seasons_with_edge: list[EdgeSeason]
    shot_speed: TeamShotSpeed
    skating_speed: TeamSkatingSpeed
    distance_skated: TeamDistanceSkated
    sog_summary: list[TeamSogSummary]
    sog_details: list[TeamSogDetail]
    zone_time: TeamZoneTimeDetails

    @classmethod
    def from_dict(cls, data: dict) -> TeamDetailResult:
        return cls(
            team = TeamDetailTeam.from_dict(data.get("team") or {}),
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            shot_speed = TeamShotSpeed.from_dict(data.get("shotSpeed") or {}),
            skating_speed = TeamSkatingSpeed.from_dict(data.get("skatingSpeed") or {}),
            distance_skated = TeamDistanceSkated.from_dict(data.get("distanceSkated") or {}),
            sog_summary = [TeamSogSummary.from_dict(s) for s in data.get("sogSummary") or []],
            sog_details = [TeamSogDetail.from_dict(d) for d in data.get("sogDetails") or []],
            zone_time = TeamZoneTimeDetails.from_dict(data.get("zoneTimeDetails") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "team": self.team.to_dict(),
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "shot_speed": self.shot_speed.to_dict(),
            "skating_speed": self.skating_speed.to_dict(),
            "distance_skated": self.distance_skated.to_dict(),
            "sog_summary": [s.to_dict() for s in self.sog_summary],
            "sog_details": [d.to_dict() for d in self.sog_details],
            "zone_time": self.zone_time.to_dict(),
        }
