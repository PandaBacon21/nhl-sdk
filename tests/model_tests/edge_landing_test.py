"""
Tests for Edge landing page models:
  SkaterLanding, SkaterLandingLeaders, SkaterPeakLeader, SkaterDistanceLeader,
  SogAreaDetail, SkaterSOGLeader, SkaterZoneTimeLeader,
  GoalieLanding, GoalieLandingLeaders, GoalieSavePctgAreaDetail, GoalieSavesAreaDetail,
  GoalieHighDangerSavePctgLeader, GoalieHighDangerSavesLeader,
  GoalieSimpleLeader, GoalieSavePctg5v5Leader
"""
from nhl_sdk.models.players.leaders.edge.skaters.skater_landing import (
    SkaterLanding,
    SkaterLandingLeaders,
    SkaterPeakLeader,
    SkaterDistanceLeader,
    SogAreaDetail,
    SkaterSOGLeader,
    SkaterZoneTimeLeader,
)
from nhl_sdk.models.players.leaders.edge.goalies.goalie_landing import (
    GoalieLanding,
    GoalieLandingLeaders,
    GoalieSavePctgAreaDetail,
    GoalieSavesAreaDetail,
    GoalieHighDangerSavePctgLeader,
    GoalieHighDangerSavesLeader,
    GoalieSimpleLeader,
    GoalieSavePctg5v5Leader,
)


# ==========================================================================
# SHARED FIXTURES
# ==========================================================================

EDGE_SEASON = {"id": 20242025, "gameTypes": [2]}

LEADER_PLAYER = {
    "id": "8477492",
    "firstName": {"default": "N."},
    "lastName": {"default": "MacKinnon"},
    "teamAbbrev": "COL",
    "teamName": {"default": "Colorado Avalanche"},
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
    "headshot": "https://assets.nhle.com/mugs/nhl/20242025/COL/8477492.png",
}

OVERLAY = {
    "firstName": {"default": "N."},
    "lastName": {"default": "MacKinnon"},
    "gameDate": "2025-01-15",
    "awayTeam": {"abbrev": "COL", "logo": ""},
    "homeTeam": {"abbrev": "EDM", "logo": ""},
    "gameOutcome": {"lastPeriodType": "REG"},
    "periodDescriptor": {"periodType": "REG", "maxRegulationPeriods": 3},
}


# ==========================================================================
# SOG AREA DETAIL
# ==========================================================================

def test_sog_area_detail_from_dict() -> None:
    d = SogAreaDetail.from_dict({"area": "slot", "sog": 42, "sogPercentile": 98.5})
    assert d.area == "slot"
    assert d.sog == 42
    assert d.sog_percentile == 98.5

def test_sog_area_detail_empty() -> None:
    d = SogAreaDetail.from_dict({})
    assert d.area is None
    assert d.sog is None
    assert d.sog_percentile is None


# ==========================================================================
# SKATER PEAK LEADER
# ==========================================================================

def test_skater_peak_leader_with_overlay() -> None:
    data = {"player": LEADER_PLAYER, "shotSpeed": {"imperial": "104.2 mph", "metric": "167.7 km/h"}, "overlay": OVERLAY}
    leader = SkaterPeakLeader.from_dict(data, stat_key="shotSpeed")
    assert leader.player.last_name.default == "MacKinnon"
    assert leader.stat.imperial == "104.2 mph"
    assert leader.overlay is not None
    assert leader.overlay.game_date == "2025-01-15"

def test_skater_peak_leader_no_overlay() -> None:
    data = {"player": LEADER_PLAYER, "skatingSpeed": {"imperial": "23.4 mph", "metric": "37.7 km/h"}}
    leader = SkaterPeakLeader.from_dict(data, stat_key="skatingSpeed")
    assert leader.stat.imperial == "23.4 mph"
    assert leader.overlay is None

def test_skater_peak_leader_empty() -> None:
    leader = SkaterPeakLeader.from_dict({}, stat_key="shotSpeed")
    assert leader.player.last_name.default is None
    assert leader.stat.imperial is None
    assert leader.overlay is None


