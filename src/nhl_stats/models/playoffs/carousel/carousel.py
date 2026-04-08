"""
PLAYOFF CAROUSEL SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .carousel_result import PlayoffCarouselResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class PlayoffCarousel(CacheFetchMixin):
    """
    Playoff carousel sub-resource.

    Provides an overview of each playoff series for a given season.

    Accessed via `playoffs.carousel`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.playoffs.carousel")
        self._ttl: int = 60 * 60

    def get_carousel(self, season: int) -> PlayoffCarouselResult:
        """
        Retrieve the playoff series carousel for a season.

        Args:
            season (int): Season in YYYYYYYY format (e.g. 20242025).
        """
        cache_key = f"playoffs:carousel:{season}"
        return self._fetch(
            cache_key,
            lambda: self._client._api.api_web.call_nhl_playoffs.get_carousel(season=season),
            self._logger, self._cache, self._ttl,
            PlayoffCarouselResult.from_dict,
        )
