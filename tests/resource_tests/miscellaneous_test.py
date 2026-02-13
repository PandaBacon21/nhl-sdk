import src.resources.api_web.miscellaneous as msc_test

YEAR: int = 2024
GAME_ID: int = 2025020417
SERIES_LETTER: str = "A"
EVENT_NUM: int = 3

def test_get_meta(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(msc_test, "_call_api_get", fake_call)

    meta = msc_test._get_meta()

    assert meta["ok"] == True
    assert meta["status_code"] == 200
    assert called["endpoint"] == f"v1/meta"

def test_game_info(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(msc_test, "_call_api_get", fake_call)

    game = msc_test._get_game_info(game_id=GAME_ID)

    assert game["ok"] == True
    assert game["status_code"] == 200
    assert called["endpoint"] == f"v1/meta/game/{GAME_ID}"

def test_playoffs_series_meta(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(msc_test, "_call_api_get", fake_call)

    game = msc_test._get_playoff_series_meta(year=YEAR, series_letter=SERIES_LETTER)

    assert game["ok"] == True
    assert game["status_code"] == 200
    assert called["endpoint"] == f"v1/meta/playoff-series/{YEAR}/{SERIES_LETTER}"

def test_goal_replay_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "error": "Test Error"}
    
    monkeypatch.setattr(msc_test, "_call_api_get", fake_call)

    game = msc_test._get_goal_replay(game_id=GAME_ID, event_number=EVENT_NUM)

    assert game["ok"] == False
    assert called["endpoint"] == f"v1/ppt-replay/goal/{GAME_ID}/{EVENT_NUM}"


