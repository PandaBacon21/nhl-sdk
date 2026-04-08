"""
Resource tests for CallNhlStatsGames.
"""
from nhl_stats.resources.api_stats.games import CallNhlStatsGames
from nhl_stats.core.transport import APICallStats, APIResponse

svc = CallNhlStatsGames(http=APICallStats())


def _fake(called: dict):
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    return fake_call


def test_get_game_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_game()
    assert called["endpoint"] == "/en/game"


def test_get_game_with_cayenne(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_game(cayenne_exp="season=20242025")
    assert called["params"]["cayenneExp"] == "season=20242025"


def test_get_game_with_limit(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_game(limit=10)
    assert called["params"]["limit"] == 10


def test_get_game_no_params_passes_none(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_game()
    assert called["params"] is None


def test_get_game_meta_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_game_meta()
    assert called["endpoint"] == "/en/game/meta"
