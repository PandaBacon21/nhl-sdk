import src.resources.api_web.teams as teams_test


TEAM_CODE: str = "COL"
TEAM_ID: int = 21

SEASON: int = 20232024
GAME_TYPE: int = 2
DATE: str = "2025-11-15"

def test_team_standings(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(teams_test, "_call_api_get", fake_call)

    landing = teams_test._get_standings()

    assert landing["ok"] == True
    assert landing["status_code"] == 200
    assert called["endpoint"] == f"v1/standings/now"

def test_get_standings_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "error": "Test Error"}
    
    monkeypatch.setattr(teams_test, "_call_api_get", fake_call)

    stats = teams_test._get_standings(date=DATE)

    assert stats["ok"] == False
    assert stats["error"] == "Test Error"
    assert called["endpoint"] == f"v1/standings/{DATE}"

def test_team_stats(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(teams_test, "_call_api_get", fake_call)

    stats = teams_test._get_team_stats(team=TEAM_CODE, season=SEASON, g_type=GAME_TYPE)

    assert stats["ok"] == True
    assert stats["status_code"] == 200
    assert called["endpoint"] == f"v1/club-stats/{TEAM_CODE}/{SEASON}/{GAME_TYPE}"

def test_team_scoreboard(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(teams_test, "_call_api_get", fake_call)

    stats = teams_test._get_team_scoreboard(team=TEAM_CODE)

    assert stats["ok"] == True
    assert stats["status_code"] == 200
    assert called["endpoint"] == f"v1/scoreboard/{TEAM_CODE}/now"

def test_team_roster(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(teams_test, "_call_api_get", fake_call)

    stats = teams_test._get_team_roster(team=TEAM_CODE, season=SEASON)

    assert stats["ok"] == True
    assert stats["status_code"] == 200
    assert called["endpoint"] == f"v1/roster/{TEAM_CODE}/{SEASON}"

def test_team_schedule(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": True, "data": {}, "status_code": 200}
    
    monkeypatch.setattr(teams_test, "_call_api_get", fake_call)

    stats = teams_test._get_schedule(team=TEAM_CODE, season=SEASON)

    assert stats["ok"] == True
    assert stats["status_code"] == 200
    assert called["endpoint"] == f"v1/club-schedule-season/{TEAM_CODE}/{SEASON}"

def test_team_schedule_week_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> dict: 
        called["endpoint"] = endpoint
        called["params"] = params
        return {"ok": False, "error": "Test Error"}
    
    monkeypatch.setattr(teams_test, "_call_api_get", fake_call)

    stats = teams_test._get_schedule_week(team=TEAM_CODE, week=DATE)

    assert stats["ok"] == False
    assert called["endpoint"] == f"v1/club-schedule/{TEAM_CODE}/week/{DATE}"