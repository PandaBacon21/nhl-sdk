"""
PLAYER STATS OBJECT
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .player_featured_stats import Featured
from .player_career_stats import Career
from .season import Season, FeaturedGame
from .games import GameLogs
from .edge.skaters.skater_edge import SkaterEdge
from .edge.goalies.goalie_edge import GoalieEdge
from .reports import (
    SkaterSummaryReport, SkaterBioReport, SkaterFaceoffPctReport,
    SkaterFaceoffWinsReport, SkaterGoalsForAgainstReport, SkaterPenaltiesReport,
    SkaterPenaltyKillReport, SkaterPenaltyShotsReport, SkaterPowerPlayReport,
    SkaterPuckPossessionsReport, SkaterRealtimeReport, SkaterShotTypeReport,
    SkaterTimeOnIceReport, SkaterPercentagesReport,
    GoalieSummaryReport, GoalieBioReport, GoalieAdvancedReport,
    GoalieDaysRestReport, GoaliePenaltyShotsReport, GoalieSavesByStrengthReport,
    GoalieShootoutReport, GoalieStartedVsRelievedReport,
)
from .....core.cache import get_cache
from .....core.utilities import CacheFetchMixin

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient

class PlayerStats(CacheFetchMixin):
    """
    Player statistical sub-resource.

    Provides structured access to a player's statistical data,
    including featured stats, career totals, per-season statistics,
    recent game performance (last 5 games),
    and method for retrieving full season game logs.


    Instances of this class are accessed via `Player.stats`.
    """
    def __init__(self, pos: str, pid: int, data: dict, client: NhlClient):
        """
        Parameters
        ----------
        data : dict
            Raw player landing data as returned by the NHL API.
        """
        featured_stats: dict = data.get("featuredStats") or {}
        career_stats: dict = data.get("careerTotals") or {}

        self._pos = pos
        self._pid = pid
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.player.stats")

        self._game_key: str = f"player:{pid}:game-log"
        self._ttl: int = 60 * 60 * 1

        self.featured: Featured = Featured.from_dict(featured_stats)
        self.career: Career = Career.from_dict(career_stats)
        self.seasons = [Season.from_dict(season) for season in data.get("seasonTotals") or []]
        self.last_5_games = [FeaturedGame.from_dict(game) for game in data.get("last5Games") or []]
        self._logger.debug(f"{self._pid} Stats initialized")

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _build_cayenne(self, season: int | None, game_type: int | None) -> str:
        parts = [f"playerId={self._pid}"]
        if season:
            parts.append(f"seasonId={season}")
        if game_type:
            parts.append(f"gameTypeId={game_type}")
        return " and ".join(parts)

    def _report(self, endpoint: str, season: int | None, game_type: int | None, builder_fn):
        """Fetch a single-row report (first item in data array) with caching."""
        key = f"player:{self._pid}:{endpoint}:{season or 'now'}:{game_type or 2}"
        cayenne_exp = self._build_cayenne(season, game_type)
        stats_players = self._client._api.api_stats.call_nhl_stats_players

        def _build(d: dict):
            items = d.get("data") or []
            return builder_fn(items[0]) if items else None

        if self._pos == "G":
            api_fn = lambda: stats_players.get_goalie_stats(endpoint, cayenne_exp=cayenne_exp)
        else:
            api_fn = lambda: stats_players.get_skater_stats(endpoint, cayenne_exp=cayenne_exp)

        return self._fetch(key, api_fn, self._logger, self._cache, self._ttl, _build)

    # ------------------------------------------------------------------
    # Edge
    # ------------------------------------------------------------------

    def edge(self) -> SkaterEdge | GoalieEdge:
        """
        Player NHL Edge stats.

        Returns a SkaterEdge or GoalieEdge instance depending on the player's position.
        """
        if self._pos == "G":
            return GoalieEdge(pid=self._pid, client=self._client)
        return SkaterEdge(pid=self._pid, client=self._client)

    # ------------------------------------------------------------------
    # Shared reports (skater + goalie both have these)
    # ------------------------------------------------------------------

    def summary(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterSummaryReport | GoalieSummaryReport | None:
        """
        Retrieve the player's season summary stats from the NHL Stats API.

        Returns aggregate season-level stats including situational breakdowns
        (EV/PP/SH goals and points) not available in the player landing response.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format (e.g. 20232024). Defaults to current season.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs). Defaults to regular season.
        """
        key = f"player:{self._pid}:stats-summary:{season or 'now'}:{game_type or 2}"

        parts = [f"playerId={self._pid}"]
        if season:
            parts.append(f"seasonId={season}")
        if game_type:
            parts.append(f"gameTypeId={game_type}")
        cayenne_exp = " and ".join(parts)

        stats_players = self._client._api.api_stats.call_nhl_stats_players

        def _builder(d: dict) -> SkaterSummaryReport | GoalieSummaryReport | None:
            items = d.get("data") or []
            if not items:
                return None
            return (
                GoalieSummaryReport.from_dict(items[0])
                if self._pos == "G"
                else SkaterSummaryReport.from_dict(items[0])
            )

        if self._pos == "G":
            api_fn = lambda: stats_players.get_goalie_stats("summary", cayenne_exp=cayenne_exp)
        else:
            api_fn = lambda: stats_players.get_skater_stats("summary", cayenne_exp=cayenne_exp)

        return self._fetch(key, api_fn, self._logger, self._cache, self._ttl, _builder)

    def stats_bio(self) -> SkaterBioReport | GoalieBioReport | None:
        """
        Retrieve the player's career bio from the NHL Stats API.

        Returns career-level biographical info (birth details, draft, physical attributes).
        """
        key = f"player:{self._pid}:bios"
        cayenne_exp = f"playerId={self._pid}"
        stats_players = self._client._api.api_stats.call_nhl_stats_players

        def _build(d: dict) -> SkaterBioReport | GoalieBioReport | None:
            items = d.get("data") or []
            if not items:
                return None
            return (
                GoalieBioReport.from_dict(items[0])
                if self._pos == "G"
                else SkaterBioReport.from_dict(items[0])
            )

        if self._pos == "G":
            api_fn = lambda: stats_players.get_goalie_stats("bios", cayenne_exp=cayenne_exp)
        else:
            api_fn = lambda: stats_players.get_skater_stats("bios", cayenne_exp=cayenne_exp)

        return self._fetch(key, api_fn, self._logger, self._cache, self._ttl, _build)

    def penalty_shots(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterPenaltyShotsReport | GoaliePenaltyShotsReport | None:
        """
        Retrieve penalty shot stats from the NHL Stats API.

        Routes to skater or goalie endpoint based on player position.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns all seasons if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return self._report("penaltyShots", season, game_type, GoaliePenaltyShotsReport.from_dict)
        return self._report("penaltyShots", season, game_type, SkaterPenaltyShotsReport.from_dict)

    # ------------------------------------------------------------------
    # Skater-only reports
    # ------------------------------------------------------------------

    def faceoff_pct(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterFaceoffPctReport | None:
        """
        Retrieve the skater's faceoff percentage report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("faceoffpercentages", season, game_type, SkaterFaceoffPctReport.from_dict)

    def faceoff_wins(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterFaceoffWinsReport | None:
        """
        Retrieve the skater's faceoff wins report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("faceoffwins", season, game_type, SkaterFaceoffWinsReport.from_dict)

    def goals_for_against(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterGoalsForAgainstReport | None:
        """
        Retrieve the skater's goals for/against report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("goalsForAgainst", season, game_type, SkaterGoalsForAgainstReport.from_dict)

    def penalties(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterPenaltiesReport | None:
        """
        Retrieve the skater's penalties report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("penalties", season, game_type, SkaterPenaltiesReport.from_dict)

    def penalty_kill(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterPenaltyKillReport | None:
        """
        Retrieve the skater's penalty kill report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("penaltykill", season, game_type, SkaterPenaltyKillReport.from_dict)

    def powerplay(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterPowerPlayReport | None:
        """
        Retrieve the skater's power play report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("powerplay", season, game_type, SkaterPowerPlayReport.from_dict)

    def puck_possessions(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterPuckPossessionsReport | None:
        """
        Retrieve the skater's puck possessions report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("puckPossessions", season, game_type, SkaterPuckPossessionsReport.from_dict)

    def realtime(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterRealtimeReport | None:
        """
        Retrieve the skater's realtime stats report. Returns None for goalies.

        Includes hits, blocks, giveaways, takeaways, empty net stats, and missed shots.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("realtime", season, game_type, SkaterRealtimeReport.from_dict)

    def shot_type(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterShotTypeReport | None:
        """
        Retrieve the skater's shot type breakdown report. Returns None for goalies.

        Includes goals and shooting percentage broken down by shot type
        (wrist, slap, snap, backhand, tip-in, etc.).

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("shottype", season, game_type, SkaterShotTypeReport.from_dict)

    def time_on_ice(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterTimeOnIceReport | None:
        """
        Retrieve the skater's time on ice report. Returns None for goalies.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("timeonice", season, game_type, SkaterTimeOnIceReport.from_dict)

    def percentages(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> SkaterPercentagesReport | None:
        """
        Retrieve the skater's percentages report. Returns None for goalies.

        Includes Corsi/Fenwick (SAT/USAT), zone start percentages, and on-ice
        shooting/save percentages at 5v5.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos == "G":
            return None
        return self._report("percentages", season, game_type, SkaterPercentagesReport.from_dict)

    # ------------------------------------------------------------------
    # Goalie-only reports
    # ------------------------------------------------------------------

    def advanced(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> GoalieAdvancedReport | None:
        """
        Retrieve the goalie's advanced stats report. Returns None for skaters.

        Includes quality starts, complete games, regulation wins/losses, and goals
        for/against averages.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos != "G":
            return None
        return self._report("advanced", season, game_type, GoalieAdvancedReport.from_dict)

    def days_rest(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> GoalieDaysRestReport | None:
        """
        Retrieve the goalie's days-rest performance report. Returns None for skaters.

        Breaks down save percentage by number of days rest (0, 1, 2, 3, 4+).

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos != "G":
            return None
        return self._report("daysrest", season, game_type, GoalieDaysRestReport.from_dict)

    def saves_by_strength(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> GoalieSavesByStrengthReport | None:
        """
        Retrieve the goalie's saves-by-strength report. Returns None for skaters.

        Breaks down saves, shots against, and save percentage by game situation
        (even strength, power play, short-handed).

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos != "G":
            return None
        return self._report("savesByStrength", season, game_type, GoalieSavesByStrengthReport.from_dict)

    def shootout(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> GoalieShootoutReport | None:
        """
        Retrieve the goalie's shootout performance report. Returns None for skaters.

        Includes both season-level and career shootout stats.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos != "G":
            return None
        return self._report("shootout", season, game_type, GoalieShootoutReport.from_dict)

    def started_vs_relieved(
        self,
        season: int | None = None,
        game_type: int | None = None,
    ) -> GoalieStartedVsRelievedReport | None:
        """
        Retrieve the goalie's started vs relieved report. Returns None for skaters.

        Splits performance stats (wins, save%, etc.) between games started and
        games where the goalie came in as a reliever.

        Parameters
        ----------
        season : int | None
            Season in YYYYYYYY format. Returns most recent if omitted.
        game_type : int | None
            Game type (2 = regular season, 3 = playoffs).
        """
        if self._pos != "G":
            return None
        return self._report("startedVsRelieved", season, game_type, GoalieStartedVsRelievedReport.from_dict)

    # ------------------------------------------------------------------
    # Raw escape hatch
    # ------------------------------------------------------------------

    def report(
        self,
        report_type: str,
        *,
        season: int | None = None,
        game_type: int | None = None,
        is_aggregate: bool | None = None,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """
        Retrieve raw stats report data from the NHL Stats API.

        Escape hatch for any report type not covered by named methods.
        Returns the raw API response dict (``{"data": [...], "total": N}``).

        Parameters
        ----------
        report_type : str
            Report name (e.g. "summary", "bios", "realtime", "faceoffwins").
        season : int | None
            Season in YYYYYYYY format. Combined into cayenneExp automatically.
        game_type : int | None
            Game type. Combined into cayenneExp automatically.
        is_aggregate : bool | None
            Whether to aggregate stats across seasons/teams.
        cayenne_exp : str | None
            Custom filter expression. Overrides auto-built expression.
        sort : str | None
            Field to sort by.
        dir : str | None
            Sort direction ("ASC" or "DESC").
        start : int | None
            Pagination offset.
        limit : int | None
            Maximum results (-1 for all).
        """
        if cayenne_exp is None:
            parts = [f"playerId={self._pid}"]
            if season:
                parts.append(f"seasonId={season}")
            if game_type:
                parts.append(f"gameTypeId={game_type}")
            cayenne_exp = " and ".join(parts)

        stats_players = self._client._api.api_stats.call_nhl_stats_players
        if self._pos == "G":
            res = stats_players.get_goalie_stats(
                report_type, is_aggregate=is_aggregate,
                cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
            )
        else:
            res = stats_players.get_skater_stats(
                report_type, is_aggregate=is_aggregate,
                cayenne_exp=cayenne_exp, sort=sort, dir=dir, start=start, limit=limit,
            )
        return res.data or {}

    # ------------------------------------------------------------------
    # Game log
    # ------------------------------------------------------------------

    def game_log(self, season: int | None = None, game_type: int | None = 2) -> GameLogs:
        """
        Retrieve Game Logs by Season

        If no season or game_type specified, defaults to current or most recent season (if player not currently active).
        If season specified but not game_type, game_type defaults to 2 (regular season).
        """
        if season and game_type:
            key = f"{self._game_key}:{season}:{game_type}"
            return self._fetch(
                key,
                lambda: self._client._api.api_web.call_nhl_players.get_game_log(
                    pid=self._pid, season=season, g_type=game_type
                ),
                self._logger, self._cache, self._ttl,
                lambda d: GameLogs.from_dict(data=d),
            )
        key = f"{self._game_key}:now"
        return self._fetch(
            key,
            lambda: self._client._api.api_web.call_nhl_players.get_game_log(pid=self._pid),
            self._logger, self._cache, self._ttl,
            lambda d: GameLogs.from_dict(data=d),
        )
