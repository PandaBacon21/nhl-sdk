from src.resources.api_web.draft import CallNhlDraft as DraftTest
from src.core.transport import APICallWeb, APIResponse

SEASON: int = 20232024
CATEGORY: int = 1


draft_test = DraftTest(http=APICallWeb())

def test_draft_rankings(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(draft_test._http, "get", fake_call)

    res = draft_test.get_rankings(season=SEASON, category=CATEGORY)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/draft/rankings/{SEASON}/{CATEGORY}"

def test_draft_tracker(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(draft_test._http, "get", fake_call)

    res = draft_test.get_tracker_now()

    assert res.ok == False
    assert called["endpoint"] == f"/v1/draft-tracker/picks/now"