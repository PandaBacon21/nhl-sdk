"""
Tests for game landing models:
  GoalAssist, ScoringGoal, ScoringPeriod, ThreeStar,
  PenaltyPlayer, LandingPenalty, PenaltyPeriod, GameSummary, GameLandingResult
"""
from nhl_sdk.models.games.landing.landing_result import (
    GoalAssist,
    ScoringGoal,
    ScoringPeriod,
    ThreeStar,
    PenaltyPlayer,
    LandingPenalty,
    PenaltyPeriod,
    GameSummary,
    GameLandingResult,
)


ASSIST_DATA = {
    "playerId": 8483395,
    "firstName": {"default": "Arshdeep"},
    "lastName": {"default": "Bains"},
    "name": {"default": "A. Bains"},
    "assistsToDate": 4,
    "sweaterNumber": 13,
}

GOAL_DATA = {
    "situationCode": "1551",
    "eventId": 95,
    "strength": "ev",
    "playerId": 8481024,
    "firstName": {"default": "Linus"},
    "lastName": {"default": "Karlsson"},
    "name": {"default": "L. Karlsson"},
    "teamAbbrev": {"default": "VAN"},
    "headshot": "https://assets.nhle.com/mugs/nhl/20252026/VAN/8481024.png",
    "highlightClipSharingUrl": "https://nhl.com/video/van-col-karlsson",
    "highlightClipSharingUrlFr": "https://nhl.com/fr/video/van-col-karlsson",
    "highlightClip": 6385878785112,
    "highlightClipFr": 6385877180112,
    "discreteClip": 6385879567112,
    "discreteClipFr": 6385879181112,
    "goalsToDate": 5,
    "awayScore": 1,
    "homeScore": 0,
    "leadingTeamAbbrev": {"default": "VAN"},
    "timeInPeriod": "02:55",
    "shotType": "backhand",
    "goalModifier": "none",
    "assists": [ASSIST_DATA],
    "pptReplayUrl": "https://wsr.nhle.com/sprites/20252026/2025020417/ev95.json",
    "homeTeamDefendingSide": "right",
    "isHome": False,
}

PENALTY_DATA = {
    "timeInPeriod": "06:56",
    "type": "MIN",
    "duration": 2,
    "committedByPlayer": {
        "firstName": {"default": "Marcus"},
        "lastName": {"default": "Pettersson"},
        "sweaterNumber": 29,
    },
    "teamAbbrev": {"default": "VAN"},
    "drawnBy": {
        "firstName": {"default": "Brock"},
        "lastName": {"default": "Nelson"},
        "sweaterNumber": 11,
    },
    "descKey": "high-sticking",
}

BENCH_PENALTY_DATA = {
    "timeInPeriod": "01:05",
    "type": "BEN",
    "duration": 2,
    "teamAbbrev": {"default": "COL"},
    "descKey": "too-many-men-on-the-ice",
    "servedBy": {"default": "Z. Bardakov"},
}

THREE_STAR_DATA = {
    "star": 1,
    "playerId": 8477492,
    "teamAbbrev": "COL",
    "headshot": "https://assets.nhle.com/mugs/nhl/20252026/COL/8477492.png",
    "name": {"default": "N. MacKinnon"},
    "sweaterNo": 29,
    "position": "C",
    "goals": 2,
    "assists": 0,
    "points": 2,
}

SUMMARY_DATA = {
    "scoring": [
        {
            "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
            "goals": [GOAL_DATA],
        }
    ],
    "threeStars": [THREE_STAR_DATA],
    "penalties": [
        {
            "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
            "penalties": [PENALTY_DATA],
        }
    ],
}

LANDING_DATA = {
    "id": 2025020417,
    "season": 20252026,
    "gameType": 2,
    "limitedScoring": False,
    "gameDate": "2025-12-02",
    "venue": {"default": "Ball Arena"},
    "venueLocation": {"default": "Denver"},
    "startTimeUTC": "2025-12-03T02:00:00Z",
    "easternUTCOffset": "-05:00",
    "venueUTCOffset": "-07:00",
    "venueTimezone": "America/Denver",
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "tvBroadcasts": [{"id": 290, "market": "A", "countryCode": "CA", "network": "SNP", "sequenceNumber": 33}],
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "awayTeam": {
        "id": 23, "commonName": {"default": "Canucks"}, "abbrev": "VAN",
        "score": 1, "sog": 21, "logo": "", "darkLogo": "",
        "placeName": {"default": "Vancouver"}, "placeNameWithPreposition": {"default": "Vancouver"},
    },
    "homeTeam": {
        "id": 21, "commonName": {"default": "Avalanche"}, "abbrev": "COL",
        "score": 3, "sog": 31, "logo": "", "darkLogo": "",
        "placeName": {"default": "Colorado"}, "placeNameWithPreposition": {"default": "Colorado"},
    },
    "shootoutInUse": True,
    "maxPeriods": 5,
    "regPeriods": 3,
    "otInUse": True,
    "tiesInUse": False,
    "summary": SUMMARY_DATA,
    "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
}


