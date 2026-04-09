"""
GOALIE ADVANCED REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/advanced
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalieAdvancedReport:
    player_id: int | None
    goalie_full_name: str | None
    last_name: str | None
    games_played: int | None
    games_started: int | None
    season_id: int | None
    team_abbrevs: str | None
    shoots_catches: str | None
    complete_game_pct: float | None
    complete_games: int | None
    goals_against: int | None
    goals_against_average: float | None
    goals_for: int | None
    goals_for_average: float | None
    incomplete_games: int | None
    quality_start: int | None
    quality_starts_pct: float | None
    regulation_losses: int | None
    regulation_wins: int | None
    save_pct: float | None
    shots_against_per60: float | None
    time_on_ice: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieAdvancedReport:
        return cls(
            player_id = data.get("playerId"),
            goalie_full_name = data.get("goalieFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            games_started = data.get("gamesStarted"),
            season_id = data.get("seasonId"),
            team_abbrevs = data.get("teamAbbrevs"),
            shoots_catches = data.get("shootsCatches"),
            complete_game_pct = data.get("completeGamePct"),
            complete_games = data.get("completeGames"),
            goals_against = data.get("goalsAgainst"),
            goals_against_average = data.get("goalsAgainstAverage"),
            goals_for = data.get("goalsFor"),
            goals_for_average = data.get("goalsForAverage"),
            incomplete_games = data.get("incompleteGames"),
            quality_start = data.get("qualityStart"),
            quality_starts_pct = data.get("qualityStartsPct"),
            regulation_losses = data.get("regulationLosses"),
            regulation_wins = data.get("regulationWins"),
            save_pct = data.get("savePct"),
            shots_against_per60 = data.get("shotsAgainstPer60"),
            time_on_ice = data.get("timeOnIce"),
        )
