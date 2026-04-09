"""
Tests for team edge detail models: TeamDetailResult and sub-models.
"""
from nhl_sdk.models.teams.team.edge.team_details.team_details_result import (
    TeamDetailResult, TeamDetailTeam, TeamEdgeLogo,
    TeamShotSpeed, TeamSkatingSpeed, TeamDistanceSkated,
    TeamSogSummary, TeamSogDetail, TeamZoneTimeDetails,
)
from nhl_sdk.models.teams.team.edge.team_edge_types import TeamEdgeMeasurement, TeamEdgeCount


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

TEAM_DATA = {
    "id": 21,
    "commonName": {"default": "Avalanche"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
    "abbrev": "COL",
    "teamLogo": {"light": "https://example.com/light.svg", "dark": "https://example.com/dark.svg"},
    "slug": "colorado-avalanche-21",
    "conference": "Western",
    "division": "Central",
    "wins": 49,
    "losses": 14,
    "otLosses": 10,
    "gamesPlayed": 73,
    "points": 108,
}

DETAIL_RESPONSE = {
    "team": TEAM_DATA,
    "seasonsWithEdgeStats": [
        {"id": 20242025, "gameTypes": [2, 3]},
        {"id": 20252026, "gameTypes": [2]},
    ],
    "shotSpeed": {
        "shotAttemptsOver90": {"value": 57, "rank": 12},
        "topShotSpeed": {
            "imperial": 98.21, "metric": 158.05, "rank": 23,
            "leagueAvg": {"imperial": 99.35, "metric": 159.89},
            "overlay": OVERLAY,
        },
    },
    "skatingSpeed": {
        "burstsOver22": {"value": 152, "rank": 2},
        "burstsOver20": {"value": 2394, "rank": 1, "leagueAvg": {"value": 1593}},
        "speedMax": {
            "imperial": 24.01, "metric": 38.65, "rank": 8,
            "leagueAvg": {"imperial": 23.74, "metric": 38.20},
            "overlay": OVERLAY,
        },
    },
    "distanceSkated": {
        "total": {
            "imperial": 3402.75, "metric": 5475.92, "rank": 5,
            "leagueAvg": {"imperial": 3344.17, "metric": 5381.66},
        },
    },
    "sogSummary": [
        {
            "locationCode": "all",
            "shots": 2471, "shotsRank": 1, "shotsLeagueAvg": 2057.0,
            "shootingPctg": 0.1109, "shootingPctgRank": 14, "shootingPctgLeagueAvg": 0.1099,
            "goals": 274, "goalsRank": 1, "goalsLeagueAvg": 226.06,
        },
        {
            "locationCode": "high",
            "shots": 633, "shotsRank": 6, "shotsLeagueAvg": 584.66,
            "shootingPctg": 0.1801, "shootingPctgRank": 23, "shootingPctgLeagueAvg": 0.1916,
            "goals": 114, "goalsRank": 13, "goalsLeagueAvg": 112.0,
        },
    ],
    "sogDetails": [
        {"area": "Behind the Net", "shots": 13, "shotsRank": 20},
        {"area": "High Slot", "shots": 273, "shotsRank": 1},
    ],
    "zoneTimeDetails": {
        "offensiveZonePctg": 0.4286305,
        "offensiveZoneRank": 3,
        "offensiveZoneLeagueAvg": 0.4107842,
        "offensiveZoneEvPctg": 0.4232852,
        "offensiveZoneEvRank": 4,
        "offensiveZoneEvLeagueAvg": 0.4074362,
        "neutralZonePctg": 0.1815559,
        "neutralZoneRank": 8,
        "neutralZoneLeagueAvg": 0.1784317,
        "defensiveZonePctg": 0.3898136,
        "defensiveZoneRank": 3,
        "defensiveZoneLeagueAvg": 0.4107842,
    },
}


# --------------------------------------------------------------------------
# TeamEdgeLogo
# --------------------------------------------------------------------------

def test_team_edge_logo_from_dict() -> None:
    logo = TeamEdgeLogo.from_dict({"light": "light.svg", "dark": "dark.svg"})
    assert logo.light == "light.svg"
    assert logo.dark == "dark.svg"


def test_team_edge_logo_empty() -> None:
    logo = TeamEdgeLogo.from_dict({})
    assert logo.light is None
    assert logo.dark is None


# --------------------------------------------------------------------------
# TeamEdgeMeasurement
# --------------------------------------------------------------------------

def test_team_edge_measurement_fields() -> None:
    m = TeamEdgeMeasurement.from_dict({
        "imperial": 98.21, "metric": 158.05, "rank": 23,
        "leagueAvg": {"imperial": 99.35, "metric": 159.89},
        "overlay": OVERLAY,
    })
    assert m.imperial == 98.21
    assert m.metric == 158.05
    assert m.rank == 23
    assert m.league_avg.imperial == 99.35
    assert m.overlay is not None
    assert m.overlay.first_name.default == "Cale"


def test_team_edge_measurement_no_overlay() -> None:
    m = TeamEdgeMeasurement.from_dict({"imperial": 1.0, "metric": 2.0, "rank": 5})
    assert m.overlay is None


# --------------------------------------------------------------------------
# TeamEdgeCount
# --------------------------------------------------------------------------

def test_team_edge_count_plain_rank() -> None:
    c = TeamEdgeCount.from_dict({"value": 57, "rank": 12})
    assert c.value == 57
    assert c.rank == 12
    assert c.league_avg is None


def test_team_edge_count_league_avg_dict() -> None:
    c = TeamEdgeCount.from_dict({"value": 2394, "rank": 1, "leagueAvg": {"value": 1593}})
    assert c.league_avg == 1593


# --------------------------------------------------------------------------
# TeamDetailTeam
# --------------------------------------------------------------------------

def test_team_detail_team_fields() -> None:
    t = TeamDetailTeam.from_dict(TEAM_DATA)
    assert t.id == 21
    assert t.common_name.default == "Avalanche"
    assert t.place_name_with_preposition.default == "Colorado"
    assert t.abbrev == "COL"
    assert t.team_logo.light == "https://example.com/light.svg"
    assert t.slug == "colorado-avalanche-21"
    assert t.conference == "Western"
    assert t.division == "Central"
    assert t.wins == 49
    assert t.losses == 14
    assert t.ot_losses == 10
    assert t.games_played == 73
    assert t.points == 108


# --------------------------------------------------------------------------
# TeamShotSpeed / TeamSkatingSpeed / TeamDistanceSkated
# --------------------------------------------------------------------------

def test_team_shot_speed() -> None:
    ss = TeamShotSpeed.from_dict(DETAIL_RESPONSE["shotSpeed"])
    assert ss.shot_attempts_over_90.value == 57
    assert ss.shot_attempts_over_90.rank == 12
    assert ss.top_shot_speed.imperial == 98.21
    assert ss.top_shot_speed.rank == 23


def test_team_skating_speed() -> None:
    sk = TeamSkatingSpeed.from_dict(DETAIL_RESPONSE["skatingSpeed"])
    assert sk.bursts_over_22.value == 152
    assert sk.bursts_over_22.rank == 2
    assert sk.bursts_over_20.league_avg == 1593
    assert sk.speed_max.rank == 8


def test_team_distance_skated() -> None:
    d = TeamDistanceSkated.from_dict(DETAIL_RESPONSE["distanceSkated"])
    assert d.total.imperial == 3402.75
    assert d.total.rank == 5


# --------------------------------------------------------------------------
# TeamSogSummary / TeamSogDetail
# --------------------------------------------------------------------------

def test_team_sog_summary() -> None:
    entry = TeamSogSummary.from_dict(DETAIL_RESPONSE["sogSummary"][0])
    assert entry.location_code == "all"
    assert entry.shots == 2471
    assert entry.shots_rank == 1
    assert entry.shots_league_avg == 2057.0
    assert entry.shooting_pctg == 0.1109
    assert entry.shooting_pctg_rank == 14
    assert entry.goals == 274
    assert entry.goals_rank == 1


def test_team_sog_detail() -> None:
    entry = TeamSogDetail.from_dict({"area": "High Slot", "shots": 273, "shotsRank": 1})
    assert entry.area == "High Slot"
    assert entry.shots == 273
    assert entry.shots_rank == 1


# --------------------------------------------------------------------------
# TeamZoneTimeDetails
# --------------------------------------------------------------------------

def test_team_zone_time_details() -> None:
    z = TeamZoneTimeDetails.from_dict(DETAIL_RESPONSE["zoneTimeDetails"])
    assert z.offensive_zone_pctg == 0.4286305
    assert z.offensive_zone_rank == 3
    assert z.offensive_zone_league_avg == 0.4107842
    assert z.offensive_zone_ev_pctg == 0.4232852
    assert z.offensive_zone_ev_rank == 4
    assert z.neutral_zone_rank == 8
    assert z.defensive_zone_rank == 3
    assert z.defensive_zone_league_avg == 0.4107842


# --------------------------------------------------------------------------
# TeamDetailResult (top-level)
# --------------------------------------------------------------------------

def test_team_detail_result_from_dict() -> None:
    result = TeamDetailResult.from_dict(DETAIL_RESPONSE)
    assert isinstance(result, TeamDetailResult)


def test_team_detail_result_team() -> None:
    result = TeamDetailResult.from_dict(DETAIL_RESPONSE)
    assert result.team.abbrev == "COL"


def test_team_detail_result_seasons() -> None:
    result = TeamDetailResult.from_dict(DETAIL_RESPONSE)
    assert len(result.seasons_with_edge) == 2
    assert result.seasons_with_edge[0].id == 20242025


def test_team_detail_result_sog_summary_list() -> None:
    result = TeamDetailResult.from_dict(DETAIL_RESPONSE)
    assert len(result.sog_summary) == 2
    assert result.sog_summary[0].location_code == "all"
    assert result.sog_summary[1].location_code == "high"


def test_team_detail_result_sog_details_list() -> None:
    result = TeamDetailResult.from_dict(DETAIL_RESPONSE)
    assert len(result.sog_details) == 2
    assert result.sog_details[1].area == "High Slot"


def test_team_detail_result_empty() -> None:
    result = TeamDetailResult.from_dict({})
    assert result.team.id is None
    assert result.seasons_with_edge == []
    assert result.sog_summary == []
    assert result.sog_details == []
