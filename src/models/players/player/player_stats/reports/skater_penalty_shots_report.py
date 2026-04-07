"""
SKATER PENALTY SHOTS REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/penaltyShots
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterPenaltyShotsReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    season_id: int | None
    position_code: str | None
    shoots_catches: str | None
    team_abbrevs: str | None
    penalty_shot_attempts: int | None
    penalty_shot_shooting_pct: float | None
    penalty_shots_failed: int | None
    penalty_shots_goals: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterPenaltyShotsReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            season_id = data.get("seasonId"),
            position_code = data.get("positionCode"),
            shoots_catches = data.get("shootsCatches"),
            team_abbrevs = data.get("teamAbbrevs"),
            penalty_shot_attempts = data.get("penaltyShotAttempts"),
            penalty_shot_shooting_pct = data.get("penaltyShotShootingPct"),
            penalty_shots_failed = data.get("penaltyShotsFailed"),
            penalty_shots_goals = data.get("penaltyShotsGoals"),
        )
