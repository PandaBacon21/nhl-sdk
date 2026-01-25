"""
GAME_LOGS OBJECTS
"""

from .game import Game
from .season import Season

class GameLogs:
    def __init__(self, data: dict):
        self.season_id: int | None = data.get("seasonId")
        self.game_type: int | None = data.get("gameTypeId")
        self.seasons: list = [Season(season) for season in data.get("playerStatsSeasons") or []]
        self.games: list = [Game(game) for game in data.get("gameLog") or [] ] 

        print(f"Building GameLogs: {self.season_id}:{self.game_type}")
