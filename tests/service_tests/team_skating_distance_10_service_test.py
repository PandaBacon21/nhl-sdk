"""
Tests for TeamSkatingDistance10 service: get_top_10()
"""
from nhl_sdk.models.teams.edge.team_skating_distance_10 import (
    TeamSkatingDistance10, TeamDistanceLeaderEntry,
)

from .conftest import ok


TOP_10_RESPONSE = [
    {
        "team": {
            "commonName": {"default": "Kings"},
            "placeNameWithPreposition": {"default": "Los Angeles"},
            "abbrev": "LAK",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "los-angeles-kings-26",
        },
        "distanceTotal": {"imperial": 2127.79, "metric": 3424.18},
        "distancePer60": {"imperial": 9.519, "metric": 15.318},
        "distanceMaxPerGame": {
            "imperial": 32.859,
            "metric": 52.879,
            "overlay": {
                "gameDate": "2026-03-24",
                "awayTeam": {"abbrev": "LAK", "score": 2},
                "homeTeam": {"abbrev": "CGY", "score": 3},
                "gameOutcome": {"lastPeriodType": "SO"},
                "periodDescriptor": {"maxRegulationPeriods": 3, "number": 3, "periodType": "REG"},
                "gameType": 2,
            },
        },
        "distanceMaxPerPeriod": {
            "imperial": 11.408,
            "metric": 18.358,
            "overlay": {
                "gameDate": "2025-11-17",
                "awayTeam": {"abbrev": "LAK", "score": 1},
                "homeTeam": {"abbrev": "WSH", "score": 2},
                "gameOutcome": {"lastPeriodType": "REG"},
                "periodDescriptor": {"maxRegulationPeriods": 3, "number": 3, "periodType": "REG"},
                "gameType": 2,
            },
        },
    },
    {
        "team": {
            "commonName": {"default": "Panthers"},
            "placeNameWithPreposition": {"default": "Florida"},
            "abbrev": "FLA",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "florida-panthers-13",
        },
        "distanceTotal": {"imperial": 2174.41, "metric": 3499.20},
        "distancePer60": {"imperial": 9.783, "metric": 15.744},
        "distanceMaxPerGame": {"imperial": 32.289, "metric": 51.962},
        "distanceMaxPerPeriod": {"imperial": 11.099, "metric": 17.862},
    },
]


def test_get_top_10_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingDistance10(mock_client)
    result = svc.get_top_10(strength="all", sort="per-60")
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], TeamDistanceLeaderEntry)
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.assert_called_once_with(
        strength="all", sort="per-60", pos="all", season=None, game_type=None
    )


def test_get_top_10_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingDistance10(mock_client)
    _ = svc.get_top_10(strength="all", sort="per-60")
    _ = svc.get_top_10(strength="all", sort="per-60")
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.assert_called_once()


def test_get_top_10_with_pos(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingDistance10(mock_client)
    _ = svc.get_top_10(strength="es", sort="total", pos="F")
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.assert_called_once_with(
        strength="es", sort="total", pos="F", season=None, game_type=None
    )


def test_get_top_10_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingDistance10(mock_client)
    result = svc.get_top_10(strength="all", sort="per-60", season=20242025, game_type=2)
    assert isinstance(result, list)
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.assert_called_once_with(
        strength="all", sort="per-60", pos="all", season=20242025, game_type=2
    )


def test_get_top_10_different_params_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingDistance10(mock_client)
    _ = svc.get_top_10(strength="all", sort="per-60")
    _ = svc.get_top_10(strength="es", sort="per-60")
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.call_count == 2


def test_get_top_10_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_distance_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingDistance10(mock_client)
    result = svc.get_top_10(strength="all", sort="per-60")
    first = result[0]
    assert first.team.abbrev == "LAK"
    assert first.distance_total.imperial == 2127.79
    assert first.distance_per_60.metric == 15.318
    assert first.distance_max_per_game.imperial == 32.859
    assert first.distance_max_per_game.overlay
    assert first.distance_max_per_game.overlay.game_date == "2026-03-24"
    assert first.distance_max_per_period.overlay
    assert first.distance_max_per_period.overlay.away_team.abbrev == "LAK"
    # second entry has no overlay
    assert result[1].distance_max_per_game.overlay is None
