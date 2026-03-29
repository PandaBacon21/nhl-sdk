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


def test_edge_skater_details_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_details(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-detail/{SKATER_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_comparison(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_comparison(pid=SKATER_ID)
    assert called["endpoint"] == f"/v1/edge/skater-comparison/{SKATER_ID}/now"


def test_edge_skater_comparison_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_comparison(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-comparison/{SKATER_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_speed(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skating_speed(pid=SKATER_ID)
    assert called["endpoint"] == f"/v1/edge/skater-skating-speed-detail/{SKATER_ID}/now"


def test_edge_skater_speed_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skating_speed(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-skating-speed-detail/{SKATER_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_zone_time(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_zone_time(pid=SKATER_ID)
    assert called["endpoint"] == f"/v1/edge/skater-zone-time/{SKATER_ID}/now"


def test_edge_skater_zone_time_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_zone_time(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-zone-time/{SKATER_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_shot_speed(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_shot_speed(pid=SKATER_ID)
    assert called["endpoint"] == f"/v1/edge/skater-shot-speed-detail/{SKATER_ID}/now"


def test_edge_skater_shot_speed_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_shot_speed(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-shot-speed-detail/{SKATER_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_shot_location(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_shot_location(pid=SKATER_ID)
    assert called["endpoint"] == f"/v1/edge/skater-shot-location-detail/{SKATER_ID}/now"


def test_edge_skater_shot_location_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_shot_location(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-shot-location-detail/{SKATER_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_cat_details(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_cat_skater_details(pid=SKATER_ID)
    assert called["endpoint"] == f"/v1/cat/edge/skater-detail/{SKATER_ID}/now"


def test_edge_skater_cat_details_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_cat_skater_details(pid=SKATER_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/cat/edge/skater-detail/{SKATER_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_landing_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_landing(season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-landing/{SEASON}/{GAME_TYPE}"


def test_edge_skater_distance_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_distance_10(pos="F", strength="all", sort=SORT)
    assert called["endpoint"] == f"/v1/edge/skater-distance-top-10/F/all/{SORT}/now"


def test_edge_skater_distance_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_distance_10(pos="F", strength="all", sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-distance-top-10/F/all/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_skating_speed_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skating_speed_10(pos="F", sort=SORT)
    assert called["endpoint"] == f"/v1/edge/skater-speed-top-10/F/{SORT}/now"


def test_edge_skating_speed_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skating_speed_10(pos="F", sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-speed-top-10/F/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_zone_time_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_zone_time_10(pos="F", strength="all", sort=SORT)
    assert called["endpoint"] == f"/v1/edge/skater-zone-time-top-10/F/all/{SORT}/now"


def test_edge_skater_zone_time_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_zone_time_10(pos="F", strength="all", sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-zone-time-top-10/F/all/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_shot_speed_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_shot_speed_10(pos="F", sort=SORT)
    assert called["endpoint"] == f"/v1/edge/skater-shot-speed-top-10/F/{SORT}/now"


def test_edge_skater_shot_speed_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_shot_speed_10(pos="F", sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/skater-shot-speed-top-10/F/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_skater_shot_location_top_10_now(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_skater_test._http, "get", fake_call)
    edge_skater_test.get_skater_shot_location_10(category=CATEGORIES, sort=SORT)
    assert called["endpoint"] == f"/v1/edge/skater-shot-location-top-10/all/{CATEGORIES}/{SORT}/now"


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


def test_edge_goalie_details_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_details(pid=GOALIE_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-detail/{GOALIE_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_comparison(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_comparison(pid=GOALIE_ID)
    assert called["endpoint"] == f"/v1/edge/goalie-comparison/{GOALIE_ID}/now"


def test_edge_goalie_comparison_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_comparison(pid=GOALIE_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-comparison/{GOALIE_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_5v5_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_5v5(pid=GOALIE_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-5v5-detail/{GOALIE_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_shot_location(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_shot_location(pid=GOALIE_ID)
    assert called["endpoint"] == f"/v1/edge/goalie-shot-location-detail/{GOALIE_ID}/now"


def test_edge_goalie_shot_location_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_shot_location(pid=GOALIE_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-shot-location-detail/{GOALIE_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_save_pctg(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_save_pctg(pid=GOALIE_ID)
    assert called["endpoint"] == f"/v1/edge/goalie-save-percentage-detail/{GOALIE_ID}/now"


def test_edge_goalie_save_pctg_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_save_pctg(pid=GOALIE_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-save-percentage-detail/{GOALIE_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_cat_details(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_cat_goalie_details(pid=GOALIE_ID)
    assert called["endpoint"] == f"/v1/cat/edge/goalie-detail/{GOALIE_ID}/now"


def test_edge_goalie_cat_details_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_cat_goalie_details(pid=GOALIE_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/cat/edge/goalie-detail/{GOALIE_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_landing_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_landing(season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-landing/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_5v5_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalies_5v5_10(sort=SORT)
    assert called["endpoint"] == f"/v1/edge/goalie-5v5-top-10/{SORT}/now"


def test_edge_goalie_5v5_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalies_5v5_10(sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-5v5-top-10/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_goalie_shot_location_10_now(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_shot_location_10(category=CATEGORIES, sort=SORT)
    assert called["endpoint"] == f"/v1/edge/goalie-shot-location-top-10/{CATEGORIES}/{SORT}/now"


def test_edge_goalie_save_pctg_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_save_pctg_10(sort=SORT)
    assert called["endpoint"] == f"/v1/edge/goalie-edge-save-pctg-top-10/{SORT}/now"


def test_edge_goalie_save_pctg_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_goalie_test._http, "get", fake_call)
    edge_goalie_test.get_goalie_save_pctg_10(sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/goalie-edge-save-pctg-top-10/{SORT}/{SEASON}/{GAME_TYPE}"


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


def test_edge_team_comparison(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_comparison(team_id=TEAM_ID)
    assert called["endpoint"] == f"/v1/edge/team-comparison/{TEAM_ID}/now"


def test_edge_team_comparison_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_comparison(team_id=TEAM_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-comparison/{TEAM_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_team_distance(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_distance(team_id=TEAM_ID)
    assert called["endpoint"] == f"/v1/edge/team-skating-distance-detail/{TEAM_ID}/now"


def test_edge_team_distance_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_distance(team_id=TEAM_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-skating-distance-detail/{TEAM_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_team_zone_time(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_zone_time(team_id=TEAM_ID)
    assert called["endpoint"] == f"/v1/edge/team-zone-time-details/{TEAM_ID}/now"


def test_edge_team_zone_time_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_zone_time(team_id=TEAM_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-zone-time-details/{TEAM_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_team_shot_speed(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_shot_speed(team_id=TEAM_ID)
    assert called["endpoint"] == f"/v1/edge/team-shot-speed-detail/{TEAM_ID}/now"


def test_edge_team_shot_speed_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_shot_speed(team_id=TEAM_ID, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-shot-speed-detail/{TEAM_ID}/{SEASON}/{GAME_TYPE}"


def test_edge_team_skating_distance_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_skating_distance_10(strength="all", sort=SORT)
    assert called["endpoint"] == f"/v1/edge/team-skating-distance-top-10/all/all/{SORT}/now"


def test_edge_team_skating_distance_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_skating_distance_10(strength="all", sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-skating-distance-top-10/all/all/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_team_skating_speed_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_skating_speed_10(sort=SORT)
    assert called["endpoint"] == f"/v1/edge/team-skating-speed-top-10/all/{SORT}/now"


def test_edge_team_skating_speed_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_skating_speed_10(sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-skating-speed-top-10/all/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_team_zone_time_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_zone_time_10(strength="all", sort=SORT)
    assert called["endpoint"] == f"/v1/edge/team-zone-time-top-10/all/{SORT}/now"


def test_edge_team_zone_time_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_zone_time_10(strength="all", sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-zone-time-top-10/all/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_team_shot_speed_10(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_shot_speed_10(sort=SORT)
    assert called["endpoint"] == f"/v1/edge/team-shot-speed-top-10/all/{SORT}/now"


def test_edge_team_shot_speed_10_with_season(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_shot_speed_10(sort=SORT, season=SEASON, game_type=GAME_TYPE)
    assert called["endpoint"] == f"/v1/edge/team-shot-speed-top-10/all/{SORT}/{SEASON}/{GAME_TYPE}"


def test_edge_team_shot_location_10_now(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=True, data={}, status_code=200)
    monkeypatch.setattr(edge_team_test._http, "get", fake_call)
    edge_team_test.get_team_shot_location_10(category=CATEGORIES, sort=SORT)
    assert called["endpoint"] == f"/v1/edge/team-shot-location-top-10/all/{CATEGORIES}/{SORT}/now"
