"""
Tests for TeamSkatingSpeedDetails service: get_skating_speed()
"""
from src.models.teams.team.edge.team_skating_speed_details import (
    TeamSkatingSpeedDetails, TeamSkatingSpeedResult,
)

from .conftest import ok


SKATING_SPEED_RESPONSE = {
    "topSkatingSpeeds": [
        {
            "player": {
                "id": 8477492,
                "firstName": {"default": "Nathan"},
                "lastName": {"default": "MacKinnon"},
                "slug": "nathan-mackinnon-8477492",
            },
            "gameCenterLink": "/gamecenter/wpg-vs-col/2026/03/28/2025021162",
            "gameDate": "2026-03-28",
            "gameType": 2,
            "isHomeTeam": True,
            "skatingSpeed": {"imperial": 24.0129, "metric": 38.645},
            "timeInPeriod": "06:42",
            "periodDescriptor": {"number": 2, "periodType": "REG", "maxRegulationPeriods": 3},
            "homeTeam": {"commonName": {"default": "Avalanche"}, "placeNameWithPreposition": {"default": "Colorado"}, "teamLogo": {}},
            "awayTeam": {"commonName": {"default": "Jets"}, "placeNameWithPreposition": {"default": "Winnipeg"}, "teamLogo": {}},
        }
    ],
    "skatingSpeedDetails": [
        {
            "positionCode": "all",
            "maxSkatingSpeed": {"imperial": 24.0129, "metric": 38.645, "rank": 8, "leagueAvg": {"imperial": 23.74, "metric": 38.20}},
            "burstsOver22": {"value": 152, "rank": 2, "leagueAvg": 77.75},
            "bursts20To22": {"value": 2242, "rank": 1, "leagueAvg": 1516.19},
            "bursts18To20": {"value": 8206, "rank": 2, "leagueAvg": 7059.63},
        }
    ],
}


def test_get_skating_speed_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.return_value = ok(SKATING_SPEED_RESPONSE)
    svc = TeamSkatingSpeedDetails(mock_client, 21)
    result = svc.get_skating_speed()
    assert isinstance(result, TeamSkatingSpeedResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.assert_called_once_with(
        team_id=21, season=None, game_type=None
    )


def test_get_skating_speed_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.return_value = ok(SKATING_SPEED_RESPONSE)
    svc = TeamSkatingSpeedDetails(mock_client, 21)
    _ = svc.get_skating_speed()
    _ = svc.get_skating_speed()
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.assert_called_once()


def test_get_skating_speed_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.return_value = ok(SKATING_SPEED_RESPONSE)
    svc = TeamSkatingSpeedDetails(mock_client, 21)
    result = svc.get_skating_speed(season=20242025, game_type=2)
    assert isinstance(result, TeamSkatingSpeedResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.assert_called_once_with(
        team_id=21, season=20242025, game_type=2
    )


def test_get_skating_speed_different_teams_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.return_value = ok(SKATING_SPEED_RESPONSE)
    svc1 = TeamSkatingSpeedDetails(mock_client, 21)
    svc2 = TeamSkatingSpeedDetails(mock_client, 10)
    _ = svc1.get_skating_speed()
    _ = svc2.get_skating_speed()
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.call_count == 2


def test_get_skating_speed_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed.return_value = ok(SKATING_SPEED_RESPONSE)
    svc = TeamSkatingSpeedDetails(mock_client, 21)
    result = svc.get_skating_speed()
    assert len(result.top_skating_speeds) == 1
    assert result.top_skating_speeds[0].player.id == 8477492
    assert result.top_skating_speeds[0].skating_speed.imperial == 24.0129
    assert len(result.skating_speed_details) == 1
    assert result.skating_speed_details[0].position_code == "all"
    assert result.skating_speed_details[0].bursts_over_22.rank == 2
