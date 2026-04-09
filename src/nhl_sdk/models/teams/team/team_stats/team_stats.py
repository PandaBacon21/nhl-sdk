"""
TEAM STATS SUB-RESOURCE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin
from .team_stats_result import TeamStatsResult
from .team_season_game_types import TeamSeasonGameTypes
from .team_scoreboard import TeamScoreboard
from .team_aggregate_summary import TeamAggregateSummary
from .team_ref import TeamRef
from ..edge import TeamEdge

if TYPE_CHECKING:
    from nhl_sdk.client import NhlClient


class TeamStats(CacheFetchMixin):
    """
    TeamStats sub-resource.

    Provides access to per-team skater and goalie stats, season/game-type
    metadata, and the current team scoreboard.

    Accessed via ``team.stats`` on a ``Team`` object.
    """
    def __init__(self, client: NhlClient, abbrev: str, team_id: int) -> None:
        self._client = client
        self._abbrev = abbrev
        self._team_id = team_id
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.teams.stats")
        self._ttl: int = 60 * 60 * 1

    def get_team_stats(
        self,
        season: int | None = None,
        g_type: int | None = None,
    ) -> TeamStatsResult:
        """
        Retrieve skater and goalie stats for the team.

        Args:
            season (int, optional): Season in YYYYYYYY format. Defaults to current season.
            g_type (int, optional): Game type (e.g. ``2`` for regular season). Required when ``season`` is provided.
        """
        team = self._abbrev
        key = f"teams:stats:{team}:{season}:{g_type}" if season and g_type else f"teams:stats:{team}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_teams.get_team_stats(team=team, season=season, g_type=g_type),
            self._logger, self._cache, self._ttl,
            TeamStatsResult.from_dict,
        )

    def get_game_types_per_season(self) -> list[TeamSeasonGameTypes]:
        """
        Retrieve the list of seasons and game types available for the team.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:stats:{team}:seasons",
            lambda: self._client._api.api_web.call_nhl_teams.get_game_types_per_season(team=team),
            self._logger, self._cache, self._ttl,
            lambda d: [TeamSeasonGameTypes.from_dict(s) for s in d or []],
        )

    def get_team_scoreboard(self) -> TeamScoreboard:
        """
        Retrieve the current scoreboard for the team.
        """
        team = self._abbrev
        return self._fetch(
            f"teams:scoreboard:{team}:now",
            lambda: self._client._api.api_web.call_nhl_teams.get_team_scoreboard(team=team),
            self._logger, self._cache, self._ttl,
            TeamScoreboard.from_dict,
        )

    def get_summary(
        self,
        season: int | None = None,
        g_type: int | None = None,
    ) -> TeamAggregateSummary | None:
        """
        Retrieve aggregate team performance stats from the NHL Stats API.

        Returns team-level metrics such as goals for/against, win percentages,
        power play and penalty kill rates, faceoff win percentage, and more.
        This is distinct from ``get_team_stats`` which returns per-player stats.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format (e.g. 20232024). Defaults to current season.
        g_type : int | None
            Game type (2 = regular season, 3 = playoffs). Required with season.
        """
        team_id = self._team_id
        key = (
            f"teams:aggregate:{team_id}:{season}:{g_type}"
            if season and g_type
            else f"teams:aggregate:{team_id}:now"
        )

        parts = [f"teamId={team_id}"]
        if season:
            parts.append(f"seasonId={season}")
        if g_type:
            parts.append(f"gameTypeId={g_type}")
        cayenne_exp = " and ".join(parts)

        def _builder(d: dict) -> TeamAggregateSummary | None:
            items = d.get("data") or []
            return TeamAggregateSummary.from_dict(items[0]) if items else None

        return self._fetch(
            key,
            lambda: self._client._api.api_stats.call_nhl_sdk_teams.get_team_stats(
                report="summary", cayenne_exp=cayenne_exp
            ),
            self._logger, self._cache, self._ttl,
            _builder,
        )


    def get_team_ref(self) -> TeamRef | None:
        """
        Retrieve basic team reference data for this team from the NHL Stats API.

        Returns team identity fields: id, tricode, full name, franchise id, and league id.
        """
        team_id = self._team_id
        def _build(d: dict) -> TeamRef | None:
            items = d.get("data") or []
            return TeamRef.from_dict(items[0]) if items else None
        return self._fetch(
            f"teams:ref:{team_id}",
            lambda: self._client._api.api_stats.call_nhl_sdk_teams.get_team_by_id(team_id=team_id),
            self._logger, self._cache, self._ttl * 24,
            _build,
        )

    @property
    def edge(self) -> TeamEdge:
        """
        Access NHL Edge stats for the team.

        Returns a TeamEdge sub-resource with the team ID baked in.
        """
        return TeamEdge(self._client, self._team_id)
