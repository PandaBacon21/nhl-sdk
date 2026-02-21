"""
CUSTOM ERROR CLASSES
"""

class NhlApiError(Exception):
    def __init__(self, message: str, status_code: int | None = None, url: str | None = None):
        self.status_code = status_code
        self.url = url
        super().__init__(message)

class NotFoundError(NhlApiError):
    """HTTP 404"""
    pass

class ForbiddenError(NhlApiError):
    """HTTP 403"""
    pass

class RateLimitError(NhlApiError):
    """HTTP 429"""
    pass

class ServerError(NhlApiError):
    """HTTP 5xx"""
    pass