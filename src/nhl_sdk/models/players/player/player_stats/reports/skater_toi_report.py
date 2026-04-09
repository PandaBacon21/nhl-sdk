"""
SKATER TIME ON ICE REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/timeonice
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterTimeOnIceReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    position_code: str | None
    shoots_catches: str | None
    team_abbrevs: str | None
    ev_time_on_ice: int | None
    ev_time_on_ice_per_game: float | None
    ot_time_on_ice: int | None
    ot_time_on_ice_per_ot_game: float | None
    pp_time_on_ice: int | None
    pp_time_on_ice_per_game: float | None
    sh_time_on_ice: int | None
    sh_time_on_ice_per_game: float | None
    shifts: int | None
    shifts_per_game: float | None
    time_on_ice: int | None
    time_on_ice_per_game: float | None
    time_on_ice_per_shift: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterTimeOnIceReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            position_code = data.get("positionCode"),
            shoots_catches = data.get("shootsCatches"),
            team_abbrevs = data.get("teamAbbrevs"),
            ev_time_on_ice = data.get("evTimeOnIce"),
            ev_time_on_ice_per_game = data.get("evTimeOnIcePerGame"),
            ot_time_on_ice = data.get("otTimeOnIce"),
            ot_time_on_ice_per_ot_game = data.get("otTimeOnIcePerOtGame"),
            pp_time_on_ice = data.get("ppTimeOnIce"),
            pp_time_on_ice_per_game = data.get("ppTimeOnIcePerGame"),
            sh_time_on_ice = data.get("shTimeOnIce"),
            sh_time_on_ice_per_game = data.get("shTimeOnIcePerGame"),
            shifts = data.get("shifts"),
            shifts_per_game = data.get("shiftsPerGame"),
            time_on_ice = data.get("timeOnIce"),
            time_on_ice_per_game = data.get("timeOnIcePerGame"),
            time_on_ice_per_shift = data.get("timeOnIcePerShift"),
        )
