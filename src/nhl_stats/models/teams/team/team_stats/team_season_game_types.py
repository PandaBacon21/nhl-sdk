"""
TEAM SEASON GAME TYPES MODEL
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TeamSeasonGameTypes:
    """A season entry from the club-stats-season endpoint."""
    season: int | None
    game_types: list[int]

    @classmethod
    def from_dict(cls, data: dict) -> TeamSeasonGameTypes:
        return cls(
            season = data.get("season"),
            game_types = list(data.get("gameTypes") or []),
        )
