"""
Tests for daily score models:
  ScoreWeekDay, OddsPartner, ScoreTeam, GameClock,
  GoalAssist, Goal, ScoreGame, DailyScoreResult
"""
from src.models.games.scores.daily_score import (
    ScoreWeekDay, OddsPartner, ScoreTeam, GameClock,
    GoalAssist, Goal, ScoreGame, DailyScoreResult,
)


AWAY_TEAM = {
    "id": 13, "name": {"default": "Panthers"},
    "abbrev": "FLA", "score": 1, "sog": 27,
    "logo": "https://assets.nhle.com/logos/nhl/svg/FLA_light.svg",
}

HOME_TEAM = {
    "id": 3, "name": {"default": "Rangers"},
    "abbrev": "NYR", "score": 3, "sog": 21,
    "logo": "https://assets.nhle.com/logos/nhl/svg/NYR_light.svg",
}

GOAL_DATA = {
    "period": 3,
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "timeInPeriod": "05:10",
    "playerId": 8483669,
    "name": {"default": "A. Sykora"},
    "firstName": {"default": "Adam"},
    "lastName": {"default": "Sykora"},
    "goalModifier": "none",
    "assists": [
        {"playerId": 8479323, "name": {"default": "A. Fox"}, "assistsToDate": 36},
        {"playerId": 8483690, "name": {"default": "N. Laba"}, "assistsToDate": 13},
    ],
    "mugshot": "https://assets.nhle.com/mugs/nhl/20252026/NYR/8483669.png",
    "teamAbbrev": "NYR",
    "goalsToDate": 2,
    "awayScore": 0,
    "homeScore": 1,
    "strength": "ev",
    "highlightClipSharingUrl": "https://nhl.com/video/sykora-scores-6392074903112",
    "highlightClipSharingUrlFr": "https://nhl.com/fr/video/sykora-6392075391112",
    "highlightClip": 6392074903112,
    "highlightClipFr": 6392075391112,
    "discreteClip": 6392074097112,
    "discreteClipFr": 6392074711112,
}

GAME_DATA = {
    "id": 2025021167,
    "season": 20252026,
    "gameType": 2,
    "gameDate": "2026-03-29",
    "venue": {"default": "Madison Square Garden"},
    "startTimeUTC": "2026-03-29T17:00:00Z",
    "easternUTCOffset": "-04:00",
    "venueUTCOffset": "-04:00",
    "tvBroadcasts": [
        {"id": 324, "market": "N", "countryCode": "US", "network": "NHLN", "sequenceNumber": 35},
    ],
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "awayTeam": AWAY_TEAM,
    "homeTeam": HOME_TEAM,
    "gameCenterLink": "/gamecenter/fla-vs-nyr/2026/03/29/2025021167",
    "threeMinRecap": "/video/fla-at-nyr-recap-6392078453112",
    "condensedGame": "/video/fla-at-nyr-condensed-game-6392077472112",
    "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
    "neutralSite": False,
    "venueTimezone": "America/New_York",
    "period": 3,
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "gameOutcome": {"lastPeriodType": "REG"},
    "goals": [GOAL_DATA],
}


# ==========================================================================
# SCORE WEEK DAY
# ==========================================================================

def test_score_week_day_from_dict() -> None:
    d = ScoreWeekDay.from_dict({"date": "2026-03-26", "dayAbbrev": "THU", "numberOfGames": 13})
    assert d.date == "2026-03-26"
    assert d.day_abbrev == "THU"
    assert d.number_of_games == 13


def test_score_week_day_empty() -> None:
    d = ScoreWeekDay.from_dict({})
    assert d.date is None
    assert d.day_abbrev is None
    assert d.number_of_games is None


# ==========================================================================
# ODDS PARTNER
# ==========================================================================

