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
