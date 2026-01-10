"""
PLAYER STATS OBJECT
"""

from .featured_stats import Featured
from .career_stats import Career
from .game_stats import Game
from .season import Season

class Stats: 
    def __init__(self, data: dict):
        featured_stats: dict = data.get("featuredStats") or {}
        career_stats: dict = data.get("careerTotals") or {}

        self.featured: Featured = Featured(featured_stats)
        self.career: Career = Career(career_stats)
        self.seasons = [Season(season) for season in data.get("seasonTotals") or []]
        self.last_5_games = [Game(game) for game in data.get("last5Games") or []]
