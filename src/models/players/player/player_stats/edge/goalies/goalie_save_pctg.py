"""
GOALIE SAVE PERCENTAGE MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import EdgeCount, EdgeSeason


@dataclass(slots=True, frozen=True)
class GoalieSavePctgGame:
    """Per-game save percentage entry."""
    game_center_link: str | None
    game_date: str | None
    decision: str | None
    player_on_home_team: bool | None
    save_pctg: float | None
    home_team: dict | None
    away_team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavePctgGame:
        return cls(
            game_center_link=data.get("gameCenterLink"),
            game_date=data.get("gameDate"),
            decision=data.get("decision"),
            player_on_home_team=data.get("playerOnHomeTeam"),
            save_pctg=data.get("savePctg"),
            home_team=data.get("homeTeam"),
            away_team=data.get("awayTeam"),
        )

    def to_dict(self) -> dict:
        return {
            "game_center_link": self.game_center_link,
            "game_date": self.game_date,
            "decision": self.decision,
            "player_on_home_team": self.player_on_home_team,
            "save_pctg": self.save_pctg,
            "home_team": self.home_team,
            "away_team": self.away_team,
        }


@dataclass(slots=True, frozen=True)
class GoalieSavePctgSummary:
    """Season save percentage summary with percentile rankings and league averages."""
    games_above_900: EdgeCount
    pctg_games_above_900: EdgeCount

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavePctgSummary:
        return cls(
            games_above_900=EdgeCount.from_dict(data.get("gamesAbove900") or {}),
            pctg_games_above_900=EdgeCount.from_dict(data.get("pctgGamesAbove900") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "games_above_900": self.games_above_900.to_dict(),
            "pctg_games_above_900": self.pctg_games_above_900.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class GoalieSavePctg:
    """
    Per-player overall save percentage detail.

    Provides the last 10 games of overall save percentage, plus season
    totals for save percentage, games above .900, percentage of games above .900,
    point percentage, and goals against average.

    Instances of this class are accessed via `Stats.edge.goalie.save_pctg()`.
    """
    seasons_with_edge: list
    last_10_games: list
    save_pctg_summary: GoalieSavePctgSummary

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavePctg:
        return cls(
            seasons_with_edge=[EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            last_10_games=[GoalieSavePctgGame.from_dict(g) for g in data.get("savePctgLast10") or []],
            save_pctg_summary=GoalieSavePctgSummary.from_dict(data.get("savePctgDetails") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "last_10_games": [g.to_dict() for g in self.last_10_games],
            "save_pctg_summary": self.save_pctg_summary.to_dict(),
        }
