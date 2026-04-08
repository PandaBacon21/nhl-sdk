"""
MISC SERVICE
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from ..models.misc import (
    LocationResult, PostalLookupResult, MiscMeta,
    GameMetaResult, PlayoffSeriesMetaResult,
    GoalReplayResult, PlayReplayResult,
    GameRailResult, WscPlay, StatsConfig,
    Country, Franchise, GlossaryEntry,
)
from ..core.cache import get_cache
from ..core.utilities import CacheFetchMixin

if TYPE_CHECKING:
    from nhl_stats.client import NhlClient


class Misc(CacheFetchMixin):
    """
    Miscellaneous NHL API endpoints.

    Provides access to meta information, location detection, postal lookup,
    game rail content, goal/play replays, playoff series metadata, and
    reference data (countries, franchises, glossary, config).
    """
    def __init__(self, client: NhlClient):
        self._client = client
        self._cache = get_cache()
        self._logger = logging.getLogger("nhl_sdk.misc")
        self._ttl: int = 60 * 60 * 24

    # ==========================================================================
    # META
    # ==========================================================================

    def meta(
        self,
        players: str | None = None,
        teams: str | None = None,
        season_states: str | None = None,
    ) -> MiscMeta:
        """
        Retrieve meta information for players, teams, or season states.

        Parameters
        ----------
        players : str | None
            Player ID(s).
        teams : str | None
            Three-letter team code(s).
        season_states : str | None
            Season state filter.
        """
        res = self._client._api.api_web.call_nhl_misc.get_meta(
            players=players, teams=teams, season_states=season_states
        )
        return MiscMeta.from_dict(res.data or {})

    def game_meta(self, game_id: int) -> GameMetaResult:
        """
        Retrieve metadata for a specific game.

        Parameters
        ----------
        game_id : int
        """
        res = self._client._api.api_web.call_nhl_misc.get_game_info(game_id=game_id)
        return GameMetaResult.from_dict(res.data or {})

    def playoff_series_meta(self, year: int, series_letter: str) -> PlayoffSeriesMetaResult:
        """
        Retrieve metadata for a specific playoff series.

        Parameters
        ----------
        year : int
            Season year in YYYY format.
        series_letter : str
            Series letter (e.g. "a", "b").
        """
        res = self._client._api.api_web.call_nhl_misc.get_playoff_series_meta(
            year=year, series_letter=series_letter
        )
        return PlayoffSeriesMetaResult.from_dict(res.data or {})

    # ==========================================================================
    # LOCATION & POSTAL
    # ==========================================================================

    def location(self) -> LocationResult:
        """
        Return the country code the server detects for the current request.
        """
        res = self._client._api.api_web.call_nhl_misc.get_location()
        return LocationResult.from_dict(res.data or {})

    def postal_lookup(self, postal_code: str) -> list[PostalLookupResult]:
        """
        Look up geographic information for a postal code.

        Parameters
        ----------
        postal_code : str
        """
        res = self._client._api.api_web.call_nhl_misc.get_postal_lookup(
            postal_code=postal_code
        )
        return [PostalLookupResult.from_dict(r) for r in (res.data or [])]

    # ==========================================================================
    # GAME CONTENT
    # ==========================================================================

    def game_rail(self, game_id: int) -> GameRailResult:
        """
        Retrieve sidebar content for the game center view.

        Parameters
        ----------
        game_id : int
        """
        res = self._client._api.api_web.call_nhl_misc.get_game_rail(game_id=game_id)
        return GameRailResult.from_dict(res.data or {})

    def goal_replay(self, game_id: int, event_number: int) -> GoalReplayResult:
        """
        Retrieve goal replay data for a specific game event.

        Parameters
        ----------
        game_id : int
        event_number : int
        """
        res = self._client._api.api_web.call_nhl_misc.get_goal_replay(
            game_id=game_id, event_number=event_number
        )
        return GoalReplayResult.from_dict(res.data or {})

    def play_replay(self, game_id: int, event_number: int) -> PlayReplayResult:
        """
        Retrieve replay data for a specific game event.

        Parameters
        ----------
        game_id : int
        event_number : int
        """
        res = self._client._api.api_web.call_nhl_misc.get_play_replay(
            game_id=game_id, event_number=event_number
        )
        return PlayReplayResult.from_dict(res.data or {})

    def wsc_play_by_play(self, game_id: int) -> list[WscPlay]:
        """
        Retrieve WSC (World Showcase) play-by-play data for a specific game.

        Parameters
        ----------
        game_id : int
        """
        res = self._client._api.api_web.call_nhl_misc.get_wsc(game_id=game_id)
        return [WscPlay.from_dict(p) for p in (res.data or [])]

    # ==========================================================================
    # REFERENCE DATA
    # ==========================================================================

    @property
    def countries(self) -> list[Country]:
        """
        Return all countries with a hockey presence.
        """
        return self._fetch(
            "misc:countries",
            lambda: self._client._api.api_stats.call_nhl_stats_misc.get_countries(),
            self._logger, self._cache, self._ttl,
            lambda d: [Country.from_dict(c) for c in (d.get("data") or [])],
        )

    @property
    def franchises(self) -> list[Franchise]:
        """
        Return all NHL franchises.
        """
        return self._fetch(
            "misc:franchises",
            lambda: self._client._api.api_stats.call_nhl_stats_teams.get_franchise(),
            self._logger, self._cache, self._ttl,
            lambda d: [Franchise.from_dict(f) for f in (d.get("data") or [])],
        )

    @property
    def glossary(self) -> list[GlossaryEntry]:
        """
        Return statistical term definitions.
        """
        return self._fetch(
            "misc:glossary",
            lambda: self._client._api.api_stats.call_nhl_stats_misc.get_glossary(),
            self._logger, self._cache, self._ttl,
            lambda d: [GlossaryEntry.from_dict(g) for g in (d.get("data") or [])],
        )

    @property
    def config(self) -> StatsConfig:
        """
        Return NHL Stats API configuration details.
        """
        return self._fetch(
            "misc:config",
            lambda: self._client._api.api_stats.call_nhl_stats_misc.get_config(),
            self._logger, self._cache, self._ttl,
            StatsConfig.from_dict,
        )

    # NOTE: content_module(template_key) is intentionally not implemented at the
    # service or model layer — valid templateKey values are unknown.
    # Use client._api.api_stats.call_nhl_stats_misc.get_content_module(template_key)
    # to call the raw endpoint directly until the options are identified.

    def ping(self) -> bool:
        """
        Check NHL Stats API server connectivity.

        Returns
        -------
        bool
            True if the server responds successfully.
        """
        res = self._client._api.api_stats.call_nhl_stats_misc.ping()
        return res.ok
