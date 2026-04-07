"""
SKATER GOALS FOR AGAINST REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/goalsForAgainst
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterGoalsForAgainstReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    team_abbrevs: str | None
    position_code: str | None
    assists: int | None
    goals: int | None
    points: int | None
    even_strength_goal_difference: int | None
    even_strength_goals_against: int | None
    even_strength_goals_for: int | None
    even_strength_goals_for_pct: float | None
    even_strength_time_on_ice_per_game: float | None
    power_play_goal_for: int | None
    power_play_goals_against: int | None
    power_play_time_on_ice_per_game: float | None
    short_handed_goals_against: int | None
    short_handed_goals_for: int | None
    short_handed_time_on_ice_per_game: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterGoalsForAgainstReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            team_abbrevs = data.get("teamAbbrevs"),
            position_code = data.get("positionCode"),
            assists = data.get("assists"),
            goals = data.get("goals"),
            points = data.get("points"),
            even_strength_goal_difference = data.get("evenStrengthGoalDifference"),
            even_strength_goals_against = data.get("evenStrengthGoalsAgainst"),
            even_strength_goals_for = data.get("evenStrengthGoalsFor"),
            even_strength_goals_for_pct = data.get("evenStrengthGoalsForPct"),
            even_strength_time_on_ice_per_game = data.get("evenStrengthTimeOnIcePerGame"),
            power_play_goal_for = data.get("powerPlayGoalFor"),
            power_play_goals_against = data.get("powerPlayGoalsAgainst"),
            power_play_time_on_ice_per_game = data.get("powerPlayTimeOnIcePerGame"),
            short_handed_goals_against = data.get("shortHandedGoalsAgainst"),
            short_handed_goals_for = data.get("shortHandedGoalsFor"),
            short_handed_time_on_ice_per_game = data.get("shortHandedTimeOnIcePerGame"),
        )
