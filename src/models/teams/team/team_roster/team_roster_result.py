"""
TEAM ROSTER RESULT MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString, BirthDetails


@dataclass(slots=True, frozen=True)
class RosterPlayer:
    """A single player entry on an active team roster."""
    id: int | None
    headshot: str | None
    first_name: LocalizedString
    last_name: LocalizedString
    sweater_number: int | None
    position_code: str | None
    shoots_catches: str | None
    height_in_inches: int | None
    weight_in_pounds: int | None
    height_in_centimeters: int | None
    weight_in_kilograms: int | None
    birth_details: BirthDetails

    @classmethod
    def from_dict(cls, data: dict) -> RosterPlayer:
        return cls(
            id = data.get("id"),
            headshot = data.get("headshot"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            sweater_number = data.get("sweaterNumber"),
            position_code = data.get("positionCode"),
            shoots_catches = data.get("shootsCatches"),
            height_in_inches = data.get("heightInInches"),
            weight_in_pounds = data.get("weightInPounds"),
            height_in_centimeters = data.get("heightInCentimeters"),
            weight_in_kilograms = data.get("weightInKilograms"),
            birth_details = BirthDetails.from_dict(data),
        )


@dataclass(slots=True, frozen=True)
class TeamRosterResult:
    """Top-level response from the team roster endpoint."""
    forwards: list[RosterPlayer]
    defensemen: list[RosterPlayer]
    goalies: list[RosterPlayer]

    @classmethod
    def from_dict(cls, data: dict) -> TeamRosterResult:
        return cls(
            forwards = [RosterPlayer.from_dict(p) for p in data.get("forwards") or []],
            defensemen = [RosterPlayer.from_dict(p) for p in data.get("defensemen") or []],
            goalies = [RosterPlayer.from_dict(p) for p in data.get("goalies") or []],
        )
