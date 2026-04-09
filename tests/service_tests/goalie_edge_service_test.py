from nhl_sdk.models.players.player.player_stats.edge.goalies.goalie_edge import GoalieEdge
from nhl_sdk.models.players.player.player_stats.edge.goalies.goalie_details import GoalieDetails
from nhl_sdk.models.players.player.player_stats.edge.goalies.goalie_comparison import GoalieComparison
from nhl_sdk.models.players.player.player_stats.edge.goalies.goalie_5v5 import GoalieFiveVFive
from nhl_sdk.models.players.player.player_stats.edge.goalies.goalie_shot_location import GoalieShotLocation
from nhl_sdk.models.players.player.player_stats.edge.goalies.goalie_save_pctg import GoalieSavePctg
from nhl_sdk.models.players.player.player_stats.edge.goalies.cat_goalie_details import CatGoalieDetails

from .conftest import ok

PID = 8475809
SEASON = 20232024
GAME_TYPE = 2


def test_cache_key_now(mock_client) -> None:
    ge = GoalieEdge(pid=PID, client=mock_client)
    assert ge._cache_key("details", None, None) == f"player:{PID}:edge:goalie:details:now"


def test_cache_key_with_season(mock_client) -> None:
    ge = GoalieEdge(pid=PID, client=mock_client)
    assert ge._cache_key("details", SEASON, GAME_TYPE) == f"player:{PID}:edge:goalie:details:{SEASON}:{GAME_TYPE}"


def test_details_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_details.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    result = ge.details()
    assert isinstance(result, GoalieDetails)
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_details.assert_called_once()


def test_details_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_details.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    _ = ge.details()
    _ = ge.details()
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_details.assert_called_once()


def test_details_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_details.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    result = ge.details(season=SEASON, game_type=GAME_TYPE)
    assert isinstance(result, GoalieDetails)


def test_comparison_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_comparison.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    result = ge.comparison()
    assert isinstance(result, GoalieComparison)


def test_five_v_five_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_5v5.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    result = ge.five_v_five()
    assert isinstance(result, GoalieFiveVFive)


def test_shot_location_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_shot_location.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    result = ge.shot_location()
    assert isinstance(result, GoalieShotLocation)


def test_save_pctg_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_save_pctg.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    result = ge.save_pctg()
    assert isinstance(result, GoalieSavePctg)


def test_cat_details_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_cat_goalie_details.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    result = ge.cat_details()
    assert isinstance(result, CatGoalieDetails)


def test_season_and_now_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_details.return_value = ok()
    ge = GoalieEdge(pid=PID, client=mock_client)
    _ = ge.details()
    _ = ge.details(season=SEASON, game_type=GAME_TYPE)
    assert mock_client._api.api_web.call_nhl_edge_goalies.get_goalie_details.call_count == 2