# ==========================================================================
# SKATER DISTANCE LEADER
# ==========================================================================

def test_skater_distance_leader_from_dict() -> None:
    data = {"player": LEADER_PLAYER, "distanceSkated": {"imperial": "1,234.5 mi", "metric": "1,987.3 km"}, "overlay": OVERLAY}
    leader = SkaterDistanceLeader.from_dict(data)
    assert leader.player.last_name.default == "MacKinnon"
    assert leader.distance_skated.imperial == "1,234.5 mi"
    assert leader.overlay is not None

def test_skater_distance_leader_no_overlay() -> None:
    data = {"player": LEADER_PLAYER, "distanceSkated": {"imperial": "1,000 mi", "metric": "1,609 km"}}
    leader = SkaterDistanceLeader.from_dict(data)
    assert leader.overlay is None

def test_skater_distance_leader_empty() -> None:
    leader = SkaterDistanceLeader.from_dict({})
    assert leader.player.last_name.default is None
    assert leader.distance_skated.imperial is None


# ==========================================================================
# SKATER SOG LEADER
# ==========================================================================

def test_skater_sog_leader_from_dict() -> None:
    data = {
        "player": LEADER_PLAYER,
        "sog": 55,
        "shotLocationDetails": [
            {"area": "slot", "sog": 30, "sogPercentile": 95.0},
            {"area": "left", "sog": 15, "sogPercentile": 80.0},
        ],
    }
    leader = SkaterSOGLeader.from_dict(data)
    assert leader.sog == 55
    assert len(leader.shot_location_details) == 2
    assert leader.shot_location_details[0].area == "slot"

def test_skater_sog_leader_empty() -> None:
    leader = SkaterSOGLeader.from_dict({})
    assert leader.sog is None
    assert leader.shot_location_details == []


# ==========================================================================
# SKATER ZONE TIME LEADER
# ==========================================================================

def test_skater_zone_time_leader_from_dict() -> None:
    data = {"player": LEADER_PLAYER, "zoneTime": 62.5}
    leader = SkaterZoneTimeLeader.from_dict(data)
    assert leader.zone_time == 62.5

def test_skater_zone_time_leader_empty() -> None:
    leader = SkaterZoneTimeLeader.from_dict({})
    assert leader.zone_time is None


# ==========================================================================
# SKATER LANDING LEADERS
# ==========================================================================

SKATER_LEADERS_DATA = {
    "hardestShot": {"player": LEADER_PLAYER, "shotSpeed": {"imperial": "104.2 mph", "metric": "167.7 km/h"}},
    "maxSkatingSpeed": {"player": LEADER_PLAYER, "skatingSpeed": {"imperial": "23.4 mph", "metric": "37.7 km/h"}},
    "totalDistanceSkated": {"player": LEADER_PLAYER, "distanceSkated": {"imperial": "1,200 mi", "metric": "1,931 km"}},
    "distanceMaxGame": {"player": LEADER_PLAYER, "distanceSkated": {"imperial": "3.5 mi", "metric": "5.6 km"}},
    "highDangerSOG": {"player": LEADER_PLAYER, "sog": 45, "shotLocationDetails": []},
    "offensiveZoneTime": {"player": LEADER_PLAYER, "zoneTime": 65.2},
    "defensiveZoneTime": {"player": LEADER_PLAYER, "zoneTime": 20.1},
}

def test_skater_landing_leaders_from_dict() -> None:
    leaders = SkaterLandingLeaders.from_dict(SKATER_LEADERS_DATA)
    assert leaders.hardest_shot.player.last_name.default == "MacKinnon"
    assert leaders.hardest_shot.stat.imperial == "104.2 mph"
    assert leaders.max_skating_speed.stat.imperial == "23.4 mph"
    assert leaders.total_distance_skated.distance_skated.imperial == "1,200 mi"
    assert leaders.high_danger_sog.sog == 45
    assert leaders.offensive_zone_time.zone_time == 65.2
    assert leaders.defensive_zone_time.zone_time == 20.1

