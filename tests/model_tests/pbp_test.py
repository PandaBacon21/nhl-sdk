"""
Tests for play-by-play models:
  PbpTeam, PlayDetails, Play, PlayByPlayResult
"""
from nhl_stats.models.games.pbp.pbp_result import (
    PbpTeam, PlayDetails, Play, PlayByPlayResult,
)


AWAY_TEAM = {
    "id": 23,
    "commonName": {"default": "Canucks"},
    "abbrev": "VAN",
    "score": 1,
    "sog": 21,
    "logo": "https://assets.nhle.com/logos/nhl/svg/VAN_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/VAN_dark.svg",
    "placeName": {"default": "Vancouver"},
    "placeNameWithPreposition": {"default": "Vancouver", "fr": "de Vancouver"},
}

HOME_TEAM = {
    "id": 21,
    "commonName": {"default": "Avalanche"},
    "abbrev": "COL",
    "score": 3,
    "sog": 31,
    "logo": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/COL_dark.svg",
    "placeName": {"default": "Colorado"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
}

FACEOFF_PLAY = {
    "eventId": 53,
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "timeInPeriod": "00:00",
    "timeRemaining": "20:00",
    "situationCode": "1551",
    "homeTeamDefendingSide": "right",
    "typeCode": 502,
    "typeDescKey": "faceoff",
    "sortOrder": 11,
    "details": {
        "eventOwnerTeamId": 23,
        "losingPlayerId": 8477492,
        "winningPlayerId": 8480012,
        "xCoord": 0,
        "yCoord": 0,
        "zoneCode": "N",
    },
}

GOAL_PLAY = {
    "eventId": 95,
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "timeInPeriod": "02:55",
    "timeRemaining": "17:05",
    "situationCode": "1551",
    "homeTeamDefendingSide": "right",
    "typeCode": 505,
    "typeDescKey": "goal",
    "sortOrder": 52,
    "details": {
        "xCoord": 85,
        "yCoord": 4,
        "zoneCode": "O",
        "shotType": "backhand",
        "scoringPlayerId": 8481024,
        "scoringPlayerTotal": 5,
        "assist1PlayerId": 8483395,
        "assist1PlayerTotal": 4,
        "assist2PlayerId": 8482691,
        "assist2PlayerTotal": 6,
        "eventOwnerTeamId": 23,
        "goalieInNetId": 8475809,
        "awayScore": 1,
        "homeScore": 0,
        "highlightClipSharingUrl": "https://nhl.com/video/example",
        "highlightClip": 6385878785112,
        "discreteClip": 6385879567112,
    },
    "pptReplayUrl": "https://wsr.nhle.com/sprites/20252026/2025020417/ev95.json",
}

PENALTY_PLAY = {
    "eventId": 144,
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "timeInPeriod": "06:56",
    "timeRemaining": "13:04",
    "situationCode": "1451",
    "homeTeamDefendingSide": "right",
    "typeCode": 509,
    "typeDescKey": "penalty",
    "sortOrder": 103,
    "details": {
        "xCoord": -25,
        "yCoord": 21,
        "zoneCode": "D",
        "typeCode": "MIN",
        "descKey": "high-sticking",
        "duration": 2,
        "committedByPlayerId": 8477969,
        "drawnByPlayerId": 8475754,
        "eventOwnerTeamId": 23,
    },
}

PERIOD_START_PLAY = {
    "eventId": 54,
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "timeInPeriod": "00:00",
    "timeRemaining": "20:00",
    "situationCode": "1551",
    "homeTeamDefendingSide": "right",
    "typeCode": 520,
    "typeDescKey": "period-start",
    "sortOrder": 9,
}

GAME_DATA = {
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
    "tvBroadcasts": [
        {"id": 2, "market": "H", "countryCode": "US", "network": "ALT", "sequenceNumber": 385},
    ],
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "awayTeam": AWAY_TEAM,
    "homeTeam": HOME_TEAM,
    "shootoutInUse": True,
    "otInUse": True,
    "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
    "displayPeriod": 1,
    "maxPeriods": 5,
    "gameOutcome": {"lastPeriodType": "REG"},
    "plays": [PERIOD_START_PLAY, FACEOFF_PLAY, GOAL_PLAY, PENALTY_PLAY],
}


# ==========================================================================
# PBP TEAM
# ==========================================================================

def test_pbp_team_away() -> None:
    t = PbpTeam.from_dict(AWAY_TEAM)
    assert t.id == 23
    assert t.common_name.default == "Canucks"
    assert t.abbrev == "VAN"
    assert t.score == 1
    assert t.sog == 21
    assert t.logo is not None
    assert t.dark_logo is not None
    assert t.place_name.default == "Vancouver"
    assert t.place_name_with_preposition.get_locale("fr") == "de Vancouver"


def test_pbp_team_home() -> None:
    t = PbpTeam.from_dict(HOME_TEAM)
    assert t.id == 21
    assert t.abbrev == "COL"
    assert t.score == 3
    assert t.sog == 31


def test_pbp_team_empty() -> None:
    t = PbpTeam.from_dict({})
    assert t.id is None
    assert t.common_name.default is None
    assert t.abbrev is None
    assert t.score is None
    assert t.sog is None
    assert t.logo is None
    assert t.dark_logo is None


# ==========================================================================
# PLAY DETAILS
# ==========================================================================

def test_play_details_faceoff() -> None:
    d = PlayDetails.from_dict(FACEOFF_PLAY["details"])
    assert d.event_owner_team_id == 23
    assert d.losing_player_id == 8477492
    assert d.winning_player_id == 8480012
    assert d.x_coord == 0
    assert d.y_coord == 0
    assert d.zone_code == "N"


def test_play_details_goal() -> None:
    d = PlayDetails.from_dict(GOAL_PLAY["details"])
    assert d.scoring_player_id == 8481024
    assert d.scoring_player_total == 5
    assert d.assist1_player_id == 8483395
    assert d.assist1_player_total == 4
    assert d.assist2_player_id == 8482691
    assert d.goalie_in_net_id == 8475809
    assert d.away_score == 1
    assert d.home_score == 0
    assert d.shot_type == "backhand"
    assert d.highlight_clip == 6385878785112
    assert d.discrete_clip == 6385879567112


def test_play_details_penalty() -> None:
    d = PlayDetails.from_dict(PENALTY_PLAY["details"])
    assert d.penalty_type_code == "MIN"
    assert d.penalty_desc_key == "high-sticking"
    assert d.duration == 2
    assert d.committed_by_player_id == 8477969
    assert d.drawn_by_player_id == 8475754
    assert d.zone_code == "D"


def test_play_details_empty() -> None:
    d = PlayDetails.from_dict({})
    assert d.event_owner_team_id is None
    assert d.scoring_player_id is None
    assert d.penalty_type_code is None
    assert d.duration is None


# ==========================================================================
# PLAY
# ==========================================================================

def test_play_faceoff() -> None:
    p = Play.from_dict(FACEOFF_PLAY)
    assert p.event_id == 53
    assert p.type_desc_key == "faceoff"
    assert p.type_code == 502
    assert p.time_in_period == "00:00"
    assert p.time_remaining == "20:00"
    assert p.situation_code == "1551"
    assert p.home_team_defending_side == "right"
    assert p.sort_order == 11
    assert p.period_descriptor is not None
    assert p.period_descriptor.number == 1
    assert p.details is not None
    assert p.details.winning_player_id == 8480012
    assert p.ppt_replay_url is None


def test_play_goal_with_replay_url() -> None:
    p = Play.from_dict(GOAL_PLAY)
    assert p.event_id == 95
    assert p.type_desc_key == "goal"
    assert p.details is not None
    assert p.details.scoring_player_id == 8481024
    assert p.ppt_replay_url is not None


def test_play_penalty() -> None:
    p = Play.from_dict(PENALTY_PLAY)
    assert p.type_desc_key == "penalty"
    assert p.details.penalty_type_code == "MIN"
    assert p.details.duration == 2


def test_play_no_details() -> None:
    p = Play.from_dict(PERIOD_START_PLAY)
    assert p.event_id == 54
    assert p.type_desc_key == "period-start"
    assert p.details is None
    assert p.ppt_replay_url is None


def test_play_empty() -> None:
    p = Play.from_dict({})
    assert p.event_id is None
    assert p.period_descriptor is None
    assert p.details is None
    assert p.type_desc_key is None


# ==========================================================================
# PLAY BY PLAY RESULT
# ==========================================================================

def test_pbp_result_from_dict() -> None:
    result = PlayByPlayResult.from_dict(GAME_DATA)
    assert result.id == 2025020417
    assert result.season == 20252026
    assert result.game_type == 2
    assert result.limited_scoring is False
    assert result.game_date == "2025-12-02"
    assert result.venue.default == "Ball Arena"
    assert result.venue_location.default == "Denver"
    assert result.game_state == "OFF"
    assert len(result.tv_broadcasts) == 1
    assert result.tv_broadcasts[0].network == "ALT"
    assert result.period_descriptor.period_type == "REG"
    assert result.away_team.abbrev == "VAN"
    assert result.home_team.abbrev == "COL"
    assert result.shootout_in_use is True
    assert result.ot_in_use is True
    assert result.clock is not None
    assert result.clock.running is False
    assert result.display_period == 1
    assert result.max_periods == 5
    assert result.game_outcome.last_period_type == "REG"
    assert len(result.plays) == 4


def test_pbp_result_play_types() -> None:
    result = PlayByPlayResult.from_dict(GAME_DATA)
    by_type = {p.type_desc_key: p for p in result.plays}
    assert "period-start" in by_type
    assert "faceoff" in by_type
    assert "goal" in by_type
    assert "penalty" in by_type
    assert by_type["goal"].details.scoring_player_id == 8481024
    assert by_type["penalty"].details.duration == 2


def test_pbp_result_no_clock() -> None:
    data = {**GAME_DATA}
    data.pop("clock")
    result = PlayByPlayResult.from_dict(data)
    assert result.clock is None


def test_pbp_result_empty() -> None:
    result = PlayByPlayResult.from_dict({})
    assert result.id is None
    assert result.tv_broadcasts == []
    assert result.period_descriptor is None
    assert result.clock is None
    assert result.game_outcome is None
    assert result.plays == []
