from src.models.players.player.stats.edge.edge_types import (
    LeaderPlayer,
    EdgeLeagueAvg,
    EdgeMeasurement,
    EdgeCount,
    OverlayTeam,
    OverlayGameOutcome,
    OverlayPeriodDescriptor,
    EdgeOverlay,
    EdgeValue,
    EdgePeak,
    EdgeSeason,
)


# ==========================================================================
# EDGE LEAGUE AVG
# ==========================================================================

def test_edge_league_avg_from_dict() -> None:
    data = {"imperial": 1.5, "metric": 2.4, "value": 3.0}
    avg = EdgeLeagueAvg.from_dict(data)
    assert avg.imperial == 1.5
    assert avg.metric == 2.4
    assert avg.value == 3.0

def test_edge_league_avg_empty() -> None:
    avg = EdgeLeagueAvg.from_dict({})
    assert avg.imperial is None
    assert avg.metric is None
    assert avg.value is None


# ==========================================================================
# EDGE COUNT
# ==========================================================================

def test_edge_count_league_avg_as_dict() -> None:
    data = {"value": 12, "percentile": 75.0, "leagueAvg": {"value": 8.5}}
    count = EdgeCount.from_dict(data)
    assert count.value == 12
    assert count.percentile == 75.0
    assert count.league_avg == 8.5

def test_edge_count_league_avg_as_float() -> None:
    data = {"value": 5, "percentile": 50.0, "leagueAvg": 3.385}
    count = EdgeCount.from_dict(data)
    assert count.value == 5
    assert count.percentile == 50.0
    assert count.league_avg == 3.385

def test_edge_count_league_avg_missing() -> None:
    count = EdgeCount.from_dict({"value": 3})
    assert count.league_avg is None

def test_edge_count_to_dict() -> None:
    data = {"value": 7, "percentile": 60.0, "leagueAvg": 4.2}
    count = EdgeCount.from_dict(data)
    d = count.to_dict()
    assert d["value"] == 7
    assert d["percentile"] == 60.0
    assert d["league_avg"] == 4.2


# ==========================================================================
# EDGE VALUE
# ==========================================================================

def test_edge_value_from_dict() -> None:
    data = {"imperial": 12500.0, "metric": 19312.0}
    val = EdgeValue.from_dict(data)
    assert val.imperial == 12500.0
    assert val.metric == 19312.0

def test_edge_value_empty() -> None:
    val = EdgeValue.from_dict({})
    assert val.imperial is None
    assert val.metric is None


# ==========================================================================
# OVERLAY SUPPORTING TYPES
# ==========================================================================

def test_overlay_team_from_dict() -> None:
    team = OverlayTeam.from_dict({"abbrev": "TOR", "score": 4})
    assert team.abbrev == "TOR"
    assert team.score == 4

def test_overlay_game_outcome_from_dict() -> None:
    outcome = OverlayGameOutcome.from_dict({"lastPeriodType": "OT", "otPeriods": 1})
    assert outcome.last_period_type == "OT"
    assert outcome.ot_periods == 1

def test_overlay_game_outcome_regulation() -> None:
    outcome = OverlayGameOutcome.from_dict({"lastPeriodType": "REG"})
    assert outcome.last_period_type == "REG"
    assert outcome.ot_periods is None

def test_overlay_period_descriptor_from_dict() -> None:
    pd = OverlayPeriodDescriptor.from_dict({"number": 2, "periodType": "REG", "maxRegulationPeriods": 3})
    assert pd.number == 2
    assert pd.period_type == "REG"
    assert pd.max_regulation_periods == 3


# ==========================================================================
# EDGE OVERLAY
# ==========================================================================

OVERLAY_DATA = {
    "player": {"firstName": {"default": "Connor"}, "lastName": {"default": "McDavid"}},
    "gameDate": "2024-01-15",
    "awayTeam": {"abbrev": "EDM", "score": 3},
    "homeTeam": {"abbrev": "TOR", "score": 2},
    "gameOutcome": {"lastPeriodType": "REG", "otPeriods": None},
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "timeInPeriod": "08:42",
    "gameType": 2,
}

def test_edge_overlay_from_dict() -> None:
    overlay = EdgeOverlay.from_dict(OVERLAY_DATA)
    assert overlay.first_name.default == "Connor"
    assert overlay.last_name.default == "McDavid"
    assert overlay.game_date == "2024-01-15"
    assert overlay.away_team.abbrev == "EDM"
    assert overlay.home_team.abbrev == "TOR"
    assert overlay.time_in_period == "08:42"
    assert overlay.game_type == 2
    assert overlay.period_descriptor.number == 1

