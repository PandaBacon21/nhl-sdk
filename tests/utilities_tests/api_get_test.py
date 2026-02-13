import requests
import responses 

import src.core.transport as transport_test

BASE_URL_TEST: str = "https://api.test/"
PLAYER_ID: int = 8477492

# 200 OK + JSON body → {success: True, data: ...} 
CALLED = {}

@responses.activate
def test_call_api_get_success_json(monkeypatch) -> None: 
    monkeypatch.setattr(transport_test, "BASE_URL_API_WEB", BASE_URL_TEST)
    endpoint = "v1/player/{PLAYER_ID}/landing"
    full_url = BASE_URL_TEST+endpoint

    data = {"playerId": PLAYER_ID, "last_name": {"default": "MacKinnon"}}

    responses.add(responses.GET, full_url, json=data, status=200)

    result = transport_test._call_api_get(endpoint=endpoint)

    assert len(responses.calls) == 1
    assert result["ok"] is True

# 404 → {success: False, error: ...}
@responses.activate
def test_call_api_get_404_http_error(monkeypatch) -> None:
    monkeypatch.setattr(transport_test, "BASE_URL_API_WEB", BASE_URL_TEST)
    endpoint = "v1/player/does-not-exist"
    full_url = BASE_URL_TEST+endpoint

    responses.add(responses.GET, full_url, json={"message": "Not found"}, status=404)

    result = transport_test._call_api_get(endpoint=endpoint)

    assert len(responses.calls) == 1
    assert result["ok"] is False
    assert result["status_code"] == 404
    assert "HTTP error retrieving" in result["error"]


# requests exceptions → {success: False, error: ...} 
@responses.activate
def test_call_api_get_connection_error(monkeypatch) -> None:
    monkeypatch.setattr(transport_test, "BASE_URL_API_WEB", BASE_URL_TEST)
    endpoint = "v1/down"
    full_url = BASE_URL_TEST+endpoint

    def raise_conn_error(_request):
        raise requests.ConnectionError("connection failed")

    responses.add_callback(
        responses.GET,
        full_url,
        callback=lambda req: raise_conn_error(req),
        content_type="application/json",
    )

    result = transport_test._call_api_get(endpoint=endpoint)

    assert len(responses.calls) == 1
    assert result["ok"] is False
    assert "Request failed retrieving endpoint" in result["error"]

# HTML or empty body → {success: False, error: ...} 
@responses.activate
def test_call_api_get_invalid_json(monkeypatch) -> None:
    monkeypatch.setattr(transport_test, "BASE_URL_API_WEB", BASE_URL_TEST)
    endpoint = "v1/bad-json"
    full_url = BASE_URL_TEST+endpoint

    responses.add(
        responses.GET,
        full_url,
        body="{not valid json",
        status=200,
        content_type="application/json",
    )

    result = transport_test._call_api_get(endpoint=endpoint)

    assert len(responses.calls) == 1
    assert result["ok"] is False
    assert "Invalid JSON" in result["error"]


# Rate limiting / retry behavior (if you have it)
    # 429 with Retry-After handling (even if you don’t retry yet, ensure you surface it predictably)

# Query params / headers passing
    # If you support params, headers, base_url, etc., verify they’re passed to session.get() correctly

# URL building
# Base + path joining edge cases (/v1 + /players vs v1/players)