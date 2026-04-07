"""
Resource tests for CallNhlStatsTeams.
"""
from src.resources.api_stats.teams import CallNhlStatsTeams
from src.core.transport import APICallStats, APIResponse

svc = CallNhlStatsTeams(http=APICallStats())


def _fake(called: dict):
    def fake_call(endpoint: str, params: dict | None = None) -> APIResponse:
        called["endpoint"] = endpoint
        called["params"] = params
        return APIResponse(ok=True, data={}, status_code=200)
    return fake_call


# ==========================================================================
# Team stats reports
# ==========================================================================

def test_get_team_stats_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_team_stats("summary")
    assert called["endpoint"] == "/en/team/summary"


def test_get_team_stats_with_cayenne(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_team_stats("summary", cayenne_exp="teamId=21")
    assert called["params"]["cayenneExp"] == "teamId=21"


def test_get_team_stats_no_params_passes_none(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_team_stats("summary")
    assert called["params"] is None


# ==========================================================================
# Team reference
# ==========================================================================

def test_get_teams_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_teams()
    assert called["endpoint"] == "/en/team"


def test_get_team_by_id_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_team_by_id(team_id=21)
    assert called["endpoint"] == "/en/team/id/21"


def test_get_franchise_endpoint(monkeypatch) -> None:
    called = {}
    monkeypatch.setattr(svc._http, "get", _fake(called))
    svc.get_franchise()
    assert called["endpoint"] == "/en/franchise"
