from nhl_sdk.models.players.player.player_stats.edge.skaters.skater_comparison import (
    ShotSpeedDetails,
    SkatingSpeedDetails,
    DistanceGame,
    SkatingDistanceDetails,
    ShotLocationDetail,
    ShotLocationTotal,
    ZoneTimeComparison,
    ZoneStarts,
    SkaterComparison,
)


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
# SHOT SPEED DETAILS
# ==========================================================================

def test_shot_speed_details_from_dict() -> None:
    data = {
        "topShotSpeed": {"imperial": 96.0, "metric": 154.5, "overlay": OVERLAY_DATA},
        "avgShotSpeed": {"imperial": 78.5, "metric": 126.3},
        "shotAttemptsOver100": 2,
        "shotAttempts90To100": 8,
        "shotAttempts80To90": 25,
        "shotAttempts70To80": 50,
    }
    details = ShotSpeedDetails.from_dict(data)
    assert details.top_shot_speed.imperial == 96.0
    assert details.top_shot_speed.overlay
    assert details.top_shot_speed.overlay.game_date == "2024-01-15"
    assert details.avg_shot_speed.metric == 126.3
    assert details.shot_attempts_over_100 == 2
    assert details.shot_attempts_90_100 == 8
    assert details.shot_attempts_80_90 == 25
    assert details.shot_attempts_70_80 == 50

def test_shot_speed_details_empty() -> None:
    details = ShotSpeedDetails.from_dict({})
    assert details.top_shot_speed.imperial is None
    assert details.avg_shot_speed.metric is None
    assert details.shot_attempts_over_100 is None


# ==========================================================================
# SKATING SPEED DETAILS
# ==========================================================================

def test_skating_speed_details_from_dict() -> None:
    data = {
        "maxSkatingSpeed": {"imperial": 24.8, "metric": 39.9, "overlay": OVERLAY_DATA},
        "burstsOver22": 3,
        "bursts20To22": 18,
        "bursts18To20": 42,
    }
    details = SkatingSpeedDetails.from_dict(data)
    assert details.max_skating_speed.imperial == 24.8
    assert details.max_skating_speed.overlay
    assert details.max_skating_speed.overlay.away_team.abbrev == "EDM"
    assert details.bursts_over_22 == 3
    assert details.bursts_20_22 == 18
    assert details.bursts_18_20 == 42

def test_skating_speed_details_empty() -> None:
    details = SkatingSpeedDetails.from_dict({})
    assert details.max_skating_speed.imperial is None
    assert details.bursts_over_22 is None


# ==========================================================================
# DISTANCE GAME (COMPARISON)
# ==========================================================================

def test_distance_game_from_dict() -> None:
    data = {
        "gameCenterLink": "/game/2023020001/boxscore",
        "gameDate": "2024-01-10",
        "playerOnHomeTeam": True,
        "distanceSkated": {"imperial": 3200.0, "metric": 5150.0},
        "toi": 1380.5,
        "homeTeam": {"id": 22, "abbrev": "EDM"},
        "awayTeam": {"id": 5, "abbrev": "PIT"},
    }
    game = DistanceGame.from_dict(data)
    assert game.game_center_link == "/game/2023020001/boxscore"
    assert game.game_date == "2024-01-10"
    assert game.player_on_home_team is True
    assert game.distance_skated.imperial == 3200.0
    assert game.toi == 1380.5
    assert game.home_team == {"id": 22, "abbrev": "EDM"}
    assert game.away_team == {"id": 5, "abbrev": "PIT"}

def test_distance_game_empty() -> None:
    game = DistanceGame.from_dict({})
    assert game.game_center_link is None
    assert game.game_date is None
    assert game.player_on_home_team is None
    assert game.distance_skated.imperial is None
    assert game.toi is None
    assert game.home_team is None
    assert game.away_team is None


# ==========================================================================
# SKATING DISTANCE DETAILS (COMPARISON)
# ==========================================================================

def test_skating_distance_details_from_dict() -> None:
    data = {
        "distanceTotal": {"imperial": 185000.0, "metric": 297720.0},
        "distancePer60": {"imperial": 3500.0, "metric": 5632.7},
        "distanceMaxGame": {"imperial": 3200.0, "metric": 5150.0, "overlay": OVERLAY_DATA},
        "distanceMaxPeriod": {"imperial": 1100.0, "metric": 1770.0},
    }
    details = SkatingDistanceDetails.from_dict(data)
    assert details.distance_total.imperial == 185000.0
    assert details.distance_per_60.metric == 5632.7
    assert details.distance_max_game.overlay
    assert details.distance_max_game.overlay.game_date == "2024-01-15"
    assert details.distance_max_period.imperial == 1100.0
    assert details.distance_max_period.overlay is None


# ==========================================================================
# SHOT LOCATION DETAIL & TOTAL
# ==========================================================================

def test_shot_location_detail_from_dict() -> None:
    data = {"area": "slot", "sog": 80, "goals": 20, "shootingPctg": 0.250}
    detail = ShotLocationDetail.from_dict(data)
    assert detail.area == "slot"
    assert detail.sog == 80
    assert detail.goals == 20
    assert detail.shooting_pctg == 0.250

def test_shot_location_total_from_dict() -> None:
    data = {"locationCode": "HD", "sog": 45, "goals": 12, "shootingPctg": 0.267}
    total = ShotLocationTotal.from_dict(data)
    assert total.location_code == "HD"
    assert total.sog == 45
    assert total.goals == 12
    assert total.shooting_pctg == 0.267

def test_shot_location_detail_empty() -> None:
    detail = ShotLocationDetail.from_dict({})
    assert detail.area is None
    assert detail.sog is None


# ==========================================================================
# ZONE TIME COMPARISON & ZONE STARTS
# ==========================================================================

def test_zone_time_comparison_from_dict() -> None:
    data = {
        "offensiveZonePctg": 0.38, "offensiveZoneLeagueAvg": 0.34,
        "neutralZonePctg": 0.30, "neutralZoneLeagueAvg": 0.31,
        "defensiveZonePctg": 0.32, "defensiveZoneLeagueAvg": 0.35,
    }
    zt = ZoneTimeComparison.from_dict(data)
    assert zt.offensive_zone_pctg == 0.38
    assert zt.offensive_zone_league_avg == 0.34
    assert zt.neutral_zone_pctg == 0.30
    assert zt.defensive_zone_league_avg == 0.35

def test_zone_time_comparison_empty() -> None:
    zt = ZoneTimeComparison.from_dict({})
    assert zt.offensive_zone_pctg is None
    assert zt.defensive_zone_league_avg is None

def test_zone_starts_from_dict() -> None:
    data = {
        "offensiveZoneStarts": 0.55,
        "neutralZoneStarts": 0.22,
        "defensiveZoneStarts": 0.23,
    }
    zs = ZoneStarts.from_dict(data)
    assert zs.offensive_zone_starts == 0.55
    assert zs.neutral_zone_starts == 0.22
    assert zs.defensive_zone_starts == 0.23

def test_zone_starts_empty() -> None:
    zs = ZoneStarts.from_dict({})
    assert zs.offensive_zone_starts is None


# ==========================================================================
# SKATER COMPARISON (COMPOSITE)
# ==========================================================================

