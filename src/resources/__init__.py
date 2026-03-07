from __future__ import annotations
import logging

from .api_web import APIWeb
from ..core.transport import APICallWeb


http = APICallWeb()

class API: 
    def __init__(self): 
        self.api_web = APIWeb(http=http)

__all__ = ["API"]