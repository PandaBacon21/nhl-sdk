from src.models.teams.team.team_stats.team_stats import TeamStats
from src.models.teams.team.team_stats.team_stats_result import TeamStatsResult
from src.models.teams.team.team_stats.team_scoreboard import TeamScoreboard
from src.models.teams.team.team_stats.team_season_game_types import TeamSeasonGameTypes

from .conftest import ok

ABBREV = "COL"
TEAM_ID = 21
SEASON = 20242025
G_TYPE = 2


def test_get_team_stats_now_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    result = svc.get_team_stats()
    assert isinstance(result, TeamStatsResult)
    mock_client._api.api_web.call_nhl_teams.get_team_stats.assert_called_once_with(team=ABBREV, season=None, g_type=None)


def test_get_team_stats_now_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    _ = svc.get_team_stats()
    _ = svc.get_team_stats()
    mock_client._api.api_web.call_nhl_teams.get_team_stats.assert_called_once()


def test_get_team_stats_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    result = svc.get_team_stats(season=SEASON, g_type=G_TYPE)
    assert isinstance(result, TeamStatsResult)
    mock_client._api.api_web.call_nhl_teams.get_team_stats.assert_called_once_with(team=ABBREV, season=SEASON, g_type=G_TYPE)


def test_get_team_stats_season_and_now_separate_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_stats.return_value = ok({"skaterStats": [], "goalieStats": []})
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    _ = svc.get_team_stats()
    _ = svc.get_team_stats(season=SEASON, g_type=G_TYPE)
    assert mock_client._api.api_web.call_nhl_teams.get_team_stats.call_count == 2


def test_get_game_types_per_season_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.return_value = ok([{"season": 20242025, "gameType": {"id": 2}}])
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    result = svc.get_game_types_per_season()
    assert isinstance(result, list)
    assert all(isinstance(x, TeamSeasonGameTypes) for x in result)
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.assert_called_once_with(team=ABBREV)


def test_get_game_types_per_season_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.return_value = ok([])
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    _ = svc.get_game_types_per_season()
    _ = svc.get_game_types_per_season()
    mock_client._api.api_web.call_nhl_teams.get_game_types_per_season.assert_called_once()


def test_get_team_scoreboard_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.return_value = ok({})
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    result = svc.get_team_scoreboard()
    assert isinstance(result, TeamScoreboard)
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.assert_called_once_with(team=ABBREV)


def test_get_team_scoreboard_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.return_value = ok({})
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    _ = svc.get_team_scoreboard()
    _ = svc.get_team_scoreboard()
    mock_client._api.api_web.call_nhl_teams.get_team_scoreboard.assert_called_once()


# ==========================================================================
# get_team_ref()
# ==========================================================================

def test_get_team_ref_cache_miss(mock_client) -> None:
    from src.models.teams.team.team_stats.team_ref import TeamRef
    mock_client._api.api_stats.call_nhl_stats_teams.get_team_by_id.return_value = ok(
        {"data": [{"id": TEAM_ID, "triCode": ABBREV, "fullName": "Colorado Avalanche", "franchiseId": 27, "leagueId": 133, "rawTricode": ABBREV}], "total": 1}
    )
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    result = svc.get_team_ref()
    assert isinstance(result, TeamRef)
    assert result.id == TEAM_ID
    assert result.tricode == ABBREV
    mock_client._api.api_stats.call_nhl_stats_teams.get_team_by_id.assert_called_once_with(team_id=TEAM_ID)


def test_get_team_ref_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_teams.get_team_by_id.return_value = ok(
        {"data": [{}], "total": 1}
    )
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    _ = svc.get_team_ref()
    _ = svc.get_team_ref()
    mock_client._api.api_stats.call_nhl_stats_teams.get_team_by_id.assert_called_once()


def test_get_team_ref_returns_none_on_empty(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_teams.get_team_by_id.return_value = ok(
        {"data": [], "total": 0}
    )
    svc = TeamStats(mock_client, ABBREV, TEAM_ID)
    result = svc.get_team_ref()
    assert result is None
