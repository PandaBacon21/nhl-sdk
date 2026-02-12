import src.resources.api_web.players as players_test

PLAYER_ID: int = 8477492

SEASON: int = 20232024
GAME_TYPE: int = 2
CATEGORIES: str = "goals"
LIMIT: int | None = 5


def test_player_landing(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(players_test, "_call_api_get", fake_call)

    landing = players_test._get_player_landing(pid=PLAYER_ID)

    assert landing["ok"] == True
    assert landing["status_code"] == 200
    assert called["endpoint"] == f"v1/player/{PLAYER_ID}/landing"

def test_player_landing_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "error": "Test Error"}
    
    monkeypatch.setattr(players_test, "_call_api_get", fake_call)

    landing = players_test._get_player_landing(pid=PLAYER_ID)

    assert landing["ok"] == False
    assert landing["error"]
    assert called["endpoint"] == f"v1/player/{PLAYER_ID}/landing"

def test_skater_leaders(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(players_test, "_call_api_get", fake_call)

    leaders = players_test._get_skater_leaders(season=SEASON, g_type=GAME_TYPE, categories=CATEGORIES, limit=LIMIT)

    assert leaders["ok"] == True
    assert leaders["status_code"] == 200
    assert called["endpoint"] == f"v1/skater-stats-leaders/{SEASON}/{GAME_TYPE}"
    assert called["params"] == { 
        "categories": CATEGORIES,
        "limit": LIMIT
        }

def test_skater_leaders_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "error": "Test Error"}
    
    monkeypatch.setattr(players_test, "_call_api_get", fake_call)

    leaders = players_test._get_skater_leaders(season=SEASON, g_type=GAME_TYPE)

    assert leaders["ok"] == False
    assert leaders["error"]
    assert called["endpoint"] == f"v1/skater-stats-leaders/{SEASON}/{GAME_TYPE}"






