from __future__ import annotations
from dataclasses import dataclass

from .game_rail_result import (
    RailSeasonSeriesGame, RailSeriesWins, RailGameInfo,
    RailGameVideo, RailLinescore, RailTeamGameStat, RailGameReports,
)


@dataclass(slots=True, frozen=True)
class GameRailResult:
    season_series: list[RailSeasonSeriesGame]
    season_series_wins: RailSeriesWins | None
    game_info: RailGameInfo | None
    game_video: RailGameVideo | None
    linescore: RailLinescore | None
    shots_by_period: list[dict]
    team_game_stats: list[RailTeamGameStat]
    game_reports: RailGameReports | None

    @classmethod
    def from_dict(cls, data: dict) -> GameRailResult:
        raw_ssw = data.get("seasonSeriesWins")
        raw_gi = data.get("gameInfo")
        raw_gv = data.get("gameVideo")
        raw_ls = data.get("linescore")
        raw_gr = data.get("gameReports")
        return cls(
            season_series = [RailSeasonSeriesGame.from_dict(g) for g in (data.get("seasonSeries") or [])],
            season_series_wins = RailSeriesWins.from_dict(raw_ssw) if raw_ssw else None,
            game_info = RailGameInfo.from_dict(raw_gi) if raw_gi else None,
            game_video = RailGameVideo.from_dict(raw_gv) if raw_gv else None,
            linescore = RailLinescore.from_dict(raw_ls) if raw_ls else None,
            shots_by_period = data.get("shotsByPeriod") or [],
            team_game_stats = [RailTeamGameStat.from_dict(s) for s in (data.get("teamGameStats") or [])],
            game_reports = RailGameReports.from_dict(raw_gr) if raw_gr else None,
        )
