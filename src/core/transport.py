"""
OBJECT FOR DIRECT API CALLS AND ERROR HANDLING
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import time
import requests
import logging

from .config import BASE_URL_API_WEB, BASE_URL_API_STATS
from .errors import NotFoundError, ServerError, RateLimitError, NhlApiError

session = requests.Session()


@dataclass(slots=True)
class APIResponse:
    ok: bool
    data: Any 
    status_code: int 

class APICall: 
    def __init__(self, api:str, base_url: str, logger: logging.Logger, session: requests.Session = session, max_retries: int = 3) -> None:
        self.base_url = base_url.rstrip("/")
        self.response = APIResponse
        self.session = session
        self.max_retries = max_retries
        self.logger = logger
        self.logger.info(msg=f"APICall{api} initialized: base_url - {self.base_url}")

    def get(self, endpoint: str, params: dict | None = None, *, raise_on_error: bool = True) -> APIResponse:
        url = self.base_url+endpoint
        self.logger.debug(f"GET {endpoint} | params={params}")

        for attempt in range(self.max_retries + 1):
            start = time.monotonic()
            try:
                res = self.session.get(url=url, params=params, timeout=30)
            except requests.RequestException as e:
                self.logger.error(f"Network error for {endpoint}: {e}")
                if raise_on_error:
                    raise NhlApiError(f"Request failed for {url}: {e}", status_code=None, url=url) from e
                return APIResponse(ok=False, data={"error": str(e)}, status_code=0)
            elapsed = (time.monotonic() - start) * 1000

            # Retry on 429 with backoff
            if res.status_code == 429 and attempt < self.max_retries:
                wait = self._retry_wait(res, attempt)
                raw_ra = res.headers.get("Retry-After", "none")
                self.logger.warning(f"429 {endpoint} | rate limited, Retry-After={raw_ra}, retrying in {wait:.1f}s (attempt {attempt + 1}/{self.max_retries})")
                time.sleep(wait)
                continue

            # Check for non-2xx before attempting JSON parse — error bodies may be HTML
            if not (200 <= res.status_code < 300):
                if raise_on_error:
                    self.logger.warning(f"{res.status_code} {endpoint} | {elapsed:.1f}ms | raise={raise_on_error}")
                    payload = None
                    try:
                        payload = res.json() if res.content else None
                    except ValueError:
                        pass
                    self._raise_for_status(res, endpoint=endpoint, url=url, payload=payload)
                self.logger.warning(f"{res.status_code} {endpoint} | {elapsed:.1f}ms")
                return APIResponse(
                    ok=False,
                    data={"error": f"HTTP {res.status_code} for {endpoint}"},
                    status_code=res.status_code,
                )

            try:
                payload = res.json() if res.content else None
            except ValueError as e:
                if raise_on_error:
                    raise NhlApiError(f"Invalid JSON from {url}", status_code=res.status_code, url=url) from e
                return APIResponse(ok=False, data={"error": "Invalid JSON"}, status_code=res.status_code)

            self.logger.info(f"{res.status_code} {endpoint} | {elapsed:.1f}ms")
            return APIResponse(ok=True, data=payload, status_code=res.status_code)

        # Should be unreachable — loop always returns or raises
        raise NhlApiError(f"Exhausted retries for {url}", status_code=None, url=url)  # pragma: no cover

    def _retry_wait(self, res: requests.Response, attempt: int) -> float:
        # Observed NHL API behaviour:
        #   - First 429 in a burst: Retry-After=60, counting down each retry.
        #     Must honour the full value so the window resets before we retry.
        #   - Subsequent 429s in same window: Retry-After 0  →  we apply a
        #     1s floor so we never busy-loop against a still-throttled server.
        # Observed rate limit: 35 requests per 60-second fixed window.
        fallback = float(2 ** attempt)  # 1s, 2s, 4s
        retry_after = res.headers.get("Retry-After")
        if retry_after:
            try:
                server_wait = min(float(retry_after), 60.0)
                return max(server_wait, 1.0)
            except ValueError:
                pass
        return fallback

    def _raise_for_status(self, res: requests.Response, *, endpoint: str, url: str, payload: object) -> None:
        status = res.status_code

        # Best-effort message
        msg = f"HTTP {status} for {endpoint}"
        if isinstance(payload, dict):
            msg = payload.get("message") or payload.get("error") or msg

        if status == 404:
            raise NotFoundError(msg, status_code=status, url=url)
        if status == 429:
            raise RateLimitError(msg, status_code=status, url=url)
        if 500 <= status <= 599:
            raise ServerError(msg, status_code=status, url=url)

        raise NhlApiError(msg, status_code=status, url=url)    


class APICallWeb(APICall):
    def __init__(self, base_url: str = BASE_URL_API_WEB, session: requests.Session = session, max_retries: int = 3) -> None:
        super().__init__(api="Web", base_url=base_url, logger=logging.getLogger("nhl_sdk.api_call_web"), 
                         session=session, max_retries=max_retries)
        

class APICallStats(APICall):
    def __init__(self, base_url: str = BASE_URL_API_STATS, session: requests.Session = session, max_retries: int = 3) -> None:
        super().__init__(api="Stats", base_url=base_url, logger=logging.getLogger("nhl_sdk.api_call_stats"), 
                         session=session, max_retries=max_retries)