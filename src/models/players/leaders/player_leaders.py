"""
LEADERS OBJECTS
"""
from __future__ import annotations
import logging
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass

from .edge.edge_leaders import EdgeLeaders, SkaterEdgeLeaders, GoalieEdgeLeaders
from .leaders_team import LeadersTeam
from ....core.utilities import LocalizedString, _check_cache
from ....core.cache import get_cache

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
            headshot=data.get("headshot"),
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


class PlayerLeaders(ABC):
    def __init__(self, client: NhlClient):
        self._client = client

    @property
    @abstractmethod
    def get_edge_leaders(self) -> EdgeLeaders: ...


# ---------------------------------------------------------------------------
# Pure data models — returned by get_stat_leaders()
# ---------------------------------------------------------------------------

class GoalieStatLeaders:
    """Goalie stat leader lists returned by GoalieLeaders.get_stat_leaders()."""
    def __init__(self, data: dict):
        self.wins: list[LeaderPlayer] = [LeaderPlayer.from_dict(w) for w in (data.get("wins") or [])]
        self.shutouts: list[LeaderPlayer] = [LeaderPlayer.from_dict(s) for s in (data.get("shutouts") or [])]
        self.save_pctg: list[LeaderPlayer] = [LeaderPlayer.from_dict(sp) for sp in (data.get("savePctg") or [])]
        self.goals_against_avg: list[LeaderPlayer] = [
            LeaderPlayer.from_dict(gaa) for gaa in (data.get("goalsAgainstAverage") or [])
        ]


class SkaterStatLeaders:
    """Skater stat leader lists returned by SkaterLeaders.get_stat_leaders()."""
    def __init__(self, data: dict):
        self.goals: list[LeaderPlayer] = [LeaderPlayer.from_dict(g) for g in (data.get("goals") or [])]
        self.goals_sh: list[LeaderPlayer] = [LeaderPlayer.from_dict(g) for g in (data.get("goalsSh") or [])]
        self.goals_pp: list[LeaderPlayer] = [LeaderPlayer.from_dict(g) for g in (data.get("goalsPp") or [])]
        self.assists: list[LeaderPlayer] = [LeaderPlayer.from_dict(a) for a in (data.get("assists") or [])]
        self.points: list[LeaderPlayer] = [LeaderPlayer.from_dict(p) for p in (data.get("points") or [])]
        self.plus_minus: list[LeaderPlayer] = [LeaderPlayer.from_dict(pm) for pm in (data.get("plusMinus") or [])]
        self.penalty_min: list[LeaderPlayer] = [LeaderPlayer.from_dict(pm) for pm in (data.get("penaltyMins") or [])]
        self.faceoff_leaders: list[LeaderPlayer] = [LeaderPlayer.from_dict(f) for f in (data.get("faceoffLeaders") or [])]
        self.toi: list[LeaderPlayer] = [LeaderPlayer.from_dict(t) for t in (data.get("toi") or [])]


# ---------------------------------------------------------------------------
# Service classes — accessed via client.players.leaders.skaters / .goalies
# ---------------------------------------------------------------------------

class GoalieLeaders(PlayerLeaders):
    """
    Goalie leaders namespace.

    Accessed via `client.players.leaders.goalies`. Provides stat leaders
    and Edge leaderboard access without requiring a player ID.
    """
    def __init__(self, client: NhlClient):
        super().__init__(client=client)
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.leaders.goalies")
        self._ttl: int = 60 * 60 * 1

    def _cache_key(self, season: int | None, game_type: int | None,
                   categories: str | None, limit: int | None) -> str:
        key = "leaders:g"
        key += f":{season}" if season else ":now"
        if game_type:
            key += f":{game_type}"
        if categories:
            key += f":{categories}"
        if limit:
            key += f":{limit}"
        return key

    def get_stat_leaders(self, season: Optional[int] = None, game_type: Optional[int] = None,
                         categories: Optional[str] = None, limit: Optional[int] = None) -> GoalieStatLeaders:
        """
        Retrieve goalie statistical leaders.

        Args:
            season (int, optional): NHL season (e.g. 20242025).
            game_type (int, optional): 2 = regular season, 3 = playoffs.
            categories (str, optional): Stat category filter (e.g. "wins").
            limit (int, optional): Maximum number of results to return.

        `season` and `game_type` must be provided together for a historical
        lookup, or omitted for current leaders.
        """
        cache_key = self._cache_key(season, game_type, categories, limit)
        cached = _check_cache(cache=self._cache, cache_key=cache_key)
        if cached is not None:
            self._logger.debug(f"{cache_key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{cache_key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_players.get_goalie_leaders(
            season=season, g_type=game_type, categories=categories, limit=limit
        )
        result = GoalieStatLeaders(res.data)
        self._cache.set(key=cache_key, data=result, ttl=self._ttl)
        self._logger.debug(f"{cache_key}: Cached | ttl: {self._ttl}")
        return result

    @property
    def get_edge_leaders(self) -> GoalieEdgeLeaders:
        """Access league-wide goalie Edge leaderboards."""
        return GoalieEdgeLeaders(self._client)


class SkaterLeaders(PlayerLeaders):
    """
    Skater leaders namespace.

    Accessed via `client.players.leaders.skaters`. Provides stat leaders
    and Edge leaderboard access without requiring a player ID.
    """
    def __init__(self, client: NhlClient):
        super().__init__(client=client)
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.leaders.skaters")
        self._ttl: int = 60 * 60 * 1

    def _cache_key(self, season: int | None, game_type: int | None,
                   categories: str | None, limit: int | None) -> str:
        key = "leaders:s"
        key += f":{season}" if season else ":now"
        if game_type:
            key += f":{game_type}"
        if categories:
            key += f":{categories}"
        if limit:
            key += f":{limit}"
        return key

    def get_stat_leaders(self, season: Optional[int] = None, game_type: Optional[int] = None,
                         categories: Optional[str] = None, limit: Optional[int] = None) -> SkaterStatLeaders:
        """
        Retrieve skater statistical leaders.

        Args:
            season (int, optional): NHL season (e.g. 20242025).
            game_type (int, optional): 2 = regular season, 3 = playoffs.
            categories (str, optional): Stat category filter (e.g. "goals").
            limit (int, optional): Maximum number of results to return.

        `season` and `game_type` must be provided together for a historical
        lookup, or omitted for current leaders.
        """
        cache_key = self._cache_key(season, game_type, categories, limit)
        cached = _check_cache(cache=self._cache, cache_key=cache_key)
        if cached is not None:
            self._logger.debug(f"{cache_key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{cache_key}: Cache Miss")
        res = self._client._api.api_web.call_nhl_players.get_skater_leaders(
            season=season, g_type=game_type, categories=categories, limit=limit
        )
        result = SkaterStatLeaders(res.data)
        self._cache.set(key=cache_key, data=result, ttl=self._ttl)
        self._logger.debug(f"{cache_key}: Cached | ttl: {self._ttl}")
        return result

    @property
    def get_edge_leaders(self) -> SkaterEdgeLeaders:
        """Access league-wide skater Edge leaderboards."""
        return SkaterEdgeLeaders(self._client)
