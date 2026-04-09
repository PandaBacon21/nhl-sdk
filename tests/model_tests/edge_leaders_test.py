"""
Tests for skater and goalie Edge leader methods on SkaterLeaders and GoalieLeaders.

Covers:
  - SkaterLeaders: edge_landing, edge_distance_top_10, edge_speed_top_10,
    edge_zone_time_top_10, edge_shot_speed_top_10, edge_shot_location_top_10
  - GoalieLeaders: edge_landing, edge_five_v_five_top_10, edge_shot_location_top_10,
    edge_save_pctg_top_10
"""
from unittest.mock import MagicMock

from nhl_sdk.models.players.leaders.edge.skaters.skater_landing import SkaterLanding
from nhl_sdk.models.players.leaders.edge.goalies.goalie_landing import GoalieLanding
from nhl_sdk.models.players.leaders.player_leaders import SkaterLeaders, GoalieLeaders
from nhl_sdk.core.transport import APIResponse


# ==========================================================================
# HELPERS
# ==========================================================================

def _mock_client(data=None):
    """Return a MagicMock client whose API calls return `data`."""
    client = MagicMock()
    resp = APIResponse(ok=True, data=data, status_code=200)
    client._api.api_web.call_nhl_edge_skaters.get_skater_distance_10.return_value = resp
    client._api.api_web.call_nhl_edge_skaters.get_skating_speed_10.return_value = resp
    client._api.api_web.call_nhl_edge_skaters.get_skater_zone_time_10.return_value = resp
    client._api.api_web.call_nhl_edge_skaters.get_skater_shot_speed_10.return_value = resp
    client._api.api_web.call_nhl_edge_skaters.get_skater_shot_location_10.return_value = resp
    client._api.api_web.call_nhl_edge_skaters.get_skater_landing.return_value = resp
    client._api.api_web.call_nhl_edge_goalies.get_goalie_landing.return_value = resp
    client._api.api_web.call_nhl_edge_goalies.get_goalies_5v5_10.return_value = resp
    client._api.api_web.call_nhl_edge_goalies.get_goalie_shot_location_10.return_value = resp
    client._api.api_web.call_nhl_edge_goalies.get_goalie_save_pctg_10.return_value = resp
    return client


DISTANCE_ENTRY = {
    "player": {
        "firstName": {"default": "Connor"},
        "lastName": {"default": "McDavid"},
        "slug": "connor-mcdavid-8478402",
        "headshot": "",
        "position": "C",
        "sweaterNumber": 97,
        "team": {"id": 22, "abbrev": "EDM"},
    },
    "distanceTotal": {"imperial": 185000.0, "metric": 297720.0},
    "distancePer60": {"imperial": 3500.0, "metric": 5632.7},
    "distanceMaxPerGame": {"imperial": 3200.0, "metric": 5150.0},
    "distanceMaxPerPeriod": {"imperial": 1100.0, "metric": 1770.0},
}

SPEED_ENTRY = {
    "player": {
        "firstName": {"default": "Connor"},
        "lastName": {"default": "McDavid"},
        "slug": "connor-mcdavid-8478402",
        "headshot": "",
        "position": "C",
        "sweaterNumber": 97,
        "team": {"id": 22, "abbrev": "EDM"},
    },
    "maxSpeed": {"imperial": 24.8, "metric": 39.9},
    "burstsOver22": 3,
    "bursts20To22": 18,
    "bursts18To20": 42,
}

ZONE_TIME_ENTRY = {
    "player": {
        "firstName": {"default": "N."},
        "lastName": {"default": "MacKinnon"},
        "slug": "nathan-mackinnon-8477492",
        "headshot": "",
        "position": "C",
        "sweaterNumber": 29,
        "team": {"id": 21, "abbrev": "COL"},
    },
    "offensiveZoneTime": 38.2,
    "neutralZoneTime": 30.1,
    "defensiveZoneTime": 31.7,
}

SHOT_SPEED_ENTRY = {
    "player": {
        "firstName": {"default": "Connor"},
        "lastName": {"default": "McDavid"},
        "slug": "connor-mcdavid-8478402",
        "headshot": "",
        "position": "C",
        "sweaterNumber": 97,
        "team": {"id": 22, "abbrev": "EDM"},
    },
    "hardestShot": {"imperial": 96.2, "metric": 154.8},
    "shotAttemptsOver100": 2,
    "shotAttempts90To100": 8,
    "shotAttempts80To90": 25,
    "shotAttempts70To80": 50,
}

