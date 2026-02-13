import src.resources.api_web.league as league


DATE: str = "2025-11-15"

def test_league_schedule(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(league, "_call_api_get", fake_call)

    landing = league._get_schedule(date=DATE)

    assert landing["ok"] == True
    assert landing["status_code"] == 200
    assert called["endpoint"] == f"v1/schedule/{DATE}"

