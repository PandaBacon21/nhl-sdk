"""
LAST 5 GAME STATS
"""

class FeaturedGame:
    """
    Represents a single game from a player's recent performance.
    """
    def __init__(self, data: dict):
        """
        Initialize featured game statistics.

        Parameters
        ----------
        data : dict
            Raw per-game player statistics returned by the NHL landing API.
        """
        self.assists: int | None = data.get("assists")
        self.game_date: str | None = data.get("gameDate")
        self.game_id: int | None = data.get("gameId")
        self.game_type_id: int | None = data.get("gameTypeId")
        self.goals: int | None = data.get("goals")
        self.home_road_flag: str | None = data.get("homeRoadFlag")
        self.opponent_abbrev: str | None = data.get("opponentAbbrev")
        self.pim: int | None = data.get("pim")
        self.plus_minus: int | None = data.get("plusMinus")
        self.points: int | None = data.get("points")
        self.pp_goals: int | None = data.get("powerPlayGoals")
        self.shifts: int | None = data.get("shifts")
        self.sh_goals: int | None = data.get("shorthandedGoals")
        self.shots: int | None = data.get("shots")
        self.team_abbrev: str | None = data.get("teamAbbrev")
        self.toi: str | None = data.get("toi")
    
    def to_dict(self) -> dict:
        """
        Convert game statistics to a dictionary.

        Returns
        -------
        dict
            Serializable representation of the game statistics.
        """
        return {
            "assists": self.assists,
            "game_date": self.game_date,
            "game_id": self.game_id,
            "game_type_id": self.game_type_id,
            "goals": self.goals,
            "home_road_flag": self.home_road_flag,
            "opponent_abbrev": self.opponent_abbrev,
            "pim": self.pim,
            "plus_minus": self.plus_minus,
            "points": self.points,
            "pp_goals": self.pp_goals,
            "shifts": self.shifts,
            "sh_goals": self.sh_goals,
            "shots": self.shots,
            "team_abbrev": self.team_abbrev,
            "toi": self.toi,
        }