SHOT_LOCATION_ENTRY = {
    "player": {
        "firstName": {"default": "Connor"},
        "lastName": {"default": "McDavid"},
        "slug": "connor-mcdavid-8478402",
        "headshot": "",
        "position": "C",
        "sweaterNumber": 97,
        "team": {"id": 22, "abbrev": "EDM"},
    },
    "all": 220,
    "highDanger": 85,
    "midRange": 95,
    "longRange": 40,
}

SKATER_LANDING_DATA = {
    "seasonsWithEdgeStats": [{"id": 20242025, "gameTypes": [2]}],
    "leaders": {
        "hardestShot": {},
        "maxSkatingSpeed": {},
        "totalDistanceSkated": {},
        "distanceMaxGame": {},
        "highDangerSOG": {},
        "offensiveZoneTime": {},
        "defensiveZoneTime": {},
    },
}

GOALIE_LANDING_DATA = {
    "seasonsWithEdgeStats": [{"id": 20242025, "gameTypes": [2]}],
    "minimumGamesPlayed": 20,
    "leaders": {
        "highDangerSavePctg": {},
        "highDangerSaves": {},
        "highDangerGoalsAgainst": {},
        "savePctg5v5": {},
        "gamesAbove900": {},
    },
}


# ==========================================================================
# SKATER EDGE LEADERS — LANDING
# ==========================================================================

def test_skater_edge_landing_returns_skater_landing() -> None:
    client = _mock_client(data=SKATER_LANDING_DATA)
    service = SkaterLeaders(client=client)
    result = service.edge_landing()
    assert isinstance(result, SkaterLanding)
    assert len(result.seasons_with_edge) == 1
    assert result.seasons_with_edge[0].id == 20242025

def test_skater_edge_landing_with_season_game_type() -> None:
    client = _mock_client(data=SKATER_LANDING_DATA)
    service = SkaterLeaders(client=client)
    result = service.edge_landing(season=20242025, game_type=2)
    assert isinstance(result, SkaterLanding)
    client._api.api_web.call_nhl_edge_skaters.get_skater_landing.assert_called_once_with(
        season=20242025, game_type=2
    )

def test_skater_edge_landing_cache_hit() -> None:
    client = _mock_client(data=SKATER_LANDING_DATA)
    service = SkaterLeaders(client=client)
    service.edge_landing(season=20212022, game_type=2)
    service.edge_landing(season=20212022, game_type=2)
    assert client._api.api_web.call_nhl_edge_skaters.get_skater_landing.call_count == 1


# ==========================================================================
# SKATER EDGE LEADERS — DISTANCE TOP 10
# ==========================================================================

def test_skater_distance_top10_returns_model() -> None:
    client = _mock_client(data=[DISTANCE_ENTRY, DISTANCE_ENTRY])
    service = SkaterLeaders(client=client)
    result = service.edge_distance_top_10(pos="all", strength="es", sort="total")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0].player.last_name.default == "McDavid"
    assert result[0].distance_total.imperial == 185000.0

def test_skater_distance_top10_empty_list() -> None:
    client = _mock_client(data=[])
    service = SkaterLeaders(client=client)
    result = service.edge_distance_top_10(pos="D", strength="pp", sort="per-60")
    assert isinstance(result, list)
    assert result == []

def test_skater_distance_top10_cache_hit() -> None:
    client = _mock_client(data=[DISTANCE_ENTRY])
    service = SkaterLeaders(client=client)
    service.edge_distance_top_10(pos="F", strength="es", sort="total", season=20232024, game_type=2)
    service.edge_distance_top_10(pos="F", strength="es", sort="total", season=20232024, game_type=2)
    assert client._api.api_web.call_nhl_edge_skaters.get_skater_distance_10.call_count == 1

def test_skater_distance_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterLeaders(client=client)
    service.edge_distance_top_10(pos="D", strength="pk", sort="max-game")
    client._api.api_web.call_nhl_edge_skaters.get_skater_distance_10.assert_called_once_with(
        pos="D", strength="pk", sort="max-game", season=None, game_type=None
    )


# ==========================================================================
# SKATER EDGE LEADERS — SPEED TOP 10
# ==========================================================================

def test_skater_speed_top10_returns_model() -> None:
    client = _mock_client(data=[SPEED_ENTRY])
    service = SkaterLeaders(client=client)
    result = service.edge_speed_top_10(pos="F", sort="max")
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].max_speed.imperial == 24.8
    assert result[0].bursts_over_22 == 3

