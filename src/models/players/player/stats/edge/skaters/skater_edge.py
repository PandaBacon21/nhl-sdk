"""
SKATER EDGE STATS
"""
from __future__ import annotations
import logging
from typing import Optional, TYPE_CHECKING

from .skater_details import SkaterDetails
from .skater_comparison import SkaterComparison
from .skating_distance import SkatingDistance
from .skating_speed import SkatingSpeed
from .zone_time import ZoneTime
from .shot_speed import ShotSpeed
from .shot_location import ShotLocation
from .cat_skater_details import CatSkaterDetails
from .......core.cache import get_cache
from .......core.utilities import _check_cache

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class SkaterEdge:
    """
    Per-player skater NHL Edge sub-resource.

    Provides structured access to a skater's NHL Edge statistical data,
    including details, comparison, skating distance/speed,
    zone time, shot speed/location, and CAT details.

    Instances of this class are accessed via `Stats.edge.skater`.
    """
    def __init__(self, pid: int, client: NhlClient):
        self._pid = pid
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.player.stats.edge.skater")
        self._base_key: str = f"player:{pid}:edge:skater"
        self._ttl: int = 60 * 60 * 1

        self._logger.debug(f"{self._pid} SkaterEdge initialized")

    def _cache_key(self, name: str, season: int | None, game_type: int | None) -> str:
        if season and game_type:
            return f"{self._base_key}:{name}:{season}:{game_type}"
        return f"{self._base_key}:{name}:now"

    def _fetch(self, name: str, api_fn, model_cls, season: int | None, game_type: int | None):
        key = self._cache_key(name, season, game_type)
        cached = _check_cache(cache=self._cache, cache_key=key)
        if cached is not None:
            self._logger.debug(f"{key}: Cache Hit")
            return cached.data
        self._logger.debug(f"{key}: Cache Miss")
        res = api_fn(pid=self._pid, season=season, game_type=game_type)
        result = model_cls.from_dict(res.data)
        self._cache.set(key=key, data=result, ttl=self._ttl)
        self._logger.debug(f"{key}: Cached | ttl: {self._ttl}")
        return result

    def details(self, season: Optional[int] = None, game_type: Optional[int] = None) -> SkaterDetails:
        """Retrieve NHL Edge ranking and stat summaries for the skater."""
        return self._fetch(
            "details",
            self._client._api.api_web.call_nhl_edge_skaters.get_skater_details,
            SkaterDetails, season, game_type,
        )

    def comparison(self, season: Optional[int] = None, game_type: Optional[int] = None) -> SkaterComparison:
        """Retrieve NHL Edge drill-down comparison data for the skater."""
        return self._fetch(
            "comparison",
            self._client._api.api_web.call_nhl_edge_skaters.get_skater_comparison,
            SkaterComparison, season, game_type,
        )

    def skating_distance(self, season: Optional[int] = None, game_type: Optional[int] = None) -> SkatingDistance:
        """Retrieve skating distance detail for the skater."""
        return self._fetch(
            "skating_distance",
            self._client._api.api_web.call_nhl_edge_skaters.get_skating_distance,
            SkatingDistance, season, game_type,
        )

    def skating_speed(self, season: Optional[int] = None, game_type: Optional[int] = None) -> SkatingSpeed:
        """Retrieve skating speed detail for the skater."""
        return self._fetch(
            "skating_speed",
            self._client._api.api_web.call_nhl_edge_skaters.get_skating_speed,
            SkatingSpeed, season, game_type,
        )

    def zone_time(self, season: Optional[int] = None, game_type: Optional[int] = None) -> ZoneTime:
        """Retrieve zone time detail for the skater."""
        return self._fetch(
            "zone_time",
            self._client._api.api_web.call_nhl_edge_skaters.get_zone_time,
            ZoneTime, season, game_type,
        )

    def shot_speed(self, season: Optional[int] = None, game_type: Optional[int] = None) -> ShotSpeed:
        """Retrieve shot speed detail for the skater."""
        return self._fetch(
            "shot_speed",
            self._client._api.api_web.call_nhl_edge_skaters.get_shot_speed,
            ShotSpeed, season, game_type,
        )

    def shot_location(self, season: Optional[int] = None, game_type: Optional[int] = None) -> ShotLocation:
        """Retrieve shot location detail for the skater."""
        return self._fetch(
            "shot_location",
            self._client._api.api_web.call_nhl_edge_skaters.get_shot_location,
            ShotLocation, season, game_type,
        )

    def cat_details(self, season: Optional[int] = None, game_type: Optional[int] = None) -> CatSkaterDetails:
        """Retrieve CAT endpoint NHL Edge details for the skater."""
        return self._fetch(
            "cat_details",
            self._client._api.api_web.call_nhl_edge_skaters.get_cat_skater_details,
            CatSkaterDetails, season, game_type,
        )
