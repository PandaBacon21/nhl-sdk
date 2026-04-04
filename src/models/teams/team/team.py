"""
TEAM GATEWAY OBJECT
"""
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

from .team_stats import TeamStats
from .team_roster import TeamRoster
from .team_schedule import TeamSchedule

if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient


_NHL_TEAM_IDS: dict[str, int] = {
    # Active franchises (UTA=68 Utah Mammoth 2025–; Utah HC was id=59)
    "ANA": 24, "BOS": 6,  "BUF": 7,  "CAR": 12, "CBJ": 29, "CGY": 20,
    "CHI": 16, "COL": 21, "DAL": 25, "DET": 17, "EDM": 22, "FLA": 13,
    "LAK": 26, "MIN": 30, "MTL": 8,  "NJD": 1,  "NSH": 18, "NYI": 2,
    "NYR": 3,  "OTT": 9,  "PHI": 4,  "PIT": 5,  "SEA": 55, "SJS": 28,
    "STL": 19, "TBL": 14, "TOR": 10, "UTA": 68, "VAN": 23, "VGK": 54,
    "WSH": 15, "WPG": 52,
    # Historical / relocated — abbrev used during that era
    "AFM": 47,  # Atlanta Flames → Calgary Flames (1980)
    "ARI": 53,  # Arizona Coyotes → Utah HC (2024)
    "ATL": 11,  # Atlanta Thrashers → Winnipeg Jets (2011)
    "CLR": 35,  # Colorado Rockies → New Jersey Devils (1982)
    "HFD": 34,  # Hartford Whalers → Carolina Hurricanes (1997)
    "KCS": 48,  # Kansas City Scouts → Colorado Rockies → New Jersey Devils
    "MNS": 31,  # Minnesota North Stars → Dallas Stars (1993)
    "PHX": 27,  # Phoenix Coyotes → Arizona Coyotes (2014)
    "QUE": 32,  # Quebec Nordiques → Colorado Avalanche (1995)
    "WIN": 33,  # Winnipeg Jets (1979) → Phoenix Coyotes (1996)
    # Defunct / dissolved franchises
    "CGS": 56,  # California Golden Seals → Cleveland Barons (franchise dissolved 1978)
    "CLE": 49,  # Cleveland Barons (merged with Minnesota North Stars, 1978)
    "OAK": 46,  # Oakland Seals → California Golden Seals
}


class Team:
    """
    Team gateway object.

    Created via ``client.teams.get("COL")``. Provides sub-resources for
    a specific team with the team identifier baked in.
    """
    def __init__(self, client: NhlClient, abbrev: str, team_id: int) -> None:
        self._client = client
        self._abbrev = abbrev
        self._team_id = team_id
        self._logger = logging.getLogger("nhl_sdk.teams.team")

        self._logger.debug("Team initialized: %s (id=%d)", abbrev, team_id)

    @property
    def stats(self) -> TeamStats:
        """
        Access per-team stats and NHL Edge data.

        Returns a TeamStats sub-resource with methods for club skater/goalie
        stats, season/game-type metadata, and the current scoreboard.
        NHL Edge team data is available via ``.edge``.
        """
        return TeamStats(self._client, self._abbrev, self._team_id)

    @property
    def roster(self) -> TeamRoster:
        """
        Access per-team roster data.

        Returns a TeamRoster sub-resource with methods for the current/historical
        roster, available roster seasons, and prospects.
        """
        return TeamRoster(self._client, self._abbrev)

    @property
    def schedule(self) -> TeamSchedule:
        """
        Access per-team schedule data.

        Returns a TeamSchedule sub-resource with methods for the current or
        historical full-season, monthly, and weekly schedules.
        """
        return TeamSchedule(self._client, self._abbrev)
