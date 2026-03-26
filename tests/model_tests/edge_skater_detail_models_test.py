"""
Tests for the per-player NHL Edge detail models:
  skating_distance, skating_speed, zone_time, shot_speed, shot_location, cat_skater_details
"""
from src.models.players.player.player_stats.edge.skaters.skating_distance import (
    SkatingDistanceGame,
    SkatingDistanceStrength,
    SkatingDistance,
)
from src.models.players.player.player_stats.edge.skaters.skating_speed import (
    SkatingSpeedGame,
    SkatingSpeedSummary,
    SkatingSpeed,
)
from src.models.players.player.player_stats.edge.skaters.skater_zone_time import (
    ZoneTimeStrength,
    ZoneStartsDetail,
    ZoneTime,
)
from src.models.players.player.player_stats.edge.skaters.shot_speed import (
    ShotSpeedGame,
    ShotSpeedSummary,
    ShotSpeed,
)
from src.models.players.player.player_stats.edge.skaters.shot_location import (
    ShotAreaDetail,
    ShotZoneTotal,
    ShotLocation,
)
from src.models.players.player.player_stats.edge.skaters.cat_skater_details import (
    CatPlayerSummary,
    CatSkaterDetails,
)


# ==========================================================================
# SKATING DISTANCE
# ==========================================================================

DISTANCE_GAME_DATA = {
    "gameCenterLink": "/game/2023020001/boxscore",
    "gameDate": "2024-01-10",
    "playerOnHomeTeam": True,
    "distanceSkatedAll": {"imperial": 3200.0, "metric": 5150.0},
    "toiAll": 1380,
    "distanceSkatedEven": {"imperial": 2800.0, "metric": 4506.0},
    "toiEven": 1050,
    "distanceSkatedPP": {"imperial": 280.0, "metric": 450.8},
    "toiPP": 180,
    "distanceSkatedPK": {"imperial": 120.0, "metric": 193.1},
    "toiPK": 90,
    "homeTeam": {"id": 22, "abbrev": "EDM"},
    "awayTeam": {"id": 5, "abbrev": "PIT"},
}

def test_skating_distance_game_from_dict() -> None:
    game = SkatingDistanceGame.from_dict(DISTANCE_GAME_DATA)
    assert game.game_center_link == "/game/2023020001/boxscore"
    assert game.game_date == "2024-01-10"
    assert game.player_on_home_team is True
    assert game.distance_skated_all.imperial == 3200.0
    assert game.toi_all == 1380
    assert game.distance_skated_even.metric == 4506.0
    assert game.toi_even == 1050
    assert game.distance_skated_pp.imperial == 280.0
    assert game.toi_pp == 180
    assert game.distance_skated_pk.metric == 193.1
    assert game.toi_pk == 90
    assert game.home_team == {"id": 22, "abbrev": "EDM"}
    assert game.away_team == {"id": 5, "abbrev": "PIT"}

def test_skating_distance_game_empty() -> None:
    game = SkatingDistanceGame.from_dict({})
    assert game.game_center_link is None
    assert game.distance_skated_all.imperial is None
    assert game.toi_all is None
    assert game.toi_pk is None

def test_skating_distance_game_to_dict() -> None:
    game = SkatingDistanceGame.from_dict(DISTANCE_GAME_DATA)
    d = game.to_dict()
    assert d["game_date"] == "2024-01-10"
    assert d["distance_skated_all"]["imperial"] == 3200.0
    assert d["toi_pp"] == 180


DISTANCE_STRENGTH_DATA = {
    "strengthCode": "all",
    "distanceTotal": {
        "imperial": 185000.0, "metric": 297720.0,
        "percentile": 90.0, "leagueAvg": {"imperial": 165000.0, "metric": 265545.0},
    },
    "distancePer60": {
        "imperial": 3500.0, "metric": 5632.7,
        "percentile": 88.0, "leagueAvg": {"imperial": 3200.0, "metric": 5150.1},
    },
    "distanceMaxGame": {
        "imperial": 3200.0, "metric": 5150.0,
        "percentile": 75.0, "leagueAvg": {"imperial": 2900.0, "metric": 4667.0},
    },
    "distanceMaxPeriod": {
        "imperial": 1100.0, "metric": 1770.0,
        "percentile": 72.0, "leagueAvg": {"imperial": 950.0, "metric": 1528.8},
    },
}

