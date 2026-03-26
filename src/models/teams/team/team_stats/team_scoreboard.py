"""
TEAM SCOREBOARD MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class ScoreboardTvBroadcast:
    """A single TV broadcast entry for a scoreboard game."""
    id: int | None
    market: str | None
    country_code: str | None
    network: str | None
    sequence_number: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardTvBroadcast:
        return cls(
            id = data.get("id"),
            market = data.get("market"),
            country_code = data.get("countryCode"),
            network = data.get("network"),
            sequence_number = data.get("sequenceNumber"),
        )


@dataclass(slots=True, frozen=True)
class ScoreboardTeam:
    """A team entry within a scoreboard game."""
    id: int | None
    name: LocalizedString
    common_name: LocalizedString
    place_name_with_preposition: LocalizedString
    abbrev: str | None
    score: int | None
    record: str | None
    logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardTeam:
        return cls(
            id = data.get("id"),
            name = LocalizedString(data.get("name")),
            common_name = LocalizedString(data.get("commonName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            abbrev = data.get("abbrev"),
            score = data.get("score"),
            record = data.get("record"),
            logo = data.get("logo"),
        )


@dataclass(slots=True, frozen=True)
class ScoreboardPeriodDescriptor:
    """Period info for a completed or in-progress scoreboard game."""
    number: int | None
    period_type: str | None
    max_regulation_periods: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardPeriodDescriptor:
        return cls(
            number = data.get("number"),
            period_type = data.get("periodType"),
            max_regulation_periods = data.get("maxRegulationPeriods"),
        )


@dataclass(slots=True, frozen=True)
class ScoreboardGame:
    """A single game entry in the team scoreboard."""
    id: int | None
    season: int | None
    game_type: int | None
    game_date: str | None
    game_center_link: str | None
    venue: LocalizedString
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    tv_broadcasts: list[ScoreboardTvBroadcast]
    game_state: str | None
    game_schedule_state: str | None
    away_team: ScoreboardTeam
    home_team: ScoreboardTeam
    tickets_link: str | None
    tickets_link_fr: str | None
    period: int | None
    period_descriptor: ScoreboardPeriodDescriptor | None
    three_min_recap_fr: str | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardGame:
        pd_data = data.get("periodDescriptor")
        return cls(
            id = data.get("id"),
            season = data.get("season"),
            game_type = data.get("gameType"),
            game_date = data.get("gameDate"),
            game_center_link = data.get("gameCenterLink"),
            venue = LocalizedString(data.get("venue")),
            start_time_utc = data.get("startTimeUTC"),
            eastern_utc_offset = data.get("easternUTCOffset"),
            venue_utc_offset = data.get("venueUTCOffset"),
            tv_broadcasts = [ScoreboardTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            away_team = ScoreboardTeam.from_dict(data.get("awayTeam") or {}),
            home_team = ScoreboardTeam.from_dict(data.get("homeTeam") or {}),
            tickets_link = data.get("ticketsLink"),
            tickets_link_fr = data.get("ticketsLinkFr"),
            period = data.get("period"),
            period_descriptor = ScoreboardPeriodDescriptor.from_dict(pd_data) if pd_data else None,
            three_min_recap_fr = data.get("threeMinRecapFr"),
        )


@dataclass(slots=True, frozen=True)
class ScoreboardGamesByDate:
    """Games grouped by a single date."""
    date: str | None
    games: list[ScoreboardGame]

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardGamesByDate:
        return cls(
            date = data.get("date"),
            games = [ScoreboardGame.from_dict(g) for g in data.get("games") or []],
        )


@dataclass(slots=True, frozen=True)
class TeamScoreboard:
    """Top-level response from the scoreboard endpoint."""
    focused_date: str | None
    focused_date_count: int | None
    club_time_zone: str | None
    club_utc_offset: str | None
    club_schedule_link: str | None
    games_by_date: list[ScoreboardGamesByDate]

    @classmethod
    def from_dict(cls, data: dict) -> TeamScoreboard:
        return cls(
            focused_date = data.get("focusedDate"),
            focused_date_count = data.get("focusedDateCount"),
            club_time_zone = data.get("clubTimeZone"),
            club_utc_offset = data.get("clubUTCOffset"),
            club_schedule_link = data.get("clubScheduleLink"),
            games_by_date = [ScoreboardGamesByDate.from_dict(d) for d in data.get("gamesByDate") or []],
        )
