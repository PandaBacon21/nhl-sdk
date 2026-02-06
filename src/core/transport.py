"""
INTERNAL FUNCTIONS FOR DIRECT API CALLS
"""

from typing import Optional
import requests

from .config import BASE_URL_API_WEB

session = requests.Session()

# API Retrieval function
def _call_api_get(endpoint:str, params: Optional[dict] = None) -> dict: 
    try: 
        full_url = BASE_URL_API_WEB+endpoint
        res = session.get(url=full_url, params=params)
        res.raise_for_status()
        print(f"Success: {True}, Endpoint: {endpoint}")
        return {
            "ok": True, 
            "data": res.json()
        }
    
    except requests.HTTPError as e: 
        print(f"Success: {False}, Endpoint: {endpoint}, HTTP Error: {e.response.status_code}")
        return {
            "ok": False,
            "error": f"HTTP error retrieving {endpoint}",
            "status_code": e.response.status_code if e.response is not None else None
        }
    
    except requests.RequestException as e:
        print(f"Success: {False}, Request failed retrieving endpoint: {endpoint}")
        return {
            "ok": False,
            "error": f"Request failed retrieving endpoint {endpoint}"   
        }
