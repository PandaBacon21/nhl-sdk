from src.models.games.network.network import GameNetwork
from src.models.games.network.network_schedule import NetworkScheduleResult

from .conftest import ok

DATE = "2026-03-25"


def test_get_tv_schedule_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.return_value = ok({"broadcasts": []})
    svc = GameNetwork(mock_client)
    result = svc.get_tv_schedule()
    assert isinstance(result, NetworkScheduleResult)
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.assert_called_once_with(date=None)


def test_get_tv_schedule_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.return_value = ok({"broadcasts": []})
    svc = GameNetwork(mock_client)
    _ = svc.get_tv_schedule()
    _ = svc.get_tv_schedule()
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.assert_called_once()


def test_get_tv_schedule_with_date(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.return_value = ok({"broadcasts": []})
    svc = GameNetwork(mock_client)
    result = svc.get_tv_schedule(date=DATE)
    assert isinstance(result, NetworkScheduleResult)
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.assert_called_once_with(date=DATE)


def test_get_tv_schedule_date_and_now_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.return_value = ok({"broadcasts": []})
    svc = GameNetwork(mock_client)
    _ = svc.get_tv_schedule()
    _ = svc.get_tv_schedule(date=DATE)
    assert mock_client._api.api_web.call_nhl_games.get_tv_schedule.call_count == 2


def test_get_tv_schedule_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_tv_schedule.return_value = ok({
        "date": DATE,
        "startDate": "2026-03-11",
        "endDate": "2026-04-12",
        "broadcasts": [
            {
                "startTime": f"{DATE}T00:00:00",
                "endTime": f"{DATE}T01:00:00",
                "durationSeconds": 3600,
                "title": "On The Fly With Bonus Coverage",
                "description": "On The Fly recap",
                "houseNumber": "H60ANAVAN03242026",
                "broadcastType": "HD",
                "broadcastStatus": "LIVE",
                "broadcastImageUrl": "onthefly.png",
            },
        ],
    })
    svc = GameNetwork(mock_client)
    result = svc.get_tv_schedule(date=DATE)
    assert result.date == DATE
    assert result.start_date == "2026-03-11"
    assert result.end_date == "2026-04-12"
    assert len(result.broadcasts) == 1
    assert result.broadcasts[0].title == "On The Fly With Bonus Coverage"
    assert result.broadcasts[0].broadcast_status == "LIVE"
    assert result.broadcasts[0].duration_seconds == 3600
