from src.resources.api_web.league import CallNhlLeague as LeagueTests
from src.core.transport import APICallWeb, APIResponse

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

