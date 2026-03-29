from src.services.players import Players
from src.models.players.player.player import Player
from src.models.players.leaders.leaders import Leaders
from src.models.players.spotlight import Spotlight

from .conftest import ok


def test_players_get_returns_player(mock_client) -> None:
    svc = Players(mock_client)
    result = svc.get(8477492)
    assert isinstance(result, Player)


def test_players_get_pid_preserved(mock_client) -> None:
    svc = Players(mock_client)
    result = svc.get(8477492)
    assert result._pid == 8477492


def test_players_spotlight_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_player_spotlight.return_value = ok([{}])
    svc = Players(mock_client)
    result = svc.spotlight
    assert isinstance(result, list)
    mock_client._api.api_web.call_nhl_players.get_player_spotlight.assert_called_once()


def test_players_spotlight_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_player_spotlight.return_value = ok([{}])
    svc = Players(mock_client)
    _ = svc.spotlight
    _ = svc.spotlight
    mock_client._api.api_web.call_nhl_players.get_player_spotlight.assert_called_once()


def test_players_spotlight_empty_list(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_player_spotlight.return_value = ok([])
    svc = Players(mock_client)
    result = svc.spotlight
    assert result == []


def test_players_spotlight_returns_spotlight_instances(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_player_spotlight.return_value = ok([{}, {}])
    svc = Players(mock_client)
    result = svc.spotlight
    assert all(isinstance(p, Spotlight) for p in result)


def test_players_leaders_returns_leaders(mock_client) -> None:
    svc = Players(mock_client)
    result = svc.leaders
    assert isinstance(result, Leaders)


def test_players_leaders_each_call_returns_new_instance(mock_client) -> None:
    svc = Players(mock_client)
    a = svc.leaders
    b = svc.leaders
    assert isinstance(a, Leaders)
    assert isinstance(b, Leaders)
