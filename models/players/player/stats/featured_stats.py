"""
FEATURED STATS
"""


class Featured:
    """
    Represents featured statistics for a player.

    Featured statistics highlight a subset of notable performance metrics
    for the current season, along with corresponding career totals.

    If player is retired, Featured returns their last, most recent season season. 
    """
    def __init__(self, data: dict):
        """
        Initialize featured statistics from raw NHL landing API data.

        Args:
            data (dict): Raw featured statistic data returned by the NHL landing API.
                Expected to include a ``regularSeason`` object containing
                season-specific and career summary statistics.
        """
        regular_season: dict = data.get("regularSeason") or {}
        sub_season: dict = regular_season.get("subSeason") or {}
        career: dict = regular_season.get("career") or {}

        self.season: int | None = data.get("season")
        self.season_stats: FeaturedStats = FeaturedStats(sub_season)
        self.career_stats: FeaturedStats = FeaturedStats(career)


class FeaturedStats: 
    """
    Highlighted statistical totals for a player.

    This object represents a curated subset of player statistics intended
    for quick display or summary views, rather than a complete statistical
    breakdown.
    """
    def __init__(self, data: dict):
        """
        Initialize featured statistical values.

        Args:
            data (dict): Raw featured statistic values returned by the NHL landing API.
        """
        self.assists: int | None = data.get("assists")
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
        Convert featured statistics to a dictionary.

        Returns:
            dict: Serializable representation of featured statistics.
        """
        return {
            "assists": self.assists,
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