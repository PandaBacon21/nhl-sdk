"""
LEAGUE SCHEDULE CALENDAR MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class CalendarTeam:
    id: int | None
    season_id: int | None
    common_name: LocalizedString
    abbrev: str | None
    name: LocalizedString
    place_name_with_preposition: LocalizedString
    place_name: LocalizedString
    logo: str | None
    dark_logo: str | None
    french: bool | None

    @classmethod
    def from_dict(cls, data: dict) -> CalendarTeam:
        return cls(
            id = data.get("id"),
            season_id = data.get("seasonId"),
            common_name = LocalizedString(data.get("commonName")),
            abbrev = data.get("abbrev"),
            name = LocalizedString(data.get("name")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            place_name = LocalizedString(data.get("placeName")),
            logo = data.get("logo"),
            dark_logo = data.get("darkLogo"),
            french = data.get("french"),
        )


@dataclass(slots=True, frozen=True)
class LeagueCalendarResult:
    start_date: str | None
    end_date: str | None
    next_start_date: str | None
    previous_start_date: str | None
    teams: list[CalendarTeam]

    @classmethod
    def from_dict(cls, data: dict) -> LeagueCalendarResult:
        return cls(
            start_date = data.get("startDate"),
            end_date = data.get("endDate"),
            next_start_date = data.get("nextStartDate"),
            previous_start_date = data.get("previousStartDate"),
            teams = [CalendarTeam.from_dict(t) for t in data.get("teams") or []],
        )
