"""
Resource tests for CallNhlStatsSeasons.
"""
from src.resources.api_stats.seasons import CallNhlStatsSeasons
from src.core.transport import APICallStats, APIResponse

svc = CallNhlStatsSeasons(http=APICallStats())


def _fake(called: dict):
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    return fake_call


def test_get_season_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_season()
    assert called["endpoint"] == "/en/season"


def test_get_component_season_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_component_season()
    assert called["endpoint"] == "/en/componentSeason"


def test_get_season_returns_ok(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    res = svc.get_season()
    assert res.ok
    assert res.status_code == 200


def test_get_component_season_returns_ok(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    res = svc.get_component_season()
    assert res.ok
    assert res.status_code == 200
