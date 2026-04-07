from src.core.utilities import BirthDetails, LocalizedString
from src.models.players.player.profile.draft import Draft
from src.models.players.player.profile.media import Media
from src.models.players.player.profile.profile_team import ProfileTeam
from src.models.players.player.profile.award import Award
from src.models.players.player.profile.badge import Badge
from src.models.players.player.profile.legacy import Legacy
from src.models.players.player.profile.profile import Profile


# ==========================================================================
# LOCALIZED STRING
# ==========================================================================

def test_localized_string_repr() -> None:
    ls = LocalizedString({"default": "Nathan"})
    assert repr(ls) == "LocalizedString(default='Nathan')"

def test_localized_string_repr_none() -> None:
    ls = LocalizedString(None)
    assert repr(ls) == "LocalizedString(default=None)"

def test_localized_string_eq_str() -> None:
    ls = LocalizedString({"default": "Nathan"})
    assert ls == "Nathan"
    assert ls != "Other"

def test_localized_string_eq_localized_string() -> None:
    a = LocalizedString({"default": "Nathan"})
    b = LocalizedString({"default": "Nathan"})
    c = LocalizedString({"default": "Cale"})
    assert a == b
    assert a != c

def test_localized_string_eq_other_type() -> None:
    ls = LocalizedString({"default": "Nathan"})
    assert ls != 42
    assert ls != None  # noqa: E711

def test_localized_string_get_locale_no_fallback() -> None:
    ls = LocalizedString({"default": "Colorado", "fr": "du Colorado"})
    assert ls.get_locale("fr") == "du Colorado"
    assert ls.get_locale("es", fallback=False) is None
    assert ls.get_locale("es", fallback=True) == "Colorado"

def test_localized_string_locales_with_multiple() -> None:
    ls = LocalizedString({"default": "Colorado", "fr": "du Colorado"})
    assert ls.locales == {"fr"}

def test_localized_string_locales_default_only() -> None:
    ls = LocalizedString({"default": "Colorado"})
    assert ls.locales == {"default"}


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
    assert legacy.in_hhof is False
    assert len(legacy.awards) == 1
    assert legacy.awards[0].trophy.default == "Hart Trophy"
    assert len(legacy.badges) == 1
    assert legacy.badges[0].title.default == "Top 100"

def test_legacy_none_flags() -> None:
    """None values for bool flags should remain None."""
    legacy = Legacy.from_dict({})
    assert legacy.in_top_100_all_time is None
    assert legacy.in_hhof is None
    assert legacy.awards == []
    assert legacy.badges == []

def test_legacy_to_bool_conversion() -> None:
    """1 → True, 0 → False."""
    legacy_true = Legacy.from_dict({"inTop100AllTime": 1, "inHHOF": 0})
    assert legacy_true.in_top_100_all_time is True
    assert legacy_true.in_hhof is False

    legacy_bool = Legacy.from_dict({"inTop100AllTime": True, "inHHOF": False})
    assert legacy_bool.in_top_100_all_time is True
    assert legacy_bool.in_hhof is False


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
    assert profile.height_in_inches == 73
    assert profile.height_in_centimeters == 185
    assert profile.weight_in_pounds == 193
    assert profile.weight_in_kilograms == 88
    assert profile.birth_details.birth_date == "1997-01-13"
    assert profile.birth_details.country == "CAN"
    assert profile.draft.year == 2015
    assert profile.draft.team == "EDM"
    assert profile.media.slug == "connor-mcdavid-8478402"
