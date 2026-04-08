"""
Tests for TeamComparisonResult and sub-models.
"""
from nhl_stats.models.teams.team.edge.team_comparison.team_comparison_result import (
    TeamComparisonResult, TeamCompShotSpeed, TeamCompSkatingSpeed,
    TeamCompTeamRef, TeamCompDistanceGame, TeamCompDistance,
    TeamCompShotLocationDetail, TeamCompShotLocationTotal,
    TeamCompZoneTime, TeamShotDifferential,
)


OVERLAY = {
    "player": {"firstName": {"default": "Cale"}, "lastName": {"default": "Makar"}},
    "gameDate": "2026-03-18",
    "awayTeam": {"abbrev": "DAL", "score": 2},
    "homeTeam": {"abbrev": "COL", "score": 1},
    "gameOutcome": {"lastPeriodType": "SO"},
    "periodDescriptor": {"maxRegulationPeriods": 3, "number": 2, "periodType": "REG"},
    "timeInPeriod": "10:39",
    "gameType": 2,
}

OVERLAY_NO_PLAYER = {
    "gameDate": "2026-01-21",
    "awayTeam": {"abbrev": "ANA", "score": 2},
    "homeTeam": {"abbrev": "COL", "score": 1},
    "gameOutcome": {"lastPeriodType": "SO"},
    "periodDescriptor": {"maxRegulationPeriods": 3, "number": 1, "periodType": "REG"},
    "gameType": 2,
}

