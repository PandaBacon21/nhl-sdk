"""
GOALIE STARTED VS RELIEVED REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/startedVsRelieved
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalieStartedVsRelievedReport:
    player_id: int | None
    goalie_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    team_abbrevs: str | None
    shoots_catches: str | None
    ties: int | None
    games_relieved: int | None
    games_started: int | None
    losses: int | None
    ot_losses: int | None
    save_pct: float | None
    wins: int | None
    games_relieved_goals_against: int | None
    games_relieved_losses: int | None
    games_relieved_ot_losses: int | None
    games_relieved_save_pct: float | None
    games_relieved_saves: int | None
    games_relieved_shots_against: int | None
    games_relieved_ties: int | None
    games_relieved_wins: int | None
    games_started_goals_against: int | None
    games_started_losses: int | None
    games_started_ot_losses: int | None
    games_started_save_pct: float | None
    games_started_saves: int | None
    games_started_shots_against: int | None
    games_started_ties: int | None
    games_started_wins: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieStartedVsRelievedReport:
        return cls(
            player_id = data.get("playerId"),
            goalie_full_name = data.get("goalieFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            team_abbrevs = data.get("teamAbbrevs"),
            shoots_catches = data.get("shootsCatches"),
            ties = data.get("ties"),
            games_relieved = data.get("gamesRelieved"),
            games_started = data.get("gamesStarted"),
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
            save_pct = data.get("savePct"),
            wins = data.get("wins"),
            games_relieved_goals_against = data.get("gamesRelievedGoalsAgainst"),
            games_relieved_losses = data.get("gamesRelievedLosses"),
            games_relieved_ot_losses = data.get("gamesRelievedOtLosses"),
            games_relieved_save_pct = data.get("gamesRelievedSavePct"),
            games_relieved_saves = data.get("gamesRelievedSaves"),
            games_relieved_shots_against = data.get("gamesRelievedShotsAgainst"),
            games_relieved_ties = data.get("gamesRelievedTies"),
            games_relieved_wins = data.get("gamesRelievedWins"),
            games_started_goals_against = data.get("gamesStartedGoalsAgainst"),
            games_started_losses = data.get("gamesStartedLosses"),
            games_started_ot_losses = data.get("gamesStartedOtLosses"),
            games_started_save_pct = data.get("gamesStartedSavePct"),
            games_started_saves = data.get("gamesStartedSaves"),
            games_started_shots_against = data.get("gamesStartedShotsAgainst"),
            games_started_ties = data.get("gamesStartedTies"),
            games_started_wins = data.get("gamesStartedWins"),
        )
