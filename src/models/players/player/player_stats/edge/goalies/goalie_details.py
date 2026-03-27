"""
GOALIE DETAILS MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from .......core.utilities import LocalizedString
from ..player_edge_types import EdgeCount, EdgeSeason


@dataclass(slots=True, frozen=True)
class CatGoaliePlayerSummary:
    """Goalie summary returned at the top level of both goalie detail and CAT goalie detail responses."""
    id: int | None
    first_name: LocalizedString
    last_name: LocalizedString
    birth_date: str | None
    shoots_catches: str | None
    sweater_number: int | None
    position: str | None
    slug: str | None
    headshot: str | None
    wins: int | None
    losses: int | None
    ot_losses: int | None
    gaa: float | None
    save_pctg: float | None
    games_played: int | None
    team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> CatGoaliePlayerSummary:
        return cls(
            id=data.get("id"),
            first_name=LocalizedString(data.get("firstName")),
            last_name=LocalizedString(data.get("lastName")),
            birth_date=data.get("birthDate"),
            shoots_catches=data.get("shootsCatches"),
            sweater_number=data.get("sweaterNumber"),
            position=data.get("position"),
            slug=data.get("slug"),
            headshot=data.get("headshot"),
            wins=data.get("wins"),
            losses=data.get("losses"),
            ot_losses=data.get("overtimeLosses"),
            gaa=data.get("goalsAgainstAvg"),
            save_pctg=data.get("savePctg"),
            games_played=data.get("gamesPlayed"),
            team=data.get("team"),
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
            "wins": self.wins,
            "losses": self.losses,
            "ot_losses": self.ot_losses,
            "gaa": self.gaa,
            "save_pctg": self.save_pctg,
            "games_played": self.games_played,
            "team": self.team,
        }


@dataclass(slots=True, frozen=True)
class GoalieShotLocationSummary:
    """Goals against, saves, and save percentage for a location zone with percentile rankings."""
    location_code: str | None
    goals_against: int | None
    goals_against_percentile: float | None
    goals_against_league_avg: float | None
    saves: int | None
    saves_percentile: float | None
    saves_league_avg: float | None
    save_pctg: float | None
    save_pctg_percentile: float | None
    save_pctg_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieShotLocationSummary:
        return cls(
            location_code=data.get("locationCode"),
            goals_against=data.get("goalsAgainst"),
            goals_against_percentile=data.get("goalsAgainstPercentile"),
            goals_against_league_avg=data.get("goalsAgainstLeagueAvg"),
            saves=data.get("saves"),
            saves_percentile=data.get("savesPercentile"),
            saves_league_avg=data.get("savesLeagueAvg"),
            save_pctg=data.get("savePctg"),
            save_pctg_percentile=data.get("savePctgPercentile"),
            save_pctg_league_avg=data.get("savePctgLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "location_code": self.location_code,
            "goals_against": self.goals_against,
            "goals_against_percentile": self.goals_against_percentile,
            "goals_against_league_avg": self.goals_against_league_avg,
            "saves": self.saves,
            "saves_percentile": self.saves_percentile,
            "saves_league_avg": self.saves_league_avg,
            "save_pctg": self.save_pctg,
            "save_pctg_percentile": self.save_pctg_percentile,
            "save_pctg_league_avg": self.save_pctg_league_avg,
        }


@dataclass(slots=True, frozen=True)
class GoalieShotLocationAreaDetail:
    """Shots, saves, goals against, and save percentage with percentile rankings for a specific rink area."""
    area: str | None
    shots_against: int | None
    shots_against_percentile: float | None
    saves: int | None
    saves_percentile: float | None
    goals_against: int | None
    goals_against_percentile: float | None
    save_pctg: float | None
    save_pctg_percentile: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieShotLocationAreaDetail:
        return cls(
            area=data.get("area"),
            shots_against=data.get("shotsAgainst"),
            shots_against_percentile=data.get("shotsAgainstPercentile") or data.get("shotsPercentile"),
            saves=data.get("saves"),
            saves_percentile=data.get("savesPercentile"),
            goals_against=data.get("goalsAgainst"),
            goals_against_percentile=data.get("goalsAgainstPercentile"),
            save_pctg=data.get("savePctg"),
            save_pctg_percentile=data.get("savePctgPercentile"),
        )

    def to_dict(self) -> dict:
        return {
            "area": self.area,
            "shots_against": self.shots_against,
            "shots_against_percentile": self.shots_against_percentile,
            "saves": self.saves,
            "saves_percentile": self.saves_percentile,
            "goals_against": self.goals_against,
            "goals_against_percentile": self.goals_against_percentile,
            "save_pctg": self.save_pctg,
            "save_pctg_percentile": self.save_pctg_percentile,
        }


@dataclass(slots=True, frozen=True)
class GoalieDetails:
    """
    NHL Edge rankings and stat summaries for a goalie.

    Provides a full per-category summary including GAA, games above .900,
    goal differential per 60, goal support average, point percentage,
    and shot location breakdowns with percentile rankings.

    Instances of this class are accessed via `Stats.edge().details()`.
    """
    player: CatGoaliePlayerSummary
    seasons_with_edge: list
    goals_against_avg: EdgeCount
    games_above_900: EdgeCount
    goal_differential_per_60: EdgeCount
    goal_support_avg: EdgeCount
    point_pctg: EdgeCount
    shot_location_summary: list
    shot_location_details: list

    @classmethod
    def from_dict(cls, data: dict) -> GoalieDetails:
        stats: dict = data.get("stats") or {}
        return cls(
            player=CatGoaliePlayerSummary.from_dict(data.get("player") or {}),
            seasons_with_edge=[EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            goals_against_avg=EdgeCount.from_dict(stats.get("goalsAgainstAvg") or {}),
            games_above_900=EdgeCount.from_dict(stats.get("gamesAbove900") or {}),
            goal_differential_per_60=EdgeCount.from_dict(stats.get("goalDifferentialPer60") or {}),
            goal_support_avg=EdgeCount.from_dict(stats.get("goalSupportAvg") or {}),
            point_pctg=EdgeCount.from_dict(stats.get("pointPctg") or {}),
            shot_location_summary=[GoalieShotLocationSummary.from_dict(s) for s in data.get("shotLocationSummary") or []],
            shot_location_details=[GoalieShotLocationAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "goals_against_avg": self.goals_against_avg.to_dict(),
            "games_above_900": self.games_above_900.to_dict(),
            "goal_differential_per_60": self.goal_differential_per_60.to_dict(),
            "goal_support_avg": self.goal_support_avg.to_dict(),
            "point_pctg": self.point_pctg.to_dict(),
            "shot_location_summary": [s.to_dict() for s in self.shot_location_summary],
            "shot_location_details": [d.to_dict() for d in self.shot_location_details],
        }
