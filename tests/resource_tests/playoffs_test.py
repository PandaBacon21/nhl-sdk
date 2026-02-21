from src.resources.api_web.playoffs import CallNhlPlayoffs as PlayoffTest
from src.core.transport import APICallWeb, APIResponse

SEASON: int = 20232024
SERIES_LETTER: str = "A"

playoffs_test = PlayoffTest(http=APICallWeb())

def test_playoff_carousel(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(playoffs_test._http, "get", fake_call)

    res = playoffs_test.get_carousel(season=SEASON)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/playoff-series/carousel/{SEASON}/"

def test_playoff_series_schedule(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(playoffs_test._http, "get", fake_call)

    res = playoffs_test.get_series_schedule(season=SEASON, series_letter=SERIES_LETTER)

    assert res.ok == False
    assert called["endpoint"] == f"/v1/schedule/playoff-series/{SEASON}/{SERIES_LETTER}/"