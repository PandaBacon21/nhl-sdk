"""
FUNCTIONS FOR RETRIEVING SEASON DATA FROM API-WEB.NHLE.COM/
"""

from ...core.config import V
from ...core.transport import APICallWeb, APIResponse

# ==========================================================================
# SEASONS
# ==========================================================================

class CallNhlSeasons:
    def __init__(self, http: APICallWeb): 
        self._http = http

    def get_seasons(self) -> APIResponse:
        """
        Retrieve a list of all season IDs past & present in the NHL
        """ 
        endpoint = f"/{V}/season"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res
