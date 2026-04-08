"""
Tests for TeamLanding service: get_landing()
"""
from nhl_stats.models.teams.edge.team_landing import TeamLanding, TeamEdgeLandingResult

from .conftest import ok


LANDING_RESPONSE = {
    "seasonsWithEdgeStats": [
        {"id": 20242025, "gameTypes": [2, 3]},
    ],
    "leaders": {
        "shotAttemptsOver90": {
            "team": {
                "id": 22,
                "commonName": {"default": "Oilers"},
                "placeNameWithPreposition": {"default": "Edmonton"},
                "abbrev": "EDM",
                "teamLogo": {"light": "l.svg", "dark": "d.svg"},
                "slug": "edmonton-oilers-22",
                "wins": 48,
                "losses": 29,
                "otLosses": 5,
            },
            "attempts": 136,
        },
        "burstsOver22": {
            "team": {
                "id": 21,
                "commonName": {"default": "Avalanche"},
                "placeNameWithPreposition": {"default": "Colorado"},
                "abbrev": "COL",
                "teamLogo": {"light": "l.svg", "dark": "d.svg"},
                "slug": "colorado-avalanche-21",
                "wins": 49,
                "losses": 29,
                "otLosses": 4,
            },
            "bursts": 212,
        },
        "distancePer60": {
            "team": {
                "id": 13,
                "commonName": {"default": "Panthers"},
                "placeNameWithPreposition": {"default": "Florida"},
                "abbrev": "FLA",
                "teamLogo": {"light": "l.svg", "dark": "d.svg"},
                "slug": "florida-panthers-13",
                "wins": 47,
                "losses": 31,
                "otLosses": 4,
            },
            "distanceSkated": {"imperial": 9.341, "metric": 15.032},
        },
        "highDangerSOG": {
            "team": {
                "id": 22,
                "commonName": {"default": "Oilers"},
                "placeNameWithPreposition": {"default": "Edmonton"},
                "abbrev": "EDM",
                "teamLogo": {"light": "l.svg", "dark": "d.svg"},
                "slug": "edmonton-oilers-22",
                "wins": 48,
                "losses": 29,
                "otLosses": 5,
            },
            "sog": 714,
            "shotLocationDetails": [{"area": "Low Slot", "sog": 603, "rank": 3}],
        },
        "offensiveZoneTime": {
            "team": {
                "id": 12,
                "commonName": {"default": "Hurricanes"},
                "placeNameWithPreposition": {"default": "Carolina"},
                "abbrev": "CAR",
                "teamLogo": {"light": "l.svg", "dark": "d.svg"},
                "slug": "carolina-hurricanes-12",
                "wins": 47,
                "losses": 30,
                "otLosses": 5,
            },
            "zoneTime": 0.4605141,
        },
        "neutralZoneTime": {
            "team": {
                "id": 25,
                "commonName": {"default": "Stars"},
                "placeNameWithPreposition": {"default": "Dallas"},
                "abbrev": "DAL",
                "teamLogo": {"light": "l.svg", "dark": "d.svg"},
                "slug": "dallas-stars-25",
                "wins": 50,
                "losses": 26,
                "otLosses": 6,
            },
            "zoneTime": 0.1873355,
        },
        "defensiveZoneTime": {
            "team": {
                "id": 12,
                "commonName": {"default": "Hurricanes"},
                "placeNameWithPreposition": {"default": "Carolina"},
                "abbrev": "CAR",
                "teamLogo": {"light": "l.svg", "dark": "d.svg"},
                "slug": "carolina-hurricanes-12",
                "wins": 47,
                "losses": 30,
                "otLosses": 5,
            },
            "zoneTime": 0.3545412,
        },
    },
}


def test_get_landing_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.return_value = ok(LANDING_RESPONSE)
    svc = TeamLanding(mock_client)
    result = svc.get_landing()
    assert isinstance(result, TeamEdgeLandingResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.assert_called_once_with(
        season=None, game_type=None
    )


def test_get_landing_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.return_value = ok(LANDING_RESPONSE)
    svc = TeamLanding(mock_client)
    _ = svc.get_landing()
    _ = svc.get_landing()
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.assert_called_once()


def test_get_landing_with_season_and_game_type(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.return_value = ok(LANDING_RESPONSE)
    svc = TeamLanding(mock_client)
    result = svc.get_landing(season=20242025, game_type=2)
    assert isinstance(result, TeamEdgeLandingResult)
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.assert_called_once_with(
        season=20242025, game_type=2
    )


def test_get_landing_different_seasons_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.return_value = ok(LANDING_RESPONSE)
    svc = TeamLanding(mock_client)
    _ = svc.get_landing()
    _ = svc.get_landing(season=20232024, game_type=2)
    assert mock_client._api.api_web.call_nhl_edge_team.get_team_landing.call_count == 2


def test_get_landing_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_edge_team.get_team_landing.return_value = ok(LANDING_RESPONSE)
    svc = TeamLanding(mock_client)
    result = svc.get_landing()
    assert len(result.seasons_with_edge) == 1
    assert result.seasons_with_edge[0].id == 20242025
    assert result.leaders.shot_attempts_over_90.attempts == 136
    assert result.leaders.shot_attempts_over_90.team.abbrev == "EDM"
    assert result.leaders.bursts_over_22.bursts == 212
    assert result.leaders.distance_per_60.distance_skated.imperial == 9.341
    assert result.leaders.high_danger_sog.sog == 714
    assert result.leaders.offensive_zone_time.zone_time == 0.4605141
