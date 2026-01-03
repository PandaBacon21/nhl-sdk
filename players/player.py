"""
Player Object
"""

from typing import Optional
from datetime import datetime

from ..resources.api_web import players
from .player_bio import Bio



class Player: 
    def __init__(self, player_id: int): 
        self._pid: int = player_id
        self._raw: Optional[dict] = None
        self._fetch_time: Optional[datetime] = None

        self._fetch_player()

    def __repr__(self): 
        return f"Player(pid: {self._pid})"
    
    def __str__(self): 
        if self.bio:
            return f"{self.bio.first_name} {self.bio.last_name}, playerId: {self._pid}" 
        else: 
            return f"Player(pid: {self._pid})"

    def _fetch_player(self) -> dict: 
        if self._raw is None: 
            res = players._get_player_info(pid=self._pid)
            if not res["ok"]:
                raise RuntimeError(res.get("error", f"Failed to fetch player: {self._pid}"))
            self._raw = res["data"]
            self._fetch_time = datetime.now()
            print(f"Player data retrieved for Player: {self._pid}")
        assert self._raw 
        return self._raw

    def _clear(self) -> None: 
        print(f"Clearing Player {self._pid} data")
        self._raw = None
        print(f"Player {self._pid} data cleared")


    def refresh(self) -> None:  
        self._clear()
        print(f"Refreshing data for Player {self._pid}")
        self._fetch_player()    

    @property
    def bio(self) -> "Bio":
        data = self._fetch_player()
        return Bio(data=data)
    
    # raw get_player_info() api response
    def raw(self) -> dict: 
        return self._fetch_player()