def test_skater_speed_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterLeaders(client=client)
    service.edge_speed_top_10(pos="all", sort="over-22", season=20242025, game_type=3)
    client._api.api_web.call_nhl_edge_skaters.get_skating_speed_10.assert_called_once_with(
        pos="all", sort="over-22", season=20242025, game_type=3
    )


# ==========================================================================
# SKATER EDGE LEADERS — ZONE TIME TOP 10
# ==========================================================================

def test_skater_zone_time_top10_returns_model() -> None:
    client = _mock_client(data=[ZONE_TIME_ENTRY])
    service = SkaterLeaders(client=client)
    result = service.edge_zone_time_top_10(pos="all", strength="all", sort="offensive")
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].offensive_zone_time == 38.2
    assert result[0].neutral_zone_time == 30.1

def test_skater_zone_time_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterLeaders(client=client)
    service.edge_zone_time_top_10(pos="D", strength="es", sort="defensive")
    client._api.api_web.call_nhl_edge_skaters.get_skater_zone_time_10.assert_called_once_with(
        pos="D", strength="es", sort="defensive", season=None, game_type=None
    )


# ==========================================================================
# SKATER EDGE LEADERS — SHOT SPEED TOP 10
# ==========================================================================

def test_skater_shot_speed_top10_returns_model() -> None:
    client = _mock_client(data=[SHOT_SPEED_ENTRY])
    service = SkaterLeaders(client=client)
    result = service.edge_shot_speed_top_10(pos="all", sort="max")
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].hardest_shot.imperial == 96.2
    assert result[0].shot_attempts_over_100 == 2

def test_skater_shot_speed_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterLeaders(client=client)
    service.edge_shot_speed_top_10(pos="F", sort="over-100", season=20242025, game_type=2)
    client._api.api_web.call_nhl_edge_skaters.get_skater_shot_speed_10.assert_called_once_with(
        pos="F", sort="over-100", season=20242025, game_type=2
    )


# ==========================================================================
# SKATER EDGE LEADERS — SHOT LOCATION TOP 10
# ==========================================================================

def test_skater_shot_location_top10_returns_model() -> None:
    client = _mock_client(data=[SHOT_LOCATION_ENTRY])
    service = SkaterLeaders(client=client)
    result = service.edge_shot_location_top_10(category="sog", sort="all")
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].all == 220
    assert result[0].high_danger == 85

def test_skater_shot_location_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterLeaders(client=client)
    service.edge_shot_location_top_10(category="goals", sort="high")
    client._api.api_web.call_nhl_edge_skaters.get_skater_shot_location_10.assert_called_once_with(
        category="goals", sort="high", season=None, game_type=None
    )


# ==========================================================================
# GOALIE EDGE LEADERS — LANDING
# ==========================================================================

def test_goalie_edge_landing_returns_goalie_landing() -> None:
    client = _mock_client(data=GOALIE_LANDING_DATA)
    service = GoalieLeaders(client=client)
    result = service.edge_landing()
    assert isinstance(result, GoalieLanding)
    assert len(result.seasons_with_edge) == 1
    assert result.seasons_with_edge[0].id == 20242025
    assert result.minimum_games_played == 20

def test_goalie_edge_landing_with_season_game_type() -> None:
    client = _mock_client(data=GOALIE_LANDING_DATA)
    service = GoalieLeaders(client=client)
    result = service.edge_landing(season=20242025, game_type=2)
    assert isinstance(result, GoalieLanding)
    client._api.api_web.call_nhl_edge_goalies.get_goalie_landing.assert_called_once_with(
        season=20242025, game_type=2
    )


# ==========================================================================
# GOALIE EDGE LEADERS — TOP 10 (raw list — no model yet)
# ==========================================================================

def test_goalie_five_v_five_top10_returns_list() -> None:
    raw = [{"player": {}, "savePctg": 0.934}]
    client = _mock_client(data=raw)
    service = GoalieLeaders(client=client)
    result = service.edge_five_v_five_top_10(sort="savePctg")
    assert isinstance(result, list)
    assert len(result) == 1

def test_goalie_shot_location_top10_returns_list() -> None:
    client = _mock_client(data=[])
    service = GoalieLeaders(client=client)
    result = service.edge_shot_location_top_10(category="sog", sort="all")
    assert isinstance(result, list)

def test_goalie_save_pctg_top10_returns_list() -> None:
    client = _mock_client(data=[{"player": {}, "savePctg": 0.921}])
    service = GoalieLeaders(client=client)
    result = service.edge_save_pctg_top_10(sort="savePctg")
    assert isinstance(result, list)
    assert len(result) == 1
