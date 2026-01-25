"""
Seasons with Game Logs
"""

class Season: 
    def __init__(self, data: dict):
        self.season: int | None = data.get("season")
        self.game_types: list[int] = data.get("gameTypes") or []
        self.playoffs: bool = True if len(self.game_types) == 2 else False