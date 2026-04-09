from nhl_sdk.models.teams.team.team_schedule.team_schedule import TeamSchedule
from nhl_sdk.models.teams.team.team_schedule.team_schedule_result import (
    TeamScheduleResult, TeamMonthScheduleResult, TeamWeekScheduleResult,
)

from .conftest import ok

ABBREV = "COL"


def test_get_schedule_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_schedule.return_value = ok({"games": []})
    svc = TeamSchedule(mock_client, ABBREV)
    result = svc.get_schedule()
    assert isinstance(result, TeamScheduleResult)
    mock_client._api.api_web.call_nhl_teams.get_schedule.assert_called_once_with(team=ABBREV, season=None)


def test_get_schedule_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_schedule.return_value = ok({"games": []})
    svc = TeamSchedule(mock_client, ABBREV)
    _ = svc.get_schedule()
    _ = svc.get_schedule()
    mock_client._api.api_web.call_nhl_teams.get_schedule.assert_called_once()


def test_get_schedule_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_schedule.return_value = ok({"games": []})
    svc = TeamSchedule(mock_client, ABBREV)
    result = svc.get_schedule(season=20242025)
    assert isinstance(result, TeamScheduleResult)
    mock_client._api.api_web.call_nhl_teams.get_schedule.assert_called_once_with(team=ABBREV, season=20242025)


def test_get_schedule_month_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_schedule_month.return_value = ok({"games": []})
    svc = TeamSchedule(mock_client, ABBREV)
    result = svc.get_schedule_month(month="2025-01")
    assert isinstance(result, TeamMonthScheduleResult)
    mock_client._api.api_web.call_nhl_teams.get_schedule_month.assert_called_once_with(team=ABBREV, month="2025-01")


def test_get_schedule_month_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_schedule_month.return_value = ok({"games": []})
    svc = TeamSchedule(mock_client, ABBREV)
    _ = svc.get_schedule_month(month="2025-01")
    _ = svc.get_schedule_month(month="2025-01")
    mock_client._api.api_web.call_nhl_teams.get_schedule_month.assert_called_once()


def test_get_schedule_week_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_schedule_week.return_value = ok({"games": []})
    svc = TeamSchedule(mock_client, ABBREV)
    result = svc.get_schedule_week(week="2025-01-06")
    assert isinstance(result, TeamWeekScheduleResult)
    mock_client._api.api_web.call_nhl_teams.get_schedule_week.assert_called_once_with(team=ABBREV, week="2025-01-06")


def test_get_schedule_week_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_schedule_week.return_value = ok({"games": []})
    svc = TeamSchedule(mock_client, ABBREV)
    _ = svc.get_schedule_week(week="2025-01-06")
    _ = svc.get_schedule_week(week="2025-01-06")
    mock_client._api.api_web.call_nhl_teams.get_schedule_week.assert_called_once()
