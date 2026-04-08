from nhl_stats.services.players import Players
from nhl_stats.models.players.player.player import Player
from nhl_stats.models.players.leaders.leaders import Leaders
from nhl_stats.models.players.spotlight import Spotlight

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


# ==========================================================================
# milestones()
# ==========================================================================

def test_milestones_both_positions_calls_two_endpoints(mock_client) -> None:
    from nhl_stats.services.players import Players
    from nhl_stats.models.players.player.achievements import PlayerMilestone
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok({"data": [{}], "total": 1})
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.return_value = ok({"data": [{}], "total": 1})
    svc = Players(mock_client)
    result = svc.milestones()
    assert len(result) == 2
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.assert_called_once()
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.assert_called_once()


def test_milestones_skaters_only(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok({"data": [{}], "total": 1})
    svc = Players(mock_client)
    result = svc.milestones(position="s")
    assert len(result) == 1
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.assert_called_once()
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.assert_not_called()


def test_milestones_goalies_only(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.return_value = ok({"data": [{}], "total": 1})
    svc = Players(mock_client)
    result = svc.milestones(position="g")
    assert len(result) == 1
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.assert_not_called()
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.assert_called_once()


def test_milestones_cache_hit_skaters(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok({"data": [], "total": 0})
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.return_value = ok({"data": [], "total": 0})
    svc = Players(mock_client)
    _ = svc.milestones(position="s")
    _ = svc.milestones(position="s")
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.assert_called_once()


def test_milestones_empty_data(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok({"data": [], "total": 0})
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.return_value = ok({"data": [], "total": 0})
    svc = Players(mock_client)
    result = svc.milestones()
    assert result == []


# ==========================================================================
# query()
# ==========================================================================

def test_players_query_returns_list(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_players.return_value = ok({"data": [{"id": 1}], "total": 1})
    svc = Players(mock_client)
    result = svc.query()
    assert isinstance(result, list)
    assert result == [{"id": 1}]


def test_players_query_cache_miss(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_players.return_value = ok({"data": [], "total": 0})
    svc = Players(mock_client)
    _ = svc.query(cayenne_exp="active=1")
    mock_client._api.api_stats.call_nhl_stats_players.get_players.assert_called_once()


def test_players_query_cache_hit(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_players.return_value = ok({"data": [], "total": 0})
    svc = Players(mock_client)
    _ = svc.query(cayenne_exp="active=1")
    _ = svc.query(cayenne_exp="active=1")
    mock_client._api.api_stats.call_nhl_stats_players.get_players.assert_called_once()


def test_players_query_empty_response(mock_client) -> None:
    from nhl_stats.services.players import Players
    mock_client._api.api_stats.call_nhl_stats_players.get_players.return_value = ok({})
    svc = Players(mock_client)
    result = svc.query()
    assert result == []
