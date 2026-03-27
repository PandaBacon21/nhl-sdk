"""
Tests for SkaterEdgeLeaders and GoalieEdgeLeaders service classes.

Covers:
  - SkaterEdgeLeaders: landing, distance_top_10, speed_top_10, zone_time_top_10,
    shot_speed_top_10, shot_location_top_10
  - GoalieEdgeLeaders: landing, five_v_five_top_10, shot_location_top_10,
    save_pctg_top_10
  - SkaterLeaders.get_edge_leaders and GoalieLeaders.get_edge_leaders properties
"""
from unittest.mock import MagicMock

from src.models.players.leaders.edge.edge_leaders import (
    SkaterEdgeLeaders,
    GoalieEdgeLeaders,
)
from src.models.players.leaders.edge.skaters import (
    SkaterDistanceTop10,
    SkaterSpeedTop10,
    SkaterZoneTimeTop10,
    SkaterShotSpeedTop10,
    SkaterShotLocationTop10,
)
from src.models.players.leaders.edge.skaters.skater_landing import SkaterLanding
from src.models.players.leaders.edge.goalies.goalie_landing import GoalieLanding
from src.models.players.leaders.player_leaders import SkaterLeaders, GoalieLeaders
from src.core.transport import APIResponse


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
    service = SkaterEdgeLeaders(client=client)
    result = service.landing()
    assert isinstance(result, SkaterLanding)
    assert len(result.seasons_with_edge) == 1
    assert result.seasons_with_edge[0].id == 20242025

def test_skater_edge_landing_with_season_game_type() -> None:
    client = _mock_client(data=SKATER_LANDING_DATA)
    service = SkaterEdgeLeaders(client=client)
    result = service.landing(season=20242025, game_type=2)
    assert isinstance(result, SkaterLanding)
    client._api.api_web.call_nhl_edge_skaters.get_skater_landing.assert_called_once_with(
        season=20242025, game_type=2
    )

def test_skater_edge_landing_cache_hit() -> None:
    client = _mock_client(data=SKATER_LANDING_DATA)
    service = SkaterEdgeLeaders(client=client)
    service.landing(season=20212022, game_type=2)
    service.landing(season=20212022, game_type=2)
    # API should only be called once; second call is a cache hit
    assert client._api.api_web.call_nhl_edge_skaters.get_skater_landing.call_count == 1


# ==========================================================================
# SKATER EDGE LEADERS — DISTANCE TOP 10
# ==========================================================================

def test_skater_distance_top10_returns_model() -> None:
    client = _mock_client(data=[DISTANCE_ENTRY, DISTANCE_ENTRY])
    service = SkaterEdgeLeaders(client=client)
    result = service.distance_top_10(pos="all", strength="es", sort="total")
    assert isinstance(result, SkaterDistanceTop10)
    assert len(result.entries) == 2
    assert result.entries[0].player.last_name.default == "McDavid"
    assert result.entries[0].distance_total.imperial == 185000.0

def test_skater_distance_top10_empty_list() -> None:
    client = _mock_client(data=[])
    service = SkaterEdgeLeaders(client=client)
    result = service.distance_top_10(pos="D", strength="pp", sort="per-60")
    assert isinstance(result, SkaterDistanceTop10)
    assert result.entries == []

def test_skater_distance_top10_cache_hit() -> None:
    client = _mock_client(data=[DISTANCE_ENTRY])
    service = SkaterEdgeLeaders(client=client)
    service.distance_top_10(pos="F", strength="es", sort="total", season=20232024, game_type=2)
    service.distance_top_10(pos="F", strength="es", sort="total", season=20232024, game_type=2)
    assert client._api.api_web.call_nhl_edge_skaters.get_skater_distance_10.call_count == 1

def test_skater_distance_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterEdgeLeaders(client=client)
    service.distance_top_10(pos="D", strength="pk", sort="max-game")
    client._api.api_web.call_nhl_edge_skaters.get_skater_distance_10.assert_called_once_with(
        pos="D", strength="pk", sort="max-game", season=None, game_type=None
    )


# ==========================================================================
# SKATER EDGE LEADERS — SPEED TOP 10
# ==========================================================================

def test_skater_speed_top10_returns_model() -> None:
    client = _mock_client(data=[SPEED_ENTRY])
    service = SkaterEdgeLeaders(client=client)
    result = service.speed_top_10(pos="F", sort="max")
    assert isinstance(result, SkaterSpeedTop10)
    assert len(result.entries) == 1
    assert result.entries[0].max_speed.imperial == 24.8
    assert result.entries[0].bursts_over_22 == 3

def test_skater_speed_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterEdgeLeaders(client=client)
    service.speed_top_10(pos="all", sort="over-22", season=20242025, game_type=3)
    client._api.api_web.call_nhl_edge_skaters.get_skating_speed_10.assert_called_once_with(
        pos="all", sort="over-22", season=20242025, game_type=3
    )


