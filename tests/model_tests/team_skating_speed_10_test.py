"""
Tests for TeamSpeedLeaderEntry model.
"""
from nhl_stats.models.teams.edge.team_skating_speed_10.team_skating_speed_10_result import (
    TeamSpeedLeaderEntry,
)
from nhl_stats.models.players.player.player_stats.edge.player_edge_types import EdgePeak, EdgeOverlay


ENTRY = {
    "team": {
        "id": 7,
        "commonName": {"default": "Sabres"},
        "placeNameWithPreposition": {"default": "Buffalo", "fr": "de Buffalo"},
        "abbrev": "BUF",
        "teamLogo": {
            "light": "https://assets.nhle.com/logos/nhl/svg/BUF_light.svg",
            "dark": "https://assets.nhle.com/logos/nhl/svg/BUF_dark.svg",
        },
        "slug": "buffalo-sabres-7",
    },
    "maxSkatingSpeed": {
        "imperial": 24.9389,
        "metric": 40.1352,
        "overlay": {
            "player": {
                "firstName": {"default": "Beck"},
                "lastName": {"default": "Malenstyn"},
            },
            "gameDate": "2026-03-12",
            "awayTeam": {"abbrev": "WSH", "score": 2},
            "homeTeam": {"abbrev": "BUF", "score": 1},
            "gameOutcome": {"lastPeriodType": "REG"},
            "periodDescriptor": {"maxRegulationPeriods": 3, "number": 3, "periodType": "REG"},
            "timeInPeriod": "12:05",
            "gameType": 2,
        },
    },
    "burstsOver22": 79,
    "bursts20To22": 1607,
    "bursts18To20": 6398,
}


def test_entry_from_dict() -> None:
    entry = TeamSpeedLeaderEntry.from_dict(ENTRY)
    assert isinstance(entry, TeamSpeedLeaderEntry)


def test_team_fields() -> None:
    entry = TeamSpeedLeaderEntry.from_dict(ENTRY)
    assert entry.team.id == 7
    assert entry.team.abbrev == "BUF"
    assert entry.team.common_name.default == "Sabres"
    assert entry.team.place_name_with_preposition.get_locale("fr") == "de Buffalo"
    assert entry.team.slug == "buffalo-sabres-7"


def test_max_skating_speed_peak() -> None:
    entry = TeamSpeedLeaderEntry.from_dict(ENTRY)
    peak = entry.max_skating_speed
    assert isinstance(peak, EdgePeak)
    assert peak.imperial == 24.9389
    assert peak.metric == 40.1352
    assert isinstance(peak.overlay, EdgeOverlay)


def test_max_skating_speed_overlay() -> None:
    entry = TeamSpeedLeaderEntry.from_dict(ENTRY)
    overlay = entry.max_skating_speed.overlay
    assert overlay.first_name.default == "Beck"
    assert overlay.last_name.default == "Malenstyn"
    assert overlay.game_date == "2026-03-12"
    assert overlay.away_team.abbrev == "WSH"
    assert overlay.away_team.score == 2
    assert overlay.home_team.abbrev == "BUF"
    assert overlay.game_outcome.last_period_type == "REG"
    assert overlay.period_descriptor.number == 3
    assert overlay.time_in_period == "12:05"
    assert overlay.game_type == 2


def test_burst_counts() -> None:
    entry = TeamSpeedLeaderEntry.from_dict(ENTRY)
    assert entry.bursts_over_22 == 79
    assert entry.bursts_20_to_22 == 1607
    assert entry.bursts_18_to_20 == 6398


def test_ot_periods_in_overlay() -> None:
    data = {**ENTRY, "maxSkatingSpeed": {
        "imperial": 24.6119,
        "metric": 39.6089,
        "overlay": {
            "player": {"firstName": {"default": "Connor"}, "lastName": {"default": "McDavid"}},
            "gameDate": "2025-10-08",
            "awayTeam": {"abbrev": "CGY", "score": 4},
            "homeTeam": {"abbrev": "EDM", "score": 3},
            "gameOutcome": {"lastPeriodType": "SO"},
            "periodDescriptor": {"maxRegulationPeriods": 3, "number": 2, "periodType": "REG"},
            "timeInPeriod": "08:04",
            "gameType": 2,
        },
    }}
    entry = TeamSpeedLeaderEntry.from_dict(data)
    assert entry.max_skating_speed.overlay.game_outcome.last_period_type == "SO"
    assert entry.max_skating_speed.overlay.game_outcome.ot_periods is None


def test_to_dict_roundtrip() -> None:
    entry = TeamSpeedLeaderEntry.from_dict(ENTRY)
    d = entry.to_dict()
    assert d["team"]["abbrev"] == "BUF"
    assert d["max_skating_speed"]["imperial"] == 24.9389
    assert d["bursts_over_22"] == 79
    assert d["bursts_20_to_22"] == 1607
    assert d["bursts_18_to_20"] == 6398
