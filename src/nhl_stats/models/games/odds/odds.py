"""
PARTNER ODDS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .odds_result import PartnerOddsResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class PartnerOdds(CacheFetchMixin):
    """
    Partner odds sub-resource.

    Provides access to partner betting odds for games in a specific country.

    Accessed via `games.odds`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.games.odds")
        self._ttl: int = 60 * 5

    def get_odds(self, country_code: str) -> PartnerOddsResult:
        """
        Retrieve partner odds for games in a specific country.

        Args:
            country_code (str): Official country code (e.g. "US", "CA").
        """
        return self._fetch(
            f"games:odds:{country_code}",
            lambda: self._client._api.api_web.call_nhl_games.get_odds(country_code=country_code),
            self._logger, self._cache, self._ttl,
            PartnerOddsResult.from_dict,
        )
