"""
PLAYER CLASS
"""

from typing import Optional
from datetime import datetime

from ..resources.api_web import _get_player_info
from .bio import Bio
from .stats import Stats


class Player: 
    """
    Represents a single NHL player.

    A Player object provides structured access to biographical and
    statistical data for an individual player. Data is fetched lazily
    from the NHL API and cached for the lifetime of the object.

    Use `refresh()` to clear cached data and retrieve the latest
    information from the API.

    Use the Players collection to obtain Player instances.
    """
    def __init__(self, player_id: int): 
        """
        Parameters
        ----------
        data : int
            Unique player Id
        """
        self._pid: int = player_id
        self._raw: Optional[dict] = None
        self._fetch_time: Optional[datetime] = None

    def __repr__(self): 
        return f"Player(pid: {self._pid})"
    
    def __str__(self): 
        # if self.bio:
        return f"{self.bio.first_name} {self.bio.last_name}, playerId: {self._pid}" 
        # else: 
        #     return f"Player(pid: {self._pid})"

    def _fetch_player(self) -> dict: 
        if self._raw is None: 
            res = _get_player_info(pid=self._pid)
            if not res["ok"]:
                raise RuntimeError(res.get("error", f"Failed to fetch player: {self._pid}"))
            self._raw = res["data"]
            self._fetch_time = datetime.now()
            print(f"Player data retrieved for Player: {self._pid}")

        if self._raw is None:
            raise RuntimeError("Player data was not loaded")
        return self._raw

    def _clear(self) -> None: 
        print(f"Clearing Player {self._pid} data")
        self._raw = None
        print(f"Player {self._pid} data cleared")

    def refresh(self) -> None:  
        """
        Refresh player data from the NHL API.

        Clears any cached data and immediately re-fetches the
        latest player information.
        """
        self._clear()
        print(f"Refreshing data for Player {self._pid}")
        self._fetch_player()    

    @property
    def bio(self) -> Bio:
        """
        Player biographical information.

        Returns
        -------
        Bio
            Structured biographical data such as name, birth details,
            physical attributes, position, and awards.
        """
        data = self._fetch_player()
        return Bio(data=data)
    
    @property
    def stats(self) -> Stats:
        """
        Player statistical information.

        Returns
        -------
        Stats
            Structured access to career totals, season statistics,
            featured stats, and recent games.
        """
        data = self._fetch_player()
        return Stats(data=data)
    
    def raw(self) -> dict: 
        """
        Return the raw NHL API response for this player.

        This mirrors the underlying NHL endpoint response for: 
        https://api-web.nhle.com/v1/player/{playerId}/landing 
        
        Contains all fields returned by the API without additional processing.

        Returns
        -------
        dict
            Raw player data.
        """
        return self._fetch_player()