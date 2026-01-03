"""
PLAYER STATS OBJECT
"""

from __future__ import annotations
from typing import Any

class Stats: 
    def __init__(self, data: dict) -> None:
        self.career = None
        self.season = None
        self.last_5_games = None
        