"""
STREAMS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


class GameStreams(CacheFetchMixin):
    """
    Streams sub-resource.

    Provides access to the NHL where-to-watch streaming information.
    Note: this endpoint may be region-restricted.

    Accessed via `games.streams`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.streams")
        self._ttl: int = 60 * 60 * 1

    def get(self) -> dict:
        """
        Retrieve streaming service information.

        Returns the raw API response as a dict. The response structure
        may vary by region.
        """
        return self._fetch(
            "games:streams:now",
            lambda: self._client._api.api_web.call_nhl_games.get_streams(),
            self._logger, self._cache, self._ttl,
            lambda d: d,
        )
