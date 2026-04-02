"""
Tests for TeamShotLocationLeaderEntry model.
"""
from src.models.teams.edge.team_shot_location_10.team_shot_location_10_result import (
    TeamShotLocationLeaderEntry,
)


ENTRY = {
    "team": {
        "id": 16,
        "commonName": {"default": "Blackhawks"},
        "placeNameWithPreposition": {"default": "Chicago", "fr": "de Chicago"},
        "abbrev": "CHI",
        "teamLogo": {
            "light": "https://assets.nhle.com/logos/nhl/svg/CHI_light.svg",
            "dark": "https://assets.nhle.com/logos/nhl/svg/CHI_dark.svg",
        },
        "slug": "chicago-blackhawks-16",
    },
    "all": 0.1044,
    "highDanger": 0.2303,
    "midRange": 0.0996,
    "longRange": 0.0124,
}


def test_entry_from_dict() -> None:
    entry = TeamShotLocationLeaderEntry.from_dict(ENTRY)
    assert isinstance(entry, TeamShotLocationLeaderEntry)


def test_team_fields() -> None:
    entry = TeamShotLocationLeaderEntry.from_dict(ENTRY)
    assert entry.team.id == 16
    assert entry.team.abbrev == "CHI"
    assert entry.team.common_name.default == "Blackhawks"
    assert entry.team.place_name_with_preposition.get_locale("fr") == "de Chicago"
    assert entry.team.slug == "chicago-blackhawks-16"


def test_shot_location_fields() -> None:
    entry = TeamShotLocationLeaderEntry.from_dict(ENTRY)
    assert entry.all == 0.1044
    assert entry.high_danger == 0.2303
    assert entry.mid_range == 0.0996
    assert entry.long_range == 0.0124


def test_to_dict_roundtrip() -> None:
    entry = TeamShotLocationLeaderEntry.from_dict(ENTRY)
    d = entry.to_dict()
    assert d["team"]["abbrev"] == "CHI"
    assert d["all"] == 0.1044
    assert d["high_danger"] == 0.2303
    assert d["mid_range"] == 0.0996
    assert d["long_range"] == 0.0124