# ==========================================================================
# SKATER EDGE LEADERS — ZONE TIME TOP 10
# ==========================================================================

def test_skater_zone_time_top10_returns_model() -> None:
    client = _mock_client(data=[ZONE_TIME_ENTRY])
    service = SkaterEdgeLeaders(client=client)
    result = service.zone_time_top_10(pos="all", strength="all", sort="offensive")
    assert isinstance(result, SkaterZoneTimeTop10)
    assert len(result.entries) == 1
    assert result.entries[0].offensive_zone_time == 38.2
    assert result.entries[0].neutral_zone_time == 30.1

def test_skater_zone_time_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterEdgeLeaders(client=client)
    service.zone_time_top_10(pos="D", strength="es", sort="defensive")
    client._api.api_web.call_nhl_edge_skaters.get_skater_zone_time_10.assert_called_once_with(
        pos="D", strength="es", sort="defensive", season=None, game_type=None
    )


# ==========================================================================
# SKATER EDGE LEADERS — SHOT SPEED TOP 10
# ==========================================================================

def test_skater_shot_speed_top10_returns_model() -> None:
    client = _mock_client(data=[SHOT_SPEED_ENTRY])
    service = SkaterEdgeLeaders(client=client)
    result = service.shot_speed_top_10(pos="all", sort="max")
    assert isinstance(result, SkaterShotSpeedTop10)
    assert len(result.entries) == 1
    assert result.entries[0].hardest_shot.imperial == 96.2
    assert result.entries[0].shot_attempts_over_100 == 2

def test_skater_shot_speed_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterEdgeLeaders(client=client)
    service.shot_speed_top_10(pos="F", sort="over-100", season=20242025, game_type=2)
    client._api.api_web.call_nhl_edge_skaters.get_skater_shot_speed_10.assert_called_once_with(
        pos="F", sort="over-100", season=20242025, game_type=2
    )


# ==========================================================================
# SKATER EDGE LEADERS — SHOT LOCATION TOP 10
# ==========================================================================

def test_skater_shot_location_top10_returns_model() -> None:
    client = _mock_client(data=[SHOT_LOCATION_ENTRY])
    service = SkaterEdgeLeaders(client=client)
    result = service.shot_location_top_10(category="sog", sort="all")
    assert isinstance(result, SkaterShotLocationTop10)
    assert len(result.entries) == 1
    assert result.entries[0].all == 220
    assert result.entries[0].high_danger == 85

def test_skater_shot_location_top10_api_params() -> None:
    client = _mock_client(data=[])
    service = SkaterEdgeLeaders(client=client)
    service.shot_location_top_10(category="goals", sort="high")
    client._api.api_web.call_nhl_edge_skaters.get_skater_shot_location_10.assert_called_once_with(
        category="goals", sort="high", season=None, game_type=None
    )


# ==========================================================================
# GOALIE EDGE LEADERS — LANDING
# ==========================================================================

def test_goalie_edge_landing_returns_goalie_landing() -> None:
    client = _mock_client(data=GOALIE_LANDING_DATA)
    service = GoalieEdgeLeaders(client=client)
    result = service.landing()
    assert isinstance(result, GoalieLanding)
    assert len(result.seasons_with_edge) == 1
    assert result.seasons_with_edge[0].id == 20242025
    assert result.minimum_games_played == 20

def test_goalie_edge_landing_with_season_game_type() -> None:
    client = _mock_client(data=GOALIE_LANDING_DATA)
    service = GoalieEdgeLeaders(client=client)
    result = service.landing(season=20242025, game_type=2)
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
    service = GoalieEdgeLeaders(client=client)
    result = service.five_v_five_top_10(sort="savePctg")
    assert isinstance(result, list)
    assert len(result) == 1

def test_goalie_shot_location_top10_returns_list() -> None:
    client = _mock_client(data=[])
    service = GoalieEdgeLeaders(client=client)
    result = service.shot_location_top_10(category="sog", sort="all")
    assert isinstance(result, list)

def test_goalie_save_pctg_top10_returns_list() -> None:
    client = _mock_client(data=[{"player": {}, "savePctg": 0.921}])
    service = GoalieEdgeLeaders(client=client)
    result = service.save_pctg_top_10(sort="savePctg")
    assert isinstance(result, list)
    assert len(result) == 1



# ==========================================================================
# SKATER LEADERS / GOALIE LEADERS — .get_edge_leaders PROPERTY
# ==========================================================================

def test_skater_leaders_get_edge_leaders_property() -> None:
    client = MagicMock()
    leaders = SkaterLeaders(client=client)
    edge = leaders.get_edge_leaders
    assert isinstance(edge, SkaterEdgeLeaders)

def test_goalie_leaders_get_edge_leaders_property() -> None:
    client = MagicMock()
    leaders = GoalieLeaders(client=client)
    edge = leaders.get_edge_leaders
    assert isinstance(edge, GoalieEdgeLeaders)
