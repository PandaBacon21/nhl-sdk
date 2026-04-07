"""
LOCATION RESULT DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class LocationResult:
    country_code: str | None

    @classmethod
    def from_dict(cls, data: dict) -> LocationResult:
        return cls(country_code=data.get("country"))
