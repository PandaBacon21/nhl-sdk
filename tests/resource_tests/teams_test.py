from src.resources.api_web.teams import CallNhlTeams as TeamsTest
from src.core.transport import APICallWeb, APIResponse


TEAM_CODE: str = "COL"
TEAM_ID: int = 21

SEASON: int = 20232024
GAME_TYPE: int = 2
DATE: str = "2025-11-15"

teams_test = TeamsTest(http=APICallWeb())

def test_team_standings(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(teams_test._http, "get", fake_call)

    res = teams_test.get_standings()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/standings/now"

def test_get_standings_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(teams_test._http, "get", fake_call)

    res = teams_test.get_standings(date=DATE)

    assert res.ok == False
    assert res.data == {"error": "Test Error"}
    assert called["endpoint"] == f"/v1/standings/{DATE}"

def test_team_stats(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(teams_test._http, "get", fake_call)

    res = teams_test.get_team_stats(team=TEAM_CODE, season=SEASON, g_type=GAME_TYPE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/club-stats/{TEAM_CODE}/{SEASON}/{GAME_TYPE}"

def test_team_scoreboard(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(teams_test._http, "get", fake_call)

    res = teams_test.get_team_scoreboard(team=TEAM_CODE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/scoreboard/{TEAM_CODE}/now"

def test_team_roster(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(teams_test._http, "get", fake_call)

    res = teams_test.get_team_roster(team=TEAM_CODE, season=SEASON)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/roster/{TEAM_CODE}/{SEASON}"

def test_team_schedule(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(teams_test._http, "get", fake_call)

    res = teams_test.get_schedule(team=TEAM_CODE, season=SEASON)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/club-schedule-season/{TEAM_CODE}/{SEASON}"

def test_team_schedule_week_error(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(teams_test._http, "get", fake_call)

    res = teams_test.get_schedule_week(team=TEAM_CODE, week=DATE)

    assert res.ok == False
    assert called["endpoint"] == f"/v1/club-schedule/{TEAM_CODE}/week/{DATE}"