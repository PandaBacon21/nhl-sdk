"""
SKATER PENALTY KILL REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/penaltykill
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterPenaltyKillReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    position_code: str | None
    team_abbrevs: str | None
    pp_goals_against_per60: float | None
    sh_assists: int | None
    sh_goals: int | None
    sh_goals_per60: float | None
    sh_individual_sat_for: int | None
    sh_individual_sat_for_per60: float | None
    sh_points: int | None
    sh_points_per60: float | None
    sh_primary_assists: int | None
    sh_primary_assists_per60: float | None
    sh_secondary_assists: int | None
    sh_secondary_assists_per60: float | None
    sh_shooting_pct: float | None
    sh_shots: int | None
    sh_shots_per60: float | None
    sh_time_on_ice: int | None
    sh_time_on_ice_pct_per_game: float | None
    sh_time_on_ice_per_game: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterPenaltyKillReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            position_code = data.get("positionCode"),
            team_abbrevs = data.get("teamAbbrevs"),
            pp_goals_against_per60 = data.get("ppGoalsAgainstPer60"),
            sh_assists = data.get("shAssists"),
            sh_goals = data.get("shGoals"),
            sh_goals_per60 = data.get("shGoalsPer60"),
            sh_individual_sat_for = data.get("shIndividualSatFor"),
            sh_individual_sat_for_per60 = data.get("shIndividualSatForPer60"),
            sh_points = data.get("shPoints"),
            sh_points_per60 = data.get("shPointsPer60"),
            sh_primary_assists = data.get("shPrimaryAssists"),
            sh_primary_assists_per60 = data.get("shPrimaryAssistsPer60"),
            sh_secondary_assists = data.get("shSecondaryAssists"),
            sh_secondary_assists_per60 = data.get("shSecondaryAssistsPer60"),
            sh_shooting_pct = data.get("shShootingPct"),
            sh_shots = data.get("shShots"),
            sh_shots_per60 = data.get("shShotsPer60"),
            sh_time_on_ice = data.get("shTimeOnIce"),
            sh_time_on_ice_pct_per_game = data.get("shTimeOnIcePctPerGame"),
            sh_time_on_ice_per_game = data.get("shTimeOnIcePerGame"),
        )