def test_skating_distance_strength_from_dict() -> None:
    strength = SkatingDistanceStrength.from_dict(DISTANCE_STRENGTH_DATA)
    assert strength.strength_code == "all"
    assert strength.distance_total.imperial == 185000.0
    assert strength.distance_total.percentile == 90.0
    assert strength.distance_total.league_avg.imperial == 165000.0
    assert strength.distance_per_60.metric == 5632.7
    assert strength.distance_max_game.percentile == 75.0
    assert strength.distance_max_period.league_avg.metric == 1528.8

def test_skating_distance_strength_empty() -> None:
    strength = SkatingDistanceStrength.from_dict({})
    assert strength.strength_code is None
    assert strength.distance_total.imperial is None

def test_skating_distance_from_dict() -> None:
    data = {
        "skatingDistanceLast10": [DISTANCE_GAME_DATA, DISTANCE_GAME_DATA],
        "skatingDistanceDetails": [DISTANCE_STRENGTH_DATA],
    }
    sd = SkatingDistance.from_dict(data)
    assert len(sd.last_10_games) == 2
    assert sd.last_10_games[0].game_date == "2024-01-10"
    assert len(sd.distance_by_strength) == 1
    assert sd.distance_by_strength[0].strength_code == "all"

def test_skating_distance_empty() -> None:
    sd = SkatingDistance.from_dict({})
    assert sd.last_10_games == []
    assert sd.distance_by_strength == []


# ==========================================================================
# SKATING SPEED (DETAIL)
# ==========================================================================

SPEED_GAME_DATA = {
    "gameCenterLink": "/game/2023020500/boxscore",
    "gameDate": "2024-02-05",
    "gameType": 2,
    "playerOnHomeTeam": False,
    "skatingSpeed": {"imperial": 24.8, "metric": 39.9},
    "timeInPeriod": "12:34",
    "periodDescriptor": {"number": 2, "periodType": "REG", "maxRegulationPeriods": 3},
    "homeTeam": {"id": 10, "abbrev": "TOR"},
    "awayTeam": {"id": 22, "abbrev": "EDM"},
}

def test_skating_speed_game_from_dict() -> None:
    game = SkatingSpeedGame.from_dict(SPEED_GAME_DATA)
    assert game.game_center_link == "/game/2023020500/boxscore"
    assert game.game_date == "2024-02-05"
    assert game.game_type == 2
    assert game.player_on_home_team is False
    assert game.skating_speed.imperial == 24.8
    assert game.skating_speed.metric == 39.9
    assert game.time_in_period == "12:34"
    assert game.period_descriptor.number == 2
    assert game.period_descriptor.period_type == "REG"
    assert game.home_team == {"id": 10, "abbrev": "TOR"}
    assert game.away_team == {"id": 22, "abbrev": "EDM"}

def test_skating_speed_game_empty() -> None:
    game = SkatingSpeedGame.from_dict({})
    assert game.game_date is None
    assert game.skating_speed.imperial is None
    assert game.period_descriptor.number is None

def test_skating_speed_game_to_dict() -> None:
    game = SkatingSpeedGame.from_dict(SPEED_GAME_DATA)
    d = game.to_dict()
    assert d["game_date"] == "2024-02-05"
    assert d["skating_speed"]["imperial"] == 24.8
    assert d["period_descriptor"]["number"] == 2


SPEED_SUMMARY_DATA = {
    "maxSkatingSpeed": {
        "imperial": 24.8, "metric": 39.9,
        "percentile": 95.0, "leagueAvg": {"imperial": 20.0, "metric": 32.2},
    },
    "burstsOver22": {"value": 3, "percentile": 92.0, "leagueAvg": 1.2},
    "bursts20To22": {"value": 18, "percentile": 85.0, "leagueAvg": 12.5},
    "bursts18To20": {"value": 42, "percentile": 78.0, "leagueAvg": 35.8},
}

