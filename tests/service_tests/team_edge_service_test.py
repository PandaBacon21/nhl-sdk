
"""
Tests for TeamDetails service: get_details()
"""
from nhl_stats.models.teams.team.edge.team_details import TeamDetails, TeamDetailResult

from .conftest import ok


DETAIL_RESPONSE = {
    "team": {
        "id": 21,
        "commonName": {"default": "Avalanche"},
        "placeNameWithPreposition": {"default": "Colorado"},
        "abbrev": "COL",
        "wins": 49, "losses": 14, "otLosses": 10, "gamesPlayed": 73, "points": 108,
    },
    "seasonsWithEdgeStats": [{"id": 20252026, "gameTypes": [2]}],
    "shotSpeed": {
        "shotAttemptsOver90": {"value": 57, "rank": 12},
        "topShotSpeed": {"imperial": 98.21, "metric": 158.05, "rank": 23, "leagueAvg": {}},
    },
    "skatingSpeed": {
        "burstsOver22": {"value": 152, "rank": 2},
        "burstsOver20": {"value": 2394, "rank": 1},
        "speedMax": {"imperial": 24.01, "metric": 38.65, "rank": 8, "leagueAvg": {}},
    },
    "distanceSkated": {
        "total": {"imperial": 3402.75, "metric": 5475.92, "rank": 5, "leagueAvg": {}},
    },
    "sogSummary": [],
    "sogDetails": [],
    "zoneTimeDetails": {},
}


def test_get_details_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.return_value = ok(DETAIL_RESPONSE)
    svc = TeamDetails(mock_client, 21)
    result = svc.get_details()
    assert isinstance(result, TeamDetailResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.assert_called_once_with(
        team_id=21, season=None, game_type=None
    )


def test_get_details_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.return_value = ok(DETAIL_RESPONSE)
    svc = TeamDetails(mock_client, 21)
    _ = svc.get_details()
    _ = svc.get_details()
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.assert_called_once()


def test_get_details_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.return_value = ok(DETAIL_RESPONSE)
    svc = TeamDetails(mock_client, 21)
    result = svc.get_details(season=20242025, game_type=2)
    assert isinstance(result, TeamDetailResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.assert_called_once_with(
        team_id=21, season=20242025, game_type=2
    )


def test_get_details_different_teams_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.return_value = ok(DETAIL_RESPONSE)
    svc1 = TeamDetails(mock_client, 21)
    svc2 = TeamDetails(mock_client, 10)
    _ = svc1.get_details()
    _ = svc2.get_details()
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_details.call_count == 2


def test_get_details_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_details.return_value = ok(DETAIL_RESPONSE)
    svc = TeamDetails(mock_client, 21)
    result = svc.get_details()
    assert result.team.abbrev == "COL"
    assert result.team.wins == 49
    assert len(result.seasons_with_edge) == 1
    assert result.shot_speed.shot_attempts_over_90.value == 57
