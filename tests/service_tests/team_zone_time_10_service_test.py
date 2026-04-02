"""
Tests for TeamZoneTime10 service: get_top_10()
"""
from src.models.teams.edge.team_zone_time_10 import (
    TeamZoneTime10, TeamZoneTimeLeaderEntry,
)

from .conftest import ok


TOP_10_RESPONSE = [
    {
        "team": {
            "commonName": {"default": "Hurricanes"},
            "placeNameWithPreposition": {"default": "Carolina", "fr": "de la Caroline"},
            "abbrev": "CAR",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "carolina-hurricanes-12",
        },
        "offensiveZoneTime": 0.4563367,
        "neutralZoneTime": 0.1829148,
        "defensiveZoneTime": 0.3607485,
    },
    {
        "team": {
            "commonName": {"default": "Senators"},
            "placeNameWithPreposition": {"default": "Ottawa"},
            "abbrev": "OTT",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "ottawa-senators-9",
        },
        "offensiveZoneTime": 0.4365089,
        "neutralZoneTime": 0.1751012,
        "defensiveZoneTime": 0.3883898,
    },
]


def test_get_top_10_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamZoneTime10(mock_client)
    result = svc.get_top_10(strength="all", sort="offensive")
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], TeamZoneTimeLeaderEntry)
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.assert_called_once_with(
        strength="all", sort="offensive", season=None, game_type=None
    )


def test_get_top_10_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamZoneTime10(mock_client)
    _ = svc.get_top_10(strength="all", sort="offensive")
    _ = svc.get_top_10(strength="all", sort="offensive")
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.assert_called_once()


def test_get_top_10_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamZoneTime10(mock_client)
    result = svc.get_top_10(strength="es", sort="defensive", season=20242025, game_type=2)
    assert isinstance(result, list)
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.assert_called_once_with(
        strength="es", sort="defensive", season=20242025, game_type=2
    )


def test_get_top_10_different_params_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamZoneTime10(mock_client)
    _ = svc.get_top_10(strength="all", sort="offensive")
    _ = svc.get_top_10(strength="pp", sort="offensive")
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.call_count == 2


def test_get_top_10_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_zone_time_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamZoneTime10(mock_client)
    result = svc.get_top_10(strength="all", sort="offensive")
    first = result[0]
    assert first.team.abbrev == "CAR"
    assert first.offensive_zone_time == 0.4563367
    assert first.neutral_zone_time == 0.1829148
    assert first.defensive_zone_time == 0.3607485
