"""
DAILY SCORE MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    SchedulePeriodDescriptor,
    ScheduleGameOutcome,
)


@dataclass(slots=True, frozen=True)
class ScoreWeekDay:
    date: str | None
    day_abbrev: str | None
    number_of_games: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoreWeekDay:
        return cls(
            date = data.get("date"),
            day_abbrev = data.get("dayAbbrev"),
            number_of_games = data.get("numberOfGames"),
        )


@dataclass(slots=True, frozen=True)
class OddsPartner:
    partner_id: int | None
    country: str | None
    name: str | None
    image_url: str | None
    site_url: str | None
    bg_color: str | None
    text_color: str | None
    accent_color: str | None

    @classmethod
    def from_dict(cls, data: dict) -> OddsPartner:
        return cls(
            partner_id = data.get("partnerId"),
            country = data.get("country"),
            name = data.get("name"),
            image_url = data.get("imageUrl"),
            site_url = data.get("siteUrl"),
            bg_color = data.get("bgColor"),
            text_color = data.get("textColor"),
            accent_color = data.get("accentColor"),
        )


@dataclass(slots=True, frozen=True)
class ScoreTeam:
    id: int | None
    name: LocalizedString
    abbrev: str | None
    score: int | None
    sog: int | None
    logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoreTeam:
        return cls(
            id = data.get("id"),
            name = LocalizedString(data.get("name")),
            abbrev = data.get("abbrev"),
            score = data.get("score"),
            sog = data.get("sog"),
            logo = data.get("logo"),
        )


@dataclass(slots=True, frozen=True)
class GameClock:
    time_remaining: str | None
    seconds_remaining: int | None
    running: bool | None
    in_intermission: bool | None

    @classmethod
    def from_dict(cls, data: dict) -> GameClock:
        return cls(
            time_remaining = data.get("timeRemaining"),
            seconds_remaining = data.get("secondsRemaining"),
            running = data.get("running"),
            in_intermission = data.get("inIntermission"),
        )


@dataclass(slots=True, frozen=True)
class GoalAssist:
    player_id: int | None
    name: LocalizedString
    assists_to_date: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalAssist:
        return cls(
            player_id = data.get("playerId"),
            name = LocalizedString(data.get("name")),
            assists_to_date = data.get("assistsToDate"),
        )


@dataclass(slots=True, frozen=True)
class Goal:
    period: int | None
    period_descriptor: SchedulePeriodDescriptor | None
    time_in_period: str | None
    player_id: int | None
    name: LocalizedString
    first_name: LocalizedString
    last_name: LocalizedString
    goal_modifier: str | None
    assists: list[GoalAssist]
    mugshot: str | None
    team_abbrev: str | None
    goals_to_date: int | None
    away_score: int | None
    home_score: int | None
    strength: str | None
    highlight_clip_sharing_url: str | None
    highlight_clip_sharing_url_fr: str | None
    highlight_clip: int | None
    highlight_clip_fr: int | None
    discrete_clip: int | None
    discrete_clip_fr: int | None

    @classmethod
    def from_dict(cls, data: dict) -> Goal:
        pd = data.get("periodDescriptor")
        return cls(
            period = data.get("period"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            time_in_period = data.get("timeInPeriod"),
            player_id = data.get("playerId"),
            name = LocalizedString(data.get("name")),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            goal_modifier = data.get("goalModifier"),
            assists = [GoalAssist.from_dict(a) for a in data.get("assists") or []],
            mugshot = data.get("mugshot"),
            team_abbrev = data.get("teamAbbrev"),
            goals_to_date = data.get("goalsToDate"),
            away_score = data.get("awayScore"),
            home_score = data.get("homeScore"),
            strength = data.get("strength"),
            highlight_clip_sharing_url = data.get("highlightClipSharingUrl"),
            highlight_clip_sharing_url_fr = data.get("highlightClipSharingUrlFr"),
            highlight_clip = data.get("highlightClip"),
            highlight_clip_fr = data.get("highlightClipFr"),
            discrete_clip = data.get("discreteClip"),
            discrete_clip_fr = data.get("discreteClipFr"),
        )


@dataclass(slots=True, frozen=True)
class ScoreGame:
    id: int | None
    season: int | None
    game_type: int | None
    game_date: str | None
    venue: LocalizedString
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    game_state: str | None
    game_schedule_state: str | None
    away_team: ScoreTeam
    home_team: ScoreTeam
    game_center_link: str | None
    three_min_recap: str | None
    three_min_recap_fr: str | None
    condensed_game: str | None
    condensed_game_fr: str | None
    clock: GameClock | None
    neutral_site: bool | None
    venue_timezone: str | None
    period: int | None
    period_descriptor: SchedulePeriodDescriptor | None
    game_outcome: ScheduleGameOutcome | None
    goals: list[Goal]

    @classmethod
    def from_dict(cls, data: dict) -> ScoreGame:
        clock = data.get("clock")
        pd = data.get("periodDescriptor")
        go = data.get("gameOutcome")
        return cls(
            id = data.get("id"),
            season = data.get("season"),
            game_type = data.get("gameType"),
            game_date = data.get("gameDate"),
            venue = LocalizedString(data.get("venue")),
            start_time_utc = data.get("startTimeUTC"),
            eastern_utc_offset = data.get("easternUTCOffset"),
            venue_utc_offset = data.get("venueUTCOffset"),
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            away_team = ScoreTeam.from_dict(data.get("awayTeam") or {}),
            home_team = ScoreTeam.from_dict(data.get("homeTeam") or {}),
            game_center_link = data.get("gameCenterLink"),
            three_min_recap = data.get("threeMinRecap"),
            three_min_recap_fr = data.get("threeMinRecapFr"),
            condensed_game = data.get("condensedGame"),
            condensed_game_fr = data.get("condensedGameFr"),
            clock = GameClock.from_dict(clock) if clock else None,
            neutral_site = data.get("neutralSite"),
            venue_timezone = data.get("venueTimezone"),
            period = data.get("period"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            game_outcome = ScheduleGameOutcome.from_dict(go) if go else None,
            goals = [Goal.from_dict(g) for g in data.get("goals") or []],
        )


@dataclass(slots=True, frozen=True)
class DailyScoreResult:
    prev_date: str | None
    current_date: str | None
    next_date: str | None
    game_week: list[ScoreWeekDay]
    odds_partners: list[OddsPartner]
    games: list[ScoreGame]

    @classmethod
    def from_dict(cls, data: dict) -> DailyScoreResult:
        return cls(
            prev_date = data.get("prevDate"),
            current_date = data.get("currentDate"),
            next_date = data.get("nextDate"),
            game_week = [ScoreWeekDay.from_dict(d) for d in data.get("gameWeek") or []],
            odds_partners = [OddsPartner.from_dict(p) for p in data.get("oddsPartners") or []],
            games = [ScoreGame.from_dict(g) for g in data.get("games") or []],
        )
