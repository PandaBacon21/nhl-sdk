from nhl_sdk.models.players.player.player_stats.edge.skaters.skater_edge import SkaterEdge
from nhl_sdk.models.players.player.player_stats.edge.skaters.skater_details import SkaterDetails
from nhl_sdk.models.players.player.player_stats.edge.skaters.skater_comparison import SkaterComparison
from nhl_sdk.models.players.player.player_stats.edge.skaters.skating_distance import SkatingDistance
from nhl_sdk.models.players.player.player_stats.edge.skaters.skating_speed import SkatingSpeed
from nhl_sdk.models.players.player.player_stats.edge.skaters.skater_zone_time import ZoneTime
from nhl_sdk.models.players.player.player_stats.edge.skaters.shot_speed import ShotSpeed
from nhl_sdk.models.players.player.player_stats.edge.skaters.shot_location import ShotLocation
from nhl_sdk.models.players.player.player_stats.edge.skaters.cat_skater_details import CatSkaterDetails

from .conftest import ok

PID = 8477492
SEASON = 20232024
GAME_TYPE = 2


def test_cache_key_now(mock_client) -> None:
    se = SkaterEdge(pid=PID, client=mock_client)
    assert se._cache_key("details", None, None) == f"player:{PID}:edge:skater:details:now"


def test_cache_key_with_season(mock_client) -> None:
    se = SkaterEdge(pid=PID, client=mock_client)
    assert se._cache_key("details", SEASON, GAME_TYPE) == f"player:{PID}:edge:skater:details:{SEASON}:{GAME_TYPE}"


def test_details_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_skater_details.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.details()
    assert isinstance(result, SkaterDetails)
    mock_client._api.api_web.call_nhl_edge_skaters.get_skater_details.assert_called_once()


def test_details_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_skater_details.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    _ = se.details()
    _ = se.details()
    mock_client._api.api_web.call_nhl_edge_skaters.get_skater_details.assert_called_once()


def test_details_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_skater_details.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.details(season=SEASON, game_type=GAME_TYPE)
    assert isinstance(result, SkaterDetails)


def test_comparison_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_skater_comparison.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.comparison()
    assert isinstance(result, SkaterComparison)


def test_skating_distance_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_skating_distance.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.skating_distance()
    assert isinstance(result, SkatingDistance)


def test_skating_speed_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_skating_speed.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.skating_speed()
    assert isinstance(result, SkatingSpeed)


def test_zone_time_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_zone_time.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.zone_time()
    assert isinstance(result, ZoneTime)


def test_shot_speed_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_shot_speed.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.shot_speed()
    assert isinstance(result, ShotSpeed)


def test_shot_location_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_shot_location.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.shot_location()
    assert isinstance(result, ShotLocation)


def test_cat_details_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_cat_skater_details.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    result = se.cat_details()
    assert isinstance(result, CatSkaterDetails)


def test_season_and_now_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_skaters.get_skater_details.return_value = ok()
    se = SkaterEdge(pid=PID, client=mock_client)
    _ = se.details()
    _ = se.details(season=SEASON, game_type=GAME_TYPE)
    assert mock_client._api.api_web.call_nhl_edge_skaters.get_skater_details.call_count == 2
