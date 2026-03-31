"""
Tests for game story models:
  StoryTeam, StoryThreeStar, TeamGameStat, GameStorySummary, GameStoryResult
"""
from src.models.games.story.story_result import (
    StoryTeam,
    StoryThreeStar,
    TeamGameStat,
    GameStorySummary,
    GameStoryResult,
)


AWAY_TEAM_DATA = {
    "id": 23,
    "name": {"default": "Canucks"},
    "abbrev": "VAN",
    "placeName": {"default": "Vancouver"},
    "score": 1,
    "sog": 21,
    "logo": "https://assets.nhle.com/logos/nhl/svg/VAN_light.svg",
}

HOME_TEAM_DATA = {
    "id": 21,
    "name": {"default": "Avalanche"},
    "abbrev": "COL",
    "placeName": {"default": "Colorado"},
    "score": 3,
    "sog": 31,
    "logo": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
}

THREE_STAR_DATA = {
    "star": 1,
    "playerId": 8477492,
    "teamAbbrev": "COL",
    "headshot": "https://assets.nhle.com/mugs/nhl/20252026/COL/8477492.png",
    "name": "N. MacKinnon",
    "sweaterNo": 29,
    "position": "C",
    "goals": 2,
    "assists": 0,
    "points": 2,
}

TEAM_GAME_STAT_INT = {"category": "sog", "awayValue": 21, "homeValue": 31}
TEAM_GAME_STAT_FLOAT = {"category": "faceoffWinningPctg", "awayValue": 0.468085, "homeValue": 0.531915}
TEAM_GAME_STAT_STR = {"category": "powerPlay", "awayValue": "0/1", "homeValue": "0/1"}

SUMMARY_DATA = {
    "scoring": [
        {
            "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
            "goals": [
                {
                    "situationCode": "1551",
                    "eventId": 95,
                    "strength": "ev",
                    "playerId": 8481024,
                    "firstName": {"default": "Linus"},
                    "lastName": {"default": "Karlsson"},
                    "name": {"default": "L. Karlsson"},
                    "teamAbbrev": {"default": "VAN"},
                    "goalsToDate": 5,
                    "awayScore": 1,
                    "homeScore": 0,
                    "timeInPeriod": "02:55",
                    "shotType": "backhand",
                    "goalModifier": "none",
                    "assists": [],
                    "isHome": False,
                }
            ],
        }
    ],
    "threeStars": [THREE_STAR_DATA],
    "teamGameStats": [TEAM_GAME_STAT_INT, TEAM_GAME_STAT_FLOAT, TEAM_GAME_STAT_STR],
}

STORY_DATA = {
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
    "tvBroadcasts": [{"id": 2, "market": "H", "countryCode": "US", "network": "ALT", "sequenceNumber": 385}],
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "awayTeam": AWAY_TEAM_DATA,
    "homeTeam": HOME_TEAM_DATA,
    "shootoutInUse": True,
    "maxPeriods": 5,
    "regPeriods": 3,
    "otInUse": True,
    "tiesInUse": False,
    "summary": SUMMARY_DATA,
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
}


# ==========================================================================
# StoryTeam
# ==========================================================================

def test_story_team_fields() -> None:
    t = StoryTeam.from_dict(AWAY_TEAM_DATA)
    assert t.id == 23
    assert t.name.default == "Canucks"
    assert t.abbrev == "VAN"
    assert t.place_name.default == "Vancouver"
    assert t.score == 1
    assert t.sog == 21
    assert t.logo == "https://assets.nhle.com/logos/nhl/svg/VAN_light.svg"


def test_story_team_empty() -> None:
    t = StoryTeam.from_dict({})
    assert t.id is None
    assert t.name.default is None
    assert t.abbrev is None


# ==========================================================================
# StoryThreeStar
# ==========================================================================

def test_story_three_star_fields() -> None:
    s = StoryThreeStar.from_dict(THREE_STAR_DATA)
    assert s.star == 1
    assert s.player_id == 8477492
    assert s.team_abbrev == "COL"
    assert s.name == "N. MacKinnon"  # plain string
    assert s.sweater_no == 29
    assert s.position == "C"
    assert s.goals == 2
    assert s.assists == 0
    assert s.points == 2


