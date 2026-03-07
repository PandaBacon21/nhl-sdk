"""
LEADERS OBJECTS
"""
from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

from .edge.edge_leaders import SkaterEdgeLeaders#, GoalieEdgeLeaders
from .leaders_team import LeadersTeam
from ....core.utilities import LocalizedString

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

@dataclass(slots=True, frozen=True)
class LeaderPlayer:
    value: int | None
    pid: str | None
    first_name: LocalizedString
    last_name: LocalizedString
    number: int | None
    position: str | None
    headshot: str | None
    team: LeadersTeam

    @classmethod
    def from_dict(cls, data: dict) -> "LeaderPlayer":
        return cls(
            value=data.get("value"),
            pid=data.get("id"),
            first_name=LocalizedString(data.get("firstName")),
            last_name=LocalizedString(data.get("lastName")),
            number=data.get("sweaterNumber"),
            position=data.get("position"),
            headshot=data.get("headshot"),  # fix typo
            team=LeadersTeam.from_dict(data),
        )

    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "id": self.pid,
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "sweater_number": self.number,
            "position": self.position,
            "headshot": self.headshot,
            "team": self.team.to_dict(),
        }

class BaseLeaders:
    def __init__(self, client: NhlClient):
        self._client = client


class GoalieLeaders(BaseLeaders):
    def __init__(self, data: dict, client: NhlClient):
        super().__init__(client=client)

        self.wins: list[LeaderPlayer] = [LeaderPlayer.from_dict(wins) for wins in (data.get("wins") or [])]
        self.shutouts: list[LeaderPlayer] = [LeaderPlayer.from_dict(shutouts) for shutouts in (data.get("shutouts") or [])]
        self.save_pctg: list[LeaderPlayer] = [LeaderPlayer.from_dict(save_pct) for save_pct in (data.get("savePctg") or [])]
        self.goals_against_avg: list[LeaderPlayer] = [
            LeaderPlayer.from_dict(gaa) for gaa in (data.get("goalsAgainstAverage") or [])
        ]

class SkaterLeaders(BaseLeaders):
    def __init__(self, data: dict, client: NhlClient):
        super().__init__(client=client)

        self.goals: list[LeaderPlayer] = [LeaderPlayer.from_dict(goals) for goals in (data.get("goals") or [])]
        self.goals_sh: list[LeaderPlayer] = [LeaderPlayer.from_dict(goals_sh) for goals_sh in (data.get("goalsSh") or [])]
        self.goals_pp: list[LeaderPlayer] = [LeaderPlayer.from_dict(goals_pp) for goals_pp in (data.get("goalsPp") or [])]
        self.assists: list[LeaderPlayer] = [LeaderPlayer.from_dict(assists) for assists in (data.get("assists") or [])]
        self.points: list[LeaderPlayer] = [LeaderPlayer.from_dict(points) for points in (data.get("points") or [])]
        self.plus_minus: list[LeaderPlayer] = [LeaderPlayer.from_dict(plus_minus) for plus_minus in (data.get("plusMinus") or [])]
        self.penalty_min: list[LeaderPlayer] = [LeaderPlayer.from_dict(pen_min) for pen_min in (data.get("penaltyMins") or [])]
        self.faceoff_leaders: list[LeaderPlayer] = [LeaderPlayer.from_dict(faceoff_leaders) for faceoff_leaders in (data.get("faceoffLeaders") or [])]
        self.toi: list[LeaderPlayer] = [LeaderPlayer.from_dict(toi) for toi in (data.get("toi") or [])]

    @property
    def edge(self) -> SkaterEdgeLeaders:
        return SkaterEdgeLeaders(client=self._client)