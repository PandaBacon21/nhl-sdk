from nhl_stats.models.players.player.player_stats.player_stats import PlayerStats
from nhl_stats.models.players.player.player_stats.games.player_game_logs import GameLogs
from nhl_stats.models.players.player.player_stats.edge.skaters.skater_edge import SkaterEdge
from nhl_stats.models.players.player.player_stats.edge.goalies.goalie_edge import GoalieEdge

from .conftest import ok

PID = 8477492
SEASON = 20232024
GAME_TYPE = 2

LANDING = {
    "featuredStats": {},
    "careerTotals": {},
    "seasonTotals": [],
    "last5Games": [],
}


def test_player_stats_init_skater(mock_client) -> None:
    ps = PlayerStats(pos="S", pid=PID, data=LANDING, client=mock_client)
    assert ps._pos == "S"
    assert ps._pid == PID


def test_player_stats_init_goalie(mock_client) -> None:
    ps = PlayerStats(pos="G", pid=PID, data=LANDING, client=mock_client)
    assert ps._pos == "G"


def test_player_stats_edge_returns_skater_edge(mock_client) -> None:
    ps = PlayerStats(pos="S", pid=PID, data=LANDING, client=mock_client)
    result = ps.edge()
    assert isinstance(result, SkaterEdge)


def test_player_stats_edge_returns_goalie_edge(mock_client) -> None:
    ps = PlayerStats(pos="G", pid=PID, data=LANDING, client=mock_client)
    result = ps.edge()
    assert isinstance(result, GoalieEdge)


def test_game_log_now_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_game_log.return_value = ok({"gameLog": []})
    ps = PlayerStats(pos="S", pid=PID, data=LANDING, client=mock_client)
    result = ps.game_log()
    assert isinstance(result, GameLogs)
    mock_client._api.api_web.call_nhl_players.get_game_log.assert_called_once()


def test_game_log_now_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_game_log.return_value = ok({"gameLog": []})
    ps = PlayerStats(pos="S", pid=PID, data=LANDING, client=mock_client)
    _ = ps.game_log()
    _ = ps.game_log()
    mock_client._api.api_web.call_nhl_players.get_game_log.assert_called_once()


def test_game_log_season_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_game_log.return_value = ok({"gameLog": []})
    ps = PlayerStats(pos="S", pid=PID, data=LANDING, client=mock_client)
    result = ps.game_log(season=SEASON, game_type=GAME_TYPE)
    assert isinstance(result, GameLogs)
    mock_client._api.api_web.call_nhl_players.get_game_log.assert_called_once()


def test_game_log_season_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_game_log.return_value = ok({"gameLog": []})
    ps = PlayerStats(pos="S", pid=PID, data=LANDING, client=mock_client)
    _ = ps.game_log(season=SEASON, game_type=GAME_TYPE)
    _ = ps.game_log(season=SEASON, game_type=GAME_TYPE)
    mock_client._api.api_web.call_nhl_players.get_game_log.assert_called_once()


def test_game_log_season_and_now_separate_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_players.get_game_log.return_value = ok({"gameLog": []})
    ps = PlayerStats(pos="S", pid=PID, data=LANDING, client=mock_client)
    _ = ps.game_log()
    _ = ps.game_log(season=SEASON, game_type=GAME_TYPE)
    assert mock_client._api.api_web.call_nhl_players.get_game_log.call_count == 2


def test_player_stats_seasons_list(mock_client) -> None:
    data = {**LANDING, "seasonTotals": [{}]}
    ps = PlayerStats(pos="S", pid=PID, data=data, client=mock_client)
    assert isinstance(ps.seasons, list)
    assert len(ps.seasons) == 1


def test_player_stats_last_5_games_list(mock_client) -> None:
    data = {**LANDING, "last5Games": [{}, {}]}
    ps = PlayerStats(pos="S", pid=PID, data=data, client=mock_client)
    assert len(ps.last_5_games) == 2
