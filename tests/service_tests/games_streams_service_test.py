"""
Service tests for GameStreams sub-resource.
"""
from nhl_stats.models.games.streams import GameStreams

from .conftest import ok


def test_streams_get_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_streams.return_value = ok({"services": []})
    svc = GameStreams(mock_client)
    result = svc.get()
    assert isinstance(result, dict)
    mock_client._api.api_web.call_nhl_games.get_streams.assert_called_once()


def test_streams_get_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_streams.return_value = ok({"services": []})
    svc = GameStreams(mock_client)
    _ = svc.get()
    _ = svc.get()
    mock_client._api.api_web.call_nhl_games.get_streams.assert_called_once()


def test_streams_get_returns_raw_dict(mock_client) -> None:
    payload = {"streamingService": "ESPN+", "url": "https://example.com"}
    mock_client._api.api_web.call_nhl_games.get_streams.return_value = ok(payload)
    svc = GameStreams(mock_client)
    result = svc.get()
    assert result == payload


def test_games_streams_property_returns_game_streams(mock_client) -> None:
    from nhl_stats.services.games import Games
    svc = Games(mock_client)
    assert isinstance(svc.streams, GameStreams)
