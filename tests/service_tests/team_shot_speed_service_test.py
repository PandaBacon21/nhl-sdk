"""
Tests for TeamShotSpeedDetails service: get_shot_speed()
"""
from nhl_stats.models.teams.team.edge.team_shot_speed_details import (
    TeamShotSpeedDetails, TeamShotSpeedResult,
)

from .conftest import ok


SHOT_SPEED_RESPONSE = {
    "hardestShots": [
        {
            "player": {
                "id": 8480069,
                "firstName": {"default": "Cale"},
                "lastName": {"default": "Makar"},
                "slug": "cale-makar-8480069",
            },
            "gameCenterLink": "/gamecenter/dal-vs-col/2026/03/18/2025021080",
            "gameDate": "2026-03-18",
            "gameType": 2,
            "isHomeTeam": True,
            "shotSpeed": {"imperial": 98.21, "metric": 158.05},
            "timeInPeriod": "10:39",
            "periodDescriptor": {"number": 2, "periodType": "REG", "maxRegulationPeriods": 3},
            "homeTeam": {"commonName": {"default": "Avalanche"}, "placeNameWithPreposition": {"default": "Colorado"}, "teamLogo": {}},
            "awayTeam": {"commonName": {"default": "Stars"}, "placeNameWithPreposition": {"default": "Dallas"}, "teamLogo": {}},
        }
    ],
    "shotSpeedDetails": [
        {
            "position": "all",
            "topShotSpeed": {"imperial": 98.21, "metric": 158.05, "rank": 23, "leagueAvg": {"imperial": 99.35, "metric": 159.89}},
            "avgShotSpeed": {"imperial": 60.47, "metric": 97.31, "rank": 1, "leagueAvg": {"imperial": 58.17, "metric": 93.61}},
            "shotAttemptsOver100": {"value": 0, "rank": 12, "leagueAvg": 0.7813},
            "shotAttempts90To100": {"value": 57, "rank": 10, "leagueAvg": 49.9375},
            "shotAttempts80To90": {"value": 525, "leagueAvg": 368.75},
            "shotAttempts70To80": {"value": 1320, "leagueAvg": 925.875},
        }
    ],
}


def test_get_shot_speed_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.return_value = ok(SHOT_SPEED_RESPONSE)
    svc = TeamShotSpeedDetails(mock_client, 21)
    result = svc.get_shot_speed()
    assert isinstance(result, TeamShotSpeedResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.assert_called_once_with(
        team_id=21, season=None, game_type=None
    )


def test_get_shot_speed_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.return_value = ok(SHOT_SPEED_RESPONSE)
    svc = TeamShotSpeedDetails(mock_client, 21)
    _ = svc.get_shot_speed()
    _ = svc.get_shot_speed()
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.assert_called_once()


def test_get_shot_speed_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.return_value = ok(SHOT_SPEED_RESPONSE)
    svc = TeamShotSpeedDetails(mock_client, 21)
    result = svc.get_shot_speed(season=20242025, game_type=2)
    assert isinstance(result, TeamShotSpeedResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.assert_called_once_with(
        team_id=21, season=20242025, game_type=2
    )


def test_get_shot_speed_different_teams_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.return_value = ok(SHOT_SPEED_RESPONSE)
    svc1 = TeamShotSpeedDetails(mock_client, 21)
    svc2 = TeamShotSpeedDetails(mock_client, 10)
    _ = svc1.get_shot_speed()
    _ = svc2.get_shot_speed()
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.call_count == 2


def test_get_shot_speed_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed.return_value = ok(SHOT_SPEED_RESPONSE)
    svc = TeamShotSpeedDetails(mock_client, 21)
    result = svc.get_shot_speed()
    assert len(result.hardest_shots) == 1
    assert result.hardest_shots[0].player.id == 8480069
    assert result.hardest_shots[0].shot_speed.imperial == 98.21
    assert len(result.shot_speed_details) == 1
    assert result.shot_speed_details[0].position == "all"
    assert result.shot_speed_details[0].shot_attempts_80_to_90.rank is None
