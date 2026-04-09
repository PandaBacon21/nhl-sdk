from nhl_sdk.resources.api_stats.misc import CallNhlStatsMisc
from nhl_sdk.core.transport import APICallStats, APIResponse

GAME_ID: int = 2025020417

stats_misc_test = CallNhlStatsMisc(http=APICallStats())


def test_get_shift_charts(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(stats_misc_test._http, "get", fake_call)

    res = stats_misc_test.get_shift_charts(game_id=GAME_ID)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == "/en/shiftcharts"
    assert called["params"] == {"cayenneExp": f"gameId={GAME_ID}"}


def test_get_countries(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(stats_misc_test._http, "get", fake_call)

    res = stats_misc_test.get_countries()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == "/en/country"


def test_get_glossary(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(stats_misc_test._http, "get", fake_call)

    res = stats_misc_test.get_glossary()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == "/en/glossary"


def test_get_config(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(stats_misc_test._http, "get", fake_call)

    res = stats_misc_test.get_config()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == "/en/config"


def test_get_content_module(monkeypatch) -> None:
    TEMPLATE_KEY = "someTemplate"
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(stats_misc_test._http, "get", fake_call)

    res = stats_misc_test.get_content_module(template_key=TEMPLATE_KEY)

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == f"/en/content/module/{TEMPLATE_KEY}"


def test_ping(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)

    monkeypatch.setattr(stats_misc_test._http, "get", fake_call)

    res = stats_misc_test.ping()

    assert res.ok == True
    assert res.status_code == 200
    assert called["endpoint"] == "/ping"


def test_ping_failure(monkeypatch) -> None:
    called = {}
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        return APIResponse(ok=False, data={}, status_code=503)

    monkeypatch.setattr(stats_misc_test._http, "get", fake_call)

    res = stats_misc_test.ping()

    assert res.ok == False
    assert called["endpoint"] == "/ping"
