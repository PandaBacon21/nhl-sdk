"""
Resource tests for CallNhlStatsDraft.
"""
from src.resources.api_stats.draft import CallNhlStatsDraft
from src.core.transport import APICallStats, APIResponse

svc = CallNhlStatsDraft(http=APICallStats())


def _fake(called: dict):
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    return fake_call


def test_get_draft_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_draft()
    assert called["endpoint"] == "/en/draft"


def test_get_draft_with_cayenne(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_draft(cayenne_exp="draftYear=2023 and roundNumber=1")
    assert called["params"]["cayenneExp"] == "draftYear=2023 and roundNumber=1"


def test_get_draft_with_limit(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_draft(limit=32)
    assert called["params"]["limit"] == 32


def test_get_draft_no_params_passes_none(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_draft()
    assert called["params"] is None


def test_get_draft_with_sort(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_draft(sort="overallPickNumber", dir="ASC")
    assert called["params"]["sort"] == "overallPickNumber"
    assert called["params"]["dir"] == "ASC"
