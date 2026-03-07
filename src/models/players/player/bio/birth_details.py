"""
BIRTH DETAILS DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString

@dataclass(slots=True, frozen=True)
class BirthDetails: 
    birth_date: str | None
    city: LocalizedString 
    state_province: LocalizedString 
    country: str | None 

    @classmethod
    def from_dict(cls, data: dict) -> BirthDetails:
        return cls(
            birth_date = data.get("birthDate"),
            city = LocalizedString(data.get("birthCity")),
            state_province = LocalizedString(data.get("birthStateProvince")),
            country = data.get("birthCountry")
        )