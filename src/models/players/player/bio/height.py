"""
HEIGHT DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Height: 
    height_in: int | None 
    height_cm: int | None

    @classmethod
    def from_dict(cls, data: dict) -> Height:
        return cls(
            height_in = data.get("heightInInches"),
            height_cm = data.get("heightInCentimeters")

        )