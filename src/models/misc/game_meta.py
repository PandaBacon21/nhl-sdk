from __future__ import annotations
from dataclasses import dataclass

from .misc_meta import MetaTeam


@dataclass(slots=True, frozen=True)
class GameMetaSeasonState:
    date: str | None
    game_type: int | None
    season: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GameMetaSeasonState:
        return cls(
            date = data.get("date"),
            game_type = data.get("gameType"),
            season = data.get("season"),
        )


@dataclass(slots=True, frozen=True)
class GameMetaResult:
    teams: list[MetaTeam]
    season_states: GameMetaSeasonState | None
    game_state: str | None

    @classmethod
    def from_dict(cls, data: dict) -> GameMetaResult:
        raw_ss = data.get("seasonStates")
        return cls(
            teams = [MetaTeam.from_dict(t) for t in (data.get("teams") or [])],
            season_states = GameMetaSeasonState.from_dict(raw_ss) if isinstance(raw_ss, dict) else None,
            game_state = data.get("gameState"),
        )
