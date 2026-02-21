from __future__ import annotations
from typing import TYPE_CHECKING

from .draft import CallNhlDraft
from .games import  CallNhlGames
from .league import CallNhlLeague
from .miscellaneous import CallNhlMisc
from .players import  CallNhlPlayers
from .playoffs import CallNhlPlayoffs
from .season import CallNhlSeasons
from .teams import CallNhlTeams
from .edge.edge_goalies import CallNhlEdgeGoalies
from .edge.edge_skaters import  CallNhlEdgeSkaters
from .edge.edge_team import CallNhlEdgeTeam

if TYPE_CHECKING: 
    from nhl_stats.src.core.transport import APICallWeb


class APIWeb:
    def __init__(self, http: APICallWeb): 
        self.call_nhl_draft = CallNhlDraft(http)
        self.call_nhl_games = CallNhlGames(http)
        self.call_nhl_league = CallNhlLeague(http)
        self.call_nhl_misc = CallNhlMisc(http)
        self.call_nhl_players = CallNhlPlayers(http)
        self.call_nhl_playoffs = CallNhlPlayoffs(http)
        self.call_nhl_seasons = CallNhlSeasons(http)
        self.call_nhl_teams = CallNhlTeams(http)
        self.call_nhl_edge_goalies = CallNhlEdgeGoalies(http)
        self.call_nhl_edge_skaters = CallNhlEdgeSkaters(http)
        self.cal_nhl_edge_team = CallNhlEdgeTeam(http)



__all__ = ["APIWeb"]