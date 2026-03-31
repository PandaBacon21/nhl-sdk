"""
GAME BOXSCORE MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    SchedulePeriodDescriptor,
    ScheduleGameOutcome,
)
from ..scores.daily_score import GameClock
from ..pbp.pbp_result import PbpTeam


@dataclass(slots=True, frozen=True)
class BoxscoreSkater:
    player_id: int | None
    sweater_number: int | None
    name: LocalizedString
    position: str | None
    goals: int | None
    assists: int | None
    points: int | None
    plus_minus: int | None
    pim: int | None
    hits: int | None
    power_play_goals: int | None
    sog: int | None
    faceoff_winning_pctg: float | None
    toi: str | None
    blocked_shots: int | None
    shifts: int | None
    giveaways: int | None
    takeaways: int | None

    @classmethod
    def from_dict(cls, data: dict) -> BoxscoreSkater:
        return cls(
            player_id = data.get("playerId"),
            sweater_number = data.get("sweaterNumber"),
            name = LocalizedString(data.get("name")),
            position = data.get("position"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
            plus_minus = data.get("plusMinus"),
            pim = data.get("pim"),
            hits = data.get("hits"),
            power_play_goals = data.get("powerPlayGoals"),
            sog = data.get("sog"),
            faceoff_winning_pctg = data.get("faceoffWinningPctg"),
            toi = data.get("toi"),
            blocked_shots = data.get("blockedShots"),
            shifts = data.get("shifts"),
            giveaways = data.get("giveaways"),
            takeaways = data.get("takeaways"),
        )


@dataclass(slots=True, frozen=True)
class BoxscoreGoalie:
    player_id: int | None
    sweater_number: int | None
    name: LocalizedString
    position: str | None
    even_strength_shots_against: str | None
    power_play_shots_against: str | None
    shorthanded_shots_against: str | None
    save_shots_against: str | None
    save_pctg: float | None
    even_strength_goals_against: int | None
    power_play_goals_against: int | None
    shorthanded_goals_against: int | None
    pim: int | None
    goals_against: int | None
    toi: str | None
    starter: bool | None
    decision: str | None
    shots_against: int | None
    saves: int | None

    @classmethod
    def from_dict(cls, data: dict) -> BoxscoreGoalie:
        return cls(
            player_id = data.get("playerId"),
            sweater_number = data.get("sweaterNumber"),
            name = LocalizedString(data.get("name")),
            position = data.get("position"),
            even_strength_shots_against = data.get("evenStrengthShotsAgainst"),
            power_play_shots_against = data.get("powerPlayShotsAgainst"),
            shorthanded_shots_against = data.get("shorthandedShotsAgainst"),
            save_shots_against = data.get("saveShotsAgainst"),
            save_pctg = data.get("savePctg"),
            even_strength_goals_against = data.get("evenStrengthGoalsAgainst"),
            power_play_goals_against = data.get("powerPlayGoalsAgainst"),
            shorthanded_goals_against = data.get("shorthandedGoalsAgainst"),
            pim = data.get("pim"),
            goals_against = data.get("goalsAgainst"),
            toi = data.get("toi"),
            starter = data.get("starter"),
            decision = data.get("decision"),
            shots_against = data.get("shotsAgainst"),
            saves = data.get("saves"),
        )


@dataclass(slots=True, frozen=True)
class BoxscoreTeam:
    forwards: list[BoxscoreSkater]
    defense: list[BoxscoreSkater]
    goalies: list[BoxscoreGoalie]

    @classmethod
    def from_dict(cls, data: dict) -> BoxscoreTeam:
        return cls(
            forwards = [BoxscoreSkater.from_dict(p) for p in data.get("forwards") or []],
            defense = [BoxscoreSkater.from_dict(p) for p in data.get("defense") or []],
            goalies = [BoxscoreGoalie.from_dict(g) for g in data.get("goalies") or []],
        )


@dataclass(slots=True, frozen=True)
class PlayerByGameStats:
    away_team: BoxscoreTeam
    home_team: BoxscoreTeam

    @classmethod
    def from_dict(cls, data: dict) -> PlayerByGameStats:
        return cls(
            away_team = BoxscoreTeam.from_dict(data.get("awayTeam") or {}),
            home_team = BoxscoreTeam.from_dict(data.get("homeTeam") or {}),
        )


@dataclass(slots=True, frozen=True)
class GameBoxscoreResult:
    id: int | None
    season: int | None
    game_type: int | None
    limited_scoring: bool | None
    game_date: str | None
    venue: LocalizedString
    venue_location: LocalizedString
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    game_state: str | None
    game_schedule_state: str | None
    period_descriptor: SchedulePeriodDescriptor | None
    reg_periods: int | None
    away_team: PbpTeam
    home_team: PbpTeam
    clock: GameClock | None
    player_by_game_stats: PlayerByGameStats | None
    game_outcome: ScheduleGameOutcome | None

    @classmethod
    def from_dict(cls, data: dict) -> GameBoxscoreResult:
        pd = data.get("periodDescriptor")
        clock = data.get("clock")
        pbgs = data.get("playerByGameStats")
        go = data.get("gameOutcome")
        return cls(
            id = data.get("id"),
            season = data.get("season"),
            game_type = data.get("gameType"),
            limited_scoring = data.get("limitedScoring"),
            game_date = data.get("gameDate"),
            venue = LocalizedString(data.get("venue")),
            venue_location = LocalizedString(data.get("venueLocation")),
            start_time_utc = data.get("startTimeUTC"),
            eastern_utc_offset = data.get("easternUTCOffset"),
            venue_utc_offset = data.get("venueUTCOffset"),
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            reg_periods = data.get("regPeriods"),
            away_team = PbpTeam.from_dict(data.get("awayTeam") or {}),
            home_team = PbpTeam.from_dict(data.get("homeTeam") or {}),
            clock = GameClock.from_dict(clock) if clock else None,
            player_by_game_stats = PlayerByGameStats.from_dict(pbgs) if pbgs else None,
            game_outcome = ScheduleGameOutcome.from_dict(go) if go else None,
        )
