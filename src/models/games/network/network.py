"""
NETWORK SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .network_schedule import NetworkScheduleResult

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GameNetwork(CacheFetchMixin):
    """
    Network sub-resource.

    Provides access to the NHL Network TV broadcast schedule for the current
    day or a specific date.

    Accessed via `games.network`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.network")
        self._ttl: int = 60 * 60 * 1

    def get_tv_schedule(self, date: str | None = None) -> NetworkScheduleResult:
        """
        Retrieve the NHL Network TV broadcast schedule.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to the current day.
        """
        return self._fetch(
            f"games:network:tv-schedule:{date or 'now'}",
            lambda: self._client._api.api_web.call_nhl_games.get_tv_schedule(date=date),
            self._logger, self._cache, self._ttl,
            NetworkScheduleResult.from_dict,
        )
