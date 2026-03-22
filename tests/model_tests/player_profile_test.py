from src.models.players.player.profile.height import Height
from src.models.players.player.profile.weight import Weight
from src.models.players.player.profile.birth_details import BirthDetails
from src.models.players.player.profile.draft import Draft
from src.models.players.player.profile.media import Media
from src.models.players.player.profile.profile_team import ProfileTeam
from src.models.players.player.profile.award import Award
from src.models.players.player.profile.badge import Badge
from src.models.players.player.profile.legacy import Legacy
from src.models.players.player.profile.profile import Profile


# ==========================================================================
# HEIGHT
# ==========================================================================

def test_height_from_dict() -> None:
    h = Height.from_dict({"heightInInches": 73, "heightInCentimeters": 185})
    assert h.height_in == 73
    assert h.height_cm == 185

def test_height_empty() -> None:
    h = Height.from_dict({})
    assert h.height_in is None
    assert h.height_cm is None


# ==========================================================================
# WEIGHT
# ==========================================================================

def test_weight_from_dict() -> None:
    w = Weight.from_dict({"weightInPounds": 193, "weightInKilograms": 88})
    assert w.weight_lbs == 193
    assert w.weight_kg == 88

def test_weight_empty() -> None:
    w = Weight.from_dict({})
    assert w.weight_lbs is None
    assert w.weight_kg is None


# ==========================================================================
# BIRTH DETAILS
# ==========================================================================

def test_birth_details_from_dict() -> None:
    data = {
        "birthDate": "1997-01-13",
        "birthCity": {"default": "Bradford"},
        "birthStateProvince": {"default": "ON"},
        "birthCountry": "CAN",
    }
    bd = BirthDetails.from_dict(data)
    assert bd.birth_date == "1997-01-13"
    assert bd.city.default == "Bradford"
    assert bd.state_province.default == "ON"
    assert bd.country == "CAN"

def test_birth_details_empty() -> None:
    bd = BirthDetails.from_dict({})
    assert bd.birth_date is None
    assert bd.city.default is None
    assert bd.country is None


# ==========================================================================
# DRAFT
# ==========================================================================

def test_draft_from_dict() -> None:
    data = {
        "draftDetails": {
            "year": 2015,
            "teamAbbrev": "EDM",
            "round": 1,
            "pickInRound": 1,
            "overallPick": 1,
        }
    }
    draft = Draft.from_dict(data)
    assert draft.year == 2015
    assert draft.team == "EDM"
    assert draft.round == 1
    assert draft.pick_in_round == 1
    assert draft.pick_overall == 1

def test_draft_missing_details_key() -> None:
    """draftDetails key absent — all fields should be None."""
    draft = Draft.from_dict({})
    assert draft.year is None
    assert draft.team is None
    assert draft.round is None

def test_draft_details_is_none() -> None:
    """draftDetails is explicitly None (undrafted player)."""
    draft = Draft.from_dict({"draftDetails": None})
    assert draft.year is None
    assert draft.pick_overall is None


# ==========================================================================
# MEDIA
# ==========================================================================

def test_media_from_dict() -> None:
    data = {
        "playerSlug": "connor-mcdavid-8478402",
        "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
        "heroImage": "https://assets.nhle.com/heros/nhl/20232024/EDM/8478402.png",
    }
    media = Media.from_dict(data)
    assert media.slug == "connor-mcdavid-8478402"
    assert media.headshot == "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png"
    assert media.hero_image == "https://assets.nhle.com/heros/nhl/20232024/EDM/8478402.png"

def test_media_empty() -> None:
    media = Media.from_dict({})
    assert media.slug is None
    assert media.headshot is None
    assert media.hero_image is None


# ==========================================================================
# PROFILE TEAM
# ==========================================================================

def test_profile_team_from_dict() -> None:
    data = {
        "currentTeamId": 22,
        "fullTeamName": {"default": "Edmonton Oilers"},
        "currentTeamAbbrev": "EDM",
        "teamLogo": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
    }
    team = ProfileTeam.from_dict(data)
    assert team.id == 22
    assert team.name.default == "Edmonton Oilers"
    assert team.code == "EDM"
    assert "EDM" in team.logo

def test_profile_team_empty() -> None:
    team = ProfileTeam.from_dict({})
    assert team.id is None
    assert team.name.default is None
    assert team.code is None


# ==========================================================================
# AWARD
# ==========================================================================

def test_award_from_dict() -> None:
    data = {
        "trophy": {"default": "Hart Trophy"},
        "seasons": [20232024, 20222023],
    }
    award = Award.from_dict(data)
    assert award.trophy.default == "Hart Trophy"
    assert award.seasons == [20232024, 20222023]

