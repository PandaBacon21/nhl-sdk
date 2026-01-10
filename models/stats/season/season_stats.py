"""
SEASON STATS
"""

class SeasonStats:
    def __init__(self, data: dict): 
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
