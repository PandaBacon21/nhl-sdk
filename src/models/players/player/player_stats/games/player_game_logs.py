"""
GAME_LOGS OBJECTS
"""
from __future__ import annotations
from dataclasses import dataclass

from .player_game import Game
from .player_season_game_type import SeasonGameType

@dataclass(slots=True, frozen=True)
class GameLogs:
    """
    Represents a collection of game log data for a player.

    This object groups per-game stats for a
    specific season and game type (e.g., regular season or playoffs).
    """
    season_id: int | None 
    game_type: int | None 
    seasons: list 
    games: list 

    @classmethod
    def from_dict(cls, data: dict) -> GameLogs:
        """
        Parameters
        ----------
        data : dict
            Raw game log data returned by the NHL gamelogs API. Expected to include
            season metadata, season summaries, and individual game entries.
        """
        season_id = data.get("seasonId")
        game_type = data.get("gameTypeId")
        seasons = [SeasonGameType.from_dict(season) for season in data.get("playerStatsSeasons") or []]
        games = [Game.from_dict(game) for game in data.get("gameLog") or [] ] 
        print(f"Building GameLogs: {season_id}:{game_type}")
        return cls(
            season_id = season_id,
            game_type = game_type,
            seasons = seasons,
            games = games 
        )
