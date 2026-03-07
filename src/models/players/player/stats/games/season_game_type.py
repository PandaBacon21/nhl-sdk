"""
Seasons with Game Logs
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class SeasonGameType: 
    season: int | None 
    game_types: list[int] 
    playoffs: bool 

    @classmethod
    def from_dict(cls, data: dict) -> SeasonGameType:
        season  = data.get("season")
        game_types = data.get("gameTypes") or []
        playoffs = True if len(game_types) == 2 else False
        return cls(
            season = season,
            game_types = game_types,
            playoffs = playoffs
    )