"""
SKATER PENALTIES REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/penalties
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterPenaltiesReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    position_code: str | None
    team_abbrevs: str | None
    assists: int | None
    goals: int | None
    points: int | None
    time_on_ice_per_game: float | None
    game_misconduct_penalties: int | None
    major_penalties: int | None
    match_penalties: int | None
    minor_penalties: int | None
    misconduct_penalties: int | None
    net_penalties: int | None
    net_penalties_per60: float | None
    penalties: int | None
    penalties_drawn: int | None
    penalties_drawn_per60: float | None
    penalties_taken_per60: float | None
    penalty_minutes: int | None
    penalty_minutes_per_time_on_ice: float | None
    penalty_seconds_per_game: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterPenaltiesReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            position_code = data.get("positionCode"),
            team_abbrevs = data.get("teamAbbrevs"),
            assists = data.get("assists"),
            goals = data.get("goals"),
            points = data.get("points"),
            time_on_ice_per_game = data.get("timeOnIcePerGame"),
            game_misconduct_penalties = data.get("gameMisconductPenalties"),
            major_penalties = data.get("majorPenalties"),
            match_penalties = data.get("matchPenalties"),
            minor_penalties = data.get("minorPenalties"),
            misconduct_penalties = data.get("misconductPenalties"),
            net_penalties = data.get("netPenalties"),
            net_penalties_per60 = data.get("netPenaltiesPer60"),
            penalties = data.get("penalties"),
            penalties_drawn = data.get("penaltiesDrawn"),
            penalties_drawn_per60 = data.get("penaltiesDrawnPer60"),
            penalties_taken_per60 = data.get("penaltiesTakenPer60"),
            penalty_minutes = data.get("penaltyMinutes"),
            penalty_minutes_per_time_on_ice = data.get("penaltyMinutesPerTimeOnIce"),
            penalty_seconds_per_game = data.get("penaltySecondsPerGame"),
        )
