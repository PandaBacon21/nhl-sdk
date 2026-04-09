"""
SKATER REALTIME REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/realtime
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterRealtimeReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    season_id: int | None
    position_code: str | None
    shoots_catches: str | None
    team_abbrevs: str | None
    time_on_ice_per_game: float | None
    blocked_shots: int | None
    blocked_shots_per60: float | None
    empty_net_assists: int | None
    empty_net_goals: int | None
    empty_net_points: int | None
    first_goals: int | None
    giveaways: int | None
    giveaways_per60: float | None
    hits: int | None
    hits_per60: float | None
    missed_shot_crossbar: int | None
    missed_shot_failed_bank_attempt: int | None
    missed_shot_goalpost: int | None
    missed_shot_over_net: int | None
    missed_shot_short: int | None
    missed_shot_wide_of_net: int | None
    missed_shots: int | None
    ot_goals: int | None
    shot_attempts_blocked: int | None
    takeaways: int | None
    takeaways_per60: float | None
    total_shot_attempts: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterRealtimeReport:
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
            blocked_shots = data.get("blockedShots"),
            blocked_shots_per60 = data.get("blockedShotsPer60"),
            empty_net_assists = data.get("emptyNetAssists"),
            empty_net_goals = data.get("emptyNetGoals"),
            empty_net_points = data.get("emptyNetPoints"),
            first_goals = data.get("firstGoals"),
            giveaways = data.get("giveaways"),
            giveaways_per60 = data.get("giveawaysPer60"),
            hits = data.get("hits"),
            hits_per60 = data.get("hitsPer60"),
            missed_shot_crossbar = data.get("missedShotCrossbar"),
            missed_shot_failed_bank_attempt = data.get("missedShotFailedBankAttempt"),
            missed_shot_goalpost = data.get("missedShotGoalpost"),
            missed_shot_over_net = data.get("missedShotOverNet"),
            missed_shot_short = data.get("missedShotShort"),
            missed_shot_wide_of_net = data.get("missedShotWideOfNet"),
            missed_shots = data.get("missedShots"),
            ot_goals = data.get("otGoals"),
            shot_attempts_blocked = data.get("shotAttemptsBlocked"),
            takeaways = data.get("takeaways"),
            takeaways_per60 = data.get("takeawaysPer60"),
            total_shot_attempts = data.get("totalShotAttempts"),
        )
