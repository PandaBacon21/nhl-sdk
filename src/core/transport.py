"""
OBJECT FOR DIRECT API CALLS AND ERROR HANDLING
"""
from dataclasses import dataclass
from typing import Optional, Any
import requests

from .config import BASE_URL_API_WEB
from .errors.errors import NotFoundError, ServerError, ForbiddenError, RateLimitError, NhlApiError

session = requests.Session()

@dataclass(slots=True)
class APIResponse:
    ok: bool
    data: Any 
    status_code: int 


class APICallWeb:
    def __init__(self, base_url: str = BASE_URL_API_WEB, session: requests.Session = session) -> None: 
        self.base_url = base_url.rstrip("/")
        self.response = APIResponse
        self.session = session
    
    def get(self, endpoint: str, params: Optional[dict] = None, *, raise_on_error: bool = True) -> APIResponse:
        url = self.base_url+endpoint

        try:
            res = self.session.get(url=url, params=params, timeout=30)
        except requests.RequestException as e:
            # network/DNS/timeout/connection issues (no HTTP response)
            if raise_on_error:
                raise NhlApiError(f"Request failed for {url}: {e}", status_code=None, url=url) from e
            return APIResponse(ok=False, data={"error": str(e)}, status_code=0)

        try:
            payload = res.json() if res.content else None
        except ValueError as e:
            if raise_on_error:
                raise NhlApiError(f"Invalid JSON from {url}", status_code=res.status_code, url=url) from e
            return APIResponse(ok=False, data={"error": "Invalid JSON"}, status_code=res.status_code)

        # Success path
        if 200 <= res.status_code < 300:
            return APIResponse(ok=True, data=payload, status_code=res.status_code)

        # Error path
        if raise_on_error:
            self._raise_for_status(res, endpoint=endpoint, url=url, payload=payload)

        # If not raising, return structured failure response
        return APIResponse(
            ok=False,
            data={
                "error": f"HTTP {res.status_code} for {endpoint}",
                "detail": payload,
            },
            status_code=res.status_code,
        )   

    def _raise_for_status(self, res: requests.Response, *, endpoint: str, url: str, payload: object) -> None:
        status = res.status_code

        # Best-effort message
        msg = f"HTTP {status} for {endpoint}"
        if isinstance(payload, dict):
            msg = payload.get("message") or payload.get("error") or msg

        if status == 404:
            raise NotFoundError(msg, status_code=status, url=url)
        if status == 403:
            raise ForbiddenError(msg, status_code=status, url=url)
        if status == 429:
            raise RateLimitError(msg, status_code=status, url=url)
        if 500 <= status <= 599:
            raise ServerError(msg, status_code=status, url=url)

        raise NhlApiError(msg, status_code=status, url=url)    
