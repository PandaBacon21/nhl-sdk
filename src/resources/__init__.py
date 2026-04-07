from __future__ import annotations

from .api_web import APIWeb
from .api_stats import APIStats
from ..core.transport import APICallWeb, APICallStats


http_web = APICallWeb()
http_stats = APICallStats()


class API:
    def __init__(self):
        self.api_web = APIWeb(http=http_web)
        self.api_stats = APIStats(http=http_stats)


__all__ = ["API"]