from nhl_stats.models.teams.team.team_roster.team_roster import TeamRoster
from nhl_stats.models.teams.team.team_roster.team_roster_result import TeamRosterResult
from nhl_stats.models.teams.team.team_roster.team_prospects import ProspectsResult

from .conftest import ok

ABBREV = "COL"
SEASON = 20242025


def test_get_team_roster_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_roster.return_value = ok({"forwards": [], "defensemen": [], "goalies": []})
    svc = TeamRoster(mock_client, ABBREV)
    result = svc.get_team_roster()
    assert isinstance(result, TeamRosterResult)
    mock_client._api.api_web.call_nhl_teams.get_team_roster.assert_called_once_with(team=ABBREV, season=None)


def test_get_team_roster_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_roster.return_value = ok({"forwards": [], "defensemen": [], "goalies": []})
    svc = TeamRoster(mock_client, ABBREV)
    _ = svc.get_team_roster()
    _ = svc.get_team_roster()
    mock_client._api.api_web.call_nhl_teams.get_team_roster.assert_called_once()


def test_get_team_roster_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_roster.return_value = ok({"forwards": [], "defensemen": [], "goalies": []})
    svc = TeamRoster(mock_client, ABBREV)
    result = svc.get_team_roster(season=SEASON)
    assert isinstance(result, TeamRosterResult)
    mock_client._api.api_web.call_nhl_teams.get_team_roster.assert_called_once_with(team=ABBREV, season=SEASON)


def test_get_team_prospects_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.return_value = ok({"prospects": []})
    svc = TeamRoster(mock_client, ABBREV)
    result = svc.get_team_prospects()
    assert isinstance(result, ProspectsResult)
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.assert_called_once_with(team=ABBREV)


def test_get_team_prospects_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.return_value = ok({"prospects": []})
    svc = TeamRoster(mock_client, ABBREV)
    _ = svc.get_team_prospects()
    _ = svc.get_team_prospects()
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.assert_called_once()


def test_get_roster_seasons_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.return_value = ok([20242025, 20232024])
    svc = TeamRoster(mock_client, ABBREV)
    result = svc.get_roster_seasons()
    assert result == [20242025, 20232024]
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.assert_called_once_with(team=ABBREV)


def test_get_roster_seasons_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.return_value = ok([20242025])
    svc = TeamRoster(mock_client, ABBREV)
    _ = svc.get_roster_seasons()
    _ = svc.get_roster_seasons()
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.assert_called_once()
