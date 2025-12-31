"""
FUNCTIONS FOR RETRIEVING LEAGUE DATA FROM API-WEB.NHLE.COM/
"""

from nhl_stats.core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# SCHEDULE
# ==========================================================================

    
def _get_schedule_now() -> dict: 
    """
    Retrieve the current schedule
    """ 
    endpoint = f"{V}/schedule/now"
    schedule: dict = _call_api_get(endpoint=endpoint)
    # print(schedule)
    return schedule


def _get_schedule(date: str) -> dict: 
    """
    Retrieve the schedule for a specific date
    date: str - YYYY-MM-DD
    """
    endpoint = f"{V}/schedule/{date}"
    schedule: dict = _call_api_get(endpoint=endpoint)
    return schedule


def _get_schedule_calendar_now() -> dict:
    """
    Retrieve the schedule calendar as of the current moment
    """
    endpoint = f"{V}/schedule-calendar/now"
    schedule_cal: dict = _call_api_get(endpoint=endpoint)
    # print(schedule_cal)
    return schedule_cal 


def _get_schedule_calendar(date: str) -> dict:
    """
    Retrieve the schedule calendar for a specific date
    date: str - YYYY-MM-DD
    """
    endpoint = f"{V}/schedule-calendar/{date}"
    schedule_cal: dict = _call_api_get(endpoint=endpoint)
    # print(schedule_cal)
    return schedule_cal


# Update this to tests
def main() -> None: 
    _get_schedule_now()
    _get_schedule(date="2025-11-28")
    _get_schedule_calendar_now()
    _get_schedule_calendar(date="2025-11-28")

if __name__ == "__main__":
    main()
