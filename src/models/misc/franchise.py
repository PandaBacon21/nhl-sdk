"""
FRANCHISE DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Franchise:
    franchise_id: int | None
    full_name: str | None
    team_common_name: str | None
    team_place_name: str | None

    @classmethod
    def from_dict(cls, data: dict) -> Franchise:
        return cls(
            franchise_id = data.get("id"),
            full_name = data.get("fullName"),
            team_common_name = data.get("teamCommonName"),
            team_place_name = data.get("teamPlaceName"),
        )
