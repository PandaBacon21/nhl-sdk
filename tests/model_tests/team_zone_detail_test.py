"""
Tests for TeamZoneDetailResult and sub-models.
"""
from src.models.teams.team.edge.team_zone_details.team_zone_detail import (
    TeamZoneDetailResult, ZoneTimeEntry, ZoneShotDifferential,
)


ZONE_ENTRY_ALL = {
    "strengthCode": "all",
    "offensiveZonePctg": 0.4286305,
    "offensiveZoneRank": 3,
    "offensiveZoneLeagueAvg": 0.4107842,
    "neutralZonePctg": 0.1815559,
    "neutralZoneRank": 8,
    "neutralZoneLeagueAvg": 0.1784317,
    "defensiveZonePctg": 0.3898136,
    "defensiveZoneRank": 3,
    "defensiveZoneLeagueAvg": 0.4107842,
}

ZONE_ENTRY_PP = {
    "strengthCode": "pp",
    "offensiveZonePctg": 0.5964566,
    "offensiveZoneRank": 13,
    "offensiveZoneLeagueAvg": 0.5893068,
    "neutralZonePctg": 0.1425310,
    "neutralZoneRank": 15,
    "neutralZoneLeagueAvg": 0.1426352,
    "defensiveZonePctg": 0.2610124,
    "defensiveZoneRank": 10,
    "defensiveZoneLeagueAvg": 0.2680580,
}

SHOT_DIFFERENTIAL = {
    "shotAttemptDifferential": 7.684932,
    "shotAttemptDifferentialRank": 2,
    "sogDifferential": 0.141059,
    "sogDifferentialRank": 3,
}

FULL_RESPONSE = {
    "zoneTimeDetails": [ZONE_ENTRY_ALL, ZONE_ENTRY_PP],
    "shotDifferential": SHOT_DIFFERENTIAL,
}


# --------------------------------------------------------------------------
# ZoneTimeEntry
# --------------------------------------------------------------------------

def test_zone_time_entry_all_fields() -> None:
    entry = ZoneTimeEntry.from_dict(ZONE_ENTRY_ALL)
    assert entry.strength_code == "all"
    assert entry.offensive_zone_pctg == 0.4286305
    assert entry.offensive_zone_rank == 3
    assert entry.offensive_zone_league_avg == 0.4107842
    assert entry.neutral_zone_pctg == 0.1815559
    assert entry.neutral_zone_rank == 8
    assert entry.neutral_zone_league_avg == 0.1784317
    assert entry.defensive_zone_pctg == 0.3898136
    assert entry.defensive_zone_rank == 3
    assert entry.defensive_zone_league_avg == 0.4107842


def test_zone_time_entry_pp() -> None:
    entry = ZoneTimeEntry.from_dict(ZONE_ENTRY_PP)
    assert entry.strength_code == "pp"
    assert entry.offensive_zone_pctg == 0.5964566
    assert entry.offensive_zone_rank == 13
    assert entry.defensive_zone_rank == 10


def test_zone_time_entry_empty() -> None:
    entry = ZoneTimeEntry.from_dict({})
    assert entry.strength_code is None
    assert entry.offensive_zone_pctg is None
    assert entry.offensive_zone_rank is None
    assert entry.neutral_zone_pctg is None
    assert entry.defensive_zone_pctg is None


# --------------------------------------------------------------------------
# ZoneShotDifferential
# --------------------------------------------------------------------------

def test_zone_shot_differential_fields() -> None:
    diff = ZoneShotDifferential.from_dict(SHOT_DIFFERENTIAL)
    assert diff.shot_attempt_differential == 7.684932
    assert diff.shot_attempt_differential_rank == 2
    assert diff.sog_differential == 0.141059
    assert diff.sog_differential_rank == 3


def test_zone_shot_differential_empty() -> None:
    diff = ZoneShotDifferential.from_dict({})
    assert diff.shot_attempt_differential is None
    assert diff.shot_attempt_differential_rank is None
    assert diff.sog_differential is None
    assert diff.sog_differential_rank is None


# --------------------------------------------------------------------------
# TeamZoneDetailResult
# --------------------------------------------------------------------------

def test_team_zone_detail_result_from_dict() -> None:
    result = TeamZoneDetailResult.from_dict(FULL_RESPONSE)
    assert isinstance(result, TeamZoneDetailResult)


def test_team_zone_detail_result_zone_entries() -> None:
    result = TeamZoneDetailResult.from_dict(FULL_RESPONSE)
    assert len(result.zone_time_details) == 2
    assert result.zone_time_details[0].strength_code == "all"
    assert result.zone_time_details[1].strength_code == "pp"


def test_team_zone_detail_result_shot_differential() -> None:
    result = TeamZoneDetailResult.from_dict(FULL_RESPONSE)
    assert result.shot_differential.shot_attempt_differential == 7.684932
    assert result.shot_differential.shot_attempt_differential_rank == 2
    assert result.shot_differential.sog_differential_rank == 3


def test_team_zone_detail_result_empty() -> None:
    result = TeamZoneDetailResult.from_dict({})
    assert result.zone_time_details == []
    assert result.shot_differential.shot_attempt_differential is None


def test_team_zone_detail_result_to_dict() -> None:
    result = TeamZoneDetailResult.from_dict(FULL_RESPONSE)
    d = result.to_dict()
    assert len(d["zone_time_details"]) == 2
    assert d["zone_time_details"][0]["strength_code"] == "all"
    assert d["zone_time_details"][0]["offensive_zone_rank"] == 3
    assert d["shot_differential"]["shot_attempt_differential"] == 7.684932
    assert d["shot_differential"]["shot_attempt_differential_rank"] == 2
