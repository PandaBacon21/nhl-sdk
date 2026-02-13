import src.resources.api_web.games as games_test


DATE: str = "2025-11-15"
GAME_ID: int = 2025020417


def test_daily_scores(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(games_test, "_call_api_get", fake_call)

    scores = games_test._get_daily_scores(date=DATE)

    assert scores["ok"] == True
    assert scores["status_code"] == 200
    assert called["endpoint"] == f"v1/score/{DATE}"

def test_play_by_play(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(games_test, "_call_api_get", fake_call)

    pbp = games_test._get_play_by_play(game_id=GAME_ID)

    assert pbp["ok"] == True
    assert pbp["status_code"] == 200
    assert called["endpoint"] == f"v1/gamecenter/{GAME_ID}/play-by-play"

def test_boxscore(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(games_test, "_call_api_get", fake_call)

    boxscore = games_test._get_boxscore(game_id=GAME_ID)

    assert boxscore["ok"] == True
    assert boxscore["status_code"] == 200
    assert called["endpoint"] == f"v1/gamecenter/{GAME_ID}/boxscore"

def test_tv_schedule_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "data": "Test Error"}
    
    monkeypatch.setattr(games_test, "_call_api_get", fake_call)

    schedule = games_test._get_tv_schedule()

    assert schedule["ok"] == False
    assert called["endpoint"] == f"v1/network/tv-schedule/now"




    