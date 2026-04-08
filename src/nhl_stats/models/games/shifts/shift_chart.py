"""
SHIFT CHART DATA CLASSES
Sourced from api.nhle.com/stats/rest — /{lang}/shiftcharts
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ShiftEntry:
    id: int | None
    game_id: int | None
    player_id: int | None
    period: int | None
    shift_number: int | None
    start_time: str | None
    end_time: str | None
    duration: str | None
    first_name: str | None
    last_name: str | None
    team_id: int | None
    team_abbrev: str | None
    team_name: str | None
    hex_value: str | None
    detail_code: int | None
    event_description: str | None
    event_details: str | None
    event_number: int | None
    type_code: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ShiftEntry:
        return cls(
            id = data.get("id"),
            game_id = data.get("gameId"),
            player_id = data.get("playerId"),
            period = data.get("period"),
            shift_number = data.get("shiftNumber"),
            start_time = data.get("startTime"),
            end_time = data.get("endTime"),
            duration = data.get("duration"),
            first_name = data.get("firstName"),
            last_name = data.get("lastName"),
            team_id = data.get("teamId"),
            team_abbrev = data.get("teamAbbrev"),
            team_name = data.get("teamName"),
            hex_value = data.get("hexValue"),
            detail_code = data.get("detailCode"),
            event_description = data.get("eventDescription"),
            event_details = data.get("eventDetails"),
            event_number = data.get("eventNumber"),
            type_code = data.get("typeCode"),
        )


@dataclass(slots=True, frozen=True)
class ShiftChart:
    game_id: int
    total: int
    shifts: list[ShiftEntry]

    @classmethod
    def from_dict(cls, game_id: int, data: dict) -> ShiftChart:
        return cls(
            game_id = game_id,
            total = data.get("total") or 0,
            shifts = [ShiftEntry.from_dict(s) for s in (data.get("data") or [])],
        )
