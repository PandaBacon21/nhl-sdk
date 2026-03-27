from src.models.players.player.player_stats.edge.skaters.skater_details import (
    SkatingSpeed,
    SogSummary,
    SogDetail,
    ZoneTimeDetails,
    SkaterDetails,
)
from src.models.players.leaders.edge.skaters.skater_distance_10 import (
    DistanceLeaderEntry,
    SkaterDistanceTop10,
)
from src.models.players.leaders.edge.skaters.skater_speed_10 import (
    SpeedLeaderEntry,
    SkaterSpeedTop10,
)
from src.models.players.leaders.edge.skaters.skater_zone_time_10 import (
    ZoneTimeLeaderEntry,
    SkaterZoneTimeTop10,
)
from src.models.players.leaders.edge.skaters.skater_shot_speed_10 import (
    ShotSpeedLeaderEntry,
    SkaterShotSpeedTop10,
)
from src.models.players.leaders.edge.skaters.skater_shot_location_10 import (
    ShotLocationLeaderEntry,
    SkaterShotLocationTop10,
)


PLAYER_DATA = {
    "firstName": {"default": "Connor"},
    "lastName": {"default": "McDavid"},
    "slug": "connor-mcdavid-8478402",
    "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
    "position": "C",
    "sweaterNumber": 97,
    "team": {"id": 22, "abbrev": "EDM"},
}

OVERLAY_DATA = {
    "player": {"firstName": {"default": "Connor"}, "lastName": {"default": "McDavid"}},
    "gameDate": "2024-01-15",
    "awayTeam": {"abbrev": "EDM", "score": 3},
    "homeTeam": {"abbrev": "TOR", "score": 2},
    "gameOutcome": {"lastPeriodType": "REG"},
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "timeInPeriod": "08:42",
    "gameType": 2,
}


# ==========================================================================
# SKATER DETAILS COMPONENTS
# ==========================================================================

def test_skating_speed_from_dict() -> None:
    data = {
        "speedMax": {
            "imperial": 24.8, "metric": 39.9, "percentile": 95.0,
            "leagueAvg": {"imperial": 20.0, "metric": 32.2},
        },
        "burstsOver20": {"value": 12, "percentile": 80.0, "leagueAvg": {"value": 7.0}},
    }
    speed = SkatingSpeed.from_dict(data)
    assert speed.speed_max.imperial == 24.8
    assert speed.speed_max.percentile == 95.0
    assert speed.bursts_over_20.value == 12
    assert speed.bursts_over_20.league_avg == 7.0

def test_skating_speed_empty() -> None:
    speed = SkatingSpeed.from_dict({})
    assert speed.speed_max.imperial is None
    assert speed.bursts_over_20.value is None

def test_sog_summary_from_dict() -> None:
    data = {
        "locationCode": "HD",
        "shots": 45, "shotsPercentile": 82.0, "shotsLeagueAvg": 30.0,
        "goals": 10, "goalsPercentile": 90.0, "goalsLeagueAvg": 6.5,
        "shootingPctg": 0.222, "shootingPctgPercentile": 75.0, "shootingPctgLeagueAvg": 0.180,
    }
    sog = SogSummary.from_dict(data)
    assert sog.location_code == "HD"
    assert sog.shots == 45
    assert sog.goals == 10
    assert sog.shooting_pctg == 0.222
    assert sog.goals_league_avg == 6.5

def test_sog_detail_from_dict() -> None:
    data = {"area": "slot", "shots": 18, "shotsPercentile": 70.0}
    detail = SogDetail.from_dict(data)
    assert detail.area == "slot"
    assert detail.shots == 18
    assert detail.shots_percentile == 70.0

def test_zone_time_details_from_dict() -> None:
    data = {
        "offensiveZonePctg": 0.38, "offensiveZonePercentile": 85.0, "offensiveZoneLeagueAvg": 0.34,
        "offensiveZoneEvPctg": 0.36, "offensiveZoneEvPercentile": 80.0, "offensiveZoneEvLeagueAvg": 0.33,
        "neutralZonePctg": 0.30, "neutralZonePercentile": 50.0, "neutralZoneLeagueAvg": 0.31,
        "defensiveZonePctg": 0.32, "defensiveZonePercentile": 40.0, "defensiveZoneLeagueAvg": 0.35,
    }
    zt = ZoneTimeDetails.from_dict(data)
    assert zt.offensive_zone_pctg == 0.38
    assert zt.offensive_zone_ev_percentile == 80.0
    assert zt.neutral_zone_league_avg == 0.31
    assert zt.defensive_zone_pctg == 0.32

def test_zone_time_details_empty() -> None:
    zt = ZoneTimeDetails.from_dict({})
    assert zt.offensive_zone_pctg is None
    assert zt.defensive_zone_league_avg is None


