"""
Tests for TeamShotSpeed10 service: get_top_10()
"""
from nhl_stats.models.teams.edge.team_shot_speed_10 import (
    TeamShotSpeed10, TeamShotSpeedLeaderEntry,
)

from .conftest import ok


TOP_10_RESPONSE = [
    {
        "team": {
            "commonName": {"default": "Blackhawks"},
            "placeNameWithPreposition": {"default": "Chicago", "fr": "de Chicago"},
            "abbrev": "CHI",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "chicago-blackhawks-16",
        },
        "hardestShot": {
            "imperial": 102.83,
            "metric": 165.4888,
            "overlay": {
                "player": {
                    "firstName": {"default": "Louis"},
                    "lastName": {"default": "Crevier"},
                },
                "gameDate": "2026-02-28",
                "awayTeam": {"abbrev": "CHI", "score": 1},
                "homeTeam": {"abbrev": "COL", "score": 3},
                "gameOutcome": {"lastPeriodType": "REG"},
                "periodDescriptor": {"maxRegulationPeriods": 3, "number": 1, "periodType": "REG"},
                "timeInPeriod": "03:19",
                "gameType": 2,
            },
        },
        "shotAttemptsOver100": 6,
        "shotAttempts90To100": 53,
        "shotAttempts80To90": 360,
        "shotAttempts70To80": 933,
    },
    {
        "team": {
            "commonName": {"default": "Capitals"},
            "placeNameWithPreposition": {"default": "Washington"},
            "abbrev": "WSH",
            "teamLogo": {"light": "l.svg", "dark": "d.svg"},
            "slug": "washington-capitals-15",
        },
        "hardestShot": {"imperial": 101.2, "metric": 162.9},
        "shotAttemptsOver100": 3,
        "shotAttempts90To100": 48,
        "shotAttempts80To90": 320,
        "shotAttempts70To80": 890,
    },
]


def test_get_top_10_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotSpeed10(mock_client)
    result = svc.get_top_10(sort="max")
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], TeamShotSpeedLeaderEntry)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.assert_called_once_with(
        sort="max", pos="all", season=None, game_type=None
    )


def test_get_top_10_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotSpeed10(mock_client)
    _ = svc.get_top_10(sort="max")
    _ = svc.get_top_10(sort="max")
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.assert_called_once()


def test_get_top_10_with_pos(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotSpeed10(mock_client)
    _ = svc.get_top_10(sort="over-100", pos="F")
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.assert_called_once_with(
        sort="over-100", pos="F", season=None, game_type=None
    )


def test_get_top_10_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotSpeed10(mock_client)
    result = svc.get_top_10(sort="max", season=20242025, game_type=2)
    assert isinstance(result, list)
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.assert_called_once_with(
        sort="max", pos="all", season=20242025, game_type=2
    )


def test_get_top_10_different_params_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotSpeed10(mock_client)
    _ = svc.get_top_10(sort="max")
    _ = svc.get_top_10(sort="over-100")
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.call_count == 2


def test_get_top_10_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_shot_speed_10.return_value = ok(TOP_10_RESPONSE)
    svc = TeamShotSpeed10(mock_client)
    result = svc.get_top_10(sort="max")
    first = result[0]
    assert first.team.abbrev == "CHI"
    assert first.hardest_shot.imperial == 102.83
    assert first.hardest_shot.overlay
    assert first.hardest_shot.overlay.first_name.default == "Louis"
    assert first.shot_attempts_over_100 == 6
    # second entry has no overlay
    assert result[1].hardest_shot.overlay is None
