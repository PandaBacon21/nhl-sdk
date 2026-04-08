"""
Tests for TeamDistanceLeaderEntry model.
"""
from nhl_stats.models.teams.edge.team_skating_distance_10.team_skating_distance_10_result import (
    TeamDistanceLeaderEntry,
)
from nhl_stats.models.teams.edge.team_edge_types import TeamEdgePeak, TeamEdgeOverlay


ENTRY = {
    "team": {
        "commonName": {"default": "Kings"},
        "placeNameWithPreposition": {"default": "Los Angeles"},
        "abbrev": "LAK",
        "teamLogo": {
            "light": "https://assets.nhle.com/logos/nhl/svg/LAK_light.svg",
            "dark": "https://assets.nhle.com/logos/nhl/svg/LAK_dark.svg",
        },
        "slug": "los-angeles-kings-26",
    },
    "distanceTotal": {"imperial": 2127.7906, "metric": 3424.1799},
    "distancePer60": {"imperial": 9.5190, "metric": 15.3186},
    "distanceMaxPerGame": {
        "imperial": 32.8591,
        "metric": 52.8790,
        "overlay": {
            "gameDate": "2026-03-24",
            "awayTeam": {"abbrev": "LAK", "score": 2},
            "homeTeam": {"abbrev": "CGY", "score": 3},
            "gameOutcome": {"lastPeriodType": "SO"},
            "periodDescriptor": {"maxRegulationPeriods": 3, "number": 3, "periodType": "REG"},
            "gameType": 2,
        },
    },
    "distanceMaxPerPeriod": {
        "imperial": 11.4081,
        "metric": 18.3587,
        "overlay": {
            "gameDate": "2025-11-17",
            "awayTeam": {"abbrev": "LAK", "score": 1},
            "homeTeam": {"abbrev": "WSH", "score": 2},
            "gameOutcome": {"lastPeriodType": "REG"},
            "periodDescriptor": {"maxRegulationPeriods": 3, "number": 3, "periodType": "REG"},
            "gameType": 2,
        },
    },
}


def test_entry_from_dict() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    assert isinstance(entry, TeamDistanceLeaderEntry)


def test_team_fields() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    assert entry.team.abbrev == "LAK"
    assert entry.team.common_name.default == "Kings"
    assert entry.team.place_name_with_preposition.default == "Los Angeles"
    assert entry.team.slug == "los-angeles-kings-26"
    assert entry.team.logo_light == "https://assets.nhle.com/logos/nhl/svg/LAK_light.svg"
    assert entry.team.logo_dark == "https://assets.nhle.com/logos/nhl/svg/LAK_dark.svg"
    # top-10 team ref has no id or record fields
    assert entry.team.id is None
    assert entry.team.wins is None


def test_distance_total() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    assert entry.distance_total.imperial == 2127.7906
    assert entry.distance_total.metric == 3424.1799


def test_distance_per_60() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    assert entry.distance_per_60.imperial == 9.5190
    assert entry.distance_per_60.metric == 15.3186


def test_distance_max_per_game_peak() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    peak = entry.distance_max_per_game
    assert isinstance(peak, TeamEdgePeak)
    assert peak.imperial == 32.8591
    assert peak.metric == 52.8790
    assert isinstance(peak.overlay, TeamEdgeOverlay)


def test_distance_max_per_game_overlay() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    overlay = entry.distance_max_per_game.overlay
    assert overlay.game_date == "2026-03-24"
    assert overlay.away_team.abbrev == "LAK"
    assert overlay.away_team.score == 2
    assert overlay.home_team.abbrev == "CGY"
    assert overlay.home_team.score == 3
    assert overlay.game_outcome.last_period_type == "SO"
    assert overlay.game_outcome.ot_periods is None
    assert overlay.period_descriptor.number == 3
    assert overlay.period_descriptor.period_type == "REG"
    assert overlay.period_descriptor.max_regulation_periods == 3
    assert overlay.game_type == 2


def test_distance_max_per_period_overlay() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    overlay = entry.distance_max_per_period.overlay
    assert overlay.game_date == "2025-11-17"
    assert overlay.away_team.abbrev == "LAK"
    assert overlay.home_team.abbrev == "WSH"
    assert overlay.game_outcome.last_period_type == "REG"


def test_ot_periods_in_overlay() -> None:
    data = {**ENTRY, "distanceMaxPerGame": {
        "imperial": 30.0,
        "metric": 48.0,
        "overlay": {
            "gameDate": "2026-01-03",
            "awayTeam": {"abbrev": "TOR", "score": 3},
            "homeTeam": {"abbrev": "NYI", "score": 4},
            "gameOutcome": {"lastPeriodType": "OT", "otPeriods": 1},
            "periodDescriptor": {"maxRegulationPeriods": 3, "number": 3, "periodType": "REG"},
            "gameType": 2,
        },
    }}
    entry = TeamDistanceLeaderEntry.from_dict(data)
    assert entry.distance_max_per_game.overlay.game_outcome.ot_periods == 1


def test_no_overlay() -> None:
    data = {**ENTRY, "distanceMaxPerGame": {"imperial": 30.0, "metric": 48.0}}
    entry = TeamDistanceLeaderEntry.from_dict(data)
    assert entry.distance_max_per_game.overlay is None


def test_to_dict_roundtrip() -> None:
    entry = TeamDistanceLeaderEntry.from_dict(ENTRY)
    d = entry.to_dict()
    assert d["team"]["abbrev"] == "LAK"
    assert d["distance_total"]["imperial"] == 2127.7906
    assert d["distance_max_per_game"]["overlay"]["game_date"] == "2026-03-24"
