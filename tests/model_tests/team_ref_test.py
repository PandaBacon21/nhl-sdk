"""
Model tests for TeamRef.
"""
from nhl_sdk.models.teams.team.team_stats.team_ref import TeamRef

DATA = {
    "id": 21,
    "franchiseId": 27,
    "fullName": "Colorado Avalanche",
    "leagueId": 133,
    "rawTricode": "COL",
    "triCode": "COL",
}


def test_team_ref_from_dict_full() -> None:
    ref = TeamRef.from_dict(DATA)
    assert ref.id == 21
    assert ref.franchise_id == 27
    assert ref.full_name == "Colorado Avalanche"
    assert ref.league_id == 133
    assert ref.raw_tricode == "COL"
    assert ref.tricode == "COL"


def test_team_ref_from_dict_empty() -> None:
    ref = TeamRef.from_dict({})
    assert ref.id is None
    assert ref.franchise_id is None
    assert ref.full_name is None
    assert ref.league_id is None
    assert ref.raw_tricode is None
    assert ref.tricode is None


def test_team_ref_historical_team() -> None:
    data = {
        "id": 32,
        "franchiseId": 27,
        "fullName": "Quebec Nordiques",
        "leagueId": 133,
        "rawTricode": "QUE",
        "triCode": "QUE",
    }
    ref = TeamRef.from_dict(data)
    assert ref.id == 32
    assert ref.full_name == "Quebec Nordiques"
    assert ref.tricode == "QUE"
