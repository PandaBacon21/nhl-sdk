"""
SKATER FACEOFF WINS REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/faceoffwins
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterFaceoffWinsReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    team_abbrevs: str | None
    faceoff_win_pct: float | None
    total_faceoffs: int | None
    total_faceoff_wins: int | None
    total_faceoff_losses: int | None
    defensive_zone_faceoffs: int | None
    defensive_zone_faceoff_wins: int | None
    defensive_zone_faceoff_losses: int | None
    ev_faceoffs: int | None
    ev_faceoffs_won: int | None
    ev_faceoffs_lost: int | None
    neutral_zone_faceoffs: int | None
    neutral_zone_faceoff_wins: int | None
    neutral_zone_faceoff_losses: int | None
    offensive_zone_faceoffs: int | None
    offensive_zone_faceoff_wins: int | None
    offensive_zone_faceoff_losses: int | None
    pp_faceoffs: int | None
    pp_faceoffs_won: int | None
    pp_faceoffs_lost: int | None
    sh_faceoffs: int | None
    sh_faceoffs_won: int | None
    sh_faceoffs_lost: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterFaceoffWinsReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            team_abbrevs = data.get("teamAbbrevs"),
            faceoff_win_pct = data.get("faceoffWinPct"),
            total_faceoffs = data.get("totalFaceoffs"),
            total_faceoff_wins = data.get("totalFaceoffWins"),
            total_faceoff_losses = data.get("totalFaceoffLosses"),
            defensive_zone_faceoffs = data.get("defensiveZoneFaceoffs"),
            defensive_zone_faceoff_wins = data.get("defensiveZoneFaceoffWins"),
            defensive_zone_faceoff_losses = data.get("defensiveZoneFaceoffLosses"),
            ev_faceoffs = data.get("evFaceoffs"),
            ev_faceoffs_won = data.get("evFaceoffsWon"),
            ev_faceoffs_lost = data.get("evFaceoffsLost"),
            neutral_zone_faceoffs = data.get("neutralZoneFaceoffs"),
            neutral_zone_faceoff_wins = data.get("neutralZoneFaceoffWins"),
            neutral_zone_faceoff_losses = data.get("neutralZoneFaceoffLosses"),
            offensive_zone_faceoffs = data.get("offensiveZoneFaceoffs"),
            offensive_zone_faceoff_wins = data.get("offensiveZoneFaceoffWins"),
            offensive_zone_faceoff_losses = data.get("offensiveZoneFaceoffLosses"),
            pp_faceoffs = data.get("ppFaceoffs"),
            pp_faceoffs_won = data.get("ppFaceoffsWon"),
            pp_faceoffs_lost = data.get("ppFaceoffsLost"),
            sh_faceoffs = data.get("shFaceoffs"),
            sh_faceoffs_won = data.get("shFaceoffsWon"),
            sh_faceoffs_lost = data.get("shFaceoffsLost"),
        )
