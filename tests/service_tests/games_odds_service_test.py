from src.models.games.odds import PartnerOdds, PartnerOddsResult

from .conftest import ok


def test_get_odds_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_odds.return_value = ok({"games": []})
    svc = PartnerOdds(mock_client)
    result = svc.get_odds(country_code="US")
    assert isinstance(result, PartnerOddsResult)
    mock_client._api.api_web.call_nhl_games.get_odds.assert_called_once_with(country_code="US")


def test_get_odds_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_odds.return_value = ok({"games": []})
    svc = PartnerOdds(mock_client)
    _ = svc.get_odds(country_code="US")
    _ = svc.get_odds(country_code="US")
    mock_client._api.api_web.call_nhl_games.get_odds.assert_called_once()


def test_get_odds_different_countries_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_odds.return_value = ok({"games": []})
    svc = PartnerOdds(mock_client)
    _ = svc.get_odds(country_code="US")
    _ = svc.get_odds(country_code="CA")
    assert mock_client._api.api_web.call_nhl_games.get_odds.call_count == 2


def test_get_odds_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_odds.return_value = ok({
        "currentOddsDate": "2026-03-30",
        "lastUpdatedUTC": "2026-03-31T03:21:21.070514777Z",
        "games": [],
    })
    svc = PartnerOdds(mock_client)
    result = svc.get_odds(country_code="US")
    assert result.current_odds_date == "2026-03-30"
    assert result.last_updated_utc == "2026-03-31T03:21:21.070514777Z"
    assert result.games == []
