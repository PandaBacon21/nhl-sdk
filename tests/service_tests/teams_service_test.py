from src.services.teams import Teams
from src.models.teams.standings.standings import Standings
from src.models.teams.team.team import Team
from src.models.teams.edge.teams_edge import TeamsEdge


def test_teams_standings_property(mock_client) -> None:
    svc = Teams(mock_client)
    assert isinstance(svc.standings, Standings)


def test_teams_edge_property(mock_client) -> None:
    svc = Teams(mock_client)
    assert isinstance(svc.edge, TeamsEdge)


def test_teams_get_returns_team(mock_client) -> None:
    svc = Teams(mock_client)
    team = svc.get("COL")
    assert isinstance(team, Team)
    assert team._abbrev == "COL"
    assert team._team_id == 21


def test_teams_get_case_insensitive(mock_client) -> None:
    svc = Teams(mock_client)
    team = svc.get("col")
    assert team._abbrev == "COL"
    assert team._team_id == 21


def test_teams_get_unknown_abbrev_raises(mock_client) -> None:
    svc = Teams(mock_client)
    try:
        svc.get("ZZZ")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "ZZZ" in str(e)


def test_teams_standings_each_call_new_instance(mock_client) -> None:
    svc = Teams(mock_client)
    a = svc.standings
    b = svc.standings
    assert isinstance(a, Standings)
    assert isinstance(b, Standings)


# ==========================================================================
# all()
# ==========================================================================

def test_teams_all_returns_list(mock_client) -> None:
    from src.models.teams.team.team_stats.team_ref import TeamRef
    from .conftest import ok
    mock_client._api.api_stats.call_nhl_stats_teams.get_teams.return_value = ok(
        {"data": [{"id": 21, "triCode": "COL", "fullName": "Colorado Avalanche", "franchiseId": 27, "leagueId": 133, "rawTricode": "COL"}], "total": 1}
    )
    svc = Teams(mock_client)
    result = svc.all()
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], TeamRef)
    assert result[0].tricode == "COL"


def test_teams_all_cache_miss(mock_client) -> None:
    from .conftest import ok
    mock_client._api.api_stats.call_nhl_stats_teams.get_teams.return_value = ok({"data": [], "total": 0})
    svc = Teams(mock_client)
    _ = svc.all()
    mock_client._api.api_stats.call_nhl_stats_teams.get_teams.assert_called_once()


def test_teams_all_cache_hit(mock_client) -> None:
    from .conftest import ok
    mock_client._api.api_stats.call_nhl_stats_teams.get_teams.return_value = ok({"data": [], "total": 0})
    svc = Teams(mock_client)
    _ = svc.all()
    _ = svc.all()
    mock_client._api.api_stats.call_nhl_stats_teams.get_teams.assert_called_once()


def test_teams_all_empty(mock_client) -> None:
    from .conftest import ok
    mock_client._api.api_stats.call_nhl_stats_teams.get_teams.return_value = ok({"data": [], "total": 0})
    svc = Teams(mock_client)
    assert svc.all() == []
