"""
PLAYOFF BRACKET SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .bracket_result import PlayoffBracketResult

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class PlayoffBracket(CacheFetchMixin):
    """
    Playoff bracket sub-resource.

    Provides the full bracket for a playoff year, with all series across all rounds.

    Accessed via `playoffs.bracket`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.playoffs.bracket")
        self._ttl: int = 60 * 60 * 6

    def get_bracket(self, year: int) -> PlayoffBracketResult:
        """
        Retrieve the full playoff bracket for a year.

        Args:
            year (int): Year in YYYY format (e.g. 2024).
        """
        cache_key = f"playoffs:bracket:{year}"
        return self._fetch(
            cache_key,
            lambda: self._client._api.api_web.call_nhl_playoffs.get_bracket(year=year),
            self._logger, self._cache, self._ttl,
            PlayoffBracketResult.from_dict,
        )
