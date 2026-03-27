"""
GOALIE EDGE STATS
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .goalie_details import GoalieDetails
from .goalie_comparison import GoalieComparison
from .goalie_5v5 import GoalieFiveVFive
from .goalie_shot_location import GoalieShotLocation
from .goalie_save_pctg import GoalieSavePctg
from .cat_goalie_details import CatGoalieDetails
from .......core.cache import get_cache
from .......core.utilities import _check_cache

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GoalieEdge:
    """
    Per-player goalie NHL Edge sub-resource.

    Provides structured access to a goalie's NHL Edge statistical data,
    including details, comparison, 5v5 save percentage, shot location,
    overall save percentage, and CAT details.

    Instances of this class are accessed via `Stats.edge()`.
    """
    def __init__(self, pid: int, client: NhlClient):
        self._pid = pid
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.player.stats.edge.goalie")
        self._base_key: str = f"player:{pid}:edge:goalie"
        self._ttl: int = 60 * 60 * 1

        self._logger.debug(f"{self._pid} GoalieEdge initialized")

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

    def details(self, season: int | None = None, game_type: int | None = None) -> GoalieDetails:
        """Retrieve NHL Edge ranking and stat summaries for the goalie."""
        return self._fetch(
            "details",
            self._client._api.api_web.call_nhl_edge_goalies.get_goalie_details,
            GoalieDetails, season, game_type,
        )

    def comparison(self, season: int | None = None, game_type: int | None = None) -> GoalieComparison:
        """Retrieve NHL Edge drill-down comparison data for the goalie."""
        return self._fetch(
            "comparison",
            self._client._api.api_web.call_nhl_edge_goalies.get_goalie_comparison,
            GoalieComparison, season, game_type,
        )

    def five_v_five(self, season: int | None = None, game_type: int | None = None) -> GoalieFiveVFive:
        """Retrieve 5v5 save percentage detail for the goalie."""
        return self._fetch(
            "five_v_five",
            self._client._api.api_web.call_nhl_edge_goalies.get_goalie_5v5,
            GoalieFiveVFive, season, game_type,
        )

    def shot_location(self, season: int | None = None, game_type: int | None = None) -> GoalieShotLocation:
        """Retrieve shot location detail for the goalie."""
        return self._fetch(
            "shot_location",
            self._client._api.api_web.call_nhl_edge_goalies.get_shot_location,
            GoalieShotLocation, season, game_type,
        )

    def save_pctg(self, season: int | None = None, game_type: int | None = None) -> GoalieSavePctg:
        """Retrieve overall save percentage detail for the goalie."""
        return self._fetch(
            "save_pctg",
            self._client._api.api_web.call_nhl_edge_goalies.get_save_pctg,
            GoalieSavePctg, season, game_type,
        )

    def cat_details(self, season: int | None = None, game_type: int | None = None) -> CatGoalieDetails:
        """Retrieve CAT endpoint NHL Edge details for the goalie."""
        return self._fetch(
            "cat_details",
            self._client._api.api_web.call_nhl_edge_goalies.get_cat_goalie_details,
            CatGoalieDetails, season, game_type,
        )
