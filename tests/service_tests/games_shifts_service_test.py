from src.models.games.shifts import GameShifts, ShiftChart

from .conftest import ok

GAME_ID = 2025020417


def test_get_shifts_cache_miss(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok(
        {"data": [], "total": 0}
    )
    svc = GameShifts(mock_client)
    result = svc.get(game_id=GAME_ID)
    assert isinstance(result, ShiftChart)
    assert result.game_id == GAME_ID
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.assert_called_once_with(
        game_id=GAME_ID
    )


def test_get_shifts_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok(
        {"data": [], "total": 0}
    )
    svc = GameShifts(mock_client)
    _ = svc.get(game_id=GAME_ID)
    _ = svc.get(game_id=GAME_ID)
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.assert_called_once()


def test_get_shifts_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok(
        {"data": [], "total": 0}
    )
    svc = GameShifts(mock_client)
    _ = svc.get(game_id=GAME_ID)
    _ = svc.get(game_id=GAME_ID + 1)
    assert mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.call_count == 2


def test_get_shifts_result_populated(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok({
        "total": 2,
        "data": [
            {
                "id": 101,
                "gameId": GAME_ID,
                "playerId": 8477492,
                "period": 1,
                "shiftNumber": 1,
                "startTime": "00:00",
                "endTime": "01:23",
                "duration": "01:23",
                "firstName": "Ryan",
                "lastName": "Johansen",
                "teamId": 21,
                "teamAbbrev": "COL",
                "teamName": "Colorado Avalanche",
                "hexValue": "#236192",
                "detailCode": 0,
                "eventDescription": None,
                "eventDetails": None,
                "eventNumber": None,
                "typeCode": 517,
            },
            {
                "id": 102,
                "gameId": GAME_ID,
                "playerId": 8478402,
                "period": 1,
                "shiftNumber": 2,
                "startTime": "01:30",
                "endTime": "03:00",
                "duration": "01:30",
                "firstName": "Nathan",
                "lastName": "MacKinnon",
                "teamId": 21,
                "teamAbbrev": "COL",
                "teamName": "Colorado Avalanche",
                "hexValue": "#236192",
                "detailCode": 0,
                "eventDescription": None,
                "eventDetails": None,
                "eventNumber": None,
                "typeCode": 517,
            },
        ],
    })
    svc = GameShifts(mock_client)
    result = svc.get(game_id=GAME_ID)
    assert result.game_id == GAME_ID
    assert result.total == 2
    assert len(result.shifts) == 2
    first = result.shifts[0]
    assert first.player_id == 8477492
    assert first.team_abbrev == "COL"
    assert first.start_time == "00:00"
    assert first.shift_number == 1
    assert first.hex_value == "#236192"
    assert first.team_name == "Colorado Avalanche"
