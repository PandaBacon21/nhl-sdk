"""
FUNCTIONS FOR RETRIEVING LEAGUE DATA FROM API-WEB.NHLE.COM/
"""

from typing import Optional

from ...core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# SCHEDULE
# ==========================================================================


def _get_schedule(date: Optional[str] = None) -> dict: 
    """
    Retrieve the schedule for the current moment or a specific date
    date: str - YYYY-MM-DD
    """
    endpoint = f"{V}/schedule/now"
    if date:   
        endpoint = f"{V}/schedule/{date}"
    schedule: dict = _call_api_get(endpoint=endpoint)
    return schedule

def _get_schedule_calendar(date: Optional[str] = None) -> dict:
    """
    Retrieve the schedule calendar for the current moment or a specific date
    date: str - YYYY-MM-DD
    """
    endpoint = f"{V}/schedule-calendar/now"
    if date: 
        endpoint = f"{V}/schedule-calendar/{date}"
    schedule_cal: dict = _call_api_get(endpoint=endpoint)
    # print(schedule_cal)
    return schedule_cal

