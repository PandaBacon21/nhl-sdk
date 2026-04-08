"""
Tests for draft tracker models: DraftPick, DraftTrackerResult
"""
from nhl_stats.models.draft.tracker.tracker_result import DraftPick, DraftTrackerResult


PICK_DATA = {
    "pickInRound": 1,
    "overallPick": 1,
    "teamId": 2,
    "teamAbbrev": "NYI",
    "teamFullName": {"default": "New York Islanders", "fr": "Islanders de New York"},
    "teamCommonName": {"default": "Islanders"},
    "teamPlaceNameWithPreposition": {"default": "New York", "fr": "de New York"},
    "teamLogoLight": "https://assets.nhle.com/logos/nhl/svg/NYI_light.svg",
    "teamLogoDark": "https://assets.nhle.com/logos/nhl/svg/NYI_dark.svg",
    "state": "confirmed",
    "lastName": {"default": "Schaefer"},
    "firstName": {"default": "Matthew"},
    "positionCode": "D",
}

TRACKER_DATA = {
    "currentDraftDate": "2025-06-27",
    "broadcastStartTimeUTC": "2025-06-27T23:00:00Z",
    "tvBroadcasts": [
        {"id": 309, "market": "N", "countryCode": "US", "network": "ESPN", "sequenceNumber": 10},
    ],
    "logoUrl": "https://assets.nhle.com/special_event_season/20242025/svg/draft_second_dark_en.svg",
    "logoFrUrl": "https://assets.nhle.com/special_event_season/20242025/svg/draft_second_dark_fr.svg",
    "uiAccentColor": "#00B5E2",
    "round": 1,
    "state": "over",
    "picks": [PICK_DATA],
}


# --------------------------------------------------------------------------
# DraftPick
# --------------------------------------------------------------------------

def test_pick_fields() -> None:
    p = DraftPick.from_dict(PICK_DATA)
    assert p.pick_in_round == 1
    assert p.overall_pick == 1
    assert p.team_id == 2
    assert p.team_abbrev == "NYI"
    assert p.team_full_name.default == "New York Islanders"
    assert p.team_common_name.default == "Islanders"
    assert p.team_place_name_with_preposition.default == "New York"
    assert p.team_logo_light is not None
    assert p.team_logo_dark is not None
    assert p.state == "confirmed"
    assert p.last_name.default == "Schaefer"
    assert p.first_name.default == "Matthew"
    assert p.position_code == "D"


def test_pick_localized_french() -> None:
    p = DraftPick.from_dict(PICK_DATA)
    assert p.team_full_name.get_locale("fr") == "Islanders de New York"
    assert p.team_place_name_with_preposition.get_locale("fr") == "de New York"


def test_pick_empty() -> None:
    p = DraftPick.from_dict({})
    assert p.pick_in_round is None
    assert p.overall_pick is None
    assert p.team_id is None
    assert p.team_abbrev is None
    assert p.state is None
    assert p.position_code is None
    assert p.team_full_name.default is None
    assert p.last_name.default is None
    assert p.first_name.default is None


# --------------------------------------------------------------------------
# DraftTrackerResult
# --------------------------------------------------------------------------

def test_tracker_result_fields() -> None:
    r = DraftTrackerResult.from_dict(TRACKER_DATA)
    assert r.current_draft_date == "2025-06-27"
    assert r.broadcast_start_time_utc == "2025-06-27T23:00:00Z"
    assert r.logo_url is not None
    assert r.logo_fr_url is not None
    assert r.ui_accent_color == "#00B5E2"
    assert r.round == 1
    assert r.state == "over"


def test_tracker_result_broadcasts_parsed() -> None:
    r = DraftTrackerResult.from_dict(TRACKER_DATA)
    assert len(r.tv_broadcasts) == 1
    b = r.tv_broadcasts[0]
    assert b.id == 309
    assert b.network == "ESPN"
    assert b.country_code == "US"


def test_tracker_result_picks_parsed() -> None:
    r = DraftTrackerResult.from_dict(TRACKER_DATA)
    assert len(r.picks) == 1
    p = r.picks[0]
    assert isinstance(p, DraftPick)
    assert p.overall_pick == 1
    assert p.team_abbrev == "NYI"


def test_tracker_result_empty() -> None:
    r = DraftTrackerResult.from_dict({})
    assert r.current_draft_date is None
    assert r.broadcast_start_time_utc is None
    assert r.round is None
    assert r.state is None
    assert r.tv_broadcasts == []
    assert r.picks == []


def test_tracker_result_multiple_picks() -> None:
    pick2 = {**PICK_DATA, "pickInRound": 2, "overallPick": 2, "teamAbbrev": "SJS"}
    r = DraftTrackerResult.from_dict({**TRACKER_DATA, "picks": [PICK_DATA, pick2]})
    assert len(r.picks) == 2
    assert r.picks[1].team_abbrev == "SJS"
