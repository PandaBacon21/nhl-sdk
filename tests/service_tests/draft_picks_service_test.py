from nhl_sdk.models.draft.picks import DraftPicks, DraftPicksResult

from .conftest import ok


PICKS_RESPONSE = {
    "broadcastStartTimeUTC": "2025-06-27T23:00:00Z",
    "draftYear": 2025,
    "draftYears": [2025, 2024],
    "selectableRounds": [1, 2, 3, 4, 5, 6, 7],
    "state": "over",
    "picks": [
        {
            "round": 1,
            "pickInRound": 1,
            "overallPick": 1,
            "teamId": 2,
            "teamAbbrev": "NYI",
            "teamName": {"default": "New York Islanders"},
            "teamCommonName": {"default": "Islanders"},
            "teamPlaceNameWithPreposition": {"default": "New York"},
            "displayAbbrev": {"default": "NYI"},
            "teamPickHistory": "NYI",
            "firstName": {"default": "Matthew"},
            "lastName": {"default": "Schaefer"},
            "positionCode": "D",
            "countryCode": "CAN",
            "height": 74,
            "weight": 186,
            "amateurLeague": "OHL",
            "amateurClubName": "Erie",
        }
    ],
}


def test_get_picks_now_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    result = svc.get_picks()
    assert isinstance(result, DraftPicksResult)
    mock_client._api.api_web.call_nhl_draft.get_picks.assert_called_once_with(season=None, round=None)


def test_get_picks_now_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    _ = svc.get_picks()
    _ = svc.get_picks()
    mock_client._api.api_web.call_nhl_draft.get_picks.assert_called_once()


def test_get_picks_by_season_and_round(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    result = svc.get_picks(season=2025, round="1")
    assert isinstance(result, DraftPicksResult)
    mock_client._api.api_web.call_nhl_draft.get_picks.assert_called_once_with(season=2025, round="1")


def test_get_picks_different_rounds_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    _ = svc.get_picks(season=2025, round="1")
    _ = svc.get_picks(season=2025, round="2")
    assert mock_client._api.api_web.call_nhl_draft.get_picks.call_count == 2


def test_get_picks_all_rounds(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    result = svc.get_picks(season=2025, round="all")
    assert isinstance(result, DraftPicksResult)
    mock_client._api.api_web.call_nhl_draft.get_picks.assert_called_once_with(season=2025, round="all")


def test_get_picks_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    result = svc.get_picks()
    assert result.draft_year == 2025
    assert result.state == "over"
    assert len(result.picks) == 1
    assert result.picks[0].team_abbrev == "NYI"
    assert result.picks[0].first_name.default == "Matthew"


# ==========================================================================
# get_all()
# ==========================================================================

def test_get_all_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_all_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    result = svc.get_all(year=2024)
    assert isinstance(result, DraftPicksResult)
    mock_client._api.api_web.call_nhl_draft.get_all_picks.assert_called_once_with(year=2024)


def test_get_all_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_all_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    _ = svc.get_all(year=2024)
    _ = svc.get_all(year=2024)
    mock_client._api.api_web.call_nhl_draft.get_all_picks.assert_called_once()


def test_get_all_different_years_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_all_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    _ = svc.get_all(year=2024)
    _ = svc.get_all(year=2023)
    assert mock_client._api.api_web.call_nhl_draft.get_all_picks.call_count == 2


def test_get_all_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_all_picks.return_value = ok(PICKS_RESPONSE)
    svc = DraftPicks(mock_client)
    result = svc.get_all(year=2025)
    assert result.draft_year == 2025
    assert len(result.picks) == 1
    assert result.picks[0].overall_pick == 1
