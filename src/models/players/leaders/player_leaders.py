"""
LEADERS OBJECTS
"""
from __future__ import annotations
import logging
from abc import ABC
from typing import TYPE_CHECKING
from dataclasses import dataclass

from .leaders_team import LeadersTeam
from .edge.skaters.skater_landing import SkaterLanding
from .edge.goalies.goalie_landing import GoalieLanding
from .edge.skaters import (
    SkaterDistanceTop10,
    SkaterSpeedTop10,
    SkaterZoneTimeTop10,
    SkaterShotSpeedTop10,
    SkaterShotLocationTop10,
)
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
    _edge_pos: str    # set by subclass — used in edge cache keys and logger
    _stat_prefix: str # set by subclass — used in stat leaders cache keys

    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger(f"nhl_sdk.leaders.{self._edge_pos}")
        self._ttl: int = 60 * 60 * 1

    def _cache_key(self, season: int | None, game_type: int | None,
                   categories: str | None, limit: int | None) -> str:
        key = f"leaders:{self._stat_prefix}"
        key += f":{season}" if season else ":now"
        if game_type:
            key += f":{game_type}"
        if categories:
            key += f":{categories}"
        if limit:
            key += f":{limit}"
        return key

    def _edge_cache_key(self, name: str, season: int | None, game_type: int | None, *args: str) -> str:
        base = f"leaders:edge:{self._edge_pos}:{name}"
        suffix = f":{season}:{game_type}" if season and game_type else ":now"
        extra = "".join(f":{a}" for a in args if a)
        return base + suffix + extra

    def _edge_fetch(self, key: str, api_fn, builder=None):
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = api_fn()
        result = builder(res.data) if builder else res.data
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result


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
    _edge_pos = "goalie"
    _stat_prefix = "g"

    def get_stat_leaders(self, season: int | None = None, game_type: int | None = None,
                         categories: str | None = None, limit: int | None = None) -> GoalieStatLeaders:
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

    def edge_landing(self, season: int | None = None, game_type: int | None = None) -> GoalieLanding:
        """Retrieve goalie Edge landing leaders."""
        key = self._edge_cache_key("landing", season, game_type)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalie_landing(
                season=season, game_type=game_type,
            ),
            lambda d: GoalieLanding.from_dict(d),
        )

    def edge_five_v_five_top_10(self, sort: str,
                                season: int | None = None, game_type: int | None = None) -> list:
        """Retrieve top 10 goalies by 5v5 save percentage."""
        key = self._edge_cache_key("5v5_10", season, game_type, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalies_5v5_10(
                sort=sort, season=season, game_type=game_type,
            ),
        )

    def edge_shot_location_top_10(self, category: str, sort: str,
                                  season: int | None = None, game_type: int | None = None) -> list:
        """Retrieve top 10 goalies by shot location."""
        key = self._edge_cache_key("shot_location_10", season, game_type, category, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalie_shot_location_10(
                category=category, sort=sort, season=season, game_type=game_type,
            ),
        )

    def edge_save_pctg_top_10(self, sort: str,
                              season: int | None = None, game_type: int | None = None) -> list:
        """Retrieve top 10 goalies by save percentage."""
        key = self._edge_cache_key("save_pctg_10", season, game_type, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalie_save_pctg_10(
                sort=sort, season=season, game_type=game_type,
            ),
        )


class SkaterLeaders(PlayerLeaders):
    """
    Skater leaders namespace.

    Accessed via `client.players.leaders.skaters`. Provides stat leaders
    and Edge leaderboard access without requiring a player ID.
    """
    _edge_pos = "skater"
    _stat_prefix = "s"

    def get_stat_leaders(self, season: int | None = None, game_type: int | None = None,
                         categories: str | None = None, limit: int | None = None) -> SkaterStatLeaders:
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

    def edge_landing(self, season: int | None = None, game_type: int | None = None) -> SkaterLanding:
        """Retrieve skater Edge landing leaders."""
        key = self._edge_cache_key("landing", season, game_type)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_landing(
                season=season, game_type=game_type,
            ),
            lambda d: SkaterLanding.from_dict(d),
        )

    def edge_distance_top_10(self, pos: str, strength: str, sort: str,
                             season: int | None = None, game_type: int | None = None) -> SkaterDistanceTop10:
        """Retrieve top 10 skaters by skating distance."""
        key = self._edge_cache_key("distance_10", season, game_type, pos, strength, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_distance_10(
                pos=pos, strength=strength, sort=sort, season=season, game_type=game_type,
            ),
            lambda d: SkaterDistanceTop10.from_list(d or []),
        )

    def edge_speed_top_10(self, pos: str, sort: str,
                          season: int | None = None, game_type: int | None = None) -> SkaterSpeedTop10:
        """Retrieve top 10 fastest skaters."""
        key = self._edge_cache_key("speed_10", season, game_type, pos, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skating_speed_10(
                pos=pos, sort=sort, season=season, game_type=game_type,
            ),
            lambda d: SkaterSpeedTop10.from_list(d or []),
        )

    def edge_zone_time_top_10(self, pos: str, strength: str, sort: str,
                              season: int | None = None, game_type: int | None = None) -> SkaterZoneTimeTop10:
        """Retrieve top 10 skaters by zone time."""
        key = self._edge_cache_key("zone_time_10", season, game_type, pos, strength, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_zone_time_10(
                pos=pos, strength=strength, sort=sort, season=season, game_type=game_type,
            ),
            lambda d: SkaterZoneTimeTop10.from_list(d or []),
        )

    def edge_shot_speed_top_10(self, pos: str, sort: str,
                               season: int | None = None, game_type: int | None = None) -> SkaterShotSpeedTop10:
        """Retrieve top 10 skaters by shot speed."""
        key = self._edge_cache_key("shot_speed_10", season, game_type, pos, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_shot_speed_10(
                pos=pos, sort=sort, season=season, game_type=game_type,
            ),
            lambda d: SkaterShotSpeedTop10.from_list(d or []),
        )

    def edge_shot_location_top_10(self, category: str, sort: str,
                                  season: int | None = None, game_type: int | None = None) -> SkaterShotLocationTop10:
        """Retrieve top 10 skaters by shot location."""
        key = self._edge_cache_key("shot_location_10", season, game_type, category, sort)
        return self._edge_fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_shot_location_10(
                category=category, sort=sort, season=season, game_type=game_type,
            ),
            lambda d: SkaterShotLocationTop10.from_list(d or []),
        )
