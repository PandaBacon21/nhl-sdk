"""
Tests for draft rankings models: DraftCategory, DraftProspect, DraftRankingsResult
"""
from nhl_stats.models.draft.rankings.rankings_result import DraftCategory, DraftProspect, DraftRankingsResult


CATEGORY_DATA = {"id": 1, "name": "North American Skater", "consumerKey": "na-skater"}

PROSPECT_DATA = {
    "lastName": "Yakemchuk",
    "firstName": "Cole",
    "positionCode": "D",
    "shootsCatches": "L",
    "heightInInches": 77,
    "weightInPounds": 195,
    "lastAmateurClub": "Calgary Hitmen",
    "lastAmateurLeague": "WHL",
    "birthDate": "2006-06-10",
    "birthCity": "Sherwood Park",
    "birthStateProvince": "AB",
    "birthCountry": "CAN",
    "midtermRank": 1,
}

PROSPECT_INTERNATIONAL = {
    "lastName": "Svenson",
    "firstName": "Erik",
    "positionCode": "C",
    "shootsCatches": "L",
    "heightInInches": 73,
    "weightInPounds": 180,
    "lastAmateurClub": "Djurgårdens IF",
    "lastAmateurLeague": "SHL-J",
    "birthDate": "2007-01-15",
    "birthCity": "Stockholm",
    "birthCountry": "SWE",
    "midtermRank": 5,
}

RANKINGS_DATA = {
    "draftYear": 2026,
    "categoryId": 1,
    "categoryKey": "na-skater",
    "draftYears": [2026, 2025, 2024],
    "categories": [CATEGORY_DATA],
    "rankings": [PROSPECT_DATA],
}


# --------------------------------------------------------------------------
# DraftCategory
# --------------------------------------------------------------------------

def test_category_fields() -> None:
    c = DraftCategory.from_dict(CATEGORY_DATA)
    assert c.id == 1
    assert c.name == "North American Skater"
    assert c.consumer_key == "na-skater"


def test_category_empty() -> None:
    c = DraftCategory.from_dict({})
    assert c.id is None
    assert c.name is None
    assert c.consumer_key is None


# --------------------------------------------------------------------------
# DraftProspect
# --------------------------------------------------------------------------

def test_prospect_fields() -> None:
    p = DraftProspect.from_dict(PROSPECT_DATA)
    assert p.last_name == "Yakemchuk"
    assert p.first_name == "Cole"
    assert p.position_code == "D"
    assert p.shoots_catches == "L"
    assert p.height_in_inches == 77
    assert p.weight_in_pounds == 195
    assert p.last_amateur_club == "Calgary Hitmen"
    assert p.last_amateur_league == "WHL"
    assert p.birth_date == "2006-06-10"
    assert p.birth_city == "Sherwood Park"
    assert p.birth_state_province == "AB"
    assert p.birth_country == "CAN"
    assert p.midterm_rank == 1


def test_prospect_no_birth_state_province() -> None:
    p = DraftProspect.from_dict(PROSPECT_INTERNATIONAL)
    assert p.birth_state_province is None
    assert p.birth_country == "SWE"


def test_prospect_final_rank() -> None:
    p = DraftProspect.from_dict({**PROSPECT_DATA, "midtermRank": 6, "finalRank": 11})
    assert p.midterm_rank == 6
    assert p.final_rank == 11


def test_prospect_final_rank_only() -> None:
    # Some late-ranked prospects have finalRank but no midtermRank
    p = DraftProspect.from_dict({"lastName": "Protas", "firstName": "Ilya", "finalRank": 49})
    assert p.midterm_rank is None
    assert p.final_rank == 49


def test_prospect_empty() -> None:
    p = DraftProspect.from_dict({})
    assert p.last_name is None
    assert p.first_name is None
    assert p.midterm_rank is None
    assert p.final_rank is None
    assert p.birth_state_province is None


# --------------------------------------------------------------------------
# DraftRankingsResult
# --------------------------------------------------------------------------

def test_rankings_result_fields() -> None:
    r = DraftRankingsResult.from_dict(RANKINGS_DATA)
    assert r.draft_year == 2026
    assert r.category_id == 1
    assert r.category_key == "na-skater"
    assert r.draft_years == [2026, 2025, 2024]
    assert len(r.categories) == 1
    assert len(r.rankings) == 1


def test_rankings_result_categories_parsed() -> None:
    r = DraftRankingsResult.from_dict(RANKINGS_DATA)
    c = r.categories[0]
    assert isinstance(c, DraftCategory)
    assert c.id == 1


def test_rankings_result_prospects_parsed() -> None:
    r = DraftRankingsResult.from_dict(RANKINGS_DATA)
    p = r.rankings[0]
    assert isinstance(p, DraftProspect)
    assert p.last_name == "Yakemchuk"


def test_rankings_result_empty() -> None:
    r = DraftRankingsResult.from_dict({})
    assert r.draft_year is None
    assert r.category_id is None
    assert r.category_key is None
    assert r.draft_years == []
    assert r.categories == []
    assert r.rankings == []


def test_rankings_result_multiple_prospects() -> None:
    data = {**RANKINGS_DATA, "rankings": [PROSPECT_DATA, PROSPECT_INTERNATIONAL]}
    r = DraftRankingsResult.from_dict(data)
    assert len(r.rankings) == 2
    assert r.rankings[1].birth_state_province is None