def test_skater_landing_leaders_empty() -> None:
    leaders = SkaterLandingLeaders.from_dict({})
    assert leaders.hardest_shot.player.last_name.default is None
    assert leaders.high_danger_sog.sog is None


# ==========================================================================
# SKATER LANDING
# ==========================================================================

def test_skater_landing_from_dict() -> None:
    data = {
        "seasonsWithEdgeStats": [EDGE_SEASON],
        "leaders": SKATER_LEADERS_DATA,
    }
    landing = SkaterLanding.from_dict(data)
    assert len(landing.seasons_with_edge) == 1
    assert landing.seasons_with_edge[0].id == 20242025
    assert landing.leaders.hardest_shot.player.last_name.default == "MacKinnon"

def test_skater_landing_empty() -> None:
    landing = SkaterLanding.from_dict({})
    assert landing.seasons_with_edge == []
    assert landing.leaders.hardest_shot.player.last_name.default is None


# ==========================================================================
# GOALIE SAVE PCTG AREA DETAIL
# ==========================================================================

def test_goalie_save_pctg_area_detail_from_dict() -> None:
    d = GoalieSavePctgAreaDetail.from_dict({"area": "slot", "savePctg": 0.923, "savePctgPercentile": 97.1})
    assert d.area == "slot"
    assert d.save_pctg == 0.923
    assert d.save_pctg_percentile == 97.1

def test_goalie_save_pctg_area_detail_empty() -> None:
    d = GoalieSavePctgAreaDetail.from_dict({})
    assert d.area is None
    assert d.save_pctg is None
    assert d.save_pctg_percentile is None


# ==========================================================================
# GOALIE SAVES AREA DETAIL
# ==========================================================================

def test_goalie_saves_area_detail_from_dict() -> None:
    d = GoalieSavesAreaDetail.from_dict({"area": "slot", "saves": 120, "savesPercentile": 95.0})
    assert d.area == "slot"
    assert d.saves == 120
    assert d.saves_percentile == 95.0

def test_goalie_saves_area_detail_empty() -> None:
    d = GoalieSavesAreaDetail.from_dict({})
    assert d.area is None
    assert d.saves is None
    assert d.saves_percentile is None


# ==========================================================================
# GOALIE HIGH DANGER SAVE PCTG LEADER
# ==========================================================================

GOALIE_PLAYER = {
    "id": "8478406",
    "firstName": {"default": "M."},
    "lastName": {"default": "Blackwood"},
    "teamAbbrev": "LAK",
    "teamName": {"default": "Los Angeles Kings"},
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/LAK_light.svg",
    "headshot": "https://assets.nhle.com/mugs/nhl/20242025/LAK/8478406.png",
}

def test_goalie_hd_save_pctg_leader_from_dict() -> None:
    data = {
        "player": GOALIE_PLAYER,
        "savePctg": 0.912,
        "shotLocationDetails": [
            {"area": "slot", "savePctg": 0.890, "savePctgPercentile": 88.0},
        ],
    }
    leader = GoalieHighDangerSavePctgLeader.from_dict(data)
    assert leader.player.last_name.default == "Blackwood"
    assert leader.save_pctg == 0.912
    assert len(leader.shot_location_details) == 1
    assert leader.shot_location_details[0].area == "slot"

def test_goalie_hd_save_pctg_leader_empty() -> None:
    leader = GoalieHighDangerSavePctgLeader.from_dict({})
    assert leader.save_pctg is None
    assert leader.shot_location_details == []


# ==========================================================================
# GOALIE HIGH DANGER SAVES LEADER
# ==========================================================================

def test_goalie_hd_saves_leader_from_dict() -> None:
    data = {
        "player": GOALIE_PLAYER,
        "saves": 95,
        "shotLocationDetails": [
            {"area": "slot", "saves": 60, "savesPercentile": 92.0},
        ],
    }
    leader = GoalieHighDangerSavesLeader.from_dict(data)
    assert leader.saves == 95
    assert len(leader.shot_location_details) == 1
    assert leader.shot_location_details[0].saves == 60

