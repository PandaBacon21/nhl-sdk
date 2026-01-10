"""
SEASON OBJECT
"""

from .season_team import SeasonTeam
from .season_stats import SeasonStats

class Season: 
    """
    Per-season statistical record for a player.

    Represents a player's statistics for a single season and game type,
    including team context and season-level performance metrics.

    Instances of this class are accessed via `Player.stats.seasons`.
    """
    def __init__(self, data: dict):
        """
        Initialize a Season record.

        Parameters
        ----------
        data : dict
            Raw season data containing statistical fields as returned in Player data
            by the NHL API.
        """
        self.season: int | None = data.get("season")
        self.sequence: int | None = data.get("sequence") # order of data in the same season
        self.game_type: str | None = data.get("gameTypeId") # Update this to helper in future 
        self.league: str | None = data.get("leagueAbbrev")
        self.team: SeasonTeam = SeasonTeam(data)
        self.stats: SeasonStats = SeasonStats(data)

