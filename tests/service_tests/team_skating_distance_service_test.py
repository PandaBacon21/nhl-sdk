"""
Tests for TeamSkatingDistance service: get_skating_distance()
"""
from nhl_stats.models.teams.team.edge.team_skating_distance_details import (
    TeamSkatingDistance, TeamSkatingDistanceResult,
)

from .conftest import ok


SKATING_DISTANCE_RESPONSE = {
    "skatingDistanceLast10": [
        {
            "gameCenterLink": "/gamecenter/cgy-vs-col/2026/03/30/2025021174",
            "gameDate": "2026-03-30",
            "isHomeTeam": True,
            "toiAll": 17880,
            "distanceSkatedAll": {"imperial": 47.34, "metric": 76.18},
            "toiEven": 15890,
            "distanceSkatedEven": {"imperial": 43.06, "metric": 69.29},
            "toiPP": 1510,
            "distanceSkatedPP": {"imperial": 3.12, "metric": 5.02},
            "toiPK": 480,
            "distanceSkatedPK": {"imperial": 1.16, "metric": 1.87},
            "homeTeam": {"commonName": {"default": "Avalanche"}, "placeNameWithPreposition": {"default": "Colorado"}, "teamLogo": {}},
            "awayTeam": {"commonName": {"default": "Flames"}, "placeNameWithPreposition": {"default": "Calgary"}, "teamLogo": {}},
        }
    ],
    "skatingDistanceDetails": [
        {
            "strengthCode": "all", "positionCode": "all",
            "distanceTotal": {"imperial": 3402.75, "metric": 5475.92, "rank": 5, "leagueAvg": {"imperial": 3344.17, "metric": 5381.66}},
            "distancePer60": {"imperial": 9.40, "metric": 15.13, "rank": 1, "leagueAvg": {"imperial": 9.16, "metric": 14.75}},
            "distanceMaxGame": {"imperial": 51.12, "metric": 82.27, "rank": 1, "leagueAvg": {"imperial": 49.38, "metric": 79.46}},
            "distanceMaxPeriod": {"imperial": 16.91, "metric": 27.21, "rank": 2, "leagueAvg": {"imperial": 16.60, "metric": 26.72}},
        }
    ],
}


def test_get_skating_distance_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.return_value = ok(SKATING_DISTANCE_RESPONSE)
    svc = TeamSkatingDistance(mock_client, 21)
    result = svc.get_skating_distance()
    assert isinstance(result, TeamSkatingDistanceResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.assert_called_once_with(
        team_id=21, season=None, game_type=None
    )


def test_get_skating_distance_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.return_value = ok(SKATING_DISTANCE_RESPONSE)
    svc = TeamSkatingDistance(mock_client, 21)
    _ = svc.get_skating_distance()
    _ = svc.get_skating_distance()
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.assert_called_once()


def test_get_skating_distance_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.return_value = ok(SKATING_DISTANCE_RESPONSE)
    svc = TeamSkatingDistance(mock_client, 21)
    result = svc.get_skating_distance(season=20242025, game_type=2)
    assert isinstance(result, TeamSkatingDistanceResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.assert_called_once_with(
        team_id=21, season=20242025, game_type=2
    )


def test_get_skating_distance_different_teams_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.return_value = ok(SKATING_DISTANCE_RESPONSE)
    svc1 = TeamSkatingDistance(mock_client, 21)
    svc2 = TeamSkatingDistance(mock_client, 10)
    _ = svc1.get_skating_distance()
    _ = svc2.get_skating_distance()
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_distance.call_count == 2


def test_get_skating_distance_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_distance.return_value = ok(SKATING_DISTANCE_RESPONSE)
    svc = TeamSkatingDistance(mock_client, 21)
    result = svc.get_skating_distance()
    assert len(result.skating_distance_last_10) == 1
    assert result.skating_distance_last_10[0].toi_all == 17880
    assert len(result.skating_distance_details) == 1
    assert result.skating_distance_details[0].strength_code == "all"
    assert result.skating_distance_details[0].distance_total.rank == 5
