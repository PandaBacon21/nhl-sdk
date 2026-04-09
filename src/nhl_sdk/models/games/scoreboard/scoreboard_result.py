"""
SCOREBOARD MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    SchedulePeriodDescriptor,
)


@dataclass(slots=True, frozen=True)
class ScoreboardTeam:
    id: int | None
    name: LocalizedString
    common_name: LocalizedString
    place_name_with_preposition: LocalizedString
    abbrev: str | None
    score: int | None
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
            logo = data.get("logo"),
        )


@dataclass(slots=True, frozen=True)
class ScoreboardGame:
    id: int | None
    season: int | None
    game_type: int | None
    game_date: str | None
    game_center_link: str | None
    venue: LocalizedString
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    game_state: str | None
    game_schedule_state: str | None
    away_team: ScoreboardTeam
    home_team: ScoreboardTeam
    tickets_link: str | None
    tickets_link_fr: str | None
    period: int | None
    period_descriptor: SchedulePeriodDescriptor | None
    three_min_recap: str | None
    three_min_recap_fr: str | None

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardGame:
        pd = data.get("periodDescriptor")
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
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            away_team = ScoreboardTeam.from_dict(data.get("awayTeam") or {}),
            home_team = ScoreboardTeam.from_dict(data.get("homeTeam") or {}),
            tickets_link = data.get("ticketsLink"),
            tickets_link_fr = data.get("ticketsLinkFr"),
            period = data.get("period"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            three_min_recap = data.get("threeMinRecap"),
            three_min_recap_fr = data.get("threeMinRecapFr"),
        )


@dataclass(slots=True, frozen=True)
class ScoreboardDate:
    date: str | None
    games: list[ScoreboardGame]

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardDate:
        return cls(
            date = data.get("date"),
            games = [ScoreboardGame.from_dict(g) for g in data.get("games") or []],
        )


@dataclass(slots=True, frozen=True)
class ScoreboardResult:
    focused_date: str | None
    focused_date_count: int | None
    games_by_date: list[ScoreboardDate]

    @classmethod
    def from_dict(cls, data: dict) -> ScoreboardResult:
        return cls(
            focused_date = data.get("focusedDate"),
            focused_date_count = data.get("focusedDateCount"),
            games_by_date = [ScoreboardDate.from_dict(d) for d in data.get("gamesByDate") or []],
        )
