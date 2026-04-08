from nhl_stats.models.draft.tracker import DraftTracker, DraftTrackerResult

from .conftest import ok


TRACKER_RESPONSE = {
    "currentDraftDate": "2025-06-27",
    "broadcastStartTimeUTC": "2025-06-27T23:00:00Z",
    "tvBroadcasts": [],
    "round": 1,
    "state": "over",
    "picks": [
        {
            "pickInRound": 1,
            "overallPick": 1,
            "teamId": 2,
            "teamAbbrev": "NYI",
            "teamFullName": {"default": "New York Islanders"},
            "teamCommonName": {"default": "Islanders"},
            "teamPlaceNameWithPreposition": {"default": "New York"},
            "state": "confirmed",
            "lastName": {"default": "Schaefer"},
            "firstName": {"default": "Matthew"},
            "positionCode": "D",
        }
    ],
}


def test_get_tracker_now_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_tracker_now.return_value = ok(TRACKER_RESPONSE)
    svc = DraftTracker(mock_client)
    result = svc.get_tracker_now()
    assert isinstance(result, DraftTrackerResult)
    mock_client._api.api_web.call_nhl_draft.get_tracker_now.assert_called_once_with()


def test_get_tracker_now_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_tracker_now.return_value = ok(TRACKER_RESPONSE)
    svc = DraftTracker(mock_client)
    _ = svc.get_tracker_now()
    _ = svc.get_tracker_now()
    mock_client._api.api_web.call_nhl_draft.get_tracker_now.assert_called_once()


def test_get_tracker_now_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_tracker_now.return_value = ok(TRACKER_RESPONSE)
    svc = DraftTracker(mock_client)
    result = svc.get_tracker_now()
    assert result.current_draft_date == "2025-06-27"
    assert result.state == "over"
    assert result.round == 1
    assert len(result.picks) == 1
    assert result.picks[0].team_abbrev == "NYI"


def test_get_tracker_now_pick_names(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_tracker_now.return_value = ok(TRACKER_RESPONSE)
    svc = DraftTracker(mock_client)
    result = svc.get_tracker_now()
    p = result.picks[0]
    assert p.first_name.default == "Matthew"
    assert p.last_name.default == "Schaefer"
    assert p.position_code == "D"
