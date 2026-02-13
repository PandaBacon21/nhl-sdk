import src.resources.api_web.playoffs as playoffs_test

SEASON: int = 20232024
SERIES_LETTER: str = "A"

def test_playoff_carousel(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(playoffs_test, "_call_api_get", fake_call)

    carousel = playoffs_test._get_carousel(season=SEASON)

    assert carousel["ok"] == True
    assert carousel["status_code"] == 200
    assert called["endpoint"] == f"v1/playoff-series/carousel/{SEASON}/"

def test_playoff_series_schedule(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "error": "Test Error"}
    
    monkeypatch.setattr(playoffs_test, "_call_api_get", fake_call)

    carousel = playoffs_test._get_series_schedule(season=SEASON, series_letter=SERIES_LETTER)

    assert carousel["ok"] == False
    assert called["endpoint"] == f"v1/schedule/playoff-series/{SEASON}/{SERIES_LETTER}/"