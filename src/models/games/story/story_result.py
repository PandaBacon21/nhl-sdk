"""
GAME STORY MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    SchedulePeriodDescriptor,
)
from ..scores.daily_score import GameClock
from ..landing.landing_result import ScoringPeriod


@dataclass(slots=True, frozen=True)
class StoryTeam:
    id: int | None
    name: LocalizedString
    abbrev: str | None
    place_name: LocalizedString
    score: int | None
    sog: int | None
    logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> StoryTeam:
        return cls(
            id = data.get("id"),
            name = LocalizedString(data.get("name")),
            abbrev = data.get("abbrev"),
            place_name = LocalizedString(data.get("placeName")),
            score = data.get("score"),
            sog = data.get("sog"),
            logo = data.get("logo"),
        )


@dataclass(slots=True, frozen=True)
class StoryThreeStar:
    star: int | None
    player_id: int | None
    team_abbrev: str | None
    headshot: str | None
    name: str | None
    sweater_no: int | None
    position: str | None
    goals: int | None
    assists: int | None
    points: int | None

    @classmethod
    def from_dict(cls, data: dict) -> StoryThreeStar:
        return cls(
            star = data.get("star"),
            player_id = data.get("playerId"),
            team_abbrev = data.get("teamAbbrev"),
            headshot = data.get("headshot"),
            name = data.get("name"),
            sweater_no = data.get("sweaterNo"),
            position = data.get("position"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
        )


@dataclass(slots=True, frozen=True)
class TeamGameStat:
    category: str | None
    away_value: str | int | float | None
    home_value: str | int | float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamGameStat:
        return cls(
            category = data.get("category"),
            away_value = data.get("awayValue"),
            home_value = data.get("homeValue"),
        )


@dataclass(slots=True, frozen=True)
class GameStorySummary:
    scoring: list[ScoringPeriod]
    three_stars: list[StoryThreeStar]
    team_game_stats: list[TeamGameStat]

    @classmethod
    def from_dict(cls, data: dict) -> GameStorySummary:
        return cls(
            scoring = [ScoringPeriod.from_dict(s) for s in data.get("scoring") or []],
            three_stars = [StoryThreeStar.from_dict(s) for s in data.get("threeStars") or []],
            team_game_stats = [TeamGameStat.from_dict(t) for t in data.get("teamGameStats") or []],
        )


@dataclass(slots=True, frozen=True)
class GameStoryResult:
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
    tv_broadcasts: list[ScheduleTvBroadcast]
    game_state: str | None
    game_schedule_state: str | None
    away_team: StoryTeam
    home_team: StoryTeam
    shootout_in_use: bool | None
    max_periods: int | None
    reg_periods: int | None
    ot_in_use: bool | None
    ties_in_use: bool | None
    summary: GameStorySummary | None
    period_descriptor: SchedulePeriodDescriptor | None
    clock: GameClock | None

    @classmethod
    def from_dict(cls, data: dict) -> GameStoryResult:
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
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            away_team = StoryTeam.from_dict(data.get("awayTeam") or {}),
            home_team = StoryTeam.from_dict(data.get("homeTeam") or {}),
            shootout_in_use = data.get("shootoutInUse"),
            max_periods = data.get("maxPeriods"),
            reg_periods = data.get("regPeriods"),
            ot_in_use = data.get("otInUse"),
            ties_in_use = data.get("tiesInUse"),
            summary = GameStorySummary.from_dict(summary) if summary is not None else None,
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            clock = GameClock.from_dict(clock) if clock else None,
        )