def test_odds_partner_from_dict() -> None:
    p = OddsPartner.from_dict({
        "partnerId": 9, "country": "US", "name": "DraftKings",
        "imageUrl": "https://assets.nhle.com/betting_partner/draftkings.svg",
        "siteUrl": "https://dksb.sng.link/...",
        "bgColor": "#000000", "textColor": "#FFFFFF", "accentColor": "#FFFFFF",
    })
    assert p.partner_id == 9
    assert p.country == "US"
    assert p.name == "DraftKings"
    assert p.bg_color == "#000000"
    assert p.text_color == "#FFFFFF"
    assert p.accent_color == "#FFFFFF"


def test_odds_partner_empty() -> None:
    p = OddsPartner.from_dict({})
    assert p.partner_id is None
    assert p.country is None
    assert p.name is None


# ==========================================================================
# SCORE TEAM
# ==========================================================================

def test_score_team_away() -> None:
    t = ScoreTeam.from_dict(AWAY_TEAM)
    assert t.id == 13
    assert t.name.default == "Panthers"
    assert t.abbrev == "FLA"
    assert t.score == 1
    assert t.sog == 27
    assert t.logo is not None


def test_score_team_home() -> None:
    t = ScoreTeam.from_dict(HOME_TEAM)
    assert t.id == 3
    assert t.abbrev == "NYR"
    assert t.score == 3
    assert t.sog == 21


def test_score_team_empty() -> None:
    t = ScoreTeam.from_dict({})
    assert t.id is None
    assert t.abbrev is None
    assert t.score is None
    assert t.sog is None
    assert t.logo is None
    assert t.name.default is None


# ==========================================================================
# GAME CLOCK
# ==========================================================================

