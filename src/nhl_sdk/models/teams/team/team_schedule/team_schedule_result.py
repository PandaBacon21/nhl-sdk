"""
TEAM SCHEDULE MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class ScheduleTvBroadcast:
    id: int | None
    market: str | None
    country_code: str | None
    network: str | None
    sequence_number: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ScheduleTvBroadcast:
        return cls(
            id = data.get("id"),
            market = data.get("market"),
            country_code = data.get("countryCode"),
            network = data.get("network"),
            sequence_number = data.get("sequenceNumber"),
        )


@dataclass(slots=True, frozen=True)
class ScheduleTeam:
    id: int | None
    common_name: LocalizedString
    place_name: LocalizedString
    place_name_with_preposition: LocalizedString
    abbrev: str | None
    logo: str | None
    dark_logo: str | None
    away_split_squad: bool | None
    home_split_squad: bool | None
    score: int | None
    radio_link: str | None

    @classmethod
    def from_dict(cls, data: dict) -> ScheduleTeam:
        return cls(
            id = data.get("id"),
            common_name = LocalizedString(data.get("commonName")),
            place_name = LocalizedString(data.get("placeName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            abbrev = data.get("abbrev"),
            logo = data.get("logo"),
            dark_logo = data.get("darkLogo"),
            away_split_squad = data.get("awaySplitSquad"),
            home_split_squad = data.get("homeSplitSquad"),
            score = data.get("score"),
            radio_link = data.get("radioLink"),
        )


@dataclass(slots=True, frozen=True)
class SchedulePeriodDescriptor:
    number: int | None
    period_type: str | None
    max_regulation_periods: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SchedulePeriodDescriptor:
        return cls(
            number = data.get("number"),
            period_type = data.get("periodType"),
            max_regulation_periods = data.get("maxRegulationPeriods"),
        )


@dataclass(slots=True, frozen=True)
class ScheduleGameOutcome:
    last_period_type: str | None

    @classmethod
    def from_dict(cls, data: dict) -> ScheduleGameOutcome:
        return cls(
            last_period_type = data.get("lastPeriodType"),
        )


@dataclass(slots=True, frozen=True)
class ScheduleGoalPlayer:
    """Shared shape for winningGoalie and winningGoalScorer."""
    player_id: int | None
    first_initial: LocalizedString
    last_name: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> ScheduleGoalPlayer:
        return cls(
            player_id = data.get("playerId"),
            first_initial = LocalizedString(data.get("firstInitial")),
            last_name = LocalizedString(data.get("lastName")),
        )


@dataclass(slots=True, frozen=True)
class ScheduleGame:
    id: int | None
    season: int | None
    game_type: int | None
    game_date: str | None
    venue: LocalizedString
    neutral_site: bool | None
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    venue_timezone: str | None
    game_state: str | None
    game_schedule_state: str | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    away_team: ScheduleTeam
    home_team: ScheduleTeam
    period_descriptor: SchedulePeriodDescriptor | None
    game_outcome: ScheduleGameOutcome | None
    winning_goalie: ScheduleGoalPlayer | None
    winning_goal_scorer: ScheduleGoalPlayer | None
    tickets_link: str | None
    tickets_link_fr: str | None
    three_min_recap: str | None
    three_min_recap_fr: str | None
    condensed_game: str | None
    condensed_game_fr: str | None
    game_center_link: str | None

    @classmethod
    def from_dict(cls, data: dict) -> ScheduleGame:
        pd = data.get("periodDescriptor")
        go = data.get("gameOutcome")
        wg = data.get("winningGoalie")
        wgs = data.get("winningGoalScorer")
        return cls(
            id = data.get("id"),
            season = data.get("season"),
            game_type = data.get("gameType"),
            game_date = data.get("gameDate"),
            venue = LocalizedString(data.get("venue")),
            neutral_site = data.get("neutralSite"),
            start_time_utc = data.get("startTimeUTC"),
            eastern_utc_offset = data.get("easternUTCOffset"),
            venue_utc_offset = data.get("venueUTCOffset"),
            venue_timezone = data.get("venueTimezone"),
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            away_team = ScheduleTeam.from_dict(data.get("awayTeam") or {}),
            home_team = ScheduleTeam.from_dict(data.get("homeTeam") or {}),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            game_outcome = ScheduleGameOutcome.from_dict(go) if go else None,
            winning_goalie = ScheduleGoalPlayer.from_dict(wg) if wg else None,
            winning_goal_scorer = ScheduleGoalPlayer.from_dict(wgs) if wgs else None,
            tickets_link = data.get("ticketsLink"),
            tickets_link_fr = data.get("ticketsLinkFr"),
            three_min_recap = data.get("threeMinRecap"),
            three_min_recap_fr = data.get("threeMinRecapFr"),
            condensed_game = data.get("condensedGame"),
            condensed_game_fr = data.get("condensedGameFr"),
            game_center_link = data.get("gameCenterLink"),
        )


@dataclass(slots=True, frozen=True)
class TeamWeekScheduleResult:
    previous_start_date: str | None
    next_start_date: str | None
    calendar_url: str | None
    club_timezone: str | None
    club_utc_offset: str | None
    games: list[ScheduleGame]

    @classmethod
    def from_dict(cls, data: dict) -> TeamWeekScheduleResult:
        return cls(
            previous_start_date = data.get("previousStartDate"),
            next_start_date = data.get("nextStartDate"),
            calendar_url = data.get("calendarUrl"),
            club_timezone = data.get("clubTimezone"),
            club_utc_offset = data.get("clubUTCOffset"),
            games = [ScheduleGame.from_dict(g) for g in data.get("games") or []],
        )


@dataclass(slots=True, frozen=True)
class TeamMonthScheduleResult:
    previous_month: str | None
    current_month: str | None
    next_month: str | None
    calendar_url: str | None
    club_timezone: str | None
    club_utc_offset: str | None
    games: list[ScheduleGame]

    @classmethod
    def from_dict(cls, data: dict) -> TeamMonthScheduleResult:
        return cls(
            previous_month = data.get("previousMonth"),
            current_month = data.get("currentMonth"),
            next_month = data.get("nextMonth"),
            calendar_url = data.get("calendarUrl"),
            club_timezone = data.get("clubTimezone"),
            club_utc_offset = data.get("clubUTCOffset"),
            games = [ScheduleGame.from_dict(g) for g in data.get("games") or []],
        )


@dataclass(slots=True, frozen=True)
class TeamScheduleResult:
    previous_season: int | None
    current_season: int | None
    next_season: int | None
    club_timezone: str | None
    club_utc_offset: str | None
    games: list[ScheduleGame]

    @classmethod
    def from_dict(cls, data: dict) -> TeamScheduleResult:
        return cls(
            previous_season = data.get("previousSeason"),
            current_season = data.get("currentSeason"),
            next_season = data.get("nextSeason"),
            club_timezone = data.get("clubTimezone"),
            club_utc_offset = data.get("clubUTCOffset"),
            games = [ScheduleGame.from_dict(g) for g in data.get("games") or []],
        )
