"""
LEADERS OBJECTS
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from .edge.edge_leaders import SkaterEdgeLeaders#, GoalieEdgeLeaders
from .leaders_team import LeadersTeam
from ....core.utilities import LocalizedString

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class Player: 
    """
    Represents a player entry in a leaderboard or statistical result.

    This object wraps raw player data returned by the NHL API and exposes 
    available attributes 
    """
    def __init__(self, data: dict): 
        self.value: int | None = data.get("value")
        self.pid: str | None = data.get("id")
        self.first_name: LocalizedString | None = LocalizedString(data.get("firstName"))
        self.last_name: LocalizedString | None = LocalizedString(data.get("lastName"))
        self.number: int | None = data.get("sweaterNumber")
        self.position: str | None = data.get("position")
        self.headshot: str | None = data.get("headhshot")
        self.team: LeadersTeam = LeadersTeam(data)



class BaseLeaders:
    def __init__(self, client: NhlClient): 
        self._client = client

class GoalieLeaders(BaseLeaders):
    """
    Container for goalie statistical leaders.

    Each attribute represents a leaderboard for a specific goalie
    statistic. Values are lists of `Player` objects ordered by the
    underlying NHL API stat ranking.
    """
    def __init__(self, data: dict, client: NhlClient): 
        super().__init__(client=client)

        self.wins: list = [Player(goalie) for goalie in data.get("wins") or []]
        self.shutouts: list = [Player(goalie) for goalie in data.get("shutouts") or []]
        self.save_pctg: list = [Player(goalie) for goalie in data.get("savePctg") or []]
        self.goals_against_avg: list = [Player(goalie) for goalie in data.get("goalsAgainstAverage") or []]

    # @property
    # def edge(self) -> GoalieEdgeLeaders:
    #     return GoalieEdgeLeaders(client=self._client)
        

class SkaterLeaders(BaseLeaders): 
    """
    Container for skater statistical leaders.

    Each attribute represents a leaderboard for a specific skater
    statistic. Values are lists of `Player` objects ordered by the
    underlying NHL API stat ranking.
    """
    def __init__(self, data: dict, client: NhlClient): 
        super().__init__(client=client)

        self.goals: list = [Player(skater) for skater in data.get("goals") or []]
        self.goals_sh: list = [Player(skater) for skater in data.get("goalsSh") or []]
        self.goals_pp: list = [Player(skater) for skater in data.get("goalsPp") or []]
        self.assists: list = [Player(skater) for skater in data.get("assists") or []]
        self.points: list = [Player(skater) for skater in data.get("points") or []]
        self.plus_minus: list = [Player(skater) for skater in data.get("plusMinus") or []]
        self.penalty_min: list = [Player(skater) for skater in data.get("penaltyMins") or []]
        self.faceoff_leaders: list = [Player(skater) for skater in data.get("faceoffLeaders") or []]
        self.toi: list = [Player(skater) for skater in data.get("toi") or []]

    @property
    def edge(self) -> SkaterEdgeLeaders:
        return SkaterEdgeLeaders(client=self._client)