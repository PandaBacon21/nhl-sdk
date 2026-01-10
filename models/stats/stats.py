"""
PLAYER STATS OBJECT
"""

from .featured_stats import Featured
from .career_stats import Career
from .game_stats import Game
from .season import Season

class Stats:
    """
    Player statistical sub-resource.

    Provides structured access to a player's statistical data,
    including featured stats, career totals, per-season statistics,
    and recent game performance (last 5 games).

    Instances of this class are accessed via `Player.stats`.
    """
    def __init__(self, data: dict):
        """
        Parameters
        ----------
        data : dict
            Raw player data as returned by the NHL API.
        """
        featured_stats: dict = data.get("featuredStats") or {}
        career_stats: dict = data.get("careerTotals") or {}

        self.featured: Featured = Featured(featured_stats)
        self.career: Career = Career(career_stats)
        self.seasons = [Season(season) for season in data.get("seasonTotals") or []]
        self.last_5_games = [Game(game) for game in data.get("last5Games") or []]
