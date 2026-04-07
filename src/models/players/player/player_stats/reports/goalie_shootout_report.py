"""
GOALIE SHOOTOUT REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/shootout
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalieShootoutReport:
    player_id: int | None
    goalie_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    shoots_catches: str | None
    team_abbrevs: str | None
    career_shootout_games_played: int | None
    career_shootout_goals_allowed: int | None
    career_shootout_losses: int | None
    career_shootout_save_pct: float | None
    career_shootout_saves: int | None
    career_shootout_shots_against: int | None
    career_shootout_wins: int | None
    shootout_goals_against: int | None
    shootout_losses: int | None
    shootout_save_pct: float | None
    shootout_saves: int | None
    shootout_shots_against: int | None
    shootout_wins: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieShootoutReport:
        return cls(
            player_id = data.get("playerId"),
            goalie_full_name = data.get("goalieFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            shoots_catches = data.get("shootsCatches"),
            team_abbrevs = data.get("teamAbbrevs"),
            career_shootout_games_played = data.get("careerShootoutGamesPlayed"),
            career_shootout_goals_allowed = data.get("careerShootoutGoalsAllowed"),
            career_shootout_losses = data.get("careerShootoutLosses"),
            career_shootout_save_pct = data.get("careerShootoutSavePct"),
            career_shootout_saves = data.get("careerShootoutSaves"),
            career_shootout_shots_against = data.get("careerShootoutShotsAgainst"),
            career_shootout_wins = data.get("careerShootoutWins"),
            shootout_goals_against = data.get("shootoutGoalsAgainst"),
            shootout_losses = data.get("shootoutLosses"),
            shootout_save_pct = data.get("shootoutSavePct"),
            shootout_saves = data.get("shootoutSaves"),
            shootout_shots_against = data.get("shootoutShotsAgainst"),
            shootout_wins = data.get("shootoutWins"),
        )
