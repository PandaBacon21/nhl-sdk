"""
NHL PLAYER EDGE LEADERS
"""
from __future__ import annotations
import logging
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import _check_cache
from .skater_landing import SkaterLanding
from .goalie_landing import GoalieLanding

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class EdgeLeaders(ABC):
    """Base class for NHL Edge leader resources. Provides shared caching and fetch logic."""
    def __init__(self, client: NhlClient, position: str) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger(f"nhl_sdk.leaders.edge.{position}")
        self._ttl: int = 60 * 60 * 1
        self._pos = position

    def _cache_key(self, name: str, season: int | None, game_type: int | None, *args: str) -> str:
        base = f"leaders:edge:{self._pos}:{name}"
        suffix = f":{season}:{game_type}" if season and game_type else ":now"
        extra = "".join(f":{a}" for a in args if a)
        return base + suffix + extra

    def _fetch(self, key: str, api_fn, model_cls=None):
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = api_fn()
        result = model_cls.from_dict(res.data) if model_cls else res.data
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    @abstractmethod
    def landing(self, season: Optional[int] = None, game_type: Optional[int] = None) -> SkaterLanding | GoalieLanding:
        ...


class SkaterEdgeLeaders(EdgeLeaders):
    """
    Skater NHL Edge leaders sub-resource.

    Provides access to league-wide skater Edge leaderboards — landing page
    leaders and top-10 lists for distance, speed, zone time, shot speed,
    and shot location. Not player-specific; no pid required.

    Instances of this class are accessed via `leaders.skaters(...).edge`.
    """
    def __init__(self, client: NhlClient) -> None:
        super().__init__(client=client, position="skater")

    def landing(self, season: Optional[int] = None, game_type: Optional[int] = None) -> SkaterLanding:
        """Retrieve skater Edge landing leaders."""
        key = self._cache_key("landing", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_landing(
                season=season, game_type=game_type,
            ),
            SkaterLanding,
        )

    def distance_top_10(self, pos: str, strength: str, sort: str,
                        season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 skaters by skating distance."""
        key = self._cache_key("distance_10", season, game_type, pos, strength, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_distance_10(
                pos=pos, strength=strength, sort=sort, season=season, game_type=game_type,
            ),
        )

    def speed_top_10(self, pos: str, sort: str,
                     season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 fastest skaters."""
        key = self._cache_key("speed_10", season, game_type, pos, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skating_speed_10(
                pos=pos, sort=sort, season=season, game_type=game_type,
            ),
        )

    def zone_time_top_10(self, pos: str, strength: str, sort: str,
                         season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 skaters by zone time."""
        key = self._cache_key("zone_time_10", season, game_type, pos, strength, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_zone_time_10(
                pos=pos, strength=strength, sort=sort, season=season, game_type=game_type,
            ),
        )

    def shot_speed_top_10(self, pos: str, sort: str,
                          season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 skaters by shot speed."""
        key = self._cache_key("shot_speed_10", season, game_type, pos, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_shot_speed_10(
                pos=pos, sort=sort, season=season, game_type=game_type,
            ),
        )

    def shot_location_top_10(self, category: str, sort: str,
                             season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 skaters by shot location."""
        key = self._cache_key("shot_location_10", season, game_type, category, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_shot_location_10(
                category=category, sort=sort, season=season, game_type=game_type,
            ),
        )


class GoalieEdgeLeaders(EdgeLeaders):
    """
    Goalie NHL Edge leaders sub-resource.

    Provides access to league-wide goalie Edge leaderboards — landing page
    leaders and top-10 lists for 5v5 save percentage, shot location,
    and overall save percentage. Not player-specific; no pid required.

    Instances of this class are accessed via `leaders.goalies(...).edge`.
    """
    def __init__(self, client: NhlClient) -> None:
        super().__init__(client=client, position="goalie")

    def landing(self, season: Optional[int] = None, game_type: Optional[int] = None) -> GoalieLanding:
        """Retrieve goalie Edge landing leaders."""
        key = self._cache_key("landing", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalie_landing(
                season=season, game_type=game_type,
            ),
            GoalieLanding,
        )

    def five_v_five_top_10(self, sort: str,
                           season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 goalies by 5v5 save percentage."""
        key = self._cache_key("5v5_10", season, game_type, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalies_5v5_10(
                sort=sort, season=season, game_type=game_type,
            ),
        )

    def shot_location_top_10(self, category: str, sort: str,
                             season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 goalies by shot location."""
        key = self._cache_key("shot_location_10", season, game_type, category, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalie_shot_location_10(
                category=category, sort=sort, season=season, game_type=game_type,
            ),
        )

    def save_pctg_top_10(self, sort: str,
                         season: Optional[int] = None, game_type: Optional[int] = None) -> list:
        """Retrieve top 10 goalies by save percentage."""
        key = self._cache_key("save_pctg_10", season, game_type, sort)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_goalies.get_goalie_save_pctg_10(
                sort=sort, season=season, game_type=game_type,
            ),
        )
