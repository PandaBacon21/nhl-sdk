from src.resources.api_web.miscellaneous import CallNhlMisc as MiscTest
from src.core.transport import APICallWeb, APIResponse

YEAR: int = 2024
GAME_ID: int = 2025020417
SERIES_LETTER: str = "A"
EVENT_NUM: int = 3

msc_test = MiscTest(http=APICallWeb())

def test_get_meta(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_meta()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/meta"

def test_game_info(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_game_info(game_id=GAME_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/meta/game/{GAME_ID}"

def test_playoffs_series_meta(monkeypatch) -> None: 
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse: 
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    
    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_playoff_series_meta(year=YEAR, series_letter=SERIES_LETTER)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/meta/playoff-series/{YEAR}/{SERIES_LETTER}"

def test_goal_replay_error(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=False, data={"error": "Test Error"}, status_code=500)

    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_goal_replay(game_id=GAME_ID, event_number=EVENT_NUM)

    assert res.ok == False
    assert called["endpoint"] == f"/v1/ppt-replay/goal/{GAME_ID}/{EVENT_NUM}"


def test_get_location(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_location()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == "/v1/location"


def test_get_postal_lookup(monkeypatch) -> None:
    POSTAL_CODE = "80202"
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_postal_lookup(postal_code=POSTAL_CODE)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/postal-lookup/{POSTAL_CODE}"


def test_get_play_replay(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_play_replay(game_id=GAME_ID, event_number=EVENT_NUM)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/ppt-replay/{GAME_ID}/{EVENT_NUM}"


def test_get_game_rail(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_game_rail(game_id=GAME_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/gamecenter/{GAME_ID}/right-rail"


def test_get_wsc(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(msc_test._http, "get", fake_call)

    res = msc_test.get_wsc(game_id=GAME_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/v1/wsc/play-by-play/{GAME_ID}"


