"""
Tests for TeamZoneTimeLeaderEntry model.
"""
from src.models.teams.edge.team_zone_time_10.team_zone_time_10_result import (
    TeamZoneTimeLeaderEntry,
)


ENTRY = {
    "team": {
        "commonName": {"default": "Hurricanes"},
        "placeNameWithPreposition": {"default": "Carolina", "fr": "de la Caroline"},
        "abbrev": "CAR",
        "teamLogo": {
            "light": "https://assets.nhle.com/logos/nhl/svg/CAR_light.svg",
            "dark": "https://assets.nhle.com/logos/nhl/svg/CAR_dark.svg",
        },
        "slug": "carolina-hurricanes-12",
    },
    "offensiveZoneTime": 0.4563367,
    "neutralZoneTime": 0.1829148,
    "defensiveZoneTime": 0.3607485,
}


def test_entry_from_dict() -> None:
    entry = TeamZoneTimeLeaderEntry.from_dict(ENTRY)
    assert isinstance(entry, TeamZoneTimeLeaderEntry)


def test_team_fields() -> None:
    entry = TeamZoneTimeLeaderEntry.from_dict(ENTRY)
    assert entry.team.abbrev == "CAR"
    assert entry.team.common_name.default == "Hurricanes"
    assert entry.team.place_name_with_preposition.default == "Carolina"
    assert entry.team.place_name_with_preposition.get_locale("fr") == "de la Caroline"
    assert entry.team.slug == "carolina-hurricanes-12"
    assert entry.team.id is None


def test_zone_time_fields() -> None:
    entry = TeamZoneTimeLeaderEntry.from_dict(ENTRY)
    assert entry.offensive_zone_time == 0.4563367
    assert entry.neutral_zone_time == 0.1829148
    assert entry.defensive_zone_time == 0.3607485


def test_to_dict_roundtrip() -> None:
    entry = TeamZoneTimeLeaderEntry.from_dict(ENTRY)
    d = entry.to_dict()
    assert d["team"]["abbrev"] == "CAR"
    assert d["offensive_zone_time"] == 0.4563367
    assert d["neutral_zone_time"] == 0.1829148
    assert d["defensive_zone_time"] == 0.3607485