def test_story_three_star_empty() -> None:
    s = StoryThreeStar.from_dict({})
    assert s.star is None
    assert s.name is None


# ==========================================================================
# TeamGameStat
# ==========================================================================

def test_team_game_stat_int_values() -> None:
    s = TeamGameStat.from_dict(TEAM_GAME_STAT_INT)
    assert s.category == "sog"
    assert s.away_value == 21
    assert s.home_value == 31


def test_team_game_stat_float_values() -> None:
    s = TeamGameStat.from_dict(TEAM_GAME_STAT_FLOAT)
    assert s.category == "faceoffWinningPctg"
    assert s.away_value == 0.468085
    assert s.home_value == 0.531915


def test_team_game_stat_string_values() -> None:
    s = TeamGameStat.from_dict(TEAM_GAME_STAT_STR)
    assert s.category == "powerPlay"
    assert s.away_value == "0/1"
    assert s.home_value == "0/1"


def test_team_game_stat_empty() -> None:
    s = TeamGameStat.from_dict({})
    assert s.category is None
    assert s.away_value is None


# ==========================================================================
# GameStorySummary
# ==========================================================================

def test_game_story_summary_fields() -> None:
    s = GameStorySummary.from_dict(SUMMARY_DATA)
    assert len(s.scoring) == 1
    assert len(s.three_stars) == 1
    assert len(s.team_game_stats) == 3
    assert s.scoring[0].period_descriptor.number == 1
    assert s.three_stars[0].name == "N. MacKinnon"
    assert s.team_game_stats[0].category == "sog"
    assert s.team_game_stats[2].away_value == "0/1"


def test_game_story_summary_empty() -> None:
    s = GameStorySummary.from_dict({})
    assert s.scoring == []
    assert s.three_stars == []
    assert s.team_game_stats == []


# ==========================================================================
# GameStoryResult
# ==========================================================================

def test_story_result_fields() -> None:
    r = GameStoryResult.from_dict(STORY_DATA)
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


def test_story_result_teams() -> None:
    r = GameStoryResult.from_dict(STORY_DATA)
    assert r.away_team.abbrev == "VAN"
    assert r.away_team.score == 1
    assert r.away_team.name.default == "Canucks"
    assert r.home_team.abbrev == "COL"
    assert r.home_team.score == 3


def test_story_result_period_descriptor() -> None:
    r = GameStoryResult.from_dict(STORY_DATA)
    assert r.period_descriptor.number == 3
    assert r.period_descriptor.period_type == "REG"


def test_story_result_clock() -> None:
    r = GameStoryResult.from_dict(STORY_DATA)
    assert r.clock.time_remaining == "00:00"
    assert r.clock.running is False


def test_story_result_tv_broadcasts() -> None:
    r = GameStoryResult.from_dict(STORY_DATA)
    assert len(r.tv_broadcasts) == 1
    assert r.tv_broadcasts[0].network == "ALT"


def test_story_result_summary() -> None:
    r = GameStoryResult.from_dict(STORY_DATA)
    assert r.summary is not None
    assert len(r.summary.scoring) == 1
    assert len(r.summary.three_stars) == 1
    assert len(r.summary.team_game_stats) == 3
    assert r.summary.three_stars[0].name == "N. MacKinnon"
    assert r.summary.team_game_stats[0].away_value == 21


def test_story_result_no_summary() -> None:
    data = {k: v for k, v in STORY_DATA.items() if k != "summary"}
    r = GameStoryResult.from_dict(data)
    assert r.summary is None


def test_story_result_empty_summary() -> None:
    data = {**STORY_DATA, "summary": {}}
    r = GameStoryResult.from_dict(data)
    assert r.summary is not None
    assert r.summary.scoring == []
    assert r.summary.three_stars == []


def test_story_result_empty() -> None:
    r = GameStoryResult.from_dict({})
    assert r.id is None
    assert r.summary is None
    assert r.clock is None
