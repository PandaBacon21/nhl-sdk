"""
Tests for TeamComparison service: get_comparison()
"""
from src.models.teams.team.edge.team_comparison import TeamComparison, TeamComparisonResult

from .conftest import ok


COMPARISON_RESPONSE = {
    "team": {"id": 21, "commonName": {"default": "Avalanche"}, "abbrev": "COL",
             "wins": 49, "losses": 14, "otLosses": 10, "gamesPlayed": 73, "points": 108},
    "seasonsWithEdgeStats": [{"id": 20252026, "gameTypes": [2]}],
    "shotSpeedDetails": {
        "topShotSpeed": {"imperial": 98.21, "metric": 158.05},
        "avgShotSpeed": {"imperial": 60.47, "metric": 97.31},
        "shotAttemptsOver100": 0,
        "shotAttempts90To100": 57,
        "shotAttempts80To90": 525,
        "shotAttempts70To80": 1320,
    },
    "skatingSpeedDetails": {
        "maxSkatingSpeed": {"imperial": 24.01, "metric": 38.65},
        "burstsOver22": 152,
        "bursts20To22": 2242,
        "bursts18To20": 8206,
    },
    "skatingDistanceLast10": [],
    "skatingDistanceDetails": {
        "distanceTotal": {"imperial": 3402.75, "metric": 5475.92},
        "distancePer60": {"imperial": 9.40, "metric": 15.13},
        "distanceMaxGame": {"imperial": 51.12, "metric": 82.27},
        "distanceMaxPeriod": {"imperial": 16.91, "metric": 27.21},
    },
    "shotLocationDetails": [],
    "shotLocationTotals": [],
    "zoneTimeDetails": {},
    "shotDifferential": {"shotAttemptDifferential": 7.68, "sogDifferential": 0.14},
}


def test_get_comparison_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.return_value = ok(COMPARISON_RESPONSE)
    svc = TeamComparison(mock_client)
    result = svc.get_comparison(team_id=21)
    assert isinstance(result, TeamComparisonResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.assert_called_once_with(
        team_id=21, season=None, game_type=None
    )


def test_get_comparison_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.return_value = ok(COMPARISON_RESPONSE)
    svc = TeamComparison(mock_client)
    _ = svc.get_comparison(team_id=21)
    _ = svc.get_comparison(team_id=21)
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.assert_called_once()


def test_get_comparison_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.return_value = ok(COMPARISON_RESPONSE)
    svc = TeamComparison(mock_client)
    result = svc.get_comparison(team_id=21, season=20242025, game_type=2)
    assert isinstance(result, TeamComparisonResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.assert_called_once_with(
        team_id=21, season=20242025, game_type=2
    )


def test_get_comparison_different_teams_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.return_value = ok(COMPARISON_RESPONSE)
    svc = TeamComparison(mock_client)
    _ = svc.get_comparison(team_id=21)
    _ = svc.get_comparison(team_id=10)
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.call_count == 2


def test_get_comparison_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_comparison.return_value = ok(COMPARISON_RESPONSE)
    svc = TeamComparison(mock_client)
    result = svc.get_comparison(team_id=21)
    assert result.team.abbrev == "COL"
    assert result.team.wins == 49
    assert len(result.seasons_with_edge) == 1
    assert result.shot_speed.shot_attempts_90_100 == 57
    assert result.skating_speed.bursts_over_22 == 152
    assert result.shot_differential.shot_attempt_differential == 7.68
