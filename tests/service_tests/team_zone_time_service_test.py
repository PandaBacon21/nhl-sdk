"""
Tests for TeamZoneDetails service: get_zone_time()
"""
from src.models.teams.team.edge.team_zone_details import (
    TeamZoneDetails, TeamZoneDetailResult,
)

from .conftest import ok


ZONE_TIME_RESPONSE = {
    "zoneTimeDetails": [
        {
            "strengthCode": "all",
            "offensiveZonePctg": 0.4286305,
            "offensiveZoneRank": 3,
            "offensiveZoneLeagueAvg": 0.4107842,
            "neutralZonePctg": 0.1815559,
            "neutralZoneRank": 8,
            "neutralZoneLeagueAvg": 0.1784317,
            "defensiveZonePctg": 0.3898136,
            "defensiveZoneRank": 3,
            "defensiveZoneLeagueAvg": 0.4107842,
        },
        {
            "strengthCode": "es",
            "offensiveZonePctg": 0.4232852,
            "offensiveZoneRank": 4,
            "offensiveZoneLeagueAvg": 0.4074362,
            "neutralZonePctg": 0.1887191,
            "neutralZoneRank": 7,
            "neutralZoneLeagueAvg": 0.1851277,
            "defensiveZonePctg": 0.3879957,
            "defensiveZoneRank": 3,
            "defensiveZoneLeagueAvg": 0.4074362,
        },
    ],
    "shotDifferential": {
        "shotAttemptDifferential": 7.684932,
        "shotAttemptDifferentialRank": 2,
        "sogDifferential": 0.141059,
        "sogDifferentialRank": 3,
    },
}


def test_get_zone_time_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.return_value = ok(ZONE_TIME_RESPONSE)
    svc = TeamZoneDetails(mock_client, 21)
    result = svc.get_zone_time()
    assert isinstance(result, TeamZoneDetailResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.assert_called_once_with(
        team_id=21, season=None, game_type=None
    )


def test_get_zone_time_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.return_value = ok(ZONE_TIME_RESPONSE)
    svc = TeamZoneDetails(mock_client, 21)
    _ = svc.get_zone_time()
    _ = svc.get_zone_time()
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.assert_called_once()


def test_get_zone_time_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.return_value = ok(ZONE_TIME_RESPONSE)
    svc = TeamZoneDetails(mock_client, 21)
    result = svc.get_zone_time(season=20242025, game_type=2)
    assert isinstance(result, TeamZoneDetailResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.assert_called_once_with(
        team_id=21, season=20242025, game_type=2
    )


def test_get_zone_time_different_teams_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.return_value = ok(ZONE_TIME_RESPONSE)
    svc1 = TeamZoneDetails(mock_client, 21)
    svc2 = TeamZoneDetails(mock_client, 10)
    _ = svc1.get_zone_time()
    _ = svc2.get_zone_time()
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.call_count == 2


def test_get_zone_time_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time.return_value = ok(ZONE_TIME_RESPONSE)
    svc = TeamZoneDetails(mock_client, 21)
    result = svc.get_zone_time()
    assert len(result.zone_time_details) == 2
    assert result.zone_time_details[0].strength_code == "all"
    assert result.zone_time_details[0].offensive_zone_rank == 3
    assert result.shot_differential.shot_attempt_differential == 7.684932
    assert result.shot_differential.sog_differential_rank == 3
