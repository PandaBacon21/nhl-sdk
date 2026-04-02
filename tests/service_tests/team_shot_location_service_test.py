"""
Tests for TeamShotLocationDetails service: get_shot_location()
"""
from src.models.teams.team.edge.team_shot_location_details import (
    TeamShotLocationDetails, TeamShotLocationResult,
)

from .conftest import ok


SHOT_LOCATION_RESPONSE = {
    "shotLocationDetails": [
        {
            "area": "High Slot",
            "sog": 273,
            "sogRank": 1,
            "goals": 41,
            "goalsRank": 1,
            "shootingPctg": 0.1502,
            "shootingPctgRank": 17,
        },
        {
            "area": "Low Slot",
            "sog": 573,
            "sogRank": 5,
            "goals": 97,
            "goalsRank": 12,
            "shootingPctg": 0.1693,
            "shootingPctgRank": 27,
        },
    ],
    "shotLocationTotals": [
        {
            "locationCode": "all",
            "position": "all",
            "sog": 2471,
            "sogRank": 1,
            "sogLeagueAvg": 2072.9063,
            "goals": 274,
            "goalsRank": 1,
            "goalsLeagueAvg": 228.1875,
            "shootingPctg": 0.1109,
            "shootingPctgRank": 15,
            "shootingPctgLeagueAvg": 0.1101,
        }
    ],
}


def test_get_shot_location_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.return_value = ok(SHOT_LOCATION_RESPONSE)
    svc = TeamShotLocationDetails(mock_client)
    result = svc.get_shot_location(team_id=21)
    assert isinstance(result, TeamShotLocationResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.assert_called_once_with(
        team_id=21, season=None, game_type=None
    )


def test_get_shot_location_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.return_value = ok(SHOT_LOCATION_RESPONSE)
    svc = TeamShotLocationDetails(mock_client)
    _ = svc.get_shot_location(team_id=21)
    _ = svc.get_shot_location(team_id=21)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.assert_called_once()


def test_get_shot_location_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.return_value = ok(SHOT_LOCATION_RESPONSE)
    svc = TeamShotLocationDetails(mock_client)
    result = svc.get_shot_location(team_id=21, season=20242025, game_type=2)
    assert isinstance(result, TeamShotLocationResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.assert_called_once_with(
        team_id=21, season=20242025, game_type=2
    )


def test_get_shot_location_different_teams_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.return_value = ok(SHOT_LOCATION_RESPONSE)
    svc = TeamShotLocationDetails(mock_client)
    _ = svc.get_shot_location(team_id=21)
    _ = svc.get_shot_location(team_id=10)
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.call_count == 2


def test_get_shot_location_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location.return_value = ok(SHOT_LOCATION_RESPONSE)
    svc = TeamShotLocationDetails(mock_client)
    result = svc.get_shot_location(team_id=21)
    assert len(result.shot_location_details) == 2
    assert result.shot_location_details[0].area == "High Slot"
    assert result.shot_location_details[0].sog_rank == 1
    assert len(result.shot_location_totals) == 1
    assert result.shot_location_totals[0].location_code == "all"
    assert result.shot_location_totals[0].sog_league_avg == 2072.9063