# ==========================================================================
# SKATER DETAILS (COMPOSITE)
# ==========================================================================

SKATER_DETAILS_DATA = {
    "seasonsWithEdgeStats": [{"id": 20232024, "gameTypes": [2]}],
    "topShotSpeed": {
        "imperial": 96.0, "metric": 154.5, "percentile": 90.0,
        "leagueAvg": {"imperial": 85.0, "metric": 136.8},
    },
    "skatingSpeed": {
        "speedMax": {"imperial": 24.8, "metric": 39.9, "percentile": 95.0, "leagueAvg": {"imperial": 20.0, "metric": 32.2}},
        "burstsOver20": {"value": 12, "percentile": 80.0, "leagueAvg": {"value": 7.0}},
    },
    "totalDistanceSkated": {
        "imperial": 12500.0, "metric": 20117.0, "percentile": 88.0,
        "leagueAvg": {"imperial": 11000.0, "metric": 17703.0},
    },
    "distanceMaxGame": {
        "imperial": 3200.0, "metric": 5150.0, "percentile": 70.0,
        "leagueAvg": {"imperial": 2900.0, "metric": 4667.0},
    },
    "sogSummary": [
        {"locationCode": "all", "shots": 180, "shotsPercentile": 92.0, "shotsLeagueAvg": 130.0,
         "goals": 60, "goalsPercentile": 95.0, "goalsLeagueAvg": 25.0,
         "shootingPctg": 0.333, "shootingPctgPercentile": 90.0, "shootingPctgLeagueAvg": 0.190},
    ],
    "sogDetails": [
        {"area": "slot", "shots": 80, "shotsPercentile": 88.0},
    ],
    "zoneTimeDetails": {
        "offensiveZonePctg": 0.38, "offensiveZonePercentile": 85.0, "offensiveZoneLeagueAvg": 0.34,
        "offensiveZoneEvPctg": 0.36, "offensiveZoneEvPercentile": 80.0, "offensiveZoneEvLeagueAvg": 0.33,
        "neutralZonePctg": 0.30, "neutralZonePercentile": 50.0, "neutralZoneLeagueAvg": 0.31,
        "defensiveZonePctg": 0.32, "defensiveZonePercentile": 40.0, "defensiveZoneLeagueAvg": 0.35,
    },
}

def test_skater_details_from_dict() -> None:
    details = SkaterDetails.from_dict(SKATER_DETAILS_DATA)
    assert len(details.seasons_with_edge) == 1
    assert details.seasons_with_edge[0].id == 20232024
    assert details.top_shot_speed.imperial == 96.0
    assert details.skating_speed.bursts_over_20.value == 12
    assert details.total_distance_skated.percentile == 88.0
    assert details.distance_max_game.imperial == 3200.0
    assert len(details.sog_summary) == 1
    assert details.sog_summary[0].location_code == "all"
    assert len(details.sog_details) == 1
    assert details.sog_details[0].area == "slot"
    assert details.zone_time.offensive_zone_pctg == 0.38

def test_skater_details_empty() -> None:
    details = SkaterDetails.from_dict({})
    assert details.seasons_with_edge == []
    assert details.top_shot_speed.imperial is None
    assert details.sog_summary == []
    assert details.sog_details == []
    assert details.zone_time.offensive_zone_pctg is None

def test_skater_details_to_dict() -> None:
    details = SkaterDetails.from_dict(SKATER_DETAILS_DATA)
    d = details.to_dict()
    assert isinstance(d["seasons_with_edge"], list)
    assert d["seasons_with_edge"][0]["id"] == 20232024
    assert d["top_shot_speed"]["imperial"] == 96.0
    assert len(d["sog_summary"]) == 1
    assert d["zone_time"]["offensive_zone_pctg"] == 0.38


# ==========================================================================
# DISTANCE TOP 10
# ==========================================================================

DISTANCE_ENTRY = {
    "player": PLAYER_DATA,
    "distanceTotal": {"imperial": 185000.0, "metric": 297720.0},
    "distancePer60": {"imperial": 3500.0, "metric": 5632.7},
    "distanceMaxPerGame": {"imperial": 3200.0, "metric": 5150.0, "overlay": OVERLAY_DATA},
    "distanceMaxPerPeriod": {"imperial": 1100.0, "metric": 1770.0},
}

def test_distance_leader_entry_from_dict() -> None:
    entry = DistanceLeaderEntry.from_dict(DISTANCE_ENTRY)
    assert entry.player.first_name.default == "Connor"
    assert entry.distance_total.imperial == 185000.0
    assert entry.distance_per_60.metric == 5632.7
    assert entry.distance_max_per_game.overlay is not None
    assert entry.distance_max_per_game.overlay.game_date == "2024-01-15"
    assert entry.distance_max_per_period.overlay is None

