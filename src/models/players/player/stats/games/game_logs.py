"""
GAME_LOGS OBJECTS
"""

from .game import Game
from .season_game_type import SeasonGameType

class GameLogs:
    """
    Represents a collection of game log data for a player.

    This object groups per-game stats for a
    specific season and game type (e.g., regular season or playoffs).
    """

    def __init__(self, data: dict):
        """
        Initialize game log data from raw NHL API response.

        Parameters
        ----------
        data : dict
            Raw game log data returned by the NHL gamelogs API. Expected to include
            season metadata, season summaries, and individual game entries.
        """
        self.season_id: int | None = data.get("seasonId")
        self.game_type: int | None = data.get("gameTypeId")
        self.seasons: list = [SeasonGameType(season) for season in data.get("playerStatsSeasons") or []]
        self.games: list = [Game(game) for game in data.get("gameLog") or [] ] 

        print(f"Building GameLogs: {self.season_id}:{self.game_type}")
