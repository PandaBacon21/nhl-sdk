"""
GOALIE PENALTY SHOTS REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/penaltyShots
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoaliePenaltyShotsReport:
    player_id: int | None
    goalie_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    team_abbrevs: str | None
    shoots_catches: str | None
    goals_against: int | None
    save_pct: float | None
    saves: int | None
    shots_against: int | None
    penalty_shot_save_pct: float | None
    penalty_shots_against: int | None
    penalty_shots_goals_against: int | None
    penalty_shots_saves: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoaliePenaltyShotsReport:
        return cls(
            player_id = data.get("playerId"),
            goalie_full_name = data.get("goalieFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            team_abbrevs = data.get("teamAbbrevs"),
            shoots_catches = data.get("shootsCatches"),
            goals_against = data.get("goalsAgainst"),
            save_pct = data.get("savePct"),
            saves = data.get("saves"),
            shots_against = data.get("shotsAgainst"),
            penalty_shot_save_pct = data.get("penaltyShotSavePct"),
            penalty_shots_against = data.get("penaltyShotsAgainst"),
            penalty_shots_goals_against = data.get("penaltyShotsGoalsAgainst"),
            penalty_shots_saves = data.get("penaltyShotsSaves"),
        )
