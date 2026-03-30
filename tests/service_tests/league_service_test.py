from src.services.league import League
from src.models.league.league_schedule import LeagueScheduleResult
from src.models.league.league_calendar import LeagueCalendarResult

from .conftest import ok

DATE = "2026-03-29"


# ==========================================================================
# GET SCHEDULE
# ==========================================================================

def test_get_schedule_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule.return_value = ok({"gameWeek": []})
    svc = League(mock_client)
    result = svc.get_schedule()
    assert isinstance(result, LeagueScheduleResult)
    mock_client._api.api_web.call_nhl_league.get_schedule.assert_called_once_with(date=None)


def test_get_schedule_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule.return_value = ok({"gameWeek": []})
    svc = League(mock_client)
    _ = svc.get_schedule()
    _ = svc.get_schedule()
    mock_client._api.api_web.call_nhl_league.get_schedule.assert_called_once()


def test_get_schedule_with_date(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule.return_value = ok({"gameWeek": []})
    svc = League(mock_client)
    result = svc.get_schedule(date=DATE)
    assert isinstance(result, LeagueScheduleResult)
    mock_client._api.api_web.call_nhl_league.get_schedule.assert_called_once_with(date=DATE)


def test_get_schedule_date_and_now_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule.return_value = ok({"gameWeek": []})
    svc = League(mock_client)
    _ = svc.get_schedule()
    _ = svc.get_schedule(date=DATE)
    assert mock_client._api.api_web.call_nhl_league.get_schedule.call_count == 2


def test_get_schedule_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule.return_value = ok({
        "nextStartDate": "2026-04-05",
        "previousStartDate": "2026-03-22",
        "gameWeek": [
            {"date": "2026-03-29", "dayAbbrev": "SUN", "numberOfGames": 6, "datePromo": [], "games": []},
        ],
    })
    svc = League(mock_client)
    result = svc.get_schedule()
    assert result.next_start_date == "2026-04-05"
    assert result.previous_start_date == "2026-03-22"
    assert len(result.game_week) == 1
    assert result.game_week[0].date == "2026-03-29"
    assert result.game_week[0].number_of_games == 6


# ==========================================================================
# GET SCHEDULE CALENDAR
# ==========================================================================

def test_get_schedule_calendar_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.return_value = ok({"teams": []})
    svc = League(mock_client)
    result = svc.get_schedule_calendar()
    assert isinstance(result, LeagueCalendarResult)
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.assert_called_once_with(date=None)


def test_get_schedule_calendar_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.return_value = ok({"teams": []})
    svc = League(mock_client)
    _ = svc.get_schedule_calendar()
    _ = svc.get_schedule_calendar()
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.assert_called_once()


def test_get_schedule_calendar_with_date(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.return_value = ok({"teams": []})
    svc = League(mock_client)
    result = svc.get_schedule_calendar(date=DATE)
    assert isinstance(result, LeagueCalendarResult)
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.assert_called_once_with(date=DATE)


def test_get_schedule_calendar_date_and_now_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.return_value = ok({"teams": []})
    svc = League(mock_client)
    _ = svc.get_schedule_calendar()
    _ = svc.get_schedule_calendar(date=DATE)
    assert mock_client._api.api_web.call_nhl_league.get_schedule_calendar.call_count == 2


def test_get_schedule_calendar_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_league.get_schedule_calendar.return_value = ok({
        "startDate": "2026-03-29",
        "endDate": "2026-04-04",
        "nextStartDate": "2026-04-05",
        "previousStartDate": "2026-03-22",
        "teams": [
            {
                "id": 1, "seasonId": 20252026,
                "commonName": {"default": "Devils"}, "abbrev": "NJD",
                "name": {"default": "New Jersey Devils", "fr": "Devils du New Jersey"},
                "placeNameWithPreposition": {"default": "New Jersey", "fr": "du New Jersey"},
                "placeName": {"default": "New Jersey"},
                "logo": "https://assets.nhle.com/logos/nhl/svg/NJD_light.svg",
                "darkLogo": "https://assets.nhle.com/logos/nhl/svg/NJD_dark.svg",
                "french": False,
            },
        ],
    })
    svc = League(mock_client)
    result = svc.get_schedule_calendar()
    assert result.start_date == "2026-03-29"
    assert result.end_date == "2026-04-04"
    assert len(result.teams) == 1
    assert result.teams[0].abbrev == "NJD"
    assert result.teams[0].french is False
