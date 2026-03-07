"""
AWARD DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString

@dataclass(slots=True, frozen=True)
class Award: 
    trophy: LocalizedString
    seasons: list 


    @classmethod
    def from_dict(cls, data: dict) -> Award:
        return cls(
            trophy = LocalizedString(data.get("trophy")),
            seasons = data.get("seasons") or []
        )
    