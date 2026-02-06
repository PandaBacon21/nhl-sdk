"""
CAREER STATS
"""


class Career:
    """
    Represents a player's career statistics.

    This object separates career totals into regular season and
    playoff statistics.
    """
    def __init__(self, data: dict):
        """
        Initialize career statistics from raw NHL API data.

        Args:
            data (dict): Raw player landing data returned by the NHL API.
                Expected to contain ``regularSeason`` and ``playoffs``
                keys.
        """
        regular_season: dict = data.get("regularSeason") or {}
        playoffs: dict = data.get("playoffs") or {}

        self.regular_season: CareerStats = CareerStats(regular_season)
        self.playoffs: CareerStats = CareerStats(playoffs)
        

class CareerStats: 
    """
    Aggregated career statistics for a player.

    All values represent cumulative or averaged statistics across
    a player's entire career for a specific game context
    (regular season or playoffs).
    """
    def __init__(self, data: dict):
        """
        Initialize aggregated career statistics.

        Args:
            data (dict): Raw career stat values returned by the NHL API.
        """
        self.assists: int | None = data.get("assists")
        self.avg_toi: str | None = data.get("avgToi")
        self.faceoff_win_pctg: float | None = data.get("faceoffWinningPctg")
        self.game_winning_goals: int | None = data.get("gameWinningGoals")
        self.games_played: int | None = data.get("gamesPlayed")
        self.goals: int | None = data.get("goals")
        self.ot_goals: int | None = data.get("otGoals")
        self.pim: int | None = data.get("pim")
        self.plus_minus: int | None = data.get("plusMinus")
        self.points: int | None = data.get("points")
        self.pp_goals: int | None = data.get("powerPlayGoals")
        self.pp_points: int | None = data.get("powerPlayPoints")
        self.shooting_pctg: float | None = data.get("shootingPctg")
        self.sh_goals: int | None = data.get("shorthandedGoals")
        self.sh_points: int | None = data.get("shorthandedPoints")
        self.shots: int | None = data.get("shots")

    def to_dict(self) -> dict:
        """
        Convert career statistics to a dictionary.

        Returns:
            dict: Serializable representation of career statistics.
        """
        return {
            "assists": self.assists,
            "avg_toi": self.avg_toi,
            "faceoff_win_pctg": self.faceoff_win_pctg,
            "game_winning_goals": self.game_winning_goals,
            "games_played": self.games_played,
            "goals": self.goals,
            "ot_goals": self.ot_goals,
            "pim": self.pim,
            "plus_minus": self.plus_minus,
            "points": self.points,
            "pp_goals": self.pp_goals,
            "pp_points": self.pp_points,
            "shooting_pctg": self.shooting_pctg,
            "sh_goals": self.sh_goals,
            "sh_points": self.sh_points,
            "shots": self.shots,
        }