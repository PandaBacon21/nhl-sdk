"""
TEAMS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.cache.init_cache import get_cache
from ..resources.api_web import teams

if TYPE_CHECKING: 
    from nhl_stats.src.client import NhlClient

class Teams: 
    """
    Teams Collection

    This is the primary interface for Team related data. 
    """
    def __init__(self, client: NhlClient): 
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams")
        