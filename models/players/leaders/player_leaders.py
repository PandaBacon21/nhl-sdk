"""
LEADERS GOALIE OBJECTS
"""

from .player import Player


class GoalieLeaders:
    """
    Container for goalie statistical leaders.

    Each attribute represents a leaderboard for a specific goalie
    statistic. Values are lists of `Player` objects ordered by the
    underlying NHL API stat ranking.
    """
    def __init__(self, data: dict): 
        self.wins: list = [Player(goalie) for goalie in data.get("wins") or []]
        self.shutouts: list = [Player(goalie) for goalie in data.get("shutouts") or []]
        self.save_pctg: list = [Player(goalie) for goalie in data.get("savePctg") or []]
        self.goals_against_avg: list = [Player(goalie) for goalie in data.get("goalsAgainstAverage") or []]

class SkaterLeaders: 
    """
    Container for skater statistical leaders.

    Each attribute represents a leaderboard for a specific skater
    statistic. Values are lists of `Player` objects ordered by the
    underlying NHL API stat ranking.
    """
    def __init__(self, data: dict): 
        self.goals: list = [Player(skater) for skater in data.get("goals") or []]
        self.goals_sh: list = [Player(skater) for skater in data.get("goalsSh") or []]
        self.goals_pp: list = [Player(skater) for skater in data.get("goalsPp") or []]
        self.assists: list = [Player(skater) for skater in data.get("assists") or []]
        self.points: list = [Player(skater) for skater in data.get("points") or []]
        self.plus_minus: list = [Player(skater) for skater in data.get("plusMinus") or []]
        self.penalty_min: list = [Player(skater) for skater in data.get("penaltyMins") or []]
        self.faceoff_leaders: list = [Player(skater) for skater in data.get("faceoffLeaders") or []]
        self.toi: list = [Player(skater) for skater in data.get("toi") or []]
