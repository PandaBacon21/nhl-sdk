"""
SKATER SHOT TYPE REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/shottype
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterShotTypeReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    team_abbrevs: str | None
    goals: int | None
    shooting_pct: float | None
    goals_backhand: int | None
    goals_bat: int | None
    goals_between_legs: int | None
    goals_cradle: int | None
    goals_deflected: int | None
    goals_poke: int | None
    goals_slap: int | None
    goals_snap: int | None
    goals_tip_in: int | None
    goals_wrap_around: int | None
    goals_wrist: int | None
    shooting_pct_backhand: float | None
    shooting_pct_bat: float | None
    shooting_pct_between_legs: float | None
    shooting_pct_cradle: float | None
    shooting_pct_deflected: float | None
    shooting_pct_poke: float | None
    shooting_pct_slap: float | None
    shooting_pct_snap: float | None
    shooting_pct_tip_in: float | None
    shooting_pct_wrap_around: float | None
    shooting_pct_wrist: float | None
    shots_on_net_backhand: int | None
    shots_on_net_bat: int | None
    shots_on_net_between_legs: int | None
    shots_on_net_cradle: int | None
    shots_on_net_deflected: int | None
    shots_on_net_poke: int | None
    shots_on_net_slap: int | None
    shots_on_net_snap: int | None
    shots_on_net_tip_in: int | None
    shots_on_net_wrap_around: int | None
    shots_on_net_wrist: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterShotTypeReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            season_id = data.get("seasonId"),
            team_abbrevs = data.get("teamAbbrevs"),
            goals = data.get("goals"),
            shooting_pct = data.get("shootingPct"),
            goals_backhand = data.get("goalsBackhand"),
            goals_bat = data.get("goalsBat"),
            goals_between_legs = data.get("goalsBetweenLegs"),
            goals_cradle = data.get("goalsCradle"),
            goals_deflected = data.get("goalsDeflected"),
            goals_poke = data.get("goalsPoke"),
            goals_slap = data.get("goalsSlap"),
            goals_snap = data.get("goalsSnap"),
            goals_tip_in = data.get("goalsTipIn"),
            goals_wrap_around = data.get("goalsWrapAround"),
            goals_wrist = data.get("goalsWrist"),
            shooting_pct_backhand = data.get("shootingPctBackhand"),
            shooting_pct_bat = data.get("shootingPctBat"),
            shooting_pct_between_legs = data.get("shootingPctBetweenLegs"),
            shooting_pct_cradle = data.get("shootingPctCradle"),
            shooting_pct_deflected = data.get("shootingPctDeflected"),
            shooting_pct_poke = data.get("shootingPctPoke"),
            shooting_pct_slap = data.get("shootingPctSlap"),
            shooting_pct_snap = data.get("shootingPctSnap"),
            shooting_pct_tip_in = data.get("shootingPctTipIn"),
            shooting_pct_wrap_around = data.get("shootingPctWrapAround"),
            shooting_pct_wrist = data.get("shootingPctWrist"),
            shots_on_net_backhand = data.get("shotsOnNetBackhand"),
            shots_on_net_bat = data.get("shotsOnNetBat"),
            shots_on_net_between_legs = data.get("shotsOnNetBetweenLegs"),
            shots_on_net_cradle = data.get("shotsOnNetCradle"),
            shots_on_net_deflected = data.get("shotsOnNetDeflected"),
            shots_on_net_poke = data.get("shotsOnNetPoke"),
            shots_on_net_slap = data.get("shotsOnNetSlap"),
            shots_on_net_snap = data.get("shotsOnNetSnap"),
            shots_on_net_tip_in = data.get("shotsOnNetTipIn"),
            shots_on_net_wrap_around = data.get("shotsOnNetWrapAround"),
            shots_on_net_wrist = data.get("shotsOnNetWrist"),
        )
