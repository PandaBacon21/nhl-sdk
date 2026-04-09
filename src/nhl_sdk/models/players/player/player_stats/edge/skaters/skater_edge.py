"""
SKATER EDGE STATS
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .skater_details import SkaterDetails
from .skater_comparison import SkaterComparison
from .skating_distance import SkatingDistance
from .skating_speed import SkatingSpeed
from .skater_zone_time import ZoneTime
from .shot_speed import ShotSpeed
from .shot_location import ShotLocation
from .cat_skater_details import CatSkaterDetails
from .......core.cache import get_cache
from .......core.utilities import CacheFetchMixin

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient


class SkaterEdge(CacheFetchMixin):
    """
    Per-player skater NHL Edge sub-resource.

    Provides structured access to a skater's NHL Edge statistical data,
    including details, comparison, skating distance/speed,
    zone time, shot speed/location, and CAT details.

    Instances of this class are accessed via `Stats.edge()`.
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

    def details(self, season: int | None = None, game_type: int | None = None) -> SkaterDetails:
        """Retrieve NHL Edge ranking and stat summaries for the skater."""
        key = self._cache_key("details", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_details(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            SkaterDetails.from_dict,
        )

    def comparison(self, season: int | None = None, game_type: int | None = None) -> SkaterComparison:
        """Retrieve NHL Edge drill-down comparison data for the skater."""
        key = self._cache_key("comparison", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skater_comparison(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            SkaterComparison.from_dict,
        )

    def skating_distance(self, season: int | None = None, game_type: int | None = None) -> SkatingDistance:
        """Retrieve skating distance detail for the skater."""
        key = self._cache_key("skating_distance", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skating_distance(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            SkatingDistance.from_dict,
        )

    def skating_speed(self, season: int | None = None, game_type: int | None = None) -> SkatingSpeed:
        """Retrieve skating speed detail for the skater."""
        key = self._cache_key("skating_speed", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_skating_speed(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            SkatingSpeed.from_dict,
        )

    def zone_time(self, season: int | None = None, game_type: int | None = None) -> ZoneTime:
        """Retrieve zone time detail for the skater."""
        key = self._cache_key("zone_time", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_zone_time(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            ZoneTime.from_dict,
        )

    def shot_speed(self, season: int | None = None, game_type: int | None = None) -> ShotSpeed:
        """Retrieve shot speed detail for the skater."""
        key = self._cache_key("shot_speed", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_shot_speed(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            ShotSpeed.from_dict,
        )

    def shot_location(self, season: int | None = None, game_type: int | None = None) -> ShotLocation:
        """Retrieve shot location detail for the skater."""
        key = self._cache_key("shot_location", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_shot_location(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            ShotLocation.from_dict,
        )

    def cat_details(self, season: int | None = None, game_type: int | None = None) -> CatSkaterDetails:
        """Retrieve CAT endpoint NHL Edge details for the skater."""
        key = self._cache_key("cat_details", season, game_type)
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_edge_skaters.get_cat_skater_details(
                pid=self._pid, season=season, game_type=game_type
            ),
            self._logger, self._cache, self._ttl,
            CatSkaterDetails.from_dict,
        )
