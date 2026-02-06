"""
TEAMS COLLECTION
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from ..resources.api_web import teams

if TYPE_CHECKING: 
    from nhl_stats.src.client import NhlClient

class Teams: 
    """
    Teams Collection

    This is the primary interface for Team related data. 
    """
    def __init__(self, client: "NhlClient"): 
        self._client = client
        