"""
Tests for team schedule models:
  ScheduleTvBroadcast, ScheduleTeam, SchedulePeriodDescriptor,
  ScheduleGameOutcome, ScheduleGoalPlayer, ScheduleGame,
  TeamScheduleResult, TeamMonthScheduleResult, TeamWeekScheduleResult
"""
from nhl_stats.models.teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    ScheduleTeam,
    SchedulePeriodDescriptor,
    ScheduleGameOutcome,
    ScheduleGoalPlayer,
    ScheduleGame,
    TeamScheduleResult,
    TeamMonthScheduleResult,
    TeamWeekScheduleResult,
)


# ==========================================================================
# SCHEDULE TV BROADCAST
# ==========================================================================

def test_schedule_tv_broadcast_from_dict() -> None:
    b = ScheduleTvBroadcast.from_dict({"id": 309, "market": "N", "countryCode": "US", "network": "ESPN", "sequenceNumber": 10})
    assert b.id == 309
    assert b.market == "N"
    assert b.country_code == "US"
    assert b.network == "ESPN"
    assert b.sequence_number == 10

def test_schedule_tv_broadcast_empty() -> None:
    b = ScheduleTvBroadcast.from_dict({})
    assert b.id is None
    assert b.network is None


# ==========================================================================
# SCHEDULE TEAM
# ==========================================================================

