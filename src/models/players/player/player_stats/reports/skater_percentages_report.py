"""
SKATER PERCENTAGES REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/percentages
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterPercentagesReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    shoots_catches: str | None
    team_abbrevs: str | None
    sat_percentage: float | None
    sat_percentage_ahead: float | None
    sat_percentage_behind: float | None
    sat_percentage_close: float | None
    sat_percentage_tied: float | None
    sat_relative: float | None
    usat_percentage: float | None
    usat_percentage_ahead: float | None
    usat_percentage_behind: float | None
    usat_percentage_tied: float | None
    usat_precentage_close: float | None  # API typo preserved
    usat_relative: float | None
    shooting_pct5v5: float | None
    skater_save_pct5v5: float | None
    skater_shooting_plus_save_pct5v5: float | None
    time_on_ice_per_game5v5: float | None
    zone_start_pct5v5: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterPercentagesReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            shoots_catches = data.get("shootsCatches"),
            team_abbrevs = data.get("teamAbbrevs"),
            sat_percentage = data.get("satPercentage"),
            sat_percentage_ahead = data.get("satPercentageAhead"),
            sat_percentage_behind = data.get("satPercentageBehind"),
            sat_percentage_close = data.get("satPercentageClose"),
            sat_percentage_tied = data.get("satPercentageTied"),
            sat_relative = data.get("satRelative"),
            usat_percentage = data.get("usatPercentage"),
            usat_percentage_ahead = data.get("usatPercentageAhead"),
            usat_percentage_behind = data.get("usatPercentageBehind"),
            usat_percentage_tied = data.get("usatPercentageTied"),
            usat_precentage_close = data.get("usatPrecentageClose"),
            usat_relative = data.get("usatRelative"),
            shooting_pct5v5 = data.get("shootingPct5v5"),
            skater_save_pct5v5 = data.get("skaterSavePct5v5"),
            skater_shooting_plus_save_pct5v5 = data.get("skaterShootingPlusSavePct5v5"),
            time_on_ice_per_game5v5 = data.get("timeOnIcePerGame5v5"),
            zone_start_pct5v5 = data.get("zoneStartPct5v5"),
        )
