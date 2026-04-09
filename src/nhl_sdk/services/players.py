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
    from nhl_sdk.client import NhlClient

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
        position: str | None = None,
    ) -> list[PlayerMilestone]:
        """
        Return a list of upcoming milestones across the league.

        By default returns both skater and goalie milestones combined.
        Use ``position`` to restrict to one group.

        Parameters
        ----------
        milestone : str | None
            Filter by milestone type (e.g. "Goals", "Assists", "Points", "Wins").
        game_type : int | None
            Filter by game type (2 = regular season, 3 = playoffs).
        limit : int | None
            Maximum number of results per position group. Pass -1 to return all.
        position : str | None
            ``"s"`` for skaters only, ``"g"`` for goalies only, or ``None`` for both.
        """
        parts: list[str] = []
        if milestone is not None:
            parts.append(f'milestone="{milestone}"')
        if game_type is not None:
            parts.append(f"gameTypeId={game_type}")
        cayenne_exp = " and ".join(parts) if parts else None

        pos = (position or "").lower()
        ttl = 60 * 60
        stats_players = self._client._api.api_stats.call_nhl_sdk_players

        def _build(d: dict) -> list[PlayerMilestone]:
            return [PlayerMilestone.from_dict(m) for m in (d.get("data") or [])]

        results: list[PlayerMilestone] = []

        if pos != "g":
            key = f"players:milestones:s:{milestone or 'all'}:{game_type or 'all'}:{limit or 'all'}"
            results += self._fetch(
                key,
                lambda: stats_players.get_skater_milestones(cayenne_exp=cayenne_exp, limit=limit),
                self._logger, self._cache, ttl,
                _build,
            )

        if pos != "s":
            key = f"players:milestones:g:{milestone or 'all'}:{game_type or 'all'}:{limit or 'all'}"
            results += self._fetch(
                key,
                lambda: stats_players.get_goalie_milestones(cayenne_exp=cayenne_exp, limit=limit),
                self._logger, self._cache, ttl,
                _build,
            )

        return results

    def query(
        self,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        """
        Query raw player records from the NHL Stats API.

        Returns basic player information filterable via cayenneExp expressions.

        Parameters
        ----------
        cayenne_exp : str | None
            Filter expression (e.g. ``"active=1"``).
        sort : str | None
            Field to sort by.
        dir : str | None
            Sort direction ("ASC" or "DESC").
        start : int | None
            Pagination offset.
        limit : int | None
            Maximum results (-1 for all).
        """
        key = f"players:query:{cayenne_exp or 'all'}:{sort}:{start}:{limit}"
        ttl = 60 * 60
        return self._fetch(
            key,
            lambda: self._client._api.api_stats.call_nhl_sdk_players.get_players(
                cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
            ),
            self._logger, self._cache, ttl,
            lambda d: d.get("data") or [],
        )