# ==========================================================================
# GoalAssist
# ==========================================================================

def test_goal_assist_fields() -> None:
    a = GoalAssist.from_dict(ASSIST_DATA)
    assert a.player_id == 8483395
    assert a.first_name.default == "Arshdeep"
    assert a.last_name.default == "Bains"
    assert a.name.default == "A. Bains"
    assert a.assists_to_date == 4
    assert a.sweater_number == 13


def test_goal_assist_empty() -> None:
    a = GoalAssist.from_dict({})
    assert a.player_id is None
    assert a.assists_to_date is None
    assert a.sweater_number is None


# ==========================================================================
# ScoringGoal
# ==========================================================================

def test_scoring_goal_fields() -> None:
    g = ScoringGoal.from_dict(GOAL_DATA)
    assert g.event_id == 95
    assert g.strength == "ev"
    assert g.player_id == 8481024
    assert g.name.default == "L. Karlsson"
    assert g.team_abbrev.default == "VAN"
    assert g.goals_to_date == 5
    assert g.away_score == 1
    assert g.home_score == 0
    assert g.leading_team_abbrev.default == "VAN"
    assert g.time_in_period == "02:55"
    assert g.shot_type == "backhand"
    assert g.goal_modifier == "none"
    assert g.is_home is False
    assert g.highlight_clip == 6385878785112
    assert g.discrete_clip == 6385879567112


def test_scoring_goal_assists() -> None:
    g = ScoringGoal.from_dict(GOAL_DATA)
    assert len(g.assists) == 1
    assert g.assists[0].name.default == "A. Bains"
    assert g.assists[0].sweater_number == 13


def test_scoring_goal_no_assists() -> None:
    data = {**GOAL_DATA, "assists": []}
    g = ScoringGoal.from_dict(data)
    assert g.assists == []


def test_scoring_goal_no_leading_team() -> None:
    data = {k: v for k, v in GOAL_DATA.items() if k != "leadingTeamAbbrev"}
    g = ScoringGoal.from_dict(data)
    assert g.leading_team_abbrev.default is None


# ==========================================================================
# ScoringPeriod
# ==========================================================================

def test_scoring_period_fields() -> None:
    sp = ScoringPeriod.from_dict(SUMMARY_DATA["scoring"][0])
    assert sp.period_descriptor.number == 1
    assert sp.period_descriptor.period_type == "REG"
    assert len(sp.goals) == 1
    assert sp.goals[0].strength == "ev"


