"""
Tests for team roster models:
  RosterPlayer, TeamRosterResult, Prospect, ProspectsResult
"""
from src.models.teams.team.team_roster.team_roster_result import RosterPlayer, TeamRosterResult
from src.models.teams.team.team_roster.team_prospects import Prospect, ProspectsResult


PLAYER_DATA = {
    "id": 8477492,
    "headshot": "https://assets.nhle.com/mugs/nhl/20252026/COL/8477492.png",
    "firstName": {"default": "Nathan"},
    "lastName": {"default": "MacKinnon"},
    "sweaterNumber": 29,
    "positionCode": "C",
    "shootsCatches": "R",
    "heightInInches": 72,
    "weightInPounds": 200,
    "heightInCentimeters": 183,
    "weightInKilograms": 91,
    "birthDate": "1995-09-01",
    "birthCity": {"default": "Halifax"},
    "birthStateProvince": {"default": "NS"},
    "birthCountry": "CAN",
}

PLAYER_DATA_MINIMAL = {
    "id": 8480069,
    "firstName": {"default": "Cale"},
    "lastName": {"default": "Makar"},
    "positionCode": "D",
}


# ==========================================================================
# ROSTER PLAYER
# ==========================================================================

def test_roster_player_from_dict() -> None:
    p = RosterPlayer.from_dict(PLAYER_DATA)
    assert p.id == 8477492
    assert p.headshot == "https://assets.nhle.com/mugs/nhl/20252026/COL/8477492.png"
    assert p.first_name.default == "Nathan"
    assert p.last_name.default == "MacKinnon"
    assert p.sweater_number == 29
    assert p.position_code == "C"
    assert p.shoots_catches == "R"
    assert p.height_in_inches == 72
    assert p.weight_in_pounds == 200
    assert p.height_in_centimeters == 183
    assert p.weight_in_kilograms == 91
    assert p.birth_details.birth_date == "1995-09-01"
    assert p.birth_details.city.default == "Halifax"
    assert p.birth_details.state_province.default == "NS"
    assert p.birth_details.country == "CAN"

def test_roster_player_minimal() -> None:
    p = RosterPlayer.from_dict(PLAYER_DATA_MINIMAL)
    assert p.id == 8480069
    assert p.headshot is None
    assert p.sweater_number is None
    assert p.shoots_catches is None
    assert p.height_in_inches is None
    assert p.birth_details.birth_date is None
    assert p.birth_details.country is None


# ==========================================================================
# TEAM ROSTER RESULT
# ==========================================================================

def test_team_roster_result_from_dict() -> None:
    data = {
        "forwards": [PLAYER_DATA],
        "defensemen": [PLAYER_DATA_MINIMAL],
        "goalies": [],
    }
    result = TeamRosterResult.from_dict(data)
    assert len(result.forwards) == 1
    assert len(result.defensemen) == 1
    assert len(result.goalies) == 0
    assert result.forwards[0].first_name.default == "Nathan"
    assert result.defensemen[0].first_name.default == "Cale"

def test_team_roster_result_empty() -> None:
    result = TeamRosterResult.from_dict({})
    assert result.forwards == []
    assert result.defensemen == []
    assert result.goalies == []


# ==========================================================================
# PROSPECT
# ==========================================================================

PROSPECT_DATA = {
    "id": 8484258,
    "headshot": "https://assets.nhle.com/mugs/nhl/20252026/COL/8484258.png",
    "firstName": {"default": "Sam"},
    "lastName": {"default": "Malinski"},
    "sweaterNumber": 70,
    "positionCode": "D",
    "shootsCatches": "R",
    "heightInInches": 71,
    "weightInPounds": 190,
    "heightInCentimeters": 180,
    "weightInKilograms": 86,
    "birthDate": "1998-07-27",
    "birthCity": {"default": "Lakeville"},
    "birthStateProvince": {"default": "MN"},
    "birthCountry": "USA",
}

def test_prospect_from_dict() -> None:
    p = Prospect.from_dict(PROSPECT_DATA)
    assert p.id == 8484258
    assert p.headshot is not None
    assert p.first_name.default == "Sam"
    assert p.last_name.default == "Malinski"
    assert p.sweater_number == 70
    assert p.position_code == "D"
    assert p.shoots_catches == "R"
    assert p.height_in_inches == 71
    assert p.weight_in_pounds == 190
    assert p.birth_details.birth_date == "1998-07-27"
    assert p.birth_details.city.default == "Lakeville"
    assert p.birth_details.state_province.default == "MN"
    assert p.birth_details.country == "USA"

def test_prospect_empty() -> None:
    p = Prospect.from_dict({})
    assert p.id is None
    assert p.headshot is None
    assert p.first_name.default is None
    assert p.birth_details.birth_date is None
    assert p.birth_details.country is None


# ==========================================================================
# PROSPECTS RESULT
# ==========================================================================

def test_prospects_result_from_dict() -> None:
    data = {
        "forwards": [PROSPECT_DATA],
        "defensemen": [PROSPECT_DATA],
        "goalies": [],
    }
    result = ProspectsResult.from_dict(data)
    assert len(result.forwards) == 1
    assert len(result.defensemen) == 1
    assert len(result.goalies) == 0
    assert result.forwards[0].last_name.default == "Malinski"

def test_prospects_result_empty() -> None:
    result = ProspectsResult.from_dict({})
    assert result.forwards == []
    assert result.defensemen == []
    assert result.goalies == []
