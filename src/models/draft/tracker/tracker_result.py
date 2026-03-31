"""
DRAFT TRACKER MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import ScheduleTvBroadcast


@dataclass(slots=True, frozen=True)
class DraftPick:
    pick_in_round: int | None
    overall_pick: int | None
    team_id: int | None
    team_abbrev: str | None
    team_full_name: LocalizedString
    team_common_name: LocalizedString
    team_place_name_with_preposition: LocalizedString
    team_logo_light: str | None
    team_logo_dark: str | None
    state: str | None
    last_name: LocalizedString
    first_name: LocalizedString
    position_code: str | None

    @classmethod
    def from_dict(cls, data: dict) -> DraftPick:
        return cls(
            pick_in_round = data.get("pickInRound"),
            overall_pick = data.get("overallPick"),
            team_id = data.get("teamId"),
            team_abbrev = data.get("teamAbbrev"),
            team_full_name = LocalizedString(data.get("teamFullName")),
            team_common_name = LocalizedString(data.get("teamCommonName")),
            team_place_name_with_preposition = LocalizedString(data.get("teamPlaceNameWithPreposition")),
            team_logo_light = data.get("teamLogoLight"),
            team_logo_dark = data.get("teamLogoDark"),
            state = data.get("state"),
            last_name = LocalizedString(data.get("lastName")),
            first_name = LocalizedString(data.get("firstName")),
            position_code = data.get("positionCode"),
        )


@dataclass(slots=True, frozen=True)
class DraftTrackerResult:
    current_draft_date: str | None
    broadcast_start_time_utc: str | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    logo_url: str | None
    logo_fr_url: str | None
    ui_accent_color: str | None
    round: int | None
    state: str | None
    picks: list[DraftPick]

    @classmethod
    def from_dict(cls, data: dict) -> DraftTrackerResult:
        return cls(
            current_draft_date = data.get("currentDraftDate"),
            broadcast_start_time_utc = data.get("broadcastStartTimeUTC"),
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            logo_url = data.get("logoUrl"),
            logo_fr_url = data.get("logoFrUrl"),
            ui_accent_color = data.get("uiAccentColor"),
            round = data.get("round"),
            state = data.get("state"),
            picks = [DraftPick.from_dict(p) for p in data.get("picks") or []],
        )