def test_scoring_period_no_goals() -> None:
    sp = ScoringPeriod.from_dict({"periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3}, "goals": []})
    assert sp.goals == []


# ==========================================================================
# ThreeStar
# ==========================================================================

def test_three_star_fields() -> None:
    s = ThreeStar.from_dict(THREE_STAR_DATA)
    assert s.star == 1
    assert s.player_id == 8477492
    assert s.team_abbrev == "COL"
    assert s.name.default == "N. MacKinnon"
    assert s.sweater_no == 29
    assert s.position == "C"
    assert s.goals == 2
    assert s.assists == 0
    assert s.points == 2


def test_three_star_empty() -> None:
    s = ThreeStar.from_dict({})
    assert s.star is None
    assert s.player_id is None
    assert s.team_abbrev is None


# ==========================================================================
# PenaltyPlayer
# ==========================================================================

def test_penalty_player_fields() -> None:
    pp = PenaltyPlayer.from_dict(PENALTY_DATA["committedByPlayer"])
    assert pp.first_name.default == "Marcus"
    assert pp.last_name.default == "Pettersson"
    assert pp.sweater_number == 29


# ==========================================================================
# LandingPenalty
# ==========================================================================

def test_landing_penalty_fields() -> None:
    p = LandingPenalty.from_dict(PENALTY_DATA)
    assert p.time_in_period == "06:56"
    assert p.type == "MIN"
    assert p.duration == 2
    assert p.desc_key == "high-sticking"
    assert p.team_abbrev.default == "VAN"
    assert p.committed_by_player.last_name.default == "Pettersson"
    assert p.drawn_by.first_name.default == "Brock"


def test_landing_penalty_bench() -> None:
    p = LandingPenalty.from_dict(BENCH_PENALTY_DATA)
    assert p.type == "BEN"
    assert p.committed_by_player is None
    assert p.drawn_by is None
    assert p.served_by.default == "Z. Bardakov"
    assert p.team_abbrev.default == "COL"


# ==========================================================================
# PenaltyPeriod
# ==========================================================================

def test_penalty_period_fields() -> None:
    pp = PenaltyPeriod.from_dict(SUMMARY_DATA["penalties"][0])
    assert pp.period_descriptor.number == 1
    assert len(pp.penalties) == 1
    assert pp.penalties[0].type == "MIN"


def test_penalty_period_empty() -> None:
    pp = PenaltyPeriod.from_dict({"periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3}, "penalties": []})
    assert pp.penalties == []


# ==========================================================================
# GameSummary
# ==========================================================================

def test_game_summary_fields() -> None:
    s = GameSummary.from_dict(SUMMARY_DATA)
    assert len(s.scoring) == 1
    assert len(s.three_stars) == 1
    assert len(s.penalties) == 1
    assert s.scoring[0].period_descriptor.number == 1
    assert s.three_stars[0].star == 1
    assert s.penalties[0].period_descriptor.number == 1


def test_game_summary_empty() -> None:
    s = GameSummary.from_dict({"scoring": [], "threeStars": [], "penalties": []})
    assert s.scoring == []
    assert s.three_stars == []
    assert s.penalties == []


# ==========================================================================
# GameLandingResult
# ==========================================================================

def test_landing_result_fields() -> None:
    r = GameLandingResult.from_dict(LANDING_DATA)
    assert r.id == 2025020417
    assert r.season == 20252026
    assert r.game_type == 2
    assert r.limited_scoring is False
    assert r.game_date == "2025-12-02"
    assert r.venue.default == "Ball Arena"
    assert r.venue_location.default == "Denver"
    assert r.venue_timezone == "America/Denver"
    assert r.game_state == "OFF"
    assert r.game_schedule_state == "OK"
    assert r.shootout_in_use is True
    assert r.max_periods == 5
    assert r.reg_periods == 3
    assert r.ot_in_use is True
    assert r.ties_in_use is False


def test_landing_result_teams() -> None:
    r = GameLandingResult.from_dict(LANDING_DATA)
    assert r.away_team.abbrev == "VAN"
    assert r.away_team.score == 1
    assert r.home_team.abbrev == "COL"
    assert r.home_team.score == 3


def test_landing_result_period_descriptor() -> None:
    r = GameLandingResult.from_dict(LANDING_DATA)
    assert r.period_descriptor.number == 3
    assert r.period_descriptor.period_type == "REG"


def test_landing_result_tv_broadcasts() -> None:
    r = GameLandingResult.from_dict(LANDING_DATA)
    assert len(r.tv_broadcasts) == 1
    assert r.tv_broadcasts[0].network == "SNP"


def test_landing_result_clock() -> None:
    r = GameLandingResult.from_dict(LANDING_DATA)
    assert r.clock.time_remaining == "00:00"
    assert r.clock.running is False


def test_landing_result_summary() -> None:
    r = GameLandingResult.from_dict(LANDING_DATA)
    assert r.summary is not None
    assert len(r.summary.scoring) == 1
    assert len(r.summary.three_stars) == 1
    assert r.summary.scoring[0].goals[0].player_id == 8481024
    assert r.summary.three_stars[0].name.default == "N. MacKinnon"


def test_landing_result_no_summary() -> None:
    data = {k: v for k, v in LANDING_DATA.items() if k != "summary"}
    r = GameLandingResult.from_dict(data)
    assert r.summary is None


def test_landing_result_empty() -> None:
    r = GameLandingResult.from_dict({})
    assert r.id is None
    assert r.summary is None
    assert r.clock is None