AWAY_TEAM_DATA = {
    "id": 21,
    "commonName": {"default": "Avalanche"},
    "placeName": {"default": "Colorado"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
    "abbrev": "COL",
    "logo": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/COL_dark.svg",
    "awaySplitSquad": False,
    "score": 4,
}

HOME_TEAM_DATA = {
    "id": 26,
    "commonName": {"default": "Kings"},
    "placeName": {"default": "Los Angeles"},
    "placeNameWithPreposition": {"default": "Los Angeles", "fr": "de Los Angeles"},
    "abbrev": "LAK",
    "logo": "https://assets.nhle.com/logos/nhl/svg/LAK_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/LAK_dark.svg",
    "homeSplitSquad": False,
    "score": 2,
    "radioLink": "https://d2igy0yla8zi0u.cloudfront.net/LAK/20252026/LAK-radio.m3u8",
}

def test_schedule_team_away() -> None:
    t = ScheduleTeam.from_dict(AWAY_TEAM_DATA)
    assert t.id == 21
    assert t.common_name.default == "Avalanche"
    assert t.place_name.default == "Colorado"
    assert t.place_name_with_preposition.get_locale("fr") == "du Colorado"
    assert t.abbrev == "COL"
    assert t.away_split_squad is False
    assert t.home_split_squad is None
    assert t.score == 4
    assert t.radio_link is None

def test_schedule_team_home_with_radio() -> None:
    t = ScheduleTeam.from_dict(HOME_TEAM_DATA)
    assert t.id == 26
    assert t.abbrev == "LAK"
    assert t.home_split_squad is False
    assert t.away_split_squad is None
    assert t.score == 2
    assert t.radio_link is not None

def test_schedule_team_empty() -> None:
    t = ScheduleTeam.from_dict({})
    assert t.id is None
    assert t.abbrev is None
    assert t.score is None
    assert t.radio_link is None


# ==========================================================================
# SCHEDULE PERIOD DESCRIPTOR
# ==========================================================================

def test_period_descriptor_reg() -> None:
    pd = SchedulePeriodDescriptor.from_dict({"number": 3, "periodType": "REG", "maxRegulationPeriods": 3})
    assert pd.number == 3
    assert pd.period_type == "REG"
    assert pd.max_regulation_periods == 3

def test_period_descriptor_ot() -> None:
    pd = SchedulePeriodDescriptor.from_dict({"number": 4, "periodType": "OT", "maxRegulationPeriods": 3})
    assert pd.number == 4
    assert pd.period_type == "OT"

def test_period_descriptor_so() -> None:
    pd = SchedulePeriodDescriptor.from_dict({"number": 5, "periodType": "SO", "maxRegulationPeriods": 3})
    assert pd.period_type == "SO"

def test_period_descriptor_no_number() -> None:
    """Season schedule responses omit the number field."""
    pd = SchedulePeriodDescriptor.from_dict({"periodType": "REG", "maxRegulationPeriods": 3})
    assert pd.number is None
    assert pd.period_type == "REG"

def test_period_descriptor_empty() -> None:
    pd = SchedulePeriodDescriptor.from_dict({})
    assert pd.number is None
    assert pd.period_type is None
    assert pd.max_regulation_periods is None


# ==========================================================================
# SCHEDULE GAME OUTCOME
# ==========================================================================

def test_game_outcome_reg() -> None:
    go = ScheduleGameOutcome.from_dict({"lastPeriodType": "REG"})
    assert go.last_period_type == "REG"

def test_game_outcome_ot() -> None:
    go = ScheduleGameOutcome.from_dict({"lastPeriodType": "OT"})
    assert go.last_period_type == "OT"

def test_game_outcome_empty() -> None:
    go = ScheduleGameOutcome.from_dict({})
    assert go.last_period_type is None


# ==========================================================================
# SCHEDULE GOAL PLAYER
# ==========================================================================

def test_schedule_goal_player_from_dict() -> None:
    gp = ScheduleGoalPlayer.from_dict({
        "playerId": 8477492,
        "firstInitial": {"default": "N."},
        "lastName": {"default": "MacKinnon"},
    })
    assert gp.player_id == 8477492
    assert gp.first_initial.default == "N."
    assert gp.last_name.default == "MacKinnon"

def test_schedule_goal_player_empty() -> None:
    gp = ScheduleGoalPlayer.from_dict({})
    assert gp.player_id is None
    assert gp.first_initial.default is None
    assert gp.last_name.default is None


# ==========================================================================
# SCHEDULE GAME
# ==========================================================================

COMPLETED_GAME_DATA = {
    "id": 2025020958,
    "season": 20252026,
    "gameType": 2,
    "gameDate": "2026-03-02",
    "venue": {"default": "Crypto.com Arena"},
    "neutralSite": False,
    "startTimeUTC": "2026-03-03T03:30:00Z",
    "easternUTCOffset": "-05:00",
    "venueUTCOffset": "-08:00",
    "venueTimezone": "America/Los_Angeles",
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "tvBroadcasts": [
        {"id": 47, "market": "A", "countryCode": "US", "network": "ALT2", "sequenceNumber": 408},
    ],
    "awayTeam": AWAY_TEAM_DATA,
    "homeTeam": HOME_TEAM_DATA,
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "gameOutcome": {"lastPeriodType": "REG"},
    "winningGoalie": {"playerId": 8478406, "firstInitial": {"default": "M."}, "lastName": {"default": "Blackwood"}},
    "winningGoalScorer": {"playerId": 8478038, "firstInitial": {"default": "D."}, "lastName": {"default": "Toews"}},
    "condensedGame": "/video/col-at-lak-condensed-game-6390303650112",
    "gameCenterLink": "/gamecenter/col-vs-lak/2026/03/02/2025020958",
}

FUTURE_GAME_DATA = {
    "id": 2025021162,
    "season": 20252026,
    "gameType": 2,
    "gameDate": "2026-03-28",
    "venue": {"default": "Ball Arena"},
    "neutralSite": False,
    "startTimeUTC": "2026-03-28T23:00:00Z",
    "easternUTCOffset": "-04:00",
    "venueUTCOffset": "-06:00",
    "venueTimezone": "America/Denver",
    "gameState": "FUT",
    "gameScheduleState": "OK",
    "tvBroadcasts": [],
    "awayTeam": {
        "id": 52, "commonName": {"default": "Jets"}, "placeName": {"default": "Winnipeg"},
        "placeNameWithPreposition": {"default": "Winnipeg"}, "abbrev": "WPG",
        "logo": "https://assets.nhle.com/logos/nhl/svg/WPG_light.svg",
        "darkLogo": "https://assets.nhle.com/logos/nhl/svg/WPG_dark.svg",
        "awaySplitSquad": False,
        "radioLink": "https://d2igy0yla8zi0u.cloudfront.net/WPG/20252026/WPG-radio.m3u8",
    },
    "homeTeam": {
        "id": 21, "commonName": {"default": "Avalanche"}, "placeName": {"default": "Colorado"},
        "placeNameWithPreposition": {"default": "Colorado"}, "abbrev": "COL",
        "logo": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
        "darkLogo": "https://assets.nhle.com/logos/nhl/svg/COL_dark.svg",
        "homeSplitSquad": False,
        "radioLink": "https://d2igy0yla8zi0u.cloudfront.net/COL/20252026/COL-radio.m3u8",
    },
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "ticketsLink": "https://www.ticketmaster.com/event/1E0062EF9EE536F5",
    "ticketsLinkFr": "https://www.ticketmaster.com/event/1E0062EF9EE536F5?fr=1",
    "gameCenterLink": "/gamecenter/wpg-vs-col/2026/03/28/2025021162",
}

def test_schedule_game_completed() -> None:
    g = ScheduleGame.from_dict(COMPLETED_GAME_DATA)
    assert g.id == 2025020958
    assert g.season == 20252026
    assert g.game_type == 2
    assert g.game_date == "2026-03-02"
    assert g.venue.default == "Crypto.com Arena"
    assert g.neutral_site is False
    assert g.game_state == "OFF"
    assert len(g.tv_broadcasts) == 1
    assert g.tv_broadcasts[0].network == "ALT2"
    assert g.away_team.abbrev == "COL"
    assert g.home_team.abbrev == "LAK"
    assert g.period_descriptor is not None
    assert g.period_descriptor.period_type == "REG"
    assert g.game_outcome is not None
    assert g.game_outcome.last_period_type == "REG"
    assert g.winning_goalie is not None
    assert g.winning_goalie.last_name.default == "Blackwood"
    assert g.winning_goal_scorer is not None
    assert g.winning_goal_scorer.last_name.default == "Toews"
    assert g.condensed_game is not None
    assert g.tickets_link is None
    assert g.game_center_link is not None

def test_schedule_game_so_no_goal_scorer() -> None:
    """SO games have a winning goalie but no winning goal scorer."""
    data = {**COMPLETED_GAME_DATA, "gameOutcome": {"lastPeriodType": "SO"}}
    data.pop("winningGoalScorer", None)
    g = ScheduleGame.from_dict(data)
    assert g.game_outcome.last_period_type == "SO"
    assert g.winning_goalie is not None
    assert g.winning_goal_scorer is None

def test_schedule_game_future() -> None:
    g = ScheduleGame.from_dict(FUTURE_GAME_DATA)
    assert g.id == 2025021162
    assert g.game_state == "FUT"
    assert g.winning_goalie is None
    assert g.winning_goal_scorer is None
    assert g.game_outcome is None
    assert g.tickets_link == "https://www.ticketmaster.com/event/1E0062EF9EE536F5"
    assert g.tickets_link_fr is not None
    assert g.away_team.radio_link is not None
    assert g.home_team.radio_link is not None
    assert g.three_min_recap is None

def test_schedule_game_empty() -> None:
    g = ScheduleGame.from_dict({})
    assert g.id is None
    assert g.tv_broadcasts == []
    assert g.period_descriptor is None
    assert g.game_outcome is None
    assert g.winning_goalie is None
    assert g.winning_goal_scorer is None


# ==========================================================================
# TEAM SCHEDULE RESULT (full season)
# ==========================================================================

def test_team_schedule_result_from_dict() -> None:
    data = {
        "previousSeason": 20232024,
        "currentSeason": 20242025,
        "nextSeason": 20252026,
        "clubTimezone": "America/Denver",
        "clubUTCOffset": "-06:00",
        "games": [COMPLETED_GAME_DATA],
    }
    result = TeamScheduleResult.from_dict(data)
    assert result.previous_season == 20232024
    assert result.current_season == 20242025
    assert result.next_season == 20252026
    assert result.club_timezone == "America/Denver"
    assert result.club_utc_offset == "-06:00"
    assert len(result.games) == 1
    assert result.games[0].id == 2025020958

def test_team_schedule_result_now_no_next_season() -> None:
    """Current season response omits nextSeason."""
    data = {
        "previousSeason": 20242025,
        "currentSeason": 20252026,
        "clubTimezone": "America/Denver",
        "clubUTCOffset": "-06:00",
        "games": [],
    }
    result = TeamScheduleResult.from_dict(data)
    assert result.next_season is None

def test_team_schedule_result_empty() -> None:
    result = TeamScheduleResult.from_dict({})
    assert result.previous_season is None
    assert result.games == []


# ==========================================================================
# TEAM MONTH SCHEDULE RESULT
# ==========================================================================

def test_team_month_schedule_result_from_dict() -> None:
    data = {
        "previousMonth": "2026-02",
        "currentMonth": "2026-03",
        "nextMonth": "2026-04",
        "calendarUrl": "https://nhl.ecal.com/avalanche",
        "clubTimezone": "America/Denver",
        "clubUTCOffset": "-06:00",
        "games": [COMPLETED_GAME_DATA, FUTURE_GAME_DATA],
    }
    result = TeamMonthScheduleResult.from_dict(data)
    assert result.previous_month == "2026-02"
    assert result.current_month == "2026-03"
    assert result.next_month == "2026-04"
    assert result.calendar_url == "https://nhl.ecal.com/avalanche"
    assert result.club_timezone == "America/Denver"
    assert len(result.games) == 2

def test_team_month_schedule_result_empty() -> None:
    result = TeamMonthScheduleResult.from_dict({})
    assert result.previous_month is None
    assert result.current_month is None
    assert result.calendar_url is None
    assert result.games == []


# ==========================================================================
# TEAM WEEK SCHEDULE RESULT
# ==========================================================================

def test_team_week_schedule_result_from_dict() -> None:
    data = {
        "previousStartDate": "2026-03-19",
        "nextStartDate": "2026-04-02",
        "calendarUrl": "https://nhl.ecal.com/avalanche",
        "clubTimezone": "America/Denver",
        "clubUTCOffset": "-06:00",
        "games": [FUTURE_GAME_DATA],
    }
    result = TeamWeekScheduleResult.from_dict(data)
    assert result.previous_start_date == "2026-03-19"
    assert result.next_start_date == "2026-04-02"
    assert result.calendar_url == "https://nhl.ecal.com/avalanche"
    assert result.club_timezone == "America/Denver"
    assert len(result.games) == 1
    assert result.games[0].game_state == "FUT"

def test_team_week_schedule_result_empty() -> None:
    result = TeamWeekScheduleResult.from_dict({})
    assert result.previous_start_date is None
    assert result.next_start_date is None
    assert result.games == []
