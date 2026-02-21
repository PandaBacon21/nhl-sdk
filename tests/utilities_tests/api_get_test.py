import requests
import responses 
import pytest

import src.core.transport as transport_test
from src.core.errors.errors import NotFoundError, NhlApiError

BASE_URL_TEST: str = "https://api.test"
PLAYER_ID: int = 8477492


def make_http(): 
    return transport_test.APICallWeb(base_url=BASE_URL_TEST)

@responses.activate
def test_call_api_get_success_json() -> None: 
    http = make_http()
    endpoint = "/v1/player/{PLAYER_ID}/landing"
    url = BASE_URL_TEST+endpoint

    data = {"playerId": PLAYER_ID, "last_name": {"default": "MacKinnon"}}

    responses.add(responses.GET, url, json=data, status=200)

    res = http.get(endpoint=endpoint)

    assert len(responses.calls) == 1
    assert res.ok is True

# 404 
@responses.activate
def test_call_api_get_404_http_error() -> None:
    http = make_http()
    endpoint = "/v1/player/does-not-exist"
    url = BASE_URL_TEST+endpoint

    responses.add(responses.GET, url, json={"error": "Not found"}, status=404)

    with pytest.raises(NotFoundError) as exc:
        http.get(endpoint=endpoint)  # default raise_on_error=True

    assert len(responses.calls) == 1
    assert getattr(exc.value, "status_code", None) == 404

# Connection Error
@responses.activate
def test_call_api_get_connection_error() -> None:
    http = make_http()
    endpoint = "/v1/down"
    url = BASE_URL_TEST+endpoint

    def raise_conn_error(_request):
        raise requests.ConnectionError("connection failed")

    responses.add_callback(
        responses.GET,
        url,
        callback=raise_conn_error,
        content_type="application/json",
    )

    with pytest.raises(NhlApiError):
        http.get(endpoint=endpoint)

    assert len(responses.calls) == 1

# HTML or empty body → {success: False, error: ...} 
@responses.activate
def test_call_api_get_invalid_json() -> None:
    http = make_http()
    endpoint = "/v1/bad-json"
    url = BASE_URL_TEST+endpoint

    responses.add(
        responses.GET,
        url,
        body="{not valid json",
        status=200,
        content_type="application/json",
    )

    with pytest.raises(NhlApiError):
        http.get(endpoint=endpoint) 
