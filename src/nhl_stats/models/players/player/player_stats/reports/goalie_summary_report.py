"""
GOALIE SUMMARY REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/summary
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalieSummaryReport:
    player_id: int | None
    season_id: int | None
    game_type_id: int | None
    goalie_full_name: str | None
    team_abbrevs: str | None
    games_played: int | None
    games_started: int | None
    wins: int | None
    losses: int | None
    ot_losses: int | None
    shots_against: int | None
    saves: int | None
    goals_against: int | None
    goals_against_avg: float | None
    save_pctg: float | None
    shutouts: int | None
    time_on_ice: str | None
    goals: int | None
    assists: int | None
    penalty_minutes: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSummaryReport:
        return cls(
            player_id = data.get("playerId"),
            season_id = data.get("seasonId"),
            game_type_id = data.get("gameTypeId"),
            goalie_full_name = data.get("goalieFullName"),
            team_abbrevs = data.get("teamAbbrevs"),
            games_played = data.get("gamesPlayed"),
            games_started = data.get("gamesStarted"),
            wins = data.get("wins"),
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
            shots_against = data.get("shotsAgainst"),
            saves = data.get("saves"),
            goals_against = data.get("goalsAgainst"),
            goals_against_avg = data.get("goalsAgainstAverage"),
            save_pctg = data.get("savePctg"),
            shutouts = data.get("shutouts"),
            time_on_ice = data.get("timeOnIce"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            penalty_minutes = data.get("penaltyMinutes"),
        )
