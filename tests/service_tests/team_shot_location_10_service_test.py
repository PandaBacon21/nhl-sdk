"""
Tests for TeamShotLocation10 service: get_top_10()
"""
from nhl_sdk.models.teams.edge.team_shot_location_10 import (
    TeamShotLocation10, TeamShotLocationLeaderEntry,
)

from .conftest import ok


TOP_10_RESPONSE = [
    {
        "team": {
            "id": 16,
            "commonName": {"default": "Blackhawks"},
            "placeNameWithPreposition": {"default": "Chicago", "fr": "de Chicago"},
            "abbrev": "CHI",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "chicago-blackhawks-16",
        },
        "all": 0.1044,
        "highDanger": 0.2303,
        "midRange": 0.0996,
        "longRange": 0.0124,
    },
    {
        "team": {
            "id": 9,
            "commonName": {"default": "Senators"},
            "placeNameWithPreposition": {"default": "Ottawa"},
            "abbrev": "OTT",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "ottawa-senators-9",
        },
        "all": 0.1021,
        "highDanger": 0.2198,
        "midRange": 0.0980,
        "longRange": 0.0110,
    },
]


def test_get_top_10_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotLocation10(mock_client)
    result = svc.get_top_10(category="sog", sort="all")
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], TeamShotLocationLeaderEntry)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.assert_called_once_with(
        category="sog", sort="all", season=None, game_type=None
    )


def test_get_top_10_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotLocation10(mock_client)
    _ = svc.get_top_10(category="sog", sort="all")
    _ = svc.get_top_10(category="sog", sort="all")
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.assert_called_once()


def test_get_top_10_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotLocation10(mock_client)
    result = svc.get_top_10(category="goals", sort="high", season=20242025, game_type=2)
    assert isinstance(result, list)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.assert_called_once_with(
        category="goals", sort="high", season=20242025, game_type=2
    )


def test_get_top_10_different_params_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotLocation10(mock_client)
    _ = svc.get_top_10(category="sog", sort="all")
    _ = svc.get_top_10(category="goals", sort="all")
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.call_count == 2


def test_get_top_10_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_location_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotLocation10(mock_client)
    result = svc.get_top_10(category="sog", sort="all")
    first = result[0]
    assert first.team.id == 16
    assert first.team.abbrev == "CHI"
    assert first.all == 0.1044
    assert first.high_danger == 0.2303
    assert first.mid_range == 0.0996
    assert first.long_range == 0.0124