def test_skating_speed_summary_from_dict() -> None:
    summary = SkatingSpeedSummary.from_dict(SPEED_SUMMARY_DATA)
    assert summary.max_skating_speed.imperial == 24.8
    assert summary.max_skating_speed.percentile == 95.0
    assert summary.bursts_over_22.value == 3
    assert summary.bursts_over_22.league_avg == 1.2  # direct float leagueAvg
    assert summary.bursts_20_22.value == 18
    assert summary.bursts_20_22.league_avg == 12.5
    assert summary.bursts_18_20.value == 42

def test_skating_speed_summary_empty() -> None:
    summary = SkatingSpeedSummary.from_dict({})
    assert summary.max_skating_speed.imperial is None
    assert summary.bursts_over_22.value is None
    assert summary.bursts_over_22.league_avg is None

def test_skating_speed_detail_from_dict() -> None:
    data = {
        "topSkatingSpeeds": [SPEED_GAME_DATA, SPEED_GAME_DATA],
        "skatingSpeedDetails": SPEED_SUMMARY_DATA,
    }
    sk = SkatingSpeed.from_dict(data)
    assert len(sk.top_speeds) == 2
    assert sk.top_speeds[0].game_date == "2024-02-05"
    assert sk.speed_summary.max_skating_speed.imperial == 24.8
    assert sk.speed_summary.bursts_over_22.value == 3

def test_skating_speed_detail_empty() -> None:
    sk = SkatingSpeed.from_dict({})
    assert sk.top_speeds == []
    assert sk.speed_summary.max_skating_speed.imperial is None


# ==========================================================================
# ZONE TIME
# ==========================================================================

ZONE_TIME_STRENGTH_DATA = {
    "strengthCode": "all",
    "offensiveZonePctg": 0.38, "offensiveZonePercentile": 85.0, "offensiveZoneLeagueAvg": 0.34,
    "neutralZonePctg": 0.30, "neutralZonePercentile": 50.0, "neutralZoneLeagueAvg": 0.31,
    "defensiveZonePctg": 0.32, "defensiveZonePercentile": 40.0, "defensiveZoneLeagueAvg": 0.35,
}

def test_zone_time_strength_from_dict() -> None:
    zt = ZoneTimeStrength.from_dict(ZONE_TIME_STRENGTH_DATA)
    assert zt.strength_code == "all"
    assert zt.offensive_zone_pctg == 0.38
    assert zt.offensive_zone_percentile == 85.0
    assert zt.offensive_zone_league_avg == 0.34
    assert zt.neutral_zone_pctg == 0.30
    assert zt.defensive_zone_percentile == 40.0

def test_zone_time_strength_empty() -> None:
    zt = ZoneTimeStrength.from_dict({})
    assert zt.strength_code is None
    assert zt.offensive_zone_pctg is None


ZONE_STARTS_DETAIL_DATA = {
    "offensiveZoneStartsPctg": 0.55,
    "offensiveZoneStartsPctgPercentile": 80.0,
    "neutralZoneStartsPctg": 0.22,
    "neutralZoneStartsPctgPercentile": 50.0,
    "defensiveZoneStartsPctg": 0.23,
    "defensiveZoneStartsPctgPercentile": 45.0,
}

def test_zone_starts_detail_from_dict() -> None:
    zs = ZoneStartsDetail.from_dict(ZONE_STARTS_DETAIL_DATA)
    assert zs.offensive_zone_starts_pctg == 0.55
    assert zs.offensive_zone_starts_percentile == 80.0
    assert zs.neutral_zone_starts_pctg == 0.22
    assert zs.neutral_zone_starts_percentile == 50.0
    assert zs.defensive_zone_starts_pctg == 0.23
    assert zs.defensive_zone_starts_percentile == 45.0

def test_zone_starts_detail_empty() -> None:
    zs = ZoneStartsDetail.from_dict({})
    assert zs.offensive_zone_starts_pctg is None
    assert zs.offensive_zone_starts_percentile is None

