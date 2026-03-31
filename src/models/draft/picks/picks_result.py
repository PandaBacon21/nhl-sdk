"""
DRAFT PICKS MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class DraftPickEntry:
    round: int | None
    pick_in_round: int | None
    overall_pick: int | None
    team_id: int | None
    team_abbrev: str | None
    team_name: LocalizedString
    team_common_name: LocalizedString
    team_place_name_with_preposition: LocalizedString
    display_abbrev: LocalizedString
    team_logo_light: str | None
    team_logo_dark: str | None
    team_pick_history: str | None
    first_name: LocalizedString
    last_name: LocalizedString
    position_code: str | None
    country_code: str | None
    height: int | None
    weight: int | None
    amateur_league: str | None
    amateur_club_name: str | None

    @classmethod
    def from_dict(cls, data: dict) -> DraftPickEntry:
        return cls(
            round = data.get("round"),
            pick_in_round = data.get("pickInRound"),
            overall_pick = data.get("overallPick"),
            team_id = data.get("teamId"),
            team_abbrev = data.get("teamAbbrev"),
            team_name = LocalizedString(data.get("teamName")),
            team_common_name = LocalizedString(data.get("teamCommonName")),
            team_place_name_with_preposition = LocalizedString(data.get("teamPlaceNameWithPreposition")),
            display_abbrev = LocalizedString(data.get("displayAbbrev")),
            team_logo_light = data.get("teamLogoLight"),
            team_logo_dark = data.get("teamLogoDark"),
            team_pick_history = data.get("teamPickHistory"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            position_code = data.get("positionCode"),
            country_code = data.get("countryCode"),
            height = data.get("height"),
            weight = data.get("weight"),
            amateur_league = data.get("amateurLeague"),
            amateur_club_name = data.get("amateurClubName"),
        )


@dataclass(slots=True, frozen=True)
class DraftPicksResult:
    broadcast_start_time_utc: str | None
    draft_year: int | None
    draft_years: list[int]
    selectable_rounds: list[int]
    state: str | None
    picks: list[DraftPickEntry]

    @classmethod
    def from_dict(cls, data: dict) -> DraftPicksResult:
        return cls(
            broadcast_start_time_utc = data.get("broadcastStartTimeUTC"),
            draft_year = data.get("draftYear"),
            draft_years = data.get("draftYears") or [],
            selectable_rounds = data.get("selectableRounds") or [],
            state = data.get("state"),
            picks = [DraftPickEntry.from_dict(p) for p in data.get("picks") or []],
        )