TEAM_DATA = {
    "id": 21,
    "commonName": {"default": "Avalanche"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
    "abbrev": "COL",
    "wins": 49, "losses": 14, "otLosses": 10, "gamesPlayed": 73, "points": 108,
}

TEAM_REF_DATA = {
    "commonName": {"default": "Avalanche"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
    "abbrev": "COL",
    "teamLogo": {"light": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg", "dark": "https://assets.nhle.com/logos/nhl/svg/COL_dark.svg"},
    "slug": "colorado-avalanche-21",
}

COMPARISON_RESPONSE = {
    "team": TEAM_DATA,
    "seasonsWithEdgeStats": [
        {"id": 20242025, "gameTypes": [2, 3]},
        {"id": 20252026, "gameTypes": [2]},
    ],
    "shotSpeedDetails": {
        "topShotSpeed": {"imperial": 98.21, "metric": 158.05, "overlay": OVERLAY},
        "avgShotSpeed": {"imperial": 60.47, "metric": 97.31},
        "shotAttemptsOver100": 0,
        "shotAttempts90To100": 57,
        "shotAttempts80To90": 525,
        "shotAttempts70To80": 1320,
    },
    "skatingSpeedDetails": {
        "maxSkatingSpeed": {"imperial": 24.01, "metric": 38.65, "overlay": OVERLAY},
        "burstsOver22": 152,
        "bursts20To22": 2242,
        "bursts18To20": 8206,
    },
    "skatingDistanceLast10": [
        {
            "gameCenterLink": "/gamecenter/col-vs-cgy/2026/03/30/2025021174",
            "gameDate": "2026-03-30",
            "isHomeTeam": True,
            "distanceSkated": {"imperial": 47.34, "metric": 76.18},
            "homeTeam": TEAM_REF_DATA,
            "awayTeam": {
                "commonName": {"default": "Flames"},
                "placeNameWithPreposition": {"default": "Calgary"},
                "abbrev": "CGY",
                "teamLogo": {"light": "https://assets.nhle.com/logos/nhl/svg/CGY_light.svg", "dark": "https://assets.nhle.com/logos/nhl/svg/CGY_dark.svg"},
                "slug": "calgary-flames-20",
            },
        },
    ],
    "skatingDistanceDetails": {
        "distanceTotal": {"imperial": 3402.75, "metric": 5475.92},
        "distancePer60": {"imperial": 9.40, "metric": 15.13},
        "distanceMaxGame": {"imperial": 51.12, "metric": 82.27, "overlay": OVERLAY_NO_PLAYER},
        "distanceMaxPeriod": {"imperial": 16.91, "metric": 27.21, "overlay": OVERLAY_NO_PLAYER},
    },
    "shotLocationDetails": [
        {"area": "High Slot", "sog": 273, "goals": 41, "shootingPctg": 0.1502},
        {"area": "Low Slot", "sog": 573, "goals": 97, "shootingPctg": 0.1693},
    ],
    "shotLocationTotals": [
        {"locationCode": "all", "sog": 2471, "goals": 274, "shootingPctg": 0.1109},
        {"locationCode": "high", "sog": 633, "goals": 114, "shootingPctg": 0.1801},
    ],
    "zoneTimeDetails": {
        "offensiveZonePctg": 0.4286305,
        "offensiveZoneLeagueAvg": 0.4107842,
        "neutralZonePctg": 0.1815559,
        "neutralZoneLeagueAvg": 0.1784317,
        "defensiveZonePctg": 0.3898136,
        "defensiveZoneLeagueAvg": 0.4107842,
    },
    "shotDifferential": {
        "shotAttemptDifferential": 7.684932,
        "sogDifferential": 0.141059,
    },
}


# --------------------------------------------------------------------------
# TeamCompShotSpeed
# --------------------------------------------------------------------------

def test_team_comp_shot_speed_fields() -> None:
    ss = TeamCompShotSpeed.from_dict(COMPARISON_RESPONSE["shotSpeedDetails"])
    assert ss.top_shot_speed.imperial == 98.21
    assert ss.top_shot_speed.metric == 158.05
    assert ss.top_shot_speed.overlay is not None
    assert ss.top_shot_speed.overlay.first_name.default == "Cale"
    assert ss.avg_shot_speed.imperial == 60.47
    assert ss.avg_shot_speed.metric == 97.31
    assert ss.shot_attempts_over_100 == 0
    assert ss.shot_attempts_90_100 == 57
    assert ss.shot_attempts_80_90 == 525
    assert ss.shot_attempts_70_80 == 1320


def test_team_comp_shot_speed_empty() -> None:
    ss = TeamCompShotSpeed.from_dict({})
    assert ss.top_shot_speed.imperial is None
    assert ss.avg_shot_speed.imperial is None
    assert ss.shot_attempts_over_100 is None


# --------------------------------------------------------------------------
# TeamCompSkatingSpeed
# --------------------------------------------------------------------------

def test_team_comp_skating_speed_fields() -> None:
    sk = TeamCompSkatingSpeed.from_dict(COMPARISON_RESPONSE["skatingSpeedDetails"])
    assert sk.max_skating_speed.imperial == 24.01
    assert sk.max_skating_speed.overlay is not None
    assert sk.bursts_over_22 == 152
    assert sk.bursts_20_22 == 2242
    assert sk.bursts_18_20 == 8206


def test_team_comp_skating_speed_empty() -> None:
    sk = TeamCompSkatingSpeed.from_dict({})
    assert sk.max_skating_speed.imperial is None
    assert sk.bursts_over_22 is None


# --------------------------------------------------------------------------
# TeamCompTeamRef
# --------------------------------------------------------------------------

def test_team_comp_team_ref_fields() -> None:
    ref = TeamCompTeamRef.from_dict(TEAM_REF_DATA)
    assert ref.common_name.default == "Avalanche"
    assert ref.place_name_with_preposition.default == "Colorado"
    assert ref.abbrev == "COL"
    assert ref.team_logo.light == "https://assets.nhle.com/logos/nhl/svg/COL_light.svg"
    assert ref.slug == "colorado-avalanche-21"


def test_team_comp_team_ref_empty() -> None:
    ref = TeamCompTeamRef.from_dict({})
    assert ref.common_name.default is None
    assert ref.abbrev is None
    assert ref.team_logo.light is None


# --------------------------------------------------------------------------
# TeamCompDistanceGame
# --------------------------------------------------------------------------

def test_team_comp_distance_game_fields() -> None:
    game = TeamCompDistanceGame.from_dict(COMPARISON_RESPONSE["skatingDistanceLast10"][0])
    assert game.game_center_link == "/gamecenter/col-vs-cgy/2026/03/30/2025021174"
    assert game.game_date == "2026-03-30"
    assert game.is_home_team is True
    assert game.distance_skated.imperial == 47.34
    assert game.distance_skated.metric == 76.18
    assert game.home_team.abbrev == "COL"
    assert game.away_team.abbrev == "CGY"


def test_team_comp_distance_game_empty() -> None:
    game = TeamCompDistanceGame.from_dict({})
    assert game.game_center_link is None
    assert game.game_date is None
    assert game.is_home_team is None
    assert game.distance_skated.imperial is None
    assert game.home_team.abbrev is None


# --------------------------------------------------------------------------
# TeamCompDistance
# --------------------------------------------------------------------------

def test_team_comp_distance_fields() -> None:
    d = TeamCompDistance.from_dict(COMPARISON_RESPONSE["skatingDistanceDetails"])
    assert d.distance_total.imperial == 3402.75
    assert d.distance_total.metric == 5475.92
    assert d.distance_per_60.imperial == 9.40
    assert d.distance_max_game.imperial == 51.12
    assert d.distance_max_game.overlay is not None
    assert d.distance_max_game.overlay.game_date == "2026-01-21"
    assert d.distance_max_period.overlay is not None


def test_team_comp_distance_overlay_no_player() -> None:
    d = TeamCompDistance.from_dict(COMPARISON_RESPONSE["skatingDistanceDetails"])
    assert d.distance_max_game.overlay
    assert d.distance_max_game.overlay.first_name.default is None


def test_team_comp_distance_empty() -> None:
    d = TeamCompDistance.from_dict({})
    assert d.distance_total.imperial is None
    assert d.distance_max_game.overlay is None


# --------------------------------------------------------------------------
# TeamCompShotLocationDetail / TeamCompShotLocationTotal
# --------------------------------------------------------------------------

def test_team_comp_shot_location_detail_fields() -> None:
    detail = TeamCompShotLocationDetail.from_dict({"area": "High Slot", "sog": 273, "goals": 41, "shootingPctg": 0.1502})
    assert detail.area == "High Slot"
    assert detail.sog == 273
    assert detail.goals == 41
    assert detail.shooting_pctg == 0.1502


def test_team_comp_shot_location_detail_empty() -> None:
    detail = TeamCompShotLocationDetail.from_dict({})
    assert detail.area is None
    assert detail.sog is None


def test_team_comp_shot_location_total_fields() -> None:
    total = TeamCompShotLocationTotal.from_dict({"locationCode": "all", "sog": 2471, "goals": 274, "shootingPctg": 0.1109})
    assert total.location_code == "all"
    assert total.sog == 2471
    assert total.goals == 274
    assert total.shooting_pctg == 0.1109


def test_team_comp_shot_location_total_empty() -> None:
    total = TeamCompShotLocationTotal.from_dict({})
    assert total.location_code is None
    assert total.sog is None


# --------------------------------------------------------------------------
# TeamCompZoneTime
# --------------------------------------------------------------------------

def test_team_comp_zone_time_fields() -> None:
    zt = TeamCompZoneTime.from_dict(COMPARISON_RESPONSE["zoneTimeDetails"])
    assert zt.offensive_zone_pctg == 0.4286305
    assert zt.offensive_zone_league_avg == 0.4107842
    assert zt.neutral_zone_pctg == 0.1815559
    assert zt.neutral_zone_league_avg == 0.1784317
    assert zt.defensive_zone_pctg == 0.3898136
    assert zt.defensive_zone_league_avg == 0.4107842


def test_team_comp_zone_time_empty() -> None:
    zt = TeamCompZoneTime.from_dict({})
    assert zt.offensive_zone_pctg is None
    assert zt.defensive_zone_league_avg is None


# --------------------------------------------------------------------------
# TeamShotDifferential
# --------------------------------------------------------------------------

def test_team_shot_differential_fields() -> None:
    sd = TeamShotDifferential.from_dict({"shotAttemptDifferential": 7.684932, "sogDifferential": 0.141059})
    assert sd.shot_attempt_differential == 7.684932
    assert sd.sog_differential == 0.141059


def test_team_shot_differential_empty() -> None:
    sd = TeamShotDifferential.from_dict({})
    assert sd.shot_attempt_differential is None
    assert sd.sog_differential is None


# --------------------------------------------------------------------------
# TeamComparisonResult (top-level)
# --------------------------------------------------------------------------

def test_team_comparison_result_from_dict() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert isinstance(result, TeamComparisonResult)


def test_team_comparison_result_team() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert result.team.abbrev == "COL"
    assert result.team.wins == 49


def test_team_comparison_result_seasons() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert len(result.seasons_with_edge) == 2
    assert result.seasons_with_edge[0].id == 20242025


def test_team_comparison_result_shot_speed() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert result.shot_speed.top_shot_speed.imperial == 98.21
    assert result.shot_speed.shot_attempts_90_100 == 57


def test_team_comparison_result_skating_speed() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert result.skating_speed.max_skating_speed.imperial == 24.01
    assert result.skating_speed.bursts_over_22 == 152


def test_team_comparison_result_last_10() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert len(result.skating_distance_last_10) == 1
    assert result.skating_distance_last_10[0].game_date == "2026-03-30"
    assert result.skating_distance_last_10[0].is_home_team is True


def test_team_comparison_result_distance() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert result.distance.distance_total.imperial == 3402.75
    assert result.distance.distance_max_game.overlay
    assert result.distance.distance_max_game.overlay.game_date == "2026-01-21"


def test_team_comparison_result_shot_location() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert len(result.shot_location_details) == 2
    assert result.shot_location_details[0].area == "High Slot"
    assert len(result.shot_location_totals) == 2
    assert result.shot_location_totals[0].location_code == "all"


def test_team_comparison_result_zone_time() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert result.zone_time.offensive_zone_pctg == 0.4286305
    assert result.zone_time.offensive_zone_league_avg == 0.4107842


def test_team_comparison_result_shot_differential() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    assert result.shot_differential.shot_attempt_differential == 7.684932
    assert result.shot_differential.sog_differential == 0.141059


def test_team_comparison_result_empty() -> None:
    result = TeamComparisonResult.from_dict({})
    assert result.team.id is None
    assert result.seasons_with_edge == []
    assert result.skating_distance_last_10 == []
    assert result.shot_location_details == []
    assert result.shot_location_totals == []
    assert result.shot_differential.shot_attempt_differential is None


def test_team_comparison_result_to_dict() -> None:
    result = TeamComparisonResult.from_dict(COMPARISON_RESPONSE)
    d = result.to_dict()
    assert d["team"]["abbrev"] == "COL"
    assert d["shot_speed"]["shot_attempts_90_100"] == 57
    assert d["skating_speed"]["bursts_over_22"] == 152
    assert len(d["skating_distance_last_10"]) == 1
    assert d["skating_distance_last_10"][0]["is_home_team"] is True
    assert len(d["shot_location_details"]) == 2
    assert d["shot_differential"]["shot_attempt_differential"] == 7.684932
