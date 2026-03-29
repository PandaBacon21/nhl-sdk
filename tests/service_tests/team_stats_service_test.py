from src.models.teams.team.team_stats.team_stats import TeamStats
from src.models.teams.team.team_stats.team_stats_result import TeamStatsResult
from src.models.teams.team.team_stats.team_scoreboard import TeamScoreboard
from src.models.teams.team.team_stats.team_season_game_types import TeamSeasonGameTypes

from .conftest import ok

TEAM = "COL"
SEASON = 20242025
G_TYPE = 2


def test_get_team_stats_now_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client)
    result = svc.get_team_stats(team=TEAM)
    assert isinstance(result, TeamStatsResult)
    mock_client._api.api_web.call_nhl_teams.get_team_stats.assert_called_once_with(team=TEAM, season=None, g_type=None)


def test_get_team_stats_now_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client)
    _ = svc.get_team_stats(team=TEAM)
    _ = svc.get_team_stats(team=TEAM)
    mock_client._api.api_web.call_nhl_teams.get_team_stats.assert_called_once()


def test_get_team_stats_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client)
    result = svc.get_team_stats(team=TEAM, season=SEASON, g_type=G_TYPE)
    assert isinstance(result, TeamStatsResult)
    mock_client._api.api_web.call_nhl_teams.get_team_stats.assert_called_once_with(team=TEAM, season=SEASON, g_type=G_TYPE)


def test_get_team_stats_season_and_now_separate_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client)
    _ = svc.get_team_stats(team=TEAM)
    _ = svc.get_team_stats(team=TEAM, season=SEASON, g_type=G_TYPE)
    assert mock_client._api.api_web.call_nhl_teams.get_team_stats.call_count == 2


def test_get_game_types_per_season_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.return_value = ok([{"season": 20242025, "gameType": {"id": 2}}])
    svc = TeamStats(mock_client)
    result = svc.get_game_types_per_season(team=TEAM)
    assert isinstance(result, list)
    assert all(isinstance(x, TeamSeasonGameTypes) for x in result)
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.assert_called_once_with(team=TEAM)


def test_get_game_types_per_season_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.return_value = ok([])
    svc = TeamStats(mock_client)
    _ = svc.get_game_types_per_season(team=TEAM)
    _ = svc.get_game_types_per_season(team=TEAM)
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.assert_called_once()


def test_get_team_scoreboard_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.return_value = ok({})
    svc = TeamStats(mock_client)
    result = svc.get_team_scoreboard(team=TEAM)
    assert isinstance(result, TeamScoreboard)
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.assert_called_once_with(team=TEAM)


def test_get_team_scoreboard_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.return_value = ok({})
    svc = TeamStats(mock_client)
    _ = svc.get_team_scoreboard(team=TEAM)
    _ = svc.get_team_scoreboard(team=TEAM)
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.assert_called_once()
