from __future__ import annotations
from typing import TYPE_CHECKING

from .players import CallNhlStatsPlayers
from .teams import CallNhlStatsTeams
from .games import CallNhlStatsGames
from .draft import CallNhlStatsDraft
from .seasons import CallNhlStatsSeasons
from .misc import CallNhlStatsMisc

if TYPE_CHECKING:
    from ...core.transport import APICallStats


class APIStats:
    def __init__(self, http: APICallStats):
        self.call_nhl_sdk_players = CallNhlStatsPlayers(http)
        self.call_nhl_sdk_teams = CallNhlStatsTeams(http)
        self.call_nhl_sdk_games = CallNhlStatsGames(http)
        self.call_nhl_sdk_draft = CallNhlStatsDraft(http)
        self.call_nhl_sdk_seasons = CallNhlStatsSeasons(http)
        self.call_nhl_sdk_misc = CallNhlStatsMisc(http)


__all__ = ["APIStats"]
