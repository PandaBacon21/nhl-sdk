"""
SEASON OBJECT
"""

from .season_team import SeasonTeam
from .season_stats import SeasonStats

class Season: 
    def __init__(self, data: dict):
        self.season: int | None = data.get("season")
        self.sequence: int | None = data.get("sequence") # order of data in the same season
        self.game_type: str | None = data.get("gameTypeId") # Update this to helper 
        self.league: str | None = data.get("leagueAbbrev")
        self.team: SeasonTeam = SeasonTeam(data)
        self.stats: SeasonStats = SeasonStats(data)

