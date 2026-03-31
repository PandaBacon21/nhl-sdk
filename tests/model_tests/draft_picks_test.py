"""
Tests for draft picks models: DraftPickEntry, DraftPicksResult
"""
from src.models.draft.picks.picks_result import DraftPickEntry, DraftPicksResult


PICK_DATA = {
    "round": 1,
    "pickInRound": 1,
    "overallPick": 1,
    "teamId": 2,
    "teamAbbrev": "NYI",
    "teamName": {"default": "New York Islanders", "fr": "Islanders de New York"},
    "teamCommonName": {"default": "Islanders"},
    "teamPlaceNameWithPreposition": {"default": "New York", "fr": "de New York"},
    "displayAbbrev": {"default": "NYI"},
    "teamLogoLight": "https://assets.nhle.com/logos/nhl/svg/NYI_light.svg",
    "teamLogoDark": "https://assets.nhle.com/logos/nhl/svg/NYI_dark.svg",
    "teamPickHistory": "NYI",
    "firstName": {"default": "Matthew"},
    "lastName": {"default": "Schaefer"},
    "positionCode": "D",
    "countryCode": "CAN",
    "height": 74,
    "weight": 186,
    "amateurLeague": "OHL",
    "amateurClubName": "Erie",
}

PICKS_DATA = {
    "broadcastStartTimeUTC": "2025-06-27T23:00:00Z",
    "draftYear": 2025,
    "draftYears": [2025, 2024, 2023],
    "selectableRounds": [1, 2, 3, 4, 5, 6, 7],
    "state": "over",
    "picks": [PICK_DATA],
}


# --------------------------------------------------------------------------
# DraftPickEntry
# --------------------------------------------------------------------------

def test_pick_entry_fields() -> None:
    p = DraftPickEntry.from_dict(PICK_DATA)
    assert p.round == 1
    assert p.pick_in_round == 1
    assert p.overall_pick == 1
    assert p.team_id == 2
    assert p.team_abbrev == "NYI"
    assert p.team_name.default == "New York Islanders"
    assert p.team_common_name.default == "Islanders"
    assert p.team_place_name_with_preposition.default == "New York"
    assert p.display_abbrev.default == "NYI"
    assert p.team_logo_light is not None
    assert p.team_logo_dark is not None
    assert p.team_pick_history == "NYI"
    assert p.first_name.default == "Matthew"
    assert p.last_name.default == "Schaefer"
    assert p.position_code == "D"
    assert p.country_code == "CAN"
    assert p.height == 74
    assert p.weight == 186
    assert p.amateur_league == "OHL"
    assert p.amateur_club_name == "Erie"


def test_pick_entry_localized_french() -> None:
    p = DraftPickEntry.from_dict(PICK_DATA)
    assert p.team_name.get_locale("fr") == "Islanders de New York"
    assert p.team_place_name_with_preposition.get_locale("fr") == "de New York"


def test_pick_entry_traded_pick_history() -> None:
    p = DraftPickEntry.from_dict({**PICK_DATA, "teamPickHistory": "NYR-VAN-PIT-PHI"})
    assert p.team_pick_history == "NYR-VAN-PIT-PHI"


def test_pick_entry_empty() -> None:
    p = DraftPickEntry.from_dict({})
    assert p.round is None
    assert p.overall_pick is None
    assert p.team_id is None
    assert p.team_abbrev is None
    assert p.country_code is None
    assert p.height is None
    assert p.weight is None
    assert p.amateur_league is None
    assert p.team_name.default is None
    assert p.first_name.default is None


# --------------------------------------------------------------------------
# DraftPicksResult
# --------------------------------------------------------------------------

def test_picks_result_fields() -> None:
    r = DraftPicksResult.from_dict(PICKS_DATA)
    assert r.broadcast_start_time_utc == "2025-06-27T23:00:00Z"
    assert r.draft_year == 2025
    assert r.draft_years == [2025, 2024, 2023]
    assert r.selectable_rounds == [1, 2, 3, 4, 5, 6, 7]
    assert r.state == "over"
    assert len(r.picks) == 1


def test_picks_result_picks_parsed() -> None:
    r = DraftPicksResult.from_dict(PICKS_DATA)
    p = r.picks[0]
    assert isinstance(p, DraftPickEntry)
    assert p.overall_pick == 1
    assert p.team_abbrev == "NYI"


def test_picks_result_empty() -> None:
    r = DraftPicksResult.from_dict({})
    assert r.broadcast_start_time_utc is None
    assert r.draft_year is None
    assert r.draft_years == []
    assert r.selectable_rounds == []
    assert r.state is None
    assert r.picks == []


def test_picks_result_multiple_picks() -> None:
    pick2 = {**PICK_DATA, "round": 1, "pickInRound": 2, "overallPick": 2, "teamAbbrev": "SJS"}
    r = DraftPicksResult.from_dict({**PICKS_DATA, "picks": [PICK_DATA, pick2]})
    assert len(r.picks) == 2
    assert r.picks[1].team_abbrev == "SJS"
