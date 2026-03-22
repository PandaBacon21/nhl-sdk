"""
WEIGHT DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Weight: 
    weight_lbs: int | None 
    weight_kg: int | None 

    @classmethod
    def from_dict(cls, data: dict) -> Weight:
        return cls(
            weight_lbs = data.get("weightInPounds"),
            weight_kg = data.get("weightInKilograms")
        )