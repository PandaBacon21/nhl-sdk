"""
NHL CLIENT
"""

from .services import Players, Teams
from .core.cache import Cache
from .resources import API

class NhlClient:
    """
    Main NHL Client

    This is the main interface for NHL SDK. 
    Exposes Players and Teams collections (will expand to League, Edge, etc over time)

    """
    def __init__(self): 
        self._api = API()
        self.cache = Cache()
        self.players = Players(self)
        self.teams = Teams(self)
