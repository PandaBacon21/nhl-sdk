from src.services.teams import Teams
from src.models.teams.standings.standings import Standings
from src.models.teams.team.team_stats.team_stats import TeamStats
from src.models.teams.team.team_roster.team_roster import TeamRoster
from src.models.teams.team.team_schedule.team_schedule import TeamSchedule


def test_teams_standings_property(mock_client) -> None:
    svc = Teams(mock_client)
    assert isinstance(svc.standings, Standings)


def test_teams_stats_property(mock_client) -> None:
    svc = Teams(mock_client)
    assert isinstance(svc.stats, TeamStats)


def test_teams_roster_property(mock_client) -> None:
    svc = Teams(mock_client)
    assert isinstance(svc.roster, TeamRoster)


def test_teams_schedule_property(mock_client) -> None:
    svc = Teams(mock_client)
    assert isinstance(svc.schedule, TeamSchedule)


def test_teams_standings_each_call_new_instance(mock_client) -> None:
    svc = Teams(mock_client)
    a = svc.standings
    b = svc.standings
    assert isinstance(a, Standings)
    assert isinstance(b, Standings)
