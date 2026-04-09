from nhl_sdk.models.teams.standings.standings import Standings
from nhl_sdk.models.teams.standings.standings_result import StandingsResult

from .conftest import ok


def test_standings_get_now_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_standings.return_value = ok({"standings": []})
    svc = Standings(mock_client)
    result = svc.get_standings()
    assert isinstance(result, StandingsResult)
    mock_client._api.api_web.call_nhl_teams.get_standings.assert_called_once_with(date=None)


def test_standings_get_now_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_standings.return_value = ok({"standings": []})
    svc = Standings(mock_client)
    _ = svc.get_standings()
    _ = svc.get_standings()
    mock_client._api.api_web.call_nhl_teams.get_standings.assert_called_once()


def test_standings_get_with_date(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_standings.return_value = ok({"standings": []})
    svc = Standings(mock_client)
    result = svc.get_standings(date="2025-01-15")
    assert isinstance(result, StandingsResult)
    mock_client._api.api_web.call_nhl_teams.get_standings.assert_called_once_with(date="2025-01-15")


def test_standings_date_and_now_are_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_standings.return_value = ok({"standings": []})
    svc = Standings(mock_client)
    _ = svc.get_standings()
    _ = svc.get_standings(date="2025-01-15")
    assert mock_client._api.api_web.call_nhl_teams.get_standings.call_count == 2


def test_standings_by_season_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_standings_per_season.return_value = ok([20242025])
    svc = Standings(mock_client)
    result = svc.get_standings_by_season()
    assert result == [20242025]
    mock_client._api.api_web.call_nhl_teams.get_standings_per_season.assert_called_once()


def test_standings_by_season_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_standings_per_season.return_value = ok([20242025])
    svc = Standings(mock_client)
    _ = svc.get_standings_by_season()
    _ = svc.get_standings_by_season()
    mock_client._api.api_web.call_nhl_teams.get_standings_per_season.assert_called_once()
