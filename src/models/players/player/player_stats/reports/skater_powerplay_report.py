"""
SKATER POWER PLAY REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/powerplay
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterPowerPlayReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    position_code: str | None
    team_abbrevs: str | None
    pp_assists: int | None
    pp_goals: int | None
    pp_goals_for_per60: float | None
    pp_goals_per60: float | None
    pp_individual_sat_for: int | None
    pp_individual_sat_for_per60: float | None
    pp_points: int | None
    pp_points_per60: float | None
    pp_primary_assists: int | None
    pp_primary_assists_per60: float | None
    pp_secondary_assists: int | None
    pp_secondary_assists_per60: float | None
    pp_shooting_pct: float | None
    pp_shots: int | None
    pp_shots_per60: float | None
    pp_time_on_ice: int | None
    pp_time_on_ice_pct_per_game: float | None
    pp_time_on_ice_per_game: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterPowerPlayReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            position_code = data.get("positionCode"),
            team_abbrevs = data.get("teamAbbrevs"),
            pp_assists = data.get("ppAssists"),
            pp_goals = data.get("ppGoals"),
            pp_goals_for_per60 = data.get("ppGoalsForPer60"),
            pp_goals_per60 = data.get("ppGoalsPer60"),
            pp_individual_sat_for = data.get("ppIndividualSatFor"),
            pp_individual_sat_for_per60 = data.get("ppIndividualSatForPer60"),
            pp_points = data.get("ppPoints"),
            pp_points_per60 = data.get("ppPointsPer60"),
            pp_primary_assists = data.get("ppPrimaryAssists"),
            pp_primary_assists_per60 = data.get("ppPrimaryAssistsPer60"),
            pp_secondary_assists = data.get("ppSecondaryAssists"),
            pp_secondary_assists_per60 = data.get("ppSecondaryAssistsPer60"),
            pp_shooting_pct = data.get("ppShootingPct"),
            pp_shots = data.get("ppShots"),
            pp_shots_per60 = data.get("ppShotsPer60"),
            pp_time_on_ice = data.get("ppTimeOnIce"),
            pp_time_on_ice_pct_per_game = data.get("ppTimeOnIcePctPerGame"),
            pp_time_on_ice_per_game = data.get("ppTimeOnIcePerGame"),
        )