def test_game_clock_finished() -> None:
    c = GameClock.from_dict({"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False})
    assert c.time_remaining == "00:00"
    assert c.seconds_remaining == 0
    assert c.running is False
    assert c.in_intermission is False


def test_game_clock_live() -> None:
    c = GameClock.from_dict({"timeRemaining": "12:34", "secondsRemaining": 754, "running": True, "inIntermission": False})
    assert c.time_remaining == "12:34"
    assert c.seconds_remaining == 754
    assert c.running is True


def test_game_clock_empty() -> None:
    c = GameClock.from_dict({})
    assert c.time_remaining is None
    assert c.seconds_remaining is None
    assert c.running is None
    assert c.in_intermission is None


# ==========================================================================
# GOAL ASSIST
# ==========================================================================

def test_goal_assist_from_dict() -> None:
    a = GoalAssist.from_dict({"playerId": 8479323, "name": {"default": "A. Fox"}, "assistsToDate": 36})
    assert a.player_id == 8479323
    assert a.name.default == "A. Fox"
    assert a.assists_to_date == 36


def test_goal_assist_empty() -> None:
    a = GoalAssist.from_dict({})
    assert a.player_id is None
    assert a.name.default is None
    assert a.assists_to_date is None


# ==========================================================================
# GOAL
# ==========================================================================

def test_goal_from_dict() -> None:
    g = Goal.from_dict(GOAL_DATA)
    assert g.period == 3
    assert g.period_descriptor is not None
    assert g.period_descriptor.period_type == "REG"
    assert g.time_in_period == "05:10"
    assert g.player_id == 8483669
    assert g.name.default == "A. Sykora"
    assert g.first_name.default == "Adam"
    assert g.last_name.default == "Sykora"
    assert g.goal_modifier == "none"
    assert len(g.assists) == 2
    assert g.assists[0].name.default == "A. Fox"
    assert g.assists[0].assists_to_date == 36
    assert g.team_abbrev == "NYR"
    assert g.goals_to_date == 2
    assert g.away_score == 0
    assert g.home_score == 1
    assert g.strength == "ev"
    assert g.highlight_clip == 6392074903112
    assert g.discrete_clip == 6392074097112


def test_goal_empty_net() -> None:
    data = {**GOAL_DATA, "goalModifier": "empty-net", "assists": [{"playerId": 1, "name": {"default": "X"}, "assistsToDate": 5}]}
    g = Goal.from_dict(data)
    assert g.goal_modifier == "empty-net"
    assert len(g.assists) == 1


def test_goal_no_assists() -> None:
    data = {**GOAL_DATA, "assists": []}
    g = Goal.from_dict(data)
    assert g.assists == []


def test_goal_empty() -> None:
    g = Goal.from_dict({})
    assert g.period is None
    assert g.period_descriptor is None
    assert g.player_id is None
    assert g.assists == []
    assert g.strength is None


# ==========================================================================
# SCORE GAME
# ==========================================================================

def test_score_game_completed() -> None:
    g = ScoreGame.from_dict(GAME_DATA)
    assert g.id == 2025021167
    assert g.season == 20252026
    assert g.game_type == 2
    assert g.game_date == "2026-03-29"
    assert g.venue.default == "Madison Square Garden"
    assert g.start_time_utc == "2026-03-29T17:00:00Z"
    assert g.game_state == "OFF"
    assert len(g.tv_broadcasts) == 1
    assert g.tv_broadcasts[0].network == "NHLN"
    assert g.away_team.abbrev == "FLA"
    assert g.away_team.score == 1
    assert g.home_team.abbrev == "NYR"
    assert g.home_team.score == 3
    assert g.clock is not None
    assert g.clock.time_remaining == "00:00"
    assert g.clock.running is False
    assert g.period == 3
    assert g.period_descriptor.period_type == "REG"
    assert g.game_outcome.last_period_type == "REG"
    assert len(g.goals) == 1
    assert g.goals[0].team_abbrev == "NYR"
    assert g.neutral_site is False
    assert g.three_min_recap is not None
    assert g.condensed_game is not None


def test_score_game_so() -> None:
    data = {
        **GAME_DATA,
        "period": 5,
        "periodDescriptor": {"number": 5, "periodType": "SO", "maxRegulationPeriods": 3},
        "gameOutcome": {"lastPeriodType": "SO"},
    }
    g = ScoreGame.from_dict(data)
    assert g.period == 5
    assert g.period_descriptor.period_type == "SO"
    assert g.game_outcome.last_period_type == "SO"


def test_score_game_no_clock() -> None:
    data = {**GAME_DATA}
    data.pop("clock", None)
    g = ScoreGame.from_dict(data)
    assert g.clock is None


def test_score_game_empty() -> None:
    g = ScoreGame.from_dict({})
    assert g.id is None
    assert g.tv_broadcasts == []
    assert g.clock is None
    assert g.period_descriptor is None
    assert g.game_outcome is None
    assert g.goals == []


# ==========================================================================
# DAILY SCORE RESULT
# ==========================================================================

SCORE_DATA = {
    "prevDate": "2026-03-28",
    "currentDate": "2026-03-29",
    "nextDate": "2026-03-30",
    "gameWeek": [
        {"date": "2026-03-26", "dayAbbrev": "THU", "numberOfGames": 13},
        {"date": "2026-03-29", "dayAbbrev": "SUN", "numberOfGames": 6},
    ],
    "oddsPartners": [
        {"partnerId": 9, "country": "US", "name": "DraftKings", "imageUrl": "", "siteUrl": "", "bgColor": "#000", "textColor": "#FFF", "accentColor": "#FFF"},
    ],
    "games": [GAME_DATA],
}


def test_daily_score_result_from_dict() -> None:
    result = DailyScoreResult.from_dict(SCORE_DATA)
    assert result.prev_date == "2026-03-28"
    assert result.current_date == "2026-03-29"
    assert result.next_date == "2026-03-30"
    assert len(result.game_week) == 2
    assert result.game_week[0].day_abbrev == "THU"
    assert len(result.odds_partners) == 1
    assert result.odds_partners[0].name == "DraftKings"
    assert len(result.games) == 1
    assert result.games[0].id == 2025021167


def test_daily_score_result_empty() -> None:
    result = DailyScoreResult.from_dict({})
    assert result.prev_date is None
    assert result.current_date is None
    assert result.next_date is None
    assert result.game_week == []
    assert result.odds_partners == []
    assert result.games == []
