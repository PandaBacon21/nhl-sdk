import src.resources.api_web.draft as draft_test

SEASON: int = 20232024
CATEGORY: int = 1


def test_draft_rankings(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(draft_test, "_call_api_get", fake_call)

    rankings = draft_test._get_rankings(season=SEASON, category=CATEGORY)

    assert rankings["ok"] == True
    assert rankings["status_code"] == 200
    assert called["endpoint"] == f"v1/draft/rankings/{SEASON}/{CATEGORY}"

def test_draft_tracker(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "error": "Test Error"}
    
    monkeypatch.setattr(draft_test, "_call_api_get", fake_call)

    tracker = draft_test._get_tracker_now()

    assert tracker["ok"] == False
    assert called["endpoint"] == f"v1/draft-tracker/picks/now"