"""
PLAYER CLASS
"""

from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ....core.utilities import _check_cache
from .profile import Profile
from .player_stats import PlayerStats
from .achievements import PlayerAchievements
from ....core.cache import get_cache

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient

class Player:
    """
    Represents a single NHL player.

    A Player object provides structured access to biographical and
    statistical data for an individual player. Data is fetched lazily
    from the NHL API and cached for the lifetime of the object.

    Use the Players collection to obtain Player instances.
    """
    def __init__(self, player_id: int, client: NhlClient):
        """
        Parameters
        ----------
        player_id : int
            Unique NHL player ID.
        client : NhlClient
            NHL API client used for requests and caching.
        """
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.player")
        self._pid: int = player_id
        self._landing_key: str = f"player:{self._pid}:landing"
        self._ttl: int = 60 * 60 * 6

        self._pos: str = "S"
        self._profile: Profile | None = None
        self._stats: PlayerStats | None = None
        self._achievements: PlayerAchievements | None = None

    def __repr__(self):
        """
        Return a string representation of the player.
        """
        return f"Player(pid: {self._pid})"

    def __str__(self):
        """
        Return a string representation of the player.
        """
        if self._profile:
            return f"{self.profile.first_name} {self.profile.last_name}, Player Id: {self._pid}"
        else:
            return f"Player Id: {self._pid}. Call .profile() to retrieve name."

    def _get_player_landing(self):
        """
        Retrieve from cache or NHL landing API for the specific player
        For internal use only
        """
        if self._cache is not None:
            cached = _check_cache(self._cache, self._landing_key)
            if cached is not None:
                self._logger.debug(f"{self._landing_key}: Cache Hit")
                self._pos = "G" if cached.data.get("position") == "G" else "S"
                return cached
            self._logger.debug(f"{self._landing_key}: Cache Miss")

        res = self._client._api.api_web.call_nhl_players.get_player_landing(pid=self._pid)

        if not res.ok:
            self._logger.warning(f"Player pid {self._pid} failed to fetch player landing")
            raise RuntimeError(res.data["error"] or f"Failed to fetch player landing: {self._pid}")
        self._pos = "G" if res.data.get("position") == "G" else "S"

        if self._cache is not None:
            cache_item = self._cache.set(key=self._landing_key, data=res.data, ttl=self._ttl)
            self._logger.debug(f"{self._landing_key}: Cached | ttl: {self._ttl}")
            return cache_item

        return res

    @property
    def profile(self) -> Profile:
        """
        Player biographical information.

        Returns
        -------
        Bio
            Structured biographical data such as name, birth details,
            physical attributes, position, and awards.
        """
        if self._profile:
            if self._cache is None or _check_cache(self._cache, self._landing_key):
                return self._profile
        data = self._get_player_landing()
        self._profile = Profile.from_dict(data=data.data)
        self._logger.debug(f"{self._pid} bio retrieved")
        return self._profile

    @property
    def stats(self) -> PlayerStats:
        """
        Player statistical information.

        Returns
        -------
        Stats
            Structured access to career totals, season statistics,
            featured stats, and recent games.
        """
        if self._stats:
            if self._cache is None or _check_cache(self._cache, self._landing_key):
                return self._stats
        data = self._get_player_landing()
        self._stats = PlayerStats(pos=self._pos, pid=self._pid, data=data.data, client=self._client)
        self._logger.debug(f"{self._pid} stats retrieved")
        return self._stats

    @property
    def achievements(self) -> PlayerAchievements:
        """
        Player career recognition and upcoming milestones.

        Returns
        -------
        PlayerAchievements
            Structured access to awards, badges, Hall of Fame status,
            top-100 ranking, and approaching statistical milestones.
        """
        if self._achievements:
            if self._cache is None or _check_cache(self._cache, self._landing_key):
                return self._achievements
        data = self._get_player_landing()
        self._achievements = PlayerAchievements(
            pid=self._pid, pos=self._pos, data=data.data, client=self._client
        )
        self._logger.debug(f"{self._pid} achievements retrieved")
        return self._achievements

