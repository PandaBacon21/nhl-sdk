"""
DRAFT TRACKER SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.cache import get_cache
from ....core.utilities import CacheFetchMixin
from .tracker_result import DraftTrackerResult

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient


class DraftTracker(CacheFetchMixin):
    """
    Draft tracker sub-resource.

    Provides access to the current draft tracker with live pick data.

    Accessed via `draft.tracker`.
    """
    def __init__(self, client: NhlClient) -> None:
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.draft.tracker")
        self._ttl: int = 60

    def get_tracker_now(self) -> DraftTrackerResult:
        """
        Retrieve the current draft tracker with all picks in the current round.
        """
        return self._fetch(
            "draft:tracker:now",
            lambda: self._client._api.api_web.call_nhl_draft.get_tracker_now(),
            self._logger, self._cache, self._ttl,
            DraftTrackerResult.from_dict,
        )
