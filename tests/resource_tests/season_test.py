from src.resources.api_web.season import CallNhlSeasons as SeasonTest
from src.core.transport import APICallWeb, APIResponse

season_test = SeasonTest(http=APICallWeb())

def test_seasons(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(season_test._http, "get", fake_call)

    res = season_test.get_seasons()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/season"
