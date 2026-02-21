from src.resources.api_web.edge.edge_goalies import CallNhlEdgeGoalies as EdgeGoaliesTest
from src.resources.api_web.edge.edge_skaters import CallNhlEdgeSkaters as EdgeSkatersTest
from src.resources.api_web.edge.edge_team import CallNhlEdgeTeam as EdgeTeamTest

from src.core.transport import APICallWeb, APIResponse

SKATER_ID: int = 8477492
GOALIE_ID: int = 8475809
TEAM_ID: int = 21

SEASON: int = 20232024
GAME_TYPE: int = 2
CATEGORIES: str = "goals"
LIMIT: int | None = 5
SORT: str = "all"

edge_goalie_test = EdgeGoaliesTest(http=APICallWeb())
edge_skater_test = EdgeSkatersTest(http=APICallWeb())
edge_team_test = EdgeTeamTest(http=APICallWeb())

"""
SKATERS
"""

def test_edge_skater_details(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)

    res = edge_skater_test.get_skater_details(pid=SKATER_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/skater-detail/{SKATER_ID}/now"


def test_edge_skater_distance(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)

    res = edge_skater_test.get_skating_distance(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/skater-skating-distance-detail/{SKATER_ID}/{SEASON}/{GAME_TYPE}"

def test_edge_skater_landing(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)

    res = edge_skater_test.get_skater_landing()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/skater-landing/now"

def test_skater_shot_location_top_10(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)

    res = edge_skater_test.get_skater_shot_location_10(category=CATEGORIES, sort=SORT, season=SEASON, game_type=GAME_TYPE)

    assert res.ok == False
    assert res.status_code == 500
    assert called["endpoint"] == f"/v1/edge/skater-shot-location-top-10/all/{CATEGORIES}/{SORT}/{SEASON}/{GAME_TYPE}"


"""
GOALIES
"""

def test_edge_goalie_details(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)

    res = edge_goalie_test.get_goalie_details(pid=SKATER_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/goalie-detail/{SKATER_ID}/now"


def test_edge_goalie_5v5(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)

    res = edge_goalie_test.get_goalie_5v5(pid=GOALIE_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/goalie-5v5-detail/{GOALIE_ID}/now"

def test_edge_goalie_landing(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)

    res = edge_goalie_test.get_goalie_landing()

    assert res.ok == False
    assert res.status_code == 500
    assert called["endpoint"] == f"/v1/edge/goalie-landing/now"

def test_goalie_shot_location_top_10(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)

    res = edge_goalie_test.get_goalie_shot_location_10(category=CATEGORIES, sort=SORT, season=SEASON, game_type=GAME_TYPE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/goalie-shot-location-top-10/{CATEGORIES}/{SORT}/{SEASON}/{GAME_TYPE}"


"""
TEAM
"""

def test_edge_team_details(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)

    res = edge_team_test.get_team_details(team_id=TEAM_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/team-detail/{TEAM_ID}/now"

def test_edge_team_skating_speed(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)
    
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)

    res = edge_team_test.get_team_skating_speed(team_id=TEAM_ID, season=SEASON, game_type=GAME_TYPE)

    assert res.ok == False
    assert res.status_code == 500
    assert called["endpoint"] == f"/v1/edge/team-skating-speed-detail/{TEAM_ID}/{SEASON}/{GAME_TYPE}"

def test_edge_team_shot_location(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)

    res = edge_team_test.get_team_shot_location_10(category=CATEGORIES, sort=SORT, season=SEASON, game_type=GAME_TYPE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/edge/team-shot-location-top-10/all/{CATEGORIES}/{SORT}/{SEASON}/{GAME_TYPE}"