def test_edge_overlay_empty() -> None:
    overlay = EdgeOverlay.from_dict({})
    assert overlay.first_name.default is None
    assert overlay.last_name.default is None
    assert overlay.game_date is None
    assert overlay.away_team.abbrev is None
    assert overlay.home_team.abbrev is None


# ==========================================================================
# EDGE PEAK
# ==========================================================================

def test_edge_peak_no_overlay() -> None:
    data = {"imperial": 24.8, "metric": 39.9}
    peak = EdgePeak.from_dict(data)
    assert peak.imperial == 24.8
    assert peak.metric == 39.9
    assert peak.overlay is None

def test_edge_peak_with_overlay() -> None:
    data = {"imperial": 24.8, "metric": 39.9, "overlay": OVERLAY_DATA}
    peak = EdgePeak.from_dict(data)
    assert peak.overlay is not None
    assert peak.overlay.game_date == "2024-01-15"
    assert peak.overlay.away_team.abbrev == "EDM"

def test_edge_peak_empty_overlay_dict() -> None:
    """An empty overlay dict is falsy — overlay should be None."""
    data = {"imperial": 20.1, "metric": 32.4, "overlay": {}}
    peak = EdgePeak.from_dict(data)
    assert peak.overlay is None


# ==========================================================================
# EDGE MEASUREMENT
# ==========================================================================

def test_edge_measurement_no_overlay() -> None:
    data = {
        "imperial": 10000.0,
        "metric": 16093.4,
        "percentile": 88.5,
        "leagueAvg": {"imperial": 9500.0, "metric": 15288.0},
    }
    m = EdgeMeasurement.from_dict(data)
    assert m.imperial == 10000.0
    assert m.metric == 16093.4
    assert m.percentile == 88.5
    assert m.league_avg.imperial == 9500.0
    assert m.overlay is None

def test_edge_measurement_with_overlay() -> None:
    data = {
        "imperial": 24.8,
        "metric": 39.9,
        "percentile": 95.0,
        "leagueAvg": {"imperial": 20.0, "metric": 32.2},
        "overlay": OVERLAY_DATA,
    }
    m = EdgeMeasurement.from_dict(data)
    assert m.overlay is not None
    assert m.overlay.game_date == "2024-01-15"

def test_edge_measurement_empty() -> None:
    m = EdgeMeasurement.from_dict({})
    assert m.imperial is None
    assert m.metric is None
    assert m.percentile is None
    assert m.league_avg.imperial is None
    assert m.overlay is None


# ==========================================================================
# EDGE SEASON
# ==========================================================================

def test_edge_season_from_dict() -> None:
    season = EdgeSeason.from_dict({"id": 20232024, "gameTypes": [2, 3]})
    assert season.id == 20232024
    assert season.game_types == [2, 3]

def test_edge_season_empty() -> None:
    season = EdgeSeason.from_dict({})
    assert season.id is None
    assert season.game_types == []


# ==========================================================================
# LEADER PLAYER
# ==========================================================================

def test_leader_player_from_dict() -> None:
    data = {
        "firstName": {"default": "Connor"},
        "lastName": {"default": "McDavid"},
        "slug": "connor-mcdavid-8478402",
        "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
        "position": "C",
        "sweaterNumber": 97,
        "team": {"id": 22, "abbrev": "EDM"},
    }
    player = LeaderPlayer.from_dict(data)
    assert player.first_name.default == "Connor"
    assert player.last_name.default == "McDavid"
    assert player.slug == "connor-mcdavid-8478402"
    assert player.position == "C"
    assert player.sweater_number == 97
    assert player.team == {"id": 22, "abbrev": "EDM"}

def test_leader_player_empty() -> None:
    player = LeaderPlayer.from_dict({})
    assert player.first_name.default is None
    assert player.last_name.default is None
    assert player.slug is None
    assert player.sweater_number is None
    assert player.team is None

def test_leader_player_to_dict() -> None:
    data = {
        "firstName": {"default": "Sidney"},
        "lastName": {"default": "Crosby"},
        "slug": "sidney-crosby-8471675",
        "headshot": None,
        "position": "C",
        "sweaterNumber": 87,
        "team": {"id": 5, "abbrev": "PIT"},
    }
    player = LeaderPlayer.from_dict(data)
    d = player.to_dict()
    assert d["first_name"] == "Sidney"
    assert d["last_name"] == "Crosby"
    assert d["sweater_number"] == 87