def test_goalie_hd_saves_leader_empty() -> None:
    leader = GoalieHighDangerSavesLeader.from_dict({})
    assert leader.saves is None
    assert leader.shot_location_details == []


# ==========================================================================
# GOALIE SIMPLE LEADER
# ==========================================================================

def test_goalie_simple_leader_goals_against() -> None:
    data = {"player": GOALIE_PLAYER, "goalsAgainst": 8}
    leader = GoalieSimpleLeader.from_dict(data, value_key="goalsAgainst")
    assert leader.player.last_name.default == "Blackwood"
    assert leader.value == 8

def test_goalie_simple_leader_games_above() -> None:
    data = {"player": GOALIE_PLAYER, "games": 42}
    leader = GoalieSimpleLeader.from_dict(data, value_key="games")
    assert leader.value == 42

def test_goalie_simple_leader_empty() -> None:
    leader = GoalieSimpleLeader.from_dict({}, value_key="goalsAgainst")
    assert leader.value is None


# ==========================================================================
# GOALIE SAVE PCTG 5V5 LEADER
# ==========================================================================

def test_goalie_save_pctg_5v5_leader_from_dict() -> None:
    data = {"player": GOALIE_PLAYER, "savePctg": 0.934}
    leader = GoalieSavePctg5v5Leader.from_dict(data)
    assert leader.save_pctg == 0.934

def test_goalie_save_pctg_5v5_leader_empty() -> None:
    leader = GoalieSavePctg5v5Leader.from_dict({})
    assert leader.save_pctg is None


# ==========================================================================
# GOALIE LANDING LEADERS
# ==========================================================================

GOALIE_LEADERS_DATA = {
    "highDangerSavePctg": {"player": GOALIE_PLAYER, "savePctg": 0.912, "shotLocationDetails": []},
    "highDangerSaves": {"player": GOALIE_PLAYER, "saves": 95, "shotLocationDetails": []},
    "highDangerGoalsAgainst": {"player": GOALIE_PLAYER, "goalsAgainst": 8},
    "savePctg5v5": {"player": GOALIE_PLAYER, "savePctg": 0.934},
    "gamesAbove900": {"player": GOALIE_PLAYER, "games": 42},
}

def test_goalie_landing_leaders_from_dict() -> None:
    leaders = GoalieLandingLeaders.from_dict(GOALIE_LEADERS_DATA)
    assert leaders.high_danger_save_pctg.save_pctg == 0.912
    assert leaders.high_danger_saves.saves == 95
    assert leaders.high_danger_goals_against.value == 8
    assert leaders.save_pctg_5v5.save_pctg == 0.934
    assert leaders.games_above_900.value == 42

def test_goalie_landing_leaders_empty() -> None:
    leaders = GoalieLandingLeaders.from_dict({})
    assert leaders.high_danger_save_pctg.save_pctg is None
    assert leaders.high_danger_saves.saves is None
    assert leaders.games_above_900.value is None


# ==========================================================================
# GOALIE LANDING
# ==========================================================================

def test_goalie_landing_from_dict() -> None:
    data = {
        "seasonsWithEdgeStats": [EDGE_SEASON],
        "minimumGamesPlayed": 20,
        "leaders": GOALIE_LEADERS_DATA,
    }
    landing = GoalieLanding.from_dict(data)
    assert len(landing.seasons_with_edge) == 1
    assert landing.seasons_with_edge[0].id == 20242025
    assert landing.minimum_games_played == 20
    assert landing.leaders.save_pctg_5v5.save_pctg == 0.934

def test_goalie_landing_empty() -> None:
    landing = GoalieLanding.from_dict({})
    assert landing.seasons_with_edge == []
    assert landing.minimum_games_played is None
    assert landing.leaders.high_danger_save_pctg.save_pctg is None
