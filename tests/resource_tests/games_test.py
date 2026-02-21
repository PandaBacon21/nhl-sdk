from src.resources.api_web.games import CallNhlGames as GamesTest
from src.core.transport import APICallWeb, APIResponse

DATE: str = "2025-11-15"
GAME_ID: int = 2025020417

games_test = GamesTest(http=APICallWeb())

def test_daily_scores(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(games_test._http, "get", fake_call)

    res = games_test.get_daily_scores(date=DATE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/score/{DATE}"

def test_play_by_play(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(games_test._http, "get", fake_call)

    res = games_test.get_play_by_play(game_id=GAME_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/gamecenter/{GAME_ID}/play-by-play"

def test_boxscore(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(games_test._http, "get", fake_call)

    res = games_test.get_boxscore(game_id=GAME_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/gamecenter/{GAME_ID}/boxscore"

def test_tv_schedule_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(games_test._http, "get", fake_call)

    res = games_test.get_tv_schedule()

    assert res.ok == False
    assert called["endpoint"] == f"/v1/network/tv-schedule/now"




    