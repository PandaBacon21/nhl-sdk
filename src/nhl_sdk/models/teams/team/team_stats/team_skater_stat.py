"""
TEAM SKATER STAT MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class TeamSkaterStat:
    """A single skater's stats entry for a team's club-stats response."""
    player_id: int | None
    headshot: str | None
    first_name: LocalizedString
    last_name: LocalizedString
    position_code: str | None
    games_played: int | None
    goals: int | None
    assists: int | None
    points: int | None
    plus_minus: int | None
    penalty_minutes: int | None
    power_play_goals: int | None
    shorthanded_goals: int | None
    game_winning_goals: int | None
    overtime_goals: int | None
    shots: int | None
    shooting_pctg: float | None
    avg_time_on_ice_per_game: float | None
    avg_shifts_per_game: float | None
    faceoff_win_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamSkaterStat:
        return cls(
            player_id = data.get("playerId"),
            headshot = data.get("headshot"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            position_code = data.get("positionCode"),
            games_played = data.get("gamesPlayed"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
            plus_minus = data.get("plusMinus"),
            penalty_minutes = data.get("penaltyMinutes"),
            power_play_goals = data.get("powerPlayGoals"),
            shorthanded_goals = data.get("shorthandedGoals"),
            game_winning_goals = data.get("gameWinningGoals"),
            overtime_goals = data.get("overtimeGoals"),
            shots = data.get("shots"),
            shooting_pctg = data.get("shootingPctg"),
            avg_time_on_ice_per_game = data.get("avgTimeOnIcePerGame"),
            avg_shifts_per_game = data.get("avgShiftsPerGame"),
            faceoff_win_pctg = data.get("faceoffWinPctg"),
        )
