"""
SKATER PUCK POSSESSIONS REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/puckPossessions
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterPuckPossessionsReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    position_code: str | None
    shoots_catches: str | None
    team_abbrevs: str | None
    defensive_zone_start_pct: float | None
    faceoff_pct5v5: float | None
    goals_pct: float | None
    individual_sat_for_per60: float | None
    individual_shots_for_per60: float | None
    neutral_zone_start_pct: float | None
    offensive_zone_start_pct: float | None
    offensive_zone_start_ratio: float | None
    on_ice_shooting_pct: float | None
    sat_pct: float | None
    time_on_ice_per_game5v5: float | None
    usat_pct: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterPuckPossessionsReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            position_code = data.get("positionCode"),
            shoots_catches = data.get("shootsCatches"),
            team_abbrevs = data.get("teamAbbrevs"),
            defensive_zone_start_pct = data.get("defensiveZoneStartPct"),
            faceoff_pct5v5 = data.get("faceoffPct5v5"),
            goals_pct = data.get("goalsPct"),
            individual_sat_for_per60 = data.get("individualSatForPer60"),
            individual_shots_for_per60 = data.get("individualShotsForPer60"),
            neutral_zone_start_pct = data.get("neutralZoneStartPct"),
            offensive_zone_start_pct = data.get("offensiveZoneStartPct"),
            offensive_zone_start_ratio = data.get("offensiveZoneStartRatio"),
            on_ice_shooting_pct = data.get("onIceShootingPct"),
            sat_pct = data.get("satPct"),
            time_on_ice_per_game5v5 = data.get("timeOnIcePerGame5v5"),
            usat_pct = data.get("usatPct"),
        )
