"""
SKATER FACEOFF PERCENTAGE REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/faceoffpercentages
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterFaceoffPctReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    position_code: str | None
    shoots_catches: str | None
    team_abbrevs: str | None
    time_on_ice_per_game: float | None
    faceoff_win_pct: float | None
    total_faceoffs: int | None
    defensive_zone_faceoff_pct: float | None
    defensive_zone_faceoffs: int | None
    ev_faceoff_pct: float | None
    ev_faceoffs: int | None
    neutral_zone_faceoff_pct: float | None
    neutral_zone_faceoffs: int | None
    offensive_zone_faceoff_pct: float | None
    offensive_zone_faceoffs: int | None
    pp_faceoff_pct: float | None
    pp_faceoffs: int | None
    sh_faceoff_pct: float | None
    sh_faceoffs: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterFaceoffPctReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            position_code = data.get("positionCode"),
            shoots_catches = data.get("shootsCatches"),
            team_abbrevs = data.get("teamAbbrevs"),
            time_on_ice_per_game = data.get("timeOnIcePerGame"),
            faceoff_win_pct = data.get("faceoffWinPct"),
            total_faceoffs = data.get("totalFaceoffs"),
            defensive_zone_faceoff_pct = data.get("defensiveZoneFaceoffPct"),
            defensive_zone_faceoffs = data.get("defensiveZoneFaceoffs"),
            ev_faceoff_pct = data.get("evFaceoffPct"),
            ev_faceoffs = data.get("evFaceoffs"),
            neutral_zone_faceoff_pct = data.get("neutralZoneFaceoffPct"),
            neutral_zone_faceoffs = data.get("neutralZoneFaceoffs"),
            offensive_zone_faceoff_pct = data.get("offensiveZoneFaceoffPct"),
            offensive_zone_faceoffs = data.get("offensiveZoneFaceoffs"),
            pp_faceoff_pct = data.get("ppFaceoffPct"),
            pp_faceoffs = data.get("ppFaceoffs"),
            sh_faceoff_pct = data.get("shFaceoffPct"),
            sh_faceoffs = data.get("shFaceoffs"),
        )
