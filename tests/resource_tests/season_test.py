import src.resources.api_web.season as season_test


def test_seasons(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(season_test, "_call_api_get", fake_call)

    seasons = season_test._get_seasons()

    assert seasons["ok"] == True
    assert seasons["status_code"] == 200
    assert called["endpoint"] == f"v1/season"
