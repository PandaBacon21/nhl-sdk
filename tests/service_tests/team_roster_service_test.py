from src.models.teams.team.team_roster.team_roster import TeamRoster
from src.models.teams.team.team_roster.team_roster_result import TeamRosterResult
from src.models.teams.team.team_roster.team_prospects import ProspectsResult

from .conftest import ok

TEAM = "COL"
SEASON = 20242025


def test_get_team_roster_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_roster.return_value = ok({"forwards": [], "defensemen": [], "goalies": []})
    svc = TeamRoster(mock_client)
    result = svc.get_team_roster(team=TEAM)
    assert isinstance(result, TeamRosterResult)
    mock_client._api.api_web.call_nhl_teams.get_team_roster.assert_called_once_with(team=TEAM, season=None)


def test_get_team_roster_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_roster.return_value = ok({"forwards": [], "defensemen": [], "goalies": []})
    svc = TeamRoster(mock_client)
    _ = svc.get_team_roster(team=TEAM)
    _ = svc.get_team_roster(team=TEAM)
    mock_client._api.api_web.call_nhl_teams.get_team_roster.assert_called_once()


def test_get_team_roster_with_season(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_roster.return_value = ok({"forwards": [], "defensemen": [], "goalies": []})
    svc = TeamRoster(mock_client)
    result = svc.get_team_roster(team=TEAM, season=SEASON)
    assert isinstance(result, TeamRosterResult)
    mock_client._api.api_web.call_nhl_teams.get_team_roster.assert_called_once_with(team=TEAM, season=SEASON)


def test_get_team_prospects_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.return_value = ok({"prospects": []})
    svc = TeamRoster(mock_client)
    result = svc.get_team_prospects(team=TEAM)
    assert isinstance(result, ProspectsResult)
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.assert_called_once_with(team=TEAM)


def test_get_team_prospects_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.return_value = ok({"prospects": []})
    svc = TeamRoster(mock_client)
    _ = svc.get_team_prospects(team=TEAM)
    _ = svc.get_team_prospects(team=TEAM)
    mock_client._api.api_web.call_nhl_teams.get_team_prospects.assert_called_once()


def test_get_roster_seasons_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.return_value = ok([20242025, 20232024])
    svc = TeamRoster(mock_client)
    result = svc.get_roster_seasons(team=TEAM)
    assert result == [20242025, 20232024]
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.assert_called_once_with(team=TEAM)


def test_get_roster_seasons_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.return_value = ok([20242025])
    svc = TeamRoster(mock_client)
    _ = svc.get_roster_seasons(team=TEAM)
    _ = svc.get_roster_seasons(team=TEAM)
    mock_client._api.api_web.call_nhl_teams.get_roster_season_by_team.assert_called_once()
