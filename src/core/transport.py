"""
INTERNAL FUNCTIONS FOR DIRECT API CALLS
"""

from typing import Optional
import requests

from .config import BASE_URL_API_WEB

session = requests.Session()

RESPONSE: dict = {}

# API Retrieval function
def _call_api_get(endpoint: str, params: Optional[dict] = None) -> dict: 
    full_url = BASE_URL_API_WEB+endpoint
    try: 
        res = session.get(url=full_url, params=params)
        res.raise_for_status()
    except requests.HTTPError as e: 
        print(f"Success: {False}, Endpoint: {endpoint}, HTTP Error: {e.response.status_code}")
        RESPONSE["ok"] = False
        RESPONSE["error"] = f"HTTP error retrieving {endpoint}"
        RESPONSE["status_code"] = e.response.status_code if e.response is not None else None
        return RESPONSE
    except requests.RequestException as e:
        print(f"Success: {False}, Request failed retrieving endpoint: {endpoint}")
        RESPONSE["ok"] = False
        RESPONSE["error"] = f"Request failed retrieving endpoint {endpoint}"
        RESPONSE["status_code"] = e.response.status_code if e.response is not None else None
        return RESPONSE
    try: 
        data = res.json()
        print(f"Success: {True}, Endpoint: {endpoint}, Status Code: {res.status_code}")
    except requests.exceptions.JSONDecodeError:
        RESPONSE["ok"] = False
        RESPONSE["error"] = f"Invalid JSON returned from endpoint {endpoint}"
        RESPONSE["status_code"] = res.status_code if "res" in locals() else None
        return RESPONSE
    except ValueError as e:
        RESPONSE["ok"] = False
        RESPONSE["error"] = f"Invalid JSON returned from endpoint {endpoint}"
        RESPONSE["status_code"] = 500
        return RESPONSE
    RESPONSE["ok"] = True
    RESPONSE["data"] = data
    RESPONSE["status_code"] = res.status_code
    return RESPONSE
