"""
PLAYER BIO DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .profile_team import ProfileTeam
from .media import Media
from .draft import Draft

from .....core.utilities import LocalizedString, BirthDetails, _to_bool

@dataclass(slots=True, frozen=True)
class Profile:
    player_id: int
    first_name: LocalizedString
    last_name: LocalizedString
    number: int | None
    position: str | None
    team: ProfileTeam
    hand: str | None
    is_active: bool | None
    height_in_inches: int | None
    height_in_centimeters: int | None
    weight_in_pounds: int | None
    weight_in_kilograms: int | None
    birth_details: BirthDetails
    draft: Draft
    media: Media

    @classmethod
    def from_dict(cls, data: dict) -> Profile:
        return cls(
            player_id = data["playerId"],
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            number = data.get("sweaterNumber"),
            position = data.get("position"),
            team = ProfileTeam.from_dict(data),
            hand = data.get("shootsCatches"),
            is_active = _to_bool(data.get("isActive")),
            height_in_inches = data.get("heightInInches"),
            height_in_centimeters = data.get("heightInCentimeters"),
            weight_in_pounds = data.get("weightInPounds"),
            weight_in_kilograms = data.get("weightInKilograms"),
            birth_details = BirthDetails.from_dict(data),
            draft = Draft.from_dict(data),
            media = Media.from_dict(data)
        )