def test_zone_time_from_dict() -> None:
    data = {
        "zoneTimeDetails": [ZONE_TIME_STRENGTH_DATA, {**ZONE_TIME_STRENGTH_DATA, "strengthCode": "ev"}],
        "zoneStarts": ZONE_STARTS_DETAIL_DATA,
    }
    zt = ZoneTime.from_dict(data)
    assert len(zt.zone_time_by_strength) == 2
    assert zt.zone_time_by_strength[0].strength_code == "all"
    assert zt.zone_time_by_strength[1].strength_code == "ev"
    assert zt.zone_starts.offensive_zone_starts_pctg == 0.55

def test_zone_time_empty() -> None:
    zt = ZoneTime.from_dict({})
    assert zt.zone_time_by_strength == []
    assert zt.zone_starts.offensive_zone_starts_pctg is None


# ==========================================================================
# SHOT SPEED (DETAIL)
# ==========================================================================

SHOT_SPEED_GAME_DATA = {
    "gameCenterLink": "/game/2023020300/boxscore",
    "gameDate": "2024-01-20",
    "gameType": 2,
    "playerOnHomeTeam": True,
    "shotSpeed": {"imperial": 96.2, "metric": 154.8},
    "timeInPeriod": "05:22",
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "homeTeam": {"id": 22, "abbrev": "EDM"},
    "awayTeam": {"id": 3, "abbrev": "NYR"},
}

def test_shot_speed_game_from_dict() -> None:
    game = ShotSpeedGame.from_dict(SHOT_SPEED_GAME_DATA)
    assert game.game_date == "2024-01-20"
    assert game.game_type == 2
    assert game.player_on_home_team is True
    assert game.shot_speed.imperial == 96.2
    assert game.shot_speed.metric == 154.8
    assert game.time_in_period == "05:22"
    assert game.period_descriptor.number == 1
    assert game.home_team == {"id": 22, "abbrev": "EDM"}

def test_shot_speed_game_empty() -> None:
    game = ShotSpeedGame.from_dict({})
    assert game.game_date is None
    assert game.shot_speed.imperial is None
    assert game.period_descriptor.number is None

def test_shot_speed_game_to_dict() -> None:
    game = ShotSpeedGame.from_dict(SHOT_SPEED_GAME_DATA)
    d = game.to_dict()
    assert d["game_date"] == "2024-01-20"
    assert d["shot_speed"]["imperial"] == 96.2
    assert d["period_descriptor"]["period_type"] == "REG"


SHOT_SPEED_SUMMARY_DATA = {
    "topShotSpeed": {
        "imperial": 96.0, "metric": 154.5,
        "percentile": 90.0, "leagueAvg": {"imperial": 85.0, "metric": 136.8},
    },
    "avgShotSpeed": {
        "imperial": 78.5, "metric": 126.3,
        "percentile": 85.0, "leagueAvg": {"imperial": 72.0, "metric": 115.9},
    },
    "shotAttemptsOver100": {"value": 2, "percentile": 88.0, "leagueAvg": {"value": 0.5}},
    "shotAttempts90To100": {"value": 8, "percentile": 82.0, "leagueAvg": {"value": 3.2}},
    "shotAttempts80To90": {"value": 25, "percentile": 75.0, "leagueAvg": {"value": 18.5}},
    "shotAttempts70To80": {"value": 50, "percentile": 70.0, "leagueAvg": {"value": 40.0}},
}

def test_shot_speed_summary_from_dict() -> None:
    summary = ShotSpeedSummary.from_dict(SHOT_SPEED_SUMMARY_DATA)
    assert summary.top_shot_speed.imperial == 96.0
    assert summary.top_shot_speed.percentile == 90.0
    assert summary.avg_shot_speed.metric == 126.3
    assert summary.shot_attempts_over_100.value == 2
    assert summary.shot_attempts_over_100.league_avg == 0.5  # from dict leagueAvg
    assert summary.shot_attempts_90_100.value == 8
    assert summary.shot_attempts_80_90.league_avg == 18.5
    assert summary.shot_attempts_70_80.value == 50

def test_shot_speed_summary_empty() -> None:
    summary = ShotSpeedSummary.from_dict({})
    assert summary.top_shot_speed.imperial is None
    assert summary.shot_attempts_over_100.value is None