def test_skater_distance_top10_from_list() -> None:
    top10 = SkaterDistanceTop10.from_list([DISTANCE_ENTRY, DISTANCE_ENTRY])
    assert len(top10.entries) == 2
    assert top10.entries[0].player.sweater_number == 97

def test_skater_distance_top10_empty_list() -> None:
    top10 = SkaterDistanceTop10.from_list([])
    assert top10.entries == []


# ==========================================================================
# SPEED TOP 10
# ==========================================================================

SPEED_ENTRY = {
    "player": PLAYER_DATA,
    "maxSpeed": {"imperial": 24.8, "metric": 39.9, "overlay": OVERLAY_DATA},
    "burstsOver22": 3,
    "bursts20To22": 18,
    "bursts18To20": 42,
}

def test_speed_leader_entry_from_dict() -> None:
    entry = SpeedLeaderEntry.from_dict(SPEED_ENTRY)
    assert entry.player.last_name.default == "McDavid"
    assert entry.max_speed.imperial == 24.8
    assert entry.max_speed.overlay
    assert entry.max_speed.overlay.away_team.abbrev == "EDM"
    assert entry.bursts_over_22 == 3
    assert entry.bursts_20_22 == 18
    assert entry.bursts_18_20 == 42

def test_skater_speed_top10_from_list() -> None:
    top10 = SkaterSpeedTop10.from_list([SPEED_ENTRY])
    assert len(top10.entries) == 1
    assert top10.entries[0].bursts_over_22 == 3


# ==========================================================================
# ZONE TIME TOP 10
# ==========================================================================

ZONE_TIME_ENTRY = {
    "player": PLAYER_DATA,
    "offensiveZoneTime": 38.2,
    "neutralZoneTime": 30.1,
    "defensiveZoneTime": 31.7,
}

def test_zone_time_leader_entry_from_dict() -> None:
    entry = ZoneTimeLeaderEntry.from_dict(ZONE_TIME_ENTRY)
    assert entry.player.position == "C"
    assert entry.offensive_zone_time == 38.2
    assert entry.neutral_zone_time == 30.1
    assert entry.defensive_zone_time == 31.7

def test_skater_zone_time_top10_from_list() -> None:
    top10 = SkaterZoneTimeTop10.from_list([ZONE_TIME_ENTRY, ZONE_TIME_ENTRY])
    assert len(top10.entries) == 2


# ==========================================================================
# SHOT SPEED TOP 10
# ==========================================================================

SHOT_SPEED_ENTRY = {
    "player": PLAYER_DATA,
    "hardestShot": {"imperial": 96.2, "metric": 154.8, "overlay": OVERLAY_DATA},
    "shotAttemptsOver100": 2,
    "shotAttempts90To100": 8,
    "shotAttempts80To90": 25,
    "shotAttempts70To80": 50,
}

def test_shot_speed_leader_entry_from_dict() -> None:
    entry = ShotSpeedLeaderEntry.from_dict(SHOT_SPEED_ENTRY)
    assert entry.player.sweater_number == 97
    assert entry.hardest_shot.imperial == 96.2
    assert entry.hardest_shot.overlay
    assert entry.hardest_shot.overlay.game_date == "2024-01-15"
    assert entry.shot_attempts_over_100 == 2
    assert entry.shot_attempts_90_100 == 8
    assert entry.shot_attempts_80_90 == 25
    assert entry.shot_attempts_70_80 == 50

def test_skater_shot_speed_top10_from_list() -> None:
    top10 = SkaterShotSpeedTop10.from_list([SHOT_SPEED_ENTRY])
    assert len(top10.entries) == 1
    assert top10.entries[0].shot_attempts_over_100 == 2


# ==========================================================================
# SHOT LOCATION TOP 10
# ==========================================================================

SHOT_LOCATION_ENTRY = {
    "player": PLAYER_DATA,
    "all": 220,
    "highDanger": 85,
    "midRange": 95,
    "longRange": 40,
}

def test_shot_location_leader_entry_from_dict() -> None:
    entry = ShotLocationLeaderEntry.from_dict(SHOT_LOCATION_ENTRY)
    assert entry.player.slug == "connor-mcdavid-8478402"
    assert entry.all == 220
    assert entry.high_danger == 85
    assert entry.mid_range == 95
    assert entry.long_range == 40

def test_shot_location_leader_entry_missing_fields() -> None:
    entry = ShotLocationLeaderEntry.from_dict({"player": PLAYER_DATA})
    assert entry.all is None
    assert entry.high_danger is None

def test_skater_shot_location_top10_from_list() -> None:
    top10 = SkaterShotLocationTop10.from_list([SHOT_LOCATION_ENTRY, SHOT_LOCATION_ENTRY])
    assert len(top10.entries) == 2
    assert top10.entries[1].high_danger == 85
