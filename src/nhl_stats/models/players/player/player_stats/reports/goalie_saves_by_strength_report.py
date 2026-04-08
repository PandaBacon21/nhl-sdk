"""
GOALIE SAVES BY STRENGTH REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/savesByStrength
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalieSavesByStrengthReport:
    player_id: int | None
    goalie_full_name: str | None
    last_name: str | None
    games_played: int | None
    games_started: int | None
    season_id: int | None
    team_abbrevs: str | None
    shoots_catches: str | None
    ties: int | None
    goals_against: int | None
    losses: int | None
    ot_losses: int | None
    save_pct: float | None
    saves: int | None
    shots_against: int | None
    wins: int | None
    ev_goals_against: int | None
    ev_save_pct: float | None
    ev_saves: int | None
    ev_shots_against: int | None
    pp_goals_against: int | None
    pp_save_pct: float | None
    pp_saves: int | None
    pp_shots_against: int | None
    sh_goals_against: int | None
    sh_save_pct: float | None
    sh_saves: int | None
    sh_shots_against: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavesByStrengthReport:
        return cls(
            player_id = data.get("playerId"),
            goalie_full_name = data.get("goalieFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            games_started = data.get("gamesStarted"),
            season_id = data.get("seasonId"),
            team_abbrevs = data.get("teamAbbrevs"),
            shoots_catches = data.get("shootsCatches"),
            ties = data.get("ties"),
            goals_against = data.get("goalsAgainst"),
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
            save_pct = data.get("savePct"),
            saves = data.get("saves"),
            shots_against = data.get("shotsAgainst"),
            wins = data.get("wins"),
            ev_goals_against = data.get("evGoalsAgainst"),
            ev_save_pct = data.get("evSavePct"),
            ev_saves = data.get("evSaves"),
            ev_shots_against = data.get("evShotsAgainst"),
            pp_goals_against = data.get("ppGoalsAgainst"),
            pp_save_pct = data.get("ppSavePct"),
            pp_saves = data.get("ppSaves"),
            pp_shots_against = data.get("ppShotsAgainst"),
            sh_goals_against = data.get("shGoalsAgainst"),
            sh_save_pct = data.get("shSavePct"),
            sh_saves = data.get("shSaves"),
            sh_shots_against = data.get("shShotsAgainst"),
        )
