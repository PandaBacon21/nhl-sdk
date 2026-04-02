"""
Tests for TeamShotLocationResult and sub-models.
"""
from src.models.teams.team.edge.team_shot_location_details.team_shot_location_detail import (
    TeamShotLocationResult, ShotLocationEntry, ShotLocationTotal,
)


LOCATION_ENTRY_HIGH_SLOT = {
    "area": "High Slot",
    "sog": 273,
    "sogRank": 1,
    "goals": 41,
    "goalsRank": 1,
    "shootingPctg": 0.1502,
    "shootingPctgRank": 17,
}

LOCATION_ENTRY_CREASE = {
    "area": "Crease",
    "sog": 60,
    "sogRank": 28,
    "goals": 17,
    "goalsRank": 19,
    "shootingPctg": 0.2833,
    "shootingPctgRank": 11,
}

LOCATION_TOTAL_ALL = {
    "locationCode": "all",
    "position": "all",
    "sog": 2471,
    "sogRank": 1,
    "sogLeagueAvg": 2072.9063,
    "goals": 274,
    "goalsRank": 1,
    "goalsLeagueAvg": 228.1875,
    "shootingPctg": 0.1109,
    "shootingPctgRank": 15,
    "shootingPctgLeagueAvg": 0.1101,
}

LOCATION_TOTAL_HIGH_D = {
    "locationCode": "high",
    "position": "D",
    "sog": 57,
    "sogRank": 2,
    "sogLeagueAvg": 37.0313,
    "goals": 6,
    "goalsRank": 14,
    "goalsLeagueAvg": 6.2813,
    "shootingPctg": 0.1053,
    "shootingPctgRank": 27,
    "shootingPctgLeagueAvg": 0.1696,
}

FULL_RESPONSE = {
    "shotLocationDetails": [LOCATION_ENTRY_HIGH_SLOT, LOCATION_ENTRY_CREASE],
    "shotLocationTotals": [LOCATION_TOTAL_ALL, LOCATION_TOTAL_HIGH_D],
}


# --------------------------------------------------------------------------
# ShotLocationEntry
# --------------------------------------------------------------------------

def test_shot_location_entry_fields() -> None:
    entry = ShotLocationEntry.from_dict(LOCATION_ENTRY_HIGH_SLOT)
    assert entry.area == "High Slot"
    assert entry.sog == 273
    assert entry.sog_rank == 1
    assert entry.goals == 41
    assert entry.goals_rank == 1
    assert entry.shooting_pctg == 0.1502
    assert entry.shooting_pctg_rank == 17


def test_shot_location_entry_crease() -> None:
    entry = ShotLocationEntry.from_dict(LOCATION_ENTRY_CREASE)
    assert entry.area == "Crease"
    assert entry.sog == 60
    assert entry.sog_rank == 28
    assert entry.shooting_pctg == 0.2833


def test_shot_location_entry_empty() -> None:
    entry = ShotLocationEntry.from_dict({})
    assert entry.area is None
    assert entry.sog is None
    assert entry.sog_rank is None
    assert entry.goals is None
    assert entry.shooting_pctg is None


# --------------------------------------------------------------------------
# ShotLocationTotal
# --------------------------------------------------------------------------

def test_shot_location_total_all() -> None:
    total = ShotLocationTotal.from_dict(LOCATION_TOTAL_ALL)
    assert total.location_code == "all"
    assert total.position == "all"
    assert total.sog == 2471
    assert total.sog_rank == 1
    assert total.sog_league_avg == 2072.9063
    assert total.goals == 274
    assert total.goals_rank == 1
    assert total.goals_league_avg == 228.1875
    assert total.shooting_pctg == 0.1109
    assert total.shooting_pctg_rank == 15
    assert total.shooting_pctg_league_avg == 0.1101


def test_shot_location_total_high_d() -> None:
    total = ShotLocationTotal.from_dict(LOCATION_TOTAL_HIGH_D)
    assert total.location_code == "high"
    assert total.position == "D"
    assert total.sog_rank == 2
    assert total.goals_rank == 14
    assert total.shooting_pctg_rank == 27


def test_shot_location_total_empty() -> None:
    total = ShotLocationTotal.from_dict({})
    assert total.location_code is None
    assert total.position is None
    assert total.sog is None
    assert total.sog_rank is None
    assert total.sog_league_avg is None
    assert total.goals is None
    assert total.shooting_pctg_league_avg is None


# --------------------------------------------------------------------------
# TeamShotLocationResult
# --------------------------------------------------------------------------

def test_team_shot_location_result_from_dict() -> None:
    result = TeamShotLocationResult.from_dict(FULL_RESPONSE)
    assert isinstance(result, TeamShotLocationResult)


def test_team_shot_location_result_details() -> None:
    result = TeamShotLocationResult.from_dict(FULL_RESPONSE)
    assert len(result.shot_location_details) == 2
    assert result.shot_location_details[0].area == "High Slot"
    assert result.shot_location_details[1].area == "Crease"


def test_team_shot_location_result_totals() -> None:
    result = TeamShotLocationResult.from_dict(FULL_RESPONSE)
    assert len(result.shot_location_totals) == 2
    assert result.shot_location_totals[0].location_code == "all"
    assert result.shot_location_totals[1].location_code == "high"


def test_team_shot_location_result_empty() -> None:
    result = TeamShotLocationResult.from_dict({})
    assert result.shot_location_details == []
    assert result.shot_location_totals == []


def test_team_shot_location_result_to_dict() -> None:
    result = TeamShotLocationResult.from_dict(FULL_RESPONSE)
    d = result.to_dict()
    assert len(d["shot_location_details"]) == 2
    assert d["shot_location_details"][0]["area"] == "High Slot"
    assert d["shot_location_details"][0]["sog_rank"] == 1
    assert len(d["shot_location_totals"]) == 2
    assert d["shot_location_totals"][0]["location_code"] == "all"
    assert d["shot_location_totals"][0]["sog_league_avg"] == 2072.9063
    assert d["shot_location_totals"][1]["position"] == "D"
