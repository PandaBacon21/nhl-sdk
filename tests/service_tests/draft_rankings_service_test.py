from nhl_stats.models.draft.rankings import DraftRankings, DraftRankingsResult

from .conftest import ok


RANKINGS_RESPONSE = {
    "draftYear": 2026,
    "categoryId": 1,
    "categoryKey": "na-skater",
    "draftYears": [2026, 2025],
    "categories": [{"id": 1, "name": "North American Skater", "consumerKey": "na-skater"}],
    "rankings": [{"lastName": "Yakemchuk", "firstName": "Cole", "positionCode": "D", "midtermRank": 1}],
}


def test_get_rankings_now_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_rankings.return_value = ok(RANKINGS_RESPONSE)
    svc = DraftRankings(mock_client)
    result = svc.get_rankings()
    assert isinstance(result, DraftRankingsResult)
    mock_client._api.api_web.call_nhl_draft.get_rankings.assert_called_once_with(season=None, category=None)


def test_get_rankings_now_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_rankings.return_value = ok(RANKINGS_RESPONSE)
    svc = DraftRankings(mock_client)
    _ = svc.get_rankings()
    _ = svc.get_rankings()
    mock_client._api.api_web.call_nhl_draft.get_rankings.assert_called_once()


def test_get_rankings_with_season_and_category(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_rankings.return_value = ok(RANKINGS_RESPONSE)
    svc = DraftRankings(mock_client)
    result = svc.get_rankings(season=2026, category=1)
    assert isinstance(result, DraftRankingsResult)
    mock_client._api.api_web.call_nhl_draft.get_rankings.assert_called_once_with(season=2026, category=1)


def test_get_rankings_different_seasons_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_rankings.return_value = ok(RANKINGS_RESPONSE)
    svc = DraftRankings(mock_client)
    _ = svc.get_rankings(season=2026, category=1)
    _ = svc.get_rankings(season=2025, category=1)
    assert mock_client._api.api_web.call_nhl_draft.get_rankings.call_count == 2


def test_get_rankings_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_draft.get_rankings.return_value = ok(RANKINGS_RESPONSE)
    svc = DraftRankings(mock_client)
    result = svc.get_rankings()
    assert result.draft_year == 2026
    assert result.category_key == "na-skater"
    assert len(result.rankings) == 1
    assert result.rankings[0].last_name == "Yakemchuk"
