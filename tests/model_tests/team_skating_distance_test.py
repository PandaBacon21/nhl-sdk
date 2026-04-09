"""
Tests for TeamSkatingDistanceResult and sub-models.
"""
from nhl_sdk.models.teams.team.edge.team_skating_distance_details.team_skating_distance_detail import (
    TeamSkatingDistanceResult, TeamDistanceTeamRef,
    TeamDistanceLast10Game, TeamDistanceEntry,
)


OVERLAY = {
    "gameDate": "2026-01-21",
    "awayTeam": {"abbrev": "ANA", "score": 2},
    "homeTeam": {"abbrev": "COL", "score": 1},
    "gameOutcome": {"lastPeriodType": "SO"},
    "periodDescriptor": {"maxRegulationPeriods": 3, "number": 1, "periodType": "REG"},
    "gameType": 2,
}

COL_TEAM_REF = {
    "commonName": {"default": "Avalanche"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
    "teamLogo": {
        "light": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
        "dark": "https://assets.nhle.com/logos/nhl/svg/COL_dark.svg",
    },
}

CGY_TEAM_REF = {
    "commonName": {"default": "Flames"},
    "placeNameWithPreposition": {"default": "Calgary", "fr": "de Calgary"},
    "teamLogo": {
        "light": "https://assets.nhle.com/logos/nhl/svg/CGY_light.svg",
        "dark": "https://assets.nhle.com/logos/nhl/svg/CGY_dark.svg",
    },
}

LAST_10_GAME = {
    "gameCenterLink": "/gamecenter/cgy-vs-col/2026/03/30/2025021174",
    "gameDate": "2026-03-30",
    "isHomeTeam": True,
    "toiAll": 17880,
    "distanceSkatedAll": {"imperial": 47.3372, "metric": 76.1817},
    "toiEven": 15890,
    "distanceSkatedEven": {"imperial": 43.0565, "metric": 69.2925},
    "toiPP": 1510,
    "distanceSkatedPP": {"imperial": 3.1211, "metric": 5.0228},
    "toiPK": 480,
    "distanceSkatedPK": {"imperial": 1.1597, "metric": 1.8664},
    "homeTeam": COL_TEAM_REF,
    "awayTeam": CGY_TEAM_REF,
}

DISTANCE_ENTRY_ALL = {
    "strengthCode": "all",
    "positionCode": "all",
    "distanceTotal": {
        "imperial": 3402.7472, "metric": 5475.9236, "rank": 5,
        "leagueAvg": {"imperial": 3344.1691, "metric": 5381.6558},
    },
    "distancePer60": {
        "imperial": 9.4017, "metric": 15.1298, "rank": 1,
        "leagueAvg": {"imperial": 9.1628, "metric": 14.7454},
    },
    "distanceMaxGame": {
        "imperial": 51.1243, "metric": 82.2726, "rank": 1,
        "leagueAvg": {"imperial": 49.3794, "metric": 79.4645},
        "overlay": OVERLAY,
    },
    "distanceMaxPeriod": {
        "imperial": 16.9063, "metric": 27.2068, "rank": 2,
        "leagueAvg": {"imperial": 16.6007, "metric": 26.7150},
        "overlay": OVERLAY,
    },
}

DISTANCE_ENTRY_PP = {
    "strengthCode": "pp",
    "positionCode": "F",
    "distanceTotal": {
        "imperial": 213.6744, "metric": 343.8588, "rank": 2,
        "leagueAvg": {"imperial": 188.3040, "metric": 303.0311},
    },
    "distancePer60": {
        "imperial": 8.1581, "metric": 13.1286, "rank": 24,
        "leagueAvg": {"imperial": 8.2449, "metric": 13.2683},
    },
    "distanceMaxGame": {
        "imperial": 8.0544, "metric": 12.9617, "rank": 4,
        "leagueAvg": {"imperial": 6.3725, "metric": 10.2551},
        "overlay": OVERLAY,
    },
    "distanceMaxPeriod": {
        "imperial": 4.3240, "metric": 6.9585, "rank": 6,
        "leagueAvg": {"imperial": 3.7293, "metric": 6.0014},
        "overlay": OVERLAY,
    },
}

FULL_RESPONSE = {
    "skatingDistanceLast10": [LAST_10_GAME],
    "skatingDistanceDetails": [DISTANCE_ENTRY_ALL, DISTANCE_ENTRY_PP],
}


# --------------------------------------------------------------------------
# TeamDistanceTeamRef
# --------------------------------------------------------------------------

def test_team_distance_team_ref_fields() -> None:
    ref = TeamDistanceTeamRef.from_dict(COL_TEAM_REF)
    assert ref.common_name.default == "Avalanche"
    assert ref.place_name_with_preposition.default == "Colorado"
    assert ref.team_logo.light == "https://assets.nhle.com/logos/nhl/svg/COL_light.svg"


def test_team_distance_team_ref_empty() -> None:
    ref = TeamDistanceTeamRef.from_dict({})
    assert ref.common_name.default is None
    assert ref.team_logo.light is None


# --------------------------------------------------------------------------
# TeamDistanceLast10Game
# --------------------------------------------------------------------------

def test_team_distance_last_10_game_fields() -> None:
    game = TeamDistanceLast10Game.from_dict(LAST_10_GAME)
    assert game.game_center_link == "/gamecenter/cgy-vs-col/2026/03/30/2025021174"
    assert game.game_date == "2026-03-30"
    assert game.is_home_team is True
    assert game.toi_all == 17880
    assert game.distance_skated_all.imperial == 47.3372
    assert game.distance_skated_all.metric == 76.1817
    assert game.toi_even == 15890
    assert game.distance_skated_even.imperial == 43.0565
    assert game.toi_pp == 1510
    assert game.distance_skated_pp.imperial == 3.1211
    assert game.toi_pk == 480
    assert game.distance_skated_pk.imperial == 1.1597
    assert game.home_team.common_name.default == "Avalanche"
    assert game.away_team.common_name.default == "Flames"


def test_team_distance_last_10_game_empty() -> None:
    game = TeamDistanceLast10Game.from_dict({})
    assert game.game_center_link is None
    assert game.game_date is None
    assert game.is_home_team is None
    assert game.toi_all is None
    assert game.distance_skated_all.imperial is None
    assert game.home_team.common_name.default is None


# --------------------------------------------------------------------------
# TeamDistanceEntry
# --------------------------------------------------------------------------

def test_team_distance_entry_all_positions() -> None:
    entry = TeamDistanceEntry.from_dict(DISTANCE_ENTRY_ALL)
    assert entry.strength_code == "all"
    assert entry.position_code == "all"
    assert entry.distance_total.imperial == 3402.7472
    assert entry.distance_total.rank == 5
    assert entry.distance_total.league_avg.imperial == 3344.1691
    assert entry.distance_per_60.rank == 1
    assert entry.distance_max_game.imperial == 51.1243
    assert entry.distance_max_game.rank == 1
    assert entry.distance_max_game.overlay is not None
    assert entry.distance_max_game.overlay.game_date == "2026-01-21"
    assert entry.distance_max_period.rank == 2


def test_team_distance_entry_pp_forwards() -> None:
    entry = TeamDistanceEntry.from_dict(DISTANCE_ENTRY_PP)
    assert entry.strength_code == "pp"
    assert entry.position_code == "F"
    assert entry.distance_total.imperial == 213.6744
    assert entry.distance_total.rank == 2
    assert entry.distance_per_60.rank == 24


def test_team_distance_entry_empty() -> None:
    entry = TeamDistanceEntry.from_dict({})
    assert entry.strength_code is None
    assert entry.position_code is None
    assert entry.distance_total.imperial is None
    assert entry.distance_total.rank is None
    assert entry.distance_max_game.overlay is None


# --------------------------------------------------------------------------
# TeamSkatingDistanceResult (top-level)
# --------------------------------------------------------------------------

def test_team_skating_distance_result_from_dict() -> None:
    result = TeamSkatingDistanceResult.from_dict(FULL_RESPONSE)
    assert isinstance(result, TeamSkatingDistanceResult)


def test_team_skating_distance_result_last_10() -> None:
    result = TeamSkatingDistanceResult.from_dict(FULL_RESPONSE)
    assert len(result.skating_distance_last_10) == 1
    assert result.skating_distance_last_10[0].game_date == "2026-03-30"
    assert result.skating_distance_last_10[0].toi_all == 17880


def test_team_skating_distance_result_details() -> None:
    result = TeamSkatingDistanceResult.from_dict(FULL_RESPONSE)
    assert len(result.skating_distance_details) == 2
    assert result.skating_distance_details[0].strength_code == "all"
    assert result.skating_distance_details[1].strength_code == "pp"


def test_team_skating_distance_result_empty() -> None:
    result = TeamSkatingDistanceResult.from_dict({})
    assert result.skating_distance_last_10 == []
    assert result.skating_distance_details == []


def test_team_skating_distance_result_to_dict() -> None:
    result = TeamSkatingDistanceResult.from_dict(FULL_RESPONSE)
    d = result.to_dict()
    assert len(d["skating_distance_last_10"]) == 1
    assert d["skating_distance_last_10"][0]["toi_all"] == 17880
    assert d["skating_distance_last_10"][0]["is_home_team"] is True
    assert len(d["skating_distance_details"]) == 2
    assert d["skating_distance_details"][0]["strength_code"] == "all"
    assert d["skating_distance_details"][0]["distance_total"]["rank"] == 5
