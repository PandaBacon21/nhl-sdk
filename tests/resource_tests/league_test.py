from nhl_stats.resources.api_web.league import CallNhlLeague as LeagueTests
from nhl_stats.core.transport import APICallWeb, APIResponse

DATE: str = "2025-11-15"

league_test = LeagueTests(http=APICallWeb())

def test_league_schedule(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(league_test._http, "get", fake_call)

    res = league_test.get_schedule(date=DATE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/schedule/{DATE}"

def test_league_schedule_now(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(league_test._http, "get", fake_call)

    res = league_test.get_schedule()

    assert res.ok == True
    assert called["endpoint"] == "/v1/schedule/now"

def test_league_schedule_calendar(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(league_test._http, "get", fake_call)

    res = league_test.get_schedule_calendar(date=DATE)

    assert res.ok == True
    assert called["endpoint"] == f"/v1/schedule-calendar/{DATE}"

def test_league_schedule_calendar_now(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(league_test._http, "get", fake_call)

    res = league_test.get_schedule_calendar()

    assert res.ok == True
    assert called["endpoint"] == "/v1/schedule-calendar/now"

