"""
TEAM STATS RESULT MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from .team_skater_stat import TeamSkaterStat
from .team_goalie_stat import TeamGoalieStat


@dataclass(slots=True, frozen=True)
class TeamStatsResult:
    """Top-level response from the club-stats endpoint."""
    season: str | None
    game_type: int | None
    skaters: list[TeamSkaterStat]
    goalies: list[TeamGoalieStat]

    @classmethod
    def from_dict(cls, data: dict) -> TeamStatsResult:
        return cls(
            season = data.get("season"),
            game_type = data.get("gameType"),
            skaters = [TeamSkaterStat.from_dict(s) for s in data.get("skaters") or []],
            goalies = [TeamGoalieStat.from_dict(g) for g in data.get("goalies") or []],
        )
