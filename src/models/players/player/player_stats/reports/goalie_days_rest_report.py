"""
GOALIE DAYS REST REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/daysrest
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalieDaysRestReport:
    player_id: int | None
    goalie_full_name: str | None
    last_name: str | None
    games_played: int | None
    games_started: int | None
    season_id: int | None
    team_abbrevs: str | None
    shoots_catches: str | None
    ties: int | None
    losses: int | None
    ot_losses: int | None
    wins: int | None
    save_pct: float | None
    games_played_days_rest0: int | None
    games_played_days_rest1: int | None
    games_played_days_rest2: int | None
    games_played_days_rest3: int | None
    games_played_days_rest4_plus: int | None
    save_pct_days_rest0: float | None
    save_pct_days_rest1: float | None
    save_pct_days_rest2: float | None
    save_pct_days_rest3: float | None
    save_pct_days_rest4_plus: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieDaysRestReport:
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
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
            wins = data.get("wins"),
            save_pct = data.get("savePct"),
            games_played_days_rest0 = data.get("gamesPlayedDaysRest0"),
            games_played_days_rest1 = data.get("gamesPlayedDaysRest1"),
            games_played_days_rest2 = data.get("gamesPlayedDaysRest2"),
            games_played_days_rest3 = data.get("gamesPlayedDaysRest3"),
            games_played_days_rest4_plus = data.get("gamesPlayedDaysRest4Plus"),
            save_pct_days_rest0 = data.get("savePctDaysRest0"),
            save_pct_days_rest1 = data.get("savePctDaysRest1"),
            save_pct_days_rest2 = data.get("savePctDaysRest2"),
            save_pct_days_rest3 = data.get("savePctDaysRest3"),
            save_pct_days_rest4_plus = data.get("savePctDaysRest4Plus"),
        )
