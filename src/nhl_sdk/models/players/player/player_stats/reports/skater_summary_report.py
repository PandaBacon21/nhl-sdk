"""
SKATER SUMMARY REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/summary
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterSummaryReport:
    player_id: int | None
    season_id: int | None
    game_type_id: int | None
    skater_full_name: str | None
    team_abbrevs: str | None
    position_code: str | None
    games_played: int | None
    goals: int | None
    assists: int | None
    points: int | None
    plus_minus: int | None
    penalty_minutes: int | None
    shots: int | None
    shooting_pctg: float | None
    ev_goals: int | None
    ev_points: int | None
    pp_goals: int | None
    pp_points: int | None
    sh_goals: int | None
    sh_points: int | None
    ot_goals: int | None
    game_winning_goals: int | None
    faceoff_win_pctg: float | None
    time_on_ice_per_game: str | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterSummaryReport:
        return cls(
            player_id = data.get("playerId"),
            season_id = data.get("seasonId"),
            game_type_id = data.get("gameTypeId"),
            skater_full_name = data.get("skaterFullName"),
            team_abbrevs = data.get("teamAbbrevs"),
            position_code = data.get("positionCode"),
            games_played = data.get("gamesPlayed"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
            plus_minus = data.get("plusMinus"),
            penalty_minutes = data.get("penaltyMinutes"),
            shots = data.get("shots"),
            shooting_pctg = data.get("shootingPctg"),
            ev_goals = data.get("evGoals"),
            ev_points = data.get("evPoints"),
            pp_goals = data.get("ppGoals"),
            pp_points = data.get("ppPoints"),
            sh_goals = data.get("shGoals"),
            sh_points = data.get("shPoints"),
            ot_goals = data.get("otGoals"),
            game_winning_goals = data.get("gameWinningGoals"),
            faceoff_win_pctg = data.get("faceoffWinPctg"),
            time_on_ice_per_game = data.get("timeOnIcePerGame"),
        )
