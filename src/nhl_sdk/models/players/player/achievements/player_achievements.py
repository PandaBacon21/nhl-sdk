"""
PLAYER ACHIEVEMENTS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.utilities import CacheFetchMixin
from .....core.cache import get_cache
from .achievements import Achievements
from .award import Award
from .badge import Badge
from .player_milestone import PlayerMilestone

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient


class PlayerAchievements(CacheFetchMixin):
    """
    Achievement and milestone data for a single player.

    Exposes career achievements (HHOF, top-100, awards, badges) from the
    player landing response, and lazily loads upcoming milestone data
    from the NHL Stats API.
    """
    def __init__(self, pid: int, pos: str, data: dict, client: NhlClient):
        self._pid = pid
        self._pos = pos
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.player_achievements")
        self._ttl: int = 60 * 60

        self._ach = Achievements.from_dict(data)

    @property
    def in_top_100_all_time(self) -> bool | None:
        """Whether the player is ranked in the top 100 all-time."""
        return self._ach.in_top_100_all_time

    @property
    def in_hhof(self) -> bool | None:
        """Whether the player is inducted into the Hockey Hall of Fame."""
        return self._ach.in_hhof

    @property
    def awards(self) -> list[Award]:
        """List of NHL awards won by the player."""
        return self._ach.awards

    @property
    def badges(self) -> list[Badge]:
        """List of achievement badges earned by the player."""
        return self._ach.badges

    def milestones(self, game_type: int | None = None) -> list[PlayerMilestone] | None:
        """
        Upcoming statistical milestones the player is approaching.

        Parameters
        ----------
        game_type : int | None
            Filter by game type (2 = regular season, 3 = playoffs).
            Omit to return all game types.

        Returns
        -------
        list[PlayerMilestone] | None
            List of approaching milestones, or None if the player has none.
        """
        key = f"player:{self._pid}:milestones:{game_type or 'all'}"

        cayenne_exp = f"playerId={self._pid}"
        if game_type is not None:
            cayenne_exp += f" and gameTypeId={game_type}"

        stats_players = self._client._api.api_stats.call_nhl_sdk_players
        api_fn = (
            stats_players.get_goalie_milestones
            if self._pos == "G"
            else stats_players.get_skater_milestones
        )

        def _builder(d: dict) -> list[PlayerMilestone] | None:
            items = [PlayerMilestone.from_dict(m) for m in (d.get("data") or [])]
            return items if items else None

        return self._fetch(
            key,
            lambda: api_fn(cayenne_exp=cayenne_exp),
            self._logger, self._cache, self._ttl,
            _builder,
        )
