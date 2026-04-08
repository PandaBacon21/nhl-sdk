"""
SEASON OBJECT
"""
from __future__ import annotations
from dataclasses import dataclass

from .player_season_team import SeasonTeam
from .player_season_stats import SeasonStats


@dataclass(slots=True, frozen=True)
class Season:
    """
    Per-season statistical record for a player.

    Represents a player's statistics for a single season and game type,
    including team context and season-level performance metrics.

    Instances of this class are accessed via `Player.stats.seasons`.
    """

    season: int | None
    sequence: int | None
    game_type_id: int | None
    league: str | None
    team: SeasonTeam
    stats: SeasonStats

    @classmethod
    def from_dict(cls, data: dict) -> Season:
        return cls(
            season=data.get("season"),
            sequence=data.get("sequence"),
            game_type_id=data.get("gameTypeId"),
            league=data.get("leagueAbbrev"),
            team=SeasonTeam.from_dict(data),
            stats=SeasonStats.from_dict(data),
        )

    def to_dict(self) -> dict:
        return {
            "season": self.season,
            "sequence": self.sequence,
            "game_type_id": self.game_type_id,
            "league": self.league,
            "team": self.team.to_dict(),
            "stats": self.stats.to_dict(),
        }