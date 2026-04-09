"""
Tests for TeamShotSpeedLeaderEntry model.
"""
from nhl_sdk.models.teams.edge.team_shot_speed_10.team_shot_speed_10_result import (
    TeamShotSpeedLeaderEntry,
)
from nhl_sdk.models.players.player.player_stats.edge.player_edge_types import EdgePeak, EdgeOverlay


ENTRY = {
    "team": {
        "commonName": {"default": "Blackhawks"},
        "placeNameWithPreposition": {"default": "Chicago", "fr": "de Chicago"},
        "abbrev": "CHI",
        "teamLogo": {
            "light": "https://assets.nhle.com/logos/nhl/svg/CHI_light.svg",
            "dark": "https://assets.nhle.com/logos/nhl/svg/CHI_dark.svg",
        },
        "slug": "chicago-blackhawks-16",
    },
    "hardestShot": {
        "imperial": 102.83,
        "metric": 165.4888,
        "overlay": {
            "player": {
                "firstName": {"default": "Louis"},
                "lastName": {"default": "Crevier"},
            },
            "gameDate": "2026-02-28",
            "awayTeam": {"abbrev": "CHI", "score": 1},
            "homeTeam": {"abbrev": "COL", "score": 3},
            "gameOutcome": {"lastPeriodType": "REG"},
            "periodDescriptor": {"maxRegulationPeriods": 3, "number": 1, "periodType": "REG"},
            "timeInPeriod": "03:19",
            "gameType": 2,
        },
    },
    "shotAttemptsOver100": 6,
    "shotAttempts90To100": 53,
    "shotAttempts80To90": 360,
    "shotAttempts70To80": 933,
}


def test_entry_from_dict() -> None:
    entry = TeamShotSpeedLeaderEntry.from_dict(ENTRY)
    assert isinstance(entry, TeamShotSpeedLeaderEntry)


def test_team_fields() -> None:
    entry = TeamShotSpeedLeaderEntry.from_dict(ENTRY)
    assert entry.team.abbrev == "CHI"
    assert entry.team.common_name.default == "Blackhawks"
    assert entry.team.place_name_with_preposition.get_locale("fr") == "de Chicago"
    assert entry.team.slug == "chicago-blackhawks-16"
    assert entry.team.id is None


def test_hardest_shot_peak() -> None:
    entry = TeamShotSpeedLeaderEntry.from_dict(ENTRY)
    peak = entry.hardest_shot
    assert isinstance(peak, EdgePeak)
    assert peak.imperial == 102.83
    assert peak.metric == 165.4888
    assert isinstance(peak.overlay, EdgeOverlay)


def test_hardest_shot_overlay() -> None:
    entry = TeamShotSpeedLeaderEntry.from_dict(ENTRY)
    overlay = entry.hardest_shot.overlay
    assert overlay.first_name.default == "Louis"
    assert overlay.last_name.default == "Crevier"
    assert overlay.game_date == "2026-02-28"
    assert overlay.away_team.abbrev == "CHI"
    assert overlay.away_team.score == 1
    assert overlay.home_team.abbrev == "COL"
    assert overlay.game_outcome.last_period_type == "REG"
    assert overlay.period_descriptor.number == 1
    assert overlay.time_in_period == "03:19"
    assert overlay.game_type == 2


def test_shot_attempt_counts() -> None:
    entry = TeamShotSpeedLeaderEntry.from_dict(ENTRY)
    assert entry.shot_attempts_over_100 == 6
    assert entry.shot_attempts_90_to_100 == 53
    assert entry.shot_attempts_80_to_90 == 360
    assert entry.shot_attempts_70_to_80 == 933


def test_no_overlay() -> None:
    data = {**ENTRY, "hardestShot": {"imperial": 99.5, "metric": 160.1}}
    entry = TeamShotSpeedLeaderEntry.from_dict(data)
    assert entry.hardest_shot.imperial == 99.5
    assert entry.hardest_shot.overlay is None


def test_to_dict_roundtrip() -> None:
    entry = TeamShotSpeedLeaderEntry.from_dict(ENTRY)
    d = entry.to_dict()
    assert d["team"]["abbrev"] == "CHI"
    assert d["hardest_shot"]["imperial"] == 102.83
    assert d["shot_attempts_over_100"] == 6
    assert d["shot_attempts_90_to_100"] == 53
    assert d["shot_attempts_80_to_90"] == 360
    assert d["shot_attempts_70_to_80"] == 933
