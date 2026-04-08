"""
Service tests for Games.query().
"""
from nhl_stats.services.games import Games

from .conftest import ok

GAME_ROW = {
    "id": 2025020001,
    "gameDate": "2025-01-01",
    "gameType": 2,
    "homeTeamId": 21,
    "visitingTeamId": 8,
    "season": 20242025,
}


def test_games_query_returns_list(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_games.get_game.return_value = ok(
        {"data": [GAME_ROW], "total": 1}
    )
    svc = Games(mock_client)
    result = svc.query()
    assert isinstance(result, list)
    assert result == [GAME_ROW]


def test_games_query_cache_miss(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_games.get_game.return_value = ok(
        {"data": [], "total": 0}
    )
    svc = Games(mock_client)
    _ = svc.query(cayenne_exp="season=20242025")
    mock_client._api.api_stats.call_nhl_stats_games.get_game.assert_called_once()


def test_games_query_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_games.get_game.return_value = ok(
        {"data": [], "total": 0}
    )
    svc = Games(mock_client)
    _ = svc.query(cayenne_exp="season=20242025")
    _ = svc.query(cayenne_exp="season=20242025")
    mock_client._api.api_stats.call_nhl_stats_games.get_game.assert_called_once()


def test_games_query_different_filters_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_games.get_game.return_value = ok(
        {"data": [], "total": 0}
    )
    svc = Games(mock_client)
    _ = svc.query(cayenne_exp="season=20242025")
    _ = svc.query(cayenne_exp="season=20232024")
    assert mock_client._api.api_stats.call_nhl_stats_games.get_game.call_count == 2


def test_games_query_empty_response(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_games.get_game.return_value = ok({})
    svc = Games(mock_client)
    result = svc.query()
    assert result == []