def test_award_empty() -> None:
    award = Award.from_dict({})
    assert award.trophy.default is None
    assert award.seasons == []


# ==========================================================================
# BADGE
# ==========================================================================

def test_badge_from_dict() -> None:
    data = {
        "logoUrl": {"default": "https://assets.nhle.com/badges/top_100.png"},
        "title": {"default": "Top 100 All-Time"},
    }
    badge = Badge.from_dict(data)
    assert badge.logo.default == "https://assets.nhle.com/badges/top_100.png"
    assert badge.title.default == "Top 100 All-Time"

def test_badge_empty() -> None:
    badge = Badge.from_dict({})
    assert badge.logo.default is None
    assert badge.title.default is None


# ==========================================================================
# LEGACY
# ==========================================================================

def test_legacy_from_dict() -> None:
    data = {
        "inTop100AllTime": 1,
        "inHHOF": 0,
        "awards": [
            {"trophy": {"default": "Hart Trophy"}, "seasons": [20232024]},
        ],
        "badges": [
            {"logoUrl": {"default": "https://badges/top100.png"}, "title": {"default": "Top 100"}},
        ],
    }
    legacy = Legacy.from_dict(data)
    assert legacy.in_top_100_all_time is True
    assert legacy.in_HHOF is False
    assert len(legacy.awards) == 1
    assert legacy.awards[0].trophy.default == "Hart Trophy"
    assert len(legacy.badges) == 1
    assert legacy.badges[0].title.default == "Top 100"

def test_legacy_none_flags() -> None:
    """None values for bool flags should remain None."""
    legacy = Legacy.from_dict({})
    assert legacy.in_top_100_all_time is None
    assert legacy.in_HHOF is None
    assert legacy.awards == []
    assert legacy.badges == []

def test_legacy_to_bool_conversion() -> None:
    """1 → True, 0 → False."""
    legacy_true = Legacy.from_dict({"inTop100AllTime": 1, "inHHOF": 0})
    assert legacy_true.in_top_100_all_time is True
    assert legacy_true.in_HHOF is False

    legacy_bool = Legacy.from_dict({"inTop100AllTime": True, "inHHOF": False})
    assert legacy_bool.in_top_100_all_time is True
    assert legacy_bool.in_HHOF is False


# ==========================================================================
# PROFILE (COMPOSITE)
# ==========================================================================

PROFILE_DATA = {
    "playerId": 8478402,
    "firstName": {"default": "Connor"},
    "lastName": {"default": "McDavid"},
    "sweaterNumber": 97,
    "position": "C",
    "currentTeamId": 22,
    "fullTeamName": {"default": "Edmonton Oilers"},
    "currentTeamAbbrev": "EDM",
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
    "shootsCatches": "L",
    "isActive": 1,
    "heightInInches": 73,
    "heightInCentimeters": 185,
    "weightInPounds": 193,
    "weightInKilograms": 88,
    "birthDate": "1997-01-13",
    "birthCity": {"default": "Bradford"},
    "birthStateProvince": {"default": "ON"},
    "birthCountry": "CAN",
    "draftDetails": {"year": 2015, "teamAbbrev": "EDM", "round": 1, "pickInRound": 1, "overallPick": 1},
    "inTop100AllTime": 1,
    "inHHOF": 0,
    "awards": [{"trophy": {"default": "Hart Trophy"}, "seasons": [20232024]}],
    "badges": [],
    "playerSlug": "connor-mcdavid-8478402",
    "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
    "heroImage": "https://assets.nhle.com/heros/nhl/20232024/EDM/8478402.png",
}

def test_profile_from_dict() -> None:
    profile = Profile.from_dict(PROFILE_DATA)
    assert profile.player_id == 8478402
    assert profile.first_name.default == "Connor"
    assert profile.last_name.default == "McDavid"
    assert profile.number == 97
    assert profile.position == "C"
    assert profile.hand == "L"
    assert profile.is_active is True
    assert profile.team.id == 22
    assert profile.team.code == "EDM"
    assert profile.height.height_in == 73
    assert profile.height.height_cm == 185
    assert profile.weight.weight_lbs == 193
    assert profile.birth_details.birth_date == "1997-01-13"
    assert profile.birth_details.country == "CAN"
    assert profile.draft.year == 2015
    assert profile.draft.team == "EDM"
    assert profile.legacy.in_top_100_all_time is True
    assert profile.legacy.in_HHOF is False
    assert len(profile.legacy.awards) == 1
    assert profile.media.slug == "connor-mcdavid-8478402"
