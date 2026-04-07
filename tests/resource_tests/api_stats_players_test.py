"""
Resource tests for CallNhlStatsPlayers.
"""
from src.resources.api_stats.players import CallNhlStatsPlayers
from src.core.transport import APICallStats, APIResponse

svc = CallNhlStatsPlayers(http=APICallStats())


def _fake(called: dict):
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    return fake_call


# ==========================================================================
# Skater stats
# ==========================================================================

def test_get_skater_stats_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    res = svc.get_skater_stats("summary")
    assert res.ok
    assert called["endpoint"] == "/en/skater/summary"


def test_get_skater_stats_with_cayenne(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_skater_stats("summary", cayenne_exp="playerId=8477492")
    assert called["params"]["cayenneExp"] == "playerId=8477492"


def test_get_skater_stats_with_limit(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_skater_stats("realtime", limit=10)
    assert called["params"]["limit"] == 10


def test_get_skater_stats_no_params_passes_none(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_skater_stats("bios")
    assert called["params"] is None


# ==========================================================================
# Skater leaders
# ==========================================================================

def test_get_skater_leaders_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_skater_leaders("goals")
    assert called["endpoint"] == "/en/leaders/skaters/goals"


# ==========================================================================
# Skater milestones
# ==========================================================================

def test_get_skater_milestones_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_skater_milestones()
    assert called["endpoint"] == "/en/milestones/skaters"


def test_get_skater_milestones_with_cayenne(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_skater_milestones(cayenne_exp='milestone="Goals"')
    assert called["params"]["cayenneExp"] == 'milestone="Goals"'


# ==========================================================================
# Goalie stats
# ==========================================================================

def test_get_goalie_stats_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_goalie_stats("summary")
    assert called["endpoint"] == "/en/goalie/summary"


def test_get_goalie_stats_with_cayenne(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_goalie_stats("advanced", cayenne_exp="playerId=8476883")
    assert called["params"]["cayenneExp"] == "playerId=8476883"


# ==========================================================================
# Goalie leaders
# ==========================================================================

def test_get_goalie_leaders_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_goalie_leaders("wins")
    assert called["endpoint"] == "/en/leaders/goalies/wins"


# ==========================================================================
# Goalie milestones
# ==========================================================================

def test_get_goalie_milestones_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_goalie_milestones()
    assert called["endpoint"] == "/en/milestones/goalies"


def test_get_goalie_milestones_with_limit(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_goalie_milestones(limit=5)
    assert called["params"]["limit"] == 5


# ==========================================================================
# Players
# ==========================================================================

def test_get_players_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_players()
    assert called["endpoint"] == "/en/players"


def test_get_players_with_cayenne(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_players(cayenne_exp="active=1")
    assert called["params"]["cayenneExp"] == "active=1"
