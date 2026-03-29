"""
GOALIE SAVE PERCENTAGE TOP 10 MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ....player.player_stats.edge.player_edge_types import LeaderPlayer


@dataclass(slots=True, frozen=True)
class GoalieSavePctgLeaderEntry:
    """One goalie's entry in the save percentage top 10 leaderboard."""
    player: LeaderPlayer
    games_over_900: int | None
    pctg_games_over_900: float | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieSavePctgLeaderEntry:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            games_over_900 = data.get("gamesOver900"),
            pctg_games_over_900 = data.get("pctgGamesOver900"),
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "games_over_900": self.games_over_900,
            "pctg_games_over_900": self.pctg_games_over_900,
        }