def test_shot_speed_from_dict() -> None:
    data = {
        "hardestShots": [SHOT_SPEED_GAME_DATA, SHOT_SPEED_GAME_DATA],
        "shotSpeedDetails": SHOT_SPEED_SUMMARY_DATA,
    }
    ss = ShotSpeed.from_dict(data)
    assert len(ss.hardest_shots) == 2
    assert ss.hardest_shots[0].game_date == "2024-01-20"
    assert ss.speed_summary.top_shot_speed.imperial == 96.0
    assert ss.speed_summary.shot_attempts_over_100.value == 2

def test_shot_speed_empty() -> None:
    ss = ShotSpeed.from_dict({})
    assert ss.hardest_shots == []
    assert ss.speed_summary.top_shot_speed.imperial is None


# ==========================================================================
# SHOT LOCATION (DETAIL)
# ==========================================================================

def test_shot_area_detail_from_dict() -> None:
    data = {
        "area": "slot",
        "sog": 80, "goals": 20, "shootingPctg": 0.250,
        "sogPercentile": 85.0, "goalsPercentile": 90.0, "shootingPctgPercentile": 75.0,
    }
    detail = ShotAreaDetail.from_dict(data)
    assert detail.area == "slot"
    assert detail.sog == 80
    assert detail.goals == 20
    assert detail.shooting_pctg == 0.250
    assert detail.sog_percentile == 85.0
    assert detail.goals_percentile == 90.0
    assert detail.shooting_pctg_percentile == 75.0

def test_shot_area_detail_empty() -> None:
    detail = ShotAreaDetail.from_dict({})
    assert detail.area is None
    assert detail.sog_percentile is None

def test_shot_zone_total_from_dict() -> None:
    data = {
        "locationCode": "HD",
        "sog": 45, "goals": 12, "shootingPctg": 0.267,
        "sogPercentile": 82.0, "goalsPercentile": 88.0, "shootingPctgPercentile": 74.0,
        "sogLeagueAvg": 30.0, "goalsLeagueAvg": 7.5, "shootingPctgLeagueAvg": 0.192,
    }
    total = ShotZoneTotal.from_dict(data)
    assert total.location_code == "HD"
    assert total.sog == 45
    assert total.goals == 12
    assert total.shooting_pctg == 0.267
    assert total.sog_percentile == 82.0
    assert total.goals_league_avg == 7.5
    assert total.shooting_pctg_league_avg == 0.192

def test_shot_zone_total_empty() -> None:
    total = ShotZoneTotal.from_dict({})
    assert total.location_code is None
    assert total.sog_league_avg is None

def test_shot_location_from_dict() -> None:
    area = {
        "area": "slot", "sog": 80, "goals": 20, "shootingPctg": 0.250,
        "sogPercentile": 85.0, "goalsPercentile": 90.0, "shootingPctgPercentile": 75.0,
    }
    zone = {
        "locationCode": "HD", "sog": 45, "goals": 12, "shootingPctg": 0.267,
        "sogPercentile": 82.0, "goalsPercentile": 88.0, "shootingPctgPercentile": 74.0,
        "sogLeagueAvg": 30.0, "goalsLeagueAvg": 7.5, "shootingPctgLeagueAvg": 0.192,
    }
    sl = ShotLocation.from_dict({"shotLocationDetails": [area], "shotLocationTotals": [zone]})
    assert len(sl.area_details) == 1
    assert sl.area_details[0].area == "slot"
    assert len(sl.zone_totals) == 1
    assert sl.zone_totals[0].location_code == "HD"
    assert sl.zone_totals[0].sog_league_avg == 30.0

def test_shot_location_empty() -> None:
    sl = ShotLocation.from_dict({})
    assert sl.area_details == []
    assert sl.zone_totals == []


# ==========================================================================
# CAT SKATER DETAILS
# ==========================================================================

CAT_PLAYER_DATA = {
    "id": 8478402,
    "firstName": {"default": "Connor"},
    "lastName": {"default": "McDavid"},
    "birthDate": "1997-01-13",
    "shootsCatches": "L",
    "sweaterNumber": 97,
    "position": "C",
    "slug": "connor-mcdavid-8478402",
    "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
    "goals": 30,
    "assists": 70,
    "points": 100,
    "gamesPlayed": 60,
    "team": {"id": 22, "abbrev": "EDM"},
}

