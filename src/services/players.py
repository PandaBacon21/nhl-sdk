"""
PLAYERS COLLECTION
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..core.utilities import CacheFetchMixin
from ..core.cache import get_cache
from ..models.players import Spotlight, Leaders, Player
from ..models.players.player.achievements import PlayerMilestone

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class Players(CacheFetchMixin):
    """
    Players Collection

    This is the primary interface for player related data.

    This interface exposes methods for retrieving individual Player
    objects and access player-related aggregates such as stat leaders.

    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.players")
        self._ttl: int = 60 * 60 * 6

    def get(self, pid: int) -> Player:
        """
        Return a Player object for the given NHL player ID.

        Parameters
        ----------
        pid : int
            Unique player Id
        """
        self._logger.debug(f"GET Player({pid})")
        return Player(player_id=pid, client=self._client)

    @property
    def spotlight(self) -> list[Spotlight]:
        """
        Return a list of currently Spotlighted Players
        """
        return self._fetch(
            "players:spotlight",
            lambda: self._client._api.api_web.call_nhl_players.get_player_spotlight(),
            self._logger, self._cache, self._ttl,
            lambda d: [Spotlight.from_dict(p) for p in d or []],
        )

    @property
    def leaders(self) -> Leaders:
        """
        Return leaders of various statistics for skaters and goalies
        """
        self._logger.debug("Retrieve Players Leaders")
        return Leaders(self._client)

    def milestones(
        self,
        milestone: str | None = None,
        game_type: int | None = None,
        limit: int | None = None,
    ) -> list[PlayerMilestone]:
        """
        Return a list of upcoming skater milestones across the league.

        Parameters
        ----------
        milestone : str | None
            Filter by milestone type (e.g. "Goals", "Assists", "Points").
        game_type : int | None
            Filter by game type (2 = regular season, 3 = playoffs).
        limit : int | None
            Maximum number of results. Pass -1 to return all.
        """
        parts: list[str] = []
        if milestone is not None:
            parts.append(f'milestone="{milestone}"')
        if game_type is not None:
            parts.append(f"gameTypeId={game_type}")
        cayenne_exp = " and ".join(parts) if parts else None

        key = f"players:milestones:{milestone or 'all'}:{game_type or 'all'}:{limit or 'all'}"
        ttl = 60 * 60

        return self._fetch(
            key,
            lambda: self._client._api.api_stats.call_nhl_stats_players.get_skater_milestones(
                cayenne_exp=cayenne_exp, limit=limit
            ),
            self._logger, self._cache, ttl,
            lambda d: [PlayerMilestone.from_dict(m) for m in (d.get("data") or [])],
        )
