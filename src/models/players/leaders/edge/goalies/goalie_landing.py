"""
GOALIE EDGE LANDING MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ....player.player_stats.edge.player_edge_types import EdgeSeason, LeaderPlayer


@dataclass(slots=True, frozen=True)
class GoalieSavePctgAreaDetail:
    """Shot location detail for high danger save percentage leader."""
    area: str | None
    save_pctg: float | None
    save_pctg_percentile: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavePctgAreaDetail:
        return cls(
            area = data.get("area"),
            save_pctg = data.get("savePctg"),
            save_pctg_percentile = data.get("savePctgPercentile"),
        )


@dataclass(slots=True, frozen=True)
class GoalieSavesAreaDetail:
    """Shot location detail for high danger saves leader."""
    area: str | None
    saves: int | None
    saves_percentile: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavesAreaDetail:
        return cls(
            area = data.get("area"),
            saves = data.get("saves"),
            saves_percentile = data.get("savesPercentile"),
        )


@dataclass(slots=True, frozen=True)
class GoalieHighDangerSavePctgLeader:
    """Leader entry for high danger save percentage."""
    player: LeaderPlayer
    save_pctg: float | None
    shot_location_details: list[GoalieSavePctgAreaDetail]

    @classmethod
    def from_dict(cls, data: dict) -> GoalieHighDangerSavePctgLeader:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            save_pctg = data.get("savePctg"),
            shot_location_details = [GoalieSavePctgAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
        )


@dataclass(slots=True, frozen=True)
class GoalieHighDangerSavesLeader:
    """Leader entry for total high danger saves."""
    player: LeaderPlayer
    saves: int | None
    shot_location_details: list[GoalieSavesAreaDetail]

    @classmethod
    def from_dict(cls, data: dict) -> GoalieHighDangerSavesLeader:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            saves = data.get("saves"),
            shot_location_details = [GoalieSavesAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
        )


@dataclass(slots=True, frozen=True)
class GoalieSimpleLeader:
    """Leader entry with player and a single integer stat (goals against or games above .900)."""
    player: LeaderPlayer
    value: int | None

    @classmethod
    def from_dict(cls, data: dict, value_key: str) -> GoalieSimpleLeader:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            value = data.get(value_key),
        )


@dataclass(slots=True, frozen=True)
class GoalieSavePctg5v5Leader:
    """Leader entry for 5v5 save percentage."""
    player: LeaderPlayer
    save_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavePctg5v5Leader:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            save_pctg = data.get("savePctg"),
        )


@dataclass(slots=True, frozen=True)
class GoalieLandingLeaders:
    """All leader categories from the goalie Edge landing page."""
    high_danger_save_pctg: GoalieHighDangerSavePctgLeader
    high_danger_saves: GoalieHighDangerSavesLeader
    high_danger_goals_against: GoalieSimpleLeader
    save_pctg_5v5: GoalieSavePctg5v5Leader
    games_above_900: GoalieSimpleLeader

    @classmethod
    def from_dict(cls, data: dict) -> GoalieLandingLeaders:
        return cls(
            high_danger_save_pctg = GoalieHighDangerSavePctgLeader.from_dict(data.get("highDangerSavePctg") or {}),
            high_danger_saves = GoalieHighDangerSavesLeader.from_dict(data.get("highDangerSaves") or {}),
            high_danger_goals_against = GoalieSimpleLeader.from_dict(data.get("highDangerGoalsAgainst") or {}, value_key="goalsAgainst"),
            save_pctg_5v5 = GoalieSavePctg5v5Leader.from_dict(data.get("savePctg5v5") or {}),
            games_above_900 = GoalieSimpleLeader.from_dict(data.get("gamesAbove900") or {}, value_key="games"),
        )


@dataclass(slots=True, frozen=True)
class GoalieLanding:
    """Top-level model for the goalie Edge landing page response."""
    seasons_with_edge: list[EdgeSeason]
    minimum_games_played: int | None
    leaders: GoalieLandingLeaders

    @classmethod
    def from_dict(cls, data: dict) -> GoalieLanding:
        return cls(
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            minimum_games_played = data.get("minimumGamesPlayed"),
            leaders = GoalieLandingLeaders.from_dict(data.get("leaders") or {}),
        )
