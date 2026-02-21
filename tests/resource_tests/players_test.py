from src.resources.api_web.players import CallNhlPlayers as PlayersTest
from src.core.transport import APICallWeb, APIResponse

PLAYER_ID: int = 8477492

SEASON: int = 20232024
GAME_TYPE: int = 2
CATEGORIES: str = "goals"
LIMIT: int | None = 5

players_test = PlayersTest(http=APICallWeb())


def test_player_landing(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(players_test._http, "get", fake_call)

    res = players_test.get_player_landing(pid=PLAYER_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/player/{PLAYER_ID}/landing"

def test_player_landing_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(players_test._http, "get", fake_call)

    res = players_test.get_player_landing(pid=PLAYER_ID)

    assert res.ok == False
    assert res.data == {"error": "Test Error"}
    assert called["endpoint"] == f"/v1/player/{PLAYER_ID}/landing"

def test_skater_leaders(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(players_test._http, "get", fake_call)

    res = players_test.get_skater_leaders(season=SEASON, g_type=GAME_TYPE, categories=CATEGORIES, limit=LIMIT)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/skater-stats-leaders/{SEASON}/{GAME_TYPE}"
    assert called["params"] == { 
        "categories": CATEGORIES,
        "limit": LIMIT
        }

def test_skater_leaders_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(players_test._http, "get", fake_call)

    res = players_test.get_skater_leaders(season=SEASON, g_type=GAME_TYPE)

    assert res.ok == False
    assert res.data == {"error": "Test Error"}
    assert called["endpoint"] == f"/v1/skater-stats-leaders/{SEASON}/{GAME_TYPE}"