def test_cat_player_summary_from_dict() -> None:
    player = CatPlayerSummary.from_dict(CAT_PLAYER_DATA)
    assert player.id == 8478402
    assert player.first_name.default == "Connor"
    assert player.last_name.default == "McDavid"
    assert player.birth_date == "1997-01-13"
    assert player.shoots_catches == "L"
    assert player.sweater_number == 97
    assert player.position == "C"
    assert player.slug == "connor-mcdavid-8478402"
    assert player.goals == 30
    assert player.assists == 70
    assert player.points == 100
    assert player.games_played == 60
    assert player.team == {"id": 22, "abbrev": "EDM"}

def test_cat_player_summary_empty() -> None:
    player = CatPlayerSummary.from_dict({})
    assert player.id is None
    assert player.first_name.default is None
    assert player.goals is None
    assert player.team is None

def test_cat_player_summary_to_dict() -> None:
    player = CatPlayerSummary.from_dict(CAT_PLAYER_DATA)
    d = player.to_dict()
    assert d["id"] == 8478402
    assert d["first_name"] == "Connor"
    assert d["last_name"] == "McDavid"
    assert d["goals"] == 30
    assert d["sweater_number"] == 97


CAT_SKATER_DATA = {
    "player": CAT_PLAYER_DATA,
    "seasonsWithEdgeStats": [{"id": 20232024, "gameTypes": [2]}],
    "topShotSpeed": {
        "imperial": 96.0, "metric": 154.5, "percentile": 90.0,
        "leagueAvg": {"imperial": 85.0, "metric": 136.8},
    },
    "skatingSpeed": {
        "speedMax": {
            "imperial": 24.8, "metric": 39.9, "percentile": 95.0,
            "leagueAvg": {"imperial": 20.0, "metric": 32.2},
        },
        "burstsOver20": {"value": 12, "percentile": 80.0, "leagueAvg": {"value": 7.0}},
    },
    "totalDistanceSkated": {
        "imperial": 12500.0, "metric": 20117.0, "percentile": 88.0,
        "leagueAvg": {"imperial": 11000.0, "metric": 17703.0},
    },
    "sogSummary": [
        {
            "locationCode": "all",
            "shots": 180, "shotsPercentile": 92.0, "shotsLeagueAvg": 130.0,
            "goals": 60, "goalsPercentile": 95.0, "goalsLeagueAvg": 25.0,
            "shootingPctg": 0.333, "shootingPctgPercentile": 90.0, "shootingPctgLeagueAvg": 0.190,
        }
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

def test_cat_skater_details_from_dict() -> None:
    details = CatSkaterDetails.from_dict(CAT_SKATER_DATA)
    assert details.player.id == 8478402
    assert details.player.first_name.default == "Connor"
    assert details.player.goals == 30
    assert len(details.seasons_with_edge) == 1
    assert details.seasons_with_edge[0].id == 20232024
    assert details.top_shot_speed.imperial == 96.0
    assert details.skating_speed.speed_max.imperial == 24.8
    assert details.skating_speed.bursts_over_20.value == 12
    assert details.total_distance_skated.percentile == 88.0
    assert len(details.sog_summary) == 1
    assert details.sog_summary[0].location_code == "all"
    assert len(details.sog_details) == 1
    assert details.sog_details[0].area == "slot"
    assert details.zone_time.offensive_zone_pctg == 0.38
    assert details.zone_time.offensive_zone_ev_percentile == 80.0

def test_cat_skater_details_empty() -> None:
    details = CatSkaterDetails.from_dict({})
    assert details.player.id is None
    assert details.seasons_with_edge == []
    assert details.top_shot_speed.imperial is None
    assert details.sog_summary == []
    assert details.zone_time.offensive_zone_pctg is None

def test_cat_skater_details_to_dict() -> None:
    details = CatSkaterDetails.from_dict(CAT_SKATER_DATA)
    d = details.to_dict()
    assert d["player"]["id"] == 8478402
    assert d["player"]["first_name"] == "Connor"
    assert d["top_shot_speed"]["imperial"] == 96.0
    assert d["skating_speed"]["bursts_over_20"]["value"] == 12
    assert len(d["sog_summary"]) == 1
