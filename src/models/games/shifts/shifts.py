"""
SHIFTS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .shift_chart import ShiftChart

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GameShifts(CacheFetchMixin):
    """
    Shifts sub-resource.

    Provides access to shift chart data for a specific game.

    Accessed via `games.shifts`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.shifts")
        self._ttl: int = 60 * 60 * 1

    def get(self, game_id: int) -> ShiftChart:
        """
        Retrieve shift chart data for a specific game.

        Parameters
        ----------
        game_id : int
            NHL game ID.
        """
        return self._fetch(
            f"games:shifts:{game_id}",
            lambda: self._client._api.api_stats.call_nhl_stats_misc.get_shift_charts(game_id=game_id),
            self._logger, self._cache, self._ttl,
            lambda d: ShiftChart.from_dict(game_id=game_id, data=d),
        )
