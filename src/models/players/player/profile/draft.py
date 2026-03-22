"""
DRAFT DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from typing import Any

@dataclass(slots=True, frozen=True)
class Draft: 
    year: int | None 
    team: str | None 
    round: int | None 
    pick_in_round: int | None 
    pick_overall: int | None 

    @classmethod
    def from_dict(cls, data: dict) -> Draft:
        _draft = data.get("draftDetails")

        return cls(
             year = cls._handle_missing(_draft, "year"),
             team = cls._handle_missing(_draft, "teamAbbrev"),
             round = cls._handle_missing(_draft, "round"),
             pick_in_round = cls._handle_missing(_draft, "pickInRound"),
             pick_overall = cls._handle_missing(_draft, "overallPick")
             )

    @staticmethod
    def _handle_missing(data: dict | None, type: str) -> Any:
        if not isinstance(data, dict):
            return None
        return data.get(type)