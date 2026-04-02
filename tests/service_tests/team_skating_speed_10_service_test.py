"""
Tests for TeamSkatingSpeed10 service: get_top_10()
"""
from src.models.teams.edge.team_skating_speed_10 import (
    TeamSkatingSpeed10, TeamSpeedLeaderEntry,
)

from .conftest import ok


TOP_10_RESPONSE = [
    {
        "team": {
            "commonName": {"default": "Sabres"},
            "placeNameWithPreposition": {"default": "Buffalo"},
            "abbrev": "BUF",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "buffalo-sabres-7",
        },
        "maxSkatingSpeed": {
            "imperial": 24.9389,
            "metric": 40.1352,
            "overlay": {
                "player": {
                    "firstName": {"default": "Beck"},
                    "lastName": {"default": "Malenstyn"},
                },
                "gameDate": "2026-03-12",
                "awayTeam": {"abbrev": "WSH", "score": 2},
                "homeTeam": {"abbrev": "BUF", "score": 1},
                "gameOutcome": {"lastPeriodType": "REG"},
                "periodDescriptor": {"maxRegulationPeriods": 3, "number": 3, "periodType": "REG"},
                "timeInPeriod": "12:05",
                "gameType": 2,
            },
        },
        "burstsOver22": 79,
        "bursts20To22": 1607,
        "bursts18To20": 6398,
    },
    {
        "team": {
            "commonName": {"default": "Capitals"},
            "placeNameWithPreposition": {"default": "Washington"},
            "abbrev": "WSH",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "washington-capitals-15",
        },
        "maxSkatingSpeed": {"imperial": 24.8, "metric": 39.9},
        "burstsOver22": 65,
        "bursts20To22": 1500,
        "bursts18To20": 6100,
    },
]


def test_get_top_10_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingSpeed10(mock_client)
    result = svc.get_top_10(sort="max")
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], TeamSpeedLeaderEntry)
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.assert_called_once_with(
        sort="max", pos="all", season=None, game_type=None
    )


def test_get_top_10_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingSpeed10(mock_client)
    _ = svc.get_top_10(sort="max")
    _ = svc.get_top_10(sort="max")
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.assert_called_once()


def test_get_top_10_with_pos(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingSpeed10(mock_client)
    _ = svc.get_top_10(sort="over-22", pos="F")
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.assert_called_once_with(
        sort="over-22", pos="F", season=None, game_type=None
    )


def test_get_top_10_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingSpeed10(mock_client)
    result = svc.get_top_10(sort="max", season=20242025, game_type=2)
    assert isinstance(result, list)
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.assert_called_once_with(
        sort="max", pos="all", season=20242025, game_type=2
    )


def test_get_top_10_different_params_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingSpeed10(mock_client)
    _ = svc.get_top_10(sort="max")
    _ = svc.get_top_10(sort="over-22")
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.call_count == 2


def test_get_top_10_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_skating_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamSkatingSpeed10(mock_client)
    result = svc.get_top_10(sort="max")
    first = result[0]
    assert first.team.abbrev == "BUF"
    assert first.max_skating_speed.imperial == 24.9389
    assert first.max_skating_speed.overlay
    assert first.max_skating_speed.overlay.first_name.default == "Beck"
    assert first.max_skating_speed.overlay.game_date == "2026-03-12"
    assert first.bursts_over_22 == 79
    # second entry has no overlay
    assert result[1].max_skating_speed.overlay is None
