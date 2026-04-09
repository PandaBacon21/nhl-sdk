"""
GAME LANDING MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    SchedulePeriodDescriptor,
)
from ..scores.daily_score import GameClock
from ..pbp.pbp_result import PbpTeam


@dataclass(slots=True, frozen=True)
class GoalAssist:
    player_id: int | None
    first_name: LocalizedString
    last_name: LocalizedString
    name: LocalizedString
    assists_to_date: int | None
    sweater_number: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalAssist:
        return cls(
            player_id = data.get("playerId"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            name = LocalizedString(data.get("name")),
            assists_to_date = data.get("assistsToDate"),
            sweater_number = data.get("sweaterNumber"),
        )


@dataclass(slots=True, frozen=True)
class ScoringGoal:
    situation_code: str | None
    event_id: int | None
    strength: str | None
    player_id: int | None
    first_name: LocalizedString
    last_name: LocalizedString
    name: LocalizedString
    team_abbrev: LocalizedString
    headshot: str | None
    highlight_clip_sharing_url: str | None
    highlight_clip_sharing_url_fr: str | None
    highlight_clip: int | None
    highlight_clip_fr: int | None
    discrete_clip: int | None
    discrete_clip_fr: int | None
    goals_to_date: int | None
    away_score: int | None
    home_score: int | None
    leading_team_abbrev: LocalizedString
    time_in_period: str | None
    shot_type: str | None
    goal_modifier: str | None
    assists: list[GoalAssist]
    ppt_replay_url: str | None
    home_team_defending_side: str | None
    is_home: bool | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoringGoal:
        return cls(
            situation_code = data.get("situationCode"),
            event_id = data.get("eventId"),
            strength = data.get("strength"),
            player_id = data.get("playerId"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            name = LocalizedString(data.get("name")),
            team_abbrev = LocalizedString(data.get("teamAbbrev")),
            headshot = data.get("headshot"),
            highlight_clip_sharing_url = data.get("highlightClipSharingUrl"),
            highlight_clip_sharing_url_fr = data.get("highlightClipSharingUrlFr"),
            highlight_clip = data.get("highlightClip"),
            highlight_clip_fr = data.get("highlightClipFr"),
            discrete_clip = data.get("discreteClip"),
            discrete_clip_fr = data.get("discreteClipFr"),
            goals_to_date = data.get("goalsToDate"),
            away_score = data.get("awayScore"),
            home_score = data.get("homeScore"),
            leading_team_abbrev = LocalizedString(data.get("leadingTeamAbbrev")),
            time_in_period = data.get("timeInPeriod"),
            shot_type = data.get("shotType"),
            goal_modifier = data.get("goalModifier"),
            assists = [GoalAssist.from_dict(a) for a in data.get("assists") or []],
            ppt_replay_url = data.get("pptReplayUrl"),
            home_team_defending_side = data.get("homeTeamDefendingSide"),
            is_home = data.get("isHome"),
        )


@dataclass(slots=True, frozen=True)
class ScoringPeriod:
    period_descriptor: SchedulePeriodDescriptor | None
    goals: list[ScoringGoal]

    @classmethod
    def from_dict(cls, data: dict) -> ScoringPeriod:
        pd = data.get("periodDescriptor")
        return cls(
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            goals = [ScoringGoal.from_dict(g) for g in data.get("goals") or []],
        )


@dataclass(slots=True, frozen=True)
class ThreeStar:
    star: int | None
    player_id: int | None
    team_abbrev: str | None
    headshot: str | None
    name: LocalizedString
    sweater_no: int | None
    position: str | None
    goals: int | None
    assists: int | None
    points: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ThreeStar:
        return cls(
            star = data.get("star"),
            player_id = data.get("playerId"),
            team_abbrev = data.get("teamAbbrev"),
            headshot = data.get("headshot"),
            name = LocalizedString(data.get("name")),
            sweater_no = data.get("sweaterNo"),
            position = data.get("position"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
        )


@dataclass(slots=True, frozen=True)
class PenaltyPlayer:
    first_name: LocalizedString
    last_name: LocalizedString
    sweater_number: int | None

    @classmethod
    def from_dict(cls, data: dict) -> PenaltyPlayer:
        return cls(
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            sweater_number = data.get("sweaterNumber"),
        )


@dataclass(slots=True, frozen=True)
class LandingPenalty:
    time_in_period: str | None
    type: str | None
    duration: int | None
    committed_by_player: PenaltyPlayer | None
    team_abbrev: LocalizedString
    drawn_by: PenaltyPlayer | None
    desc_key: str | None
    served_by: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> LandingPenalty:
        cbp = data.get("committedByPlayer")
        db = data.get("drawnBy")
        return cls(
            time_in_period = data.get("timeInPeriod"),
            type = data.get("type"),
            duration = data.get("duration"),
            committed_by_player = PenaltyPlayer.from_dict(cbp) if cbp else None,
            team_abbrev = LocalizedString(data.get("teamAbbrev")),
            drawn_by = PenaltyPlayer.from_dict(db) if db else None,
            desc_key = data.get("descKey"),
            served_by = LocalizedString(data.get("servedBy")),
        )


@dataclass(slots=True, frozen=True)
class PenaltyPeriod:
    period_descriptor: SchedulePeriodDescriptor | None
    penalties: list[LandingPenalty]

    @classmethod
    def from_dict(cls, data: dict) -> PenaltyPeriod:
        pd = data.get("periodDescriptor")
        return cls(
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            penalties = [LandingPenalty.from_dict(p) for p in data.get("penalties") or []],
        )


@dataclass(slots=True, frozen=True)
class GameSummary:
    scoring: list[ScoringPeriod]
    three_stars: list[ThreeStar]
    penalties: list[PenaltyPeriod]

    @classmethod
    def from_dict(cls, data: dict) -> GameSummary:
        return cls(
            scoring = [ScoringPeriod.from_dict(s) for s in data.get("scoring") or []],
            three_stars = [ThreeStar.from_dict(s) for s in data.get("threeStars") or []],
            penalties = [PenaltyPeriod.from_dict(p) for p in data.get("penalties") or []],
        )


@dataclass(slots=True, frozen=True)
class GameLandingResult:
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
    venue_timezone: str | None
    period_descriptor: SchedulePeriodDescriptor | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    game_state: str | None
    game_schedule_state: str | None
    away_team: PbpTeam
    home_team: PbpTeam
    shootout_in_use: bool | None
    max_periods: int | None
    reg_periods: int | None
    ot_in_use: bool | None
    ties_in_use: bool | None
    summary: GameSummary | None
    clock: GameClock | None

    @classmethod
    def from_dict(cls, data: dict) -> GameLandingResult:
        pd = data.get("periodDescriptor")
        clock = data.get("clock")
        summary = data.get("summary")
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
            venue_timezone = data.get("venueTimezone"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            away_team = PbpTeam.from_dict(data.get("awayTeam") or {}),
            home_team = PbpTeam.from_dict(data.get("homeTeam") or {}),
            shootout_in_use = data.get("shootoutInUse"),
            max_periods = data.get("maxPeriods"),
            reg_periods = data.get("regPeriods"),
            ot_in_use = data.get("otInUse"),
            ties_in_use = data.get("tiesInUse"),
            summary = GameSummary.from_dict(summary) if summary else None,
            clock = GameClock.from_dict(clock) if clock else None,
        )
