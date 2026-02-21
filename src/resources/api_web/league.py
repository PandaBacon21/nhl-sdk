"""
FUNCTIONS FOR RETRIEVING LEAGUE DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from ...core.config import V
from ...core.transport import APICallWeb, APIResponse

# ==========================================================================
# SCHEDULE
# ==========================================================================

class CallNhlLeague:
    def __init__(self, http: APICallWeb): 
        self._http = http

    def get_schedule(self, date: Optional[str] = None) -> APIResponse: 
        """
        Retrieve the schedule for the current moment or a specific date
        date: str - YYYY-MM-DD
        """
        endpoint = f"/{V}/schedule/now"
        if date:   
            endpoint = f"/{V}/schedule/{date}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        return res

    def get_schedule_calendar(self, date: Optional[str] = None) -> APIResponse:
        """
        Retrieve the schedule calendar for the current moment or a specific date
        date: str - YYYY-MM-DD
        """
        endpoint = f"/{V}/schedule-calendar/now"
        if date: 
            endpoint = f"/{V}/schedule-calendar/{date}"
        res: APIResponse = self._http.get(endpoint=endpoint)
        # print(res)
        return res

