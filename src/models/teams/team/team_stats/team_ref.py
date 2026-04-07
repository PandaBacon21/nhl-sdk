"""
TEAM REFERENCE MODEL
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TeamRef:
    """Basic team reference record from the NHL Stats API."""
    id: int | None
    franchise_id: int | None
    full_name: str | None
    league_id: int | None
    raw_tricode: str | None
    tricode: str | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamRef:
        return cls(
            id = data.get("id"),
            franchise_id = data.get("franchiseId"),
            full_name = data.get("fullName"),
            league_id = data.get("leagueId"),
            raw_tricode = data.get("rawTricode"),
            tricode = data.get("triCode"),
        )