SKATER_COMPARISON_DATA = {
    "seasonsWithEdgeStats": [{"id": 20232024, "gameTypes": [2]}],
    "shotSpeedDetails": {
        "topShotSpeed": {"imperial": 96.0, "metric": 154.5, "overlay": OVERLAY_DATA},
        "avgShotSpeed": {"imperial": 78.5, "metric": 126.3},
        "shotAttemptsOver100": 2,
        "shotAttempts90To100": 8,
        "shotAttempts80To90": 25,
        "shotAttempts70To80": 50,
    },
    "skatingSpeedDetails": {
        "maxSkatingSpeed": {"imperial": 24.8, "metric": 39.9, "overlay": OVERLAY_DATA},
        "burstsOver22": 3,
        "bursts20To22": 18,
        "bursts18To20": 42,
    },
    "skatingDistanceLast10": [
        {
            "gameCenterLink": "/game/2023020001/boxscore",
            "gameDate": "2024-01-10",
            "playerOnHomeTeam": True,
            "distanceSkated": {"imperial": 3200.0, "metric": 5150.0},
            "toi": 1380.5,
            "homeTeam": {"id": 22, "abbrev": "EDM"},
            "awayTeam": {"id": 5, "abbrev": "PIT"},
        }
    ],
    "skatingDistanceDetails": {
        "distanceTotal": {"imperial": 185000.0, "metric": 297720.0},
        "distancePer60": {"imperial": 3500.0, "metric": 5632.7},
        "distanceMaxGame": {"imperial": 3200.0, "metric": 5150.0},
        "distanceMaxPeriod": {"imperial": 1100.0, "metric": 1770.0},
    },
    "shotLocationDetails": [
        {"area": "slot", "sog": 80, "goals": 20, "shootingPctg": 0.250},
        {"area": "high_slot", "sog": 40, "goals": 8, "shootingPctg": 0.200},
    ],
    "shotLocationTotals": [
        {"locationCode": "HD", "sog": 45, "goals": 12, "shootingPctg": 0.267},
    ],
    "zoneTimeDetails": {
        "offensiveZonePctg": 0.38, "offensiveZoneLeagueAvg": 0.34,
        "neutralZonePctg": 0.30, "neutralZoneLeagueAvg": 0.31,
        "defensiveZonePctg": 0.32, "defensiveZoneLeagueAvg": 0.35,
    },
    "zoneStarts": {
        "offensiveZoneStarts": 0.55,
        "neutralZoneStarts": 0.22,
        "defensiveZoneStarts": 0.23,
    },
}

def test_skater_comparison_from_dict() -> None:
    comp = SkaterComparison.from_dict(SKATER_COMPARISON_DATA)
    assert len(comp.seasons_with_edge) == 1
    assert comp.seasons_with_edge[0].id == 20232024
    assert comp.shot_speed.top_shot_speed.imperial == 96.0
    assert comp.shot_speed.shot_attempts_90_100 == 8
    assert comp.skating_speed.max_skating_speed.imperial == 24.8
    assert comp.skating_speed.bursts_over_22 == 3
    assert len(comp.skating_distance_last_10) == 1
    assert comp.skating_distance_last_10[0].game_date == "2024-01-10"
    assert comp.skating_distance.distance_total.imperial == 185000.0
    assert len(comp.shot_location_details) == 2
    assert comp.shot_location_details[0].area == "slot"
    assert len(comp.shot_location_totals) == 1
    assert comp.shot_location_totals[0].location_code == "HD"
    assert comp.zone_time.offensive_zone_pctg == 0.38
    assert comp.zone_starts.offensive_zone_starts == 0.55

def test_skater_comparison_empty() -> None:
    comp = SkaterComparison.from_dict({})
    assert comp.seasons_with_edge == []
    assert comp.shot_speed.top_shot_speed.imperial is None
    assert comp.skating_distance_last_10 == []
    assert comp.shot_location_details == []
    assert comp.zone_starts.offensive_zone_starts is None

def test_skater_comparison_to_dict() -> None:
    comp = SkaterComparison.from_dict(SKATER_COMPARISON_DATA)
    d = comp.to_dict()
    assert d["seasons_with_edge"][0]["id"] == 20232024
    assert d["shot_speed"]["top_shot_speed"]["imperial"] == 96.0
    assert d["skating_speed"]["bursts_over_22"] == 3
    assert len(d["skating_distance_last_10"]) == 1
    assert d["zone_starts"]["offensive_zone_starts"] == 0.55
