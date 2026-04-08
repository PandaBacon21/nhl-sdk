"""
PLAYOFF SERIES SCHEDULE MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    SchedulePeriodDescriptor,
)


@dataclass(slots=True, frozen=True)
class SeriesConference:
    name: str | None
    abbrev: str | None

    @classmethod
    def from_dict(cls, data: dict) -> SeriesConference:
        return cls(
            name = data.get("name"),
            abbrev = data.get("abbrev"),
        )


@dataclass(slots=True, frozen=True)
class SeriesScheduleSeriesTeam:
    id: int | None
    name: LocalizedString
    abbrev: str | None
    place_name: LocalizedString
    place_name_with_preposition: LocalizedString
    conference: SeriesConference
    record: str | None
    series_wins: int | None
    division_abbrev: str | None
    seed: int | None
    logo: str | None
    dark_logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> SeriesScheduleSeriesTeam:
        return cls(
            id = data.get("id"),
            name = LocalizedString(data.get("name")),
            abbrev = data.get("abbrev"),
            place_name = LocalizedString(data.get("placeName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            conference = SeriesConference.from_dict(data.get("conference") or {}),
            record = data.get("record"),
            series_wins = data.get("seriesWins"),
            division_abbrev = data.get("divisionAbbrev"),
            seed = data.get("seed"),
            logo = data.get("logo"),
            dark_logo = data.get("darkLogo"),
        )


@dataclass(slots=True, frozen=True)
class SeriesScheduleGameTeam:
    id: int | None
    common_name: LocalizedString
    place_name: LocalizedString
    place_name_with_preposition: LocalizedString
    abbrev: str | None
    score: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SeriesScheduleGameTeam:
        return cls(
            id = data.get("id"),
            common_name = LocalizedString(data.get("commonName")),
            place_name = LocalizedString(data.get("placeName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            abbrev = data.get("abbrev"),
            score = data.get("score"),
        )


@dataclass(slots=True, frozen=True)
class SeriesStatus:
    top_seed_wins: int | None
    bottom_seed_wins: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SeriesStatus:
        return cls(
            top_seed_wins = data.get("topSeedWins"),
            bottom_seed_wins = data.get("bottomSeedWins"),
        )


@dataclass(slots=True, frozen=True)
class SeriesGameOutcome:
    last_period_type: str | None
    ot_periods: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SeriesGameOutcome:
        return cls(
            last_period_type = data.get("lastPeriodType"),
            ot_periods = data.get("otPeriods"),
        )


@dataclass(slots=True, frozen=True)
class SeriesScheduleGame:
    id: int | None
    season: int | None
    game_type: int | None
    game_number: int | None
    if_necessary: bool | None
    venue: LocalizedString
    neutral_site: bool | None
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    venue_timezone: str | None
    game_state: str | None
    game_schedule_state: str | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    away_team: SeriesScheduleGameTeam
    home_team: SeriesScheduleGameTeam
    game_center_link: str | None
    period_descriptor: SchedulePeriodDescriptor | None
    series_status: SeriesStatus
    game_outcome: SeriesGameOutcome | None

    @classmethod
    def from_dict(cls, data: dict) -> SeriesScheduleGame:
        pd = data.get("periodDescriptor")
        go = data.get("gameOutcome")
        return cls(
            id = data.get("id"),
            season = data.get("season"),
            game_type = data.get("gameType"),
            game_number = data.get("gameNumber"),
            if_necessary = data.get("ifNecessary"),
            venue = LocalizedString(data.get("venue")),
            neutral_site = data.get("neutralSite"),
            start_time_utc = data.get("startTimeUTC"),
            eastern_utc_offset = data.get("easternUTCOffset"),
            venue_utc_offset = data.get("venueUTCOffset"),
            venue_timezone = data.get("venueTimezone"),
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            away_team = SeriesScheduleGameTeam.from_dict(data.get("awayTeam") or {}),
            home_team = SeriesScheduleGameTeam.from_dict(data.get("homeTeam") or {}),
            game_center_link = data.get("gameCenterLink"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            series_status = SeriesStatus.from_dict(data.get("seriesStatus") or {}),
            game_outcome = SeriesGameOutcome.from_dict(go) if go else None,
        )


@dataclass(slots=True, frozen=True)
class SeriesScheduleResult:
    round: int | None
    round_abbrev: str | None
    round_label: str | None
    series_letter: str | None
    series_logo: str | None
    series_logo_fr: str | None
    needed_to_win: int | None
    length: int | None
    bottom_seed_team: SeriesScheduleSeriesTeam
    top_seed_team: SeriesScheduleSeriesTeam
    games: list[SeriesScheduleGame]
    full_coverage_url: dict[str, str]

    @classmethod
    def from_dict(cls, data: dict) -> SeriesScheduleResult:
        return cls(
            round = data.get("round"),
            round_abbrev = data.get("roundAbbrev"),
            round_label = data.get("roundLabel"),
            series_letter = data.get("seriesLetter"),
            series_logo = data.get("seriesLogo"),
            series_logo_fr = data.get("seriesLogoFr"),
            needed_to_win = data.get("neededToWin"),
            length = data.get("length"),
            bottom_seed_team = SeriesScheduleSeriesTeam.from_dict(data.get("bottomSeedTeam") or {}),
            top_seed_team = SeriesScheduleSeriesTeam.from_dict(data.get("topSeedTeam") or {}),
            games = [SeriesScheduleGame.from_dict(g) for g in data.get("games") or []],
            full_coverage_url = data.get("fullCoverageUrl") or {},
        )
