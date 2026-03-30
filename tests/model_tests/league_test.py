"""
Tests for league models:
  GameDay, LeagueScheduleResult, CalendarTeam, LeagueCalendarResult
"""
from src.models.league.league_schedule import GameDay, LeagueScheduleResult
from src.models.league.league_calendar import CalendarTeam, LeagueCalendarResult


COMPLETED_GAME = {
    "id": 2025021167,
    "season": 20252026,
    "gameType": 2,
    "venue": {"default": "Madison Square Garden"},
    "neutralSite": False,
    "startTimeUTC": "2026-03-29T17:00:00Z",
    "easternUTCOffset": "-04:00",
    "venueUTCOffset": "-04:00",
    "venueTimezone": "America/New_York",
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "tvBroadcasts": [
        {"id": 324, "market": "N", "countryCode": "US", "network": "NHLN", "sequenceNumber": 35},
    ],
    "awayTeam": {
        "id": 13, "commonName": {"default": "Panthers"}, "placeName": {"default": "Florida"},
        "placeNameWithPreposition": {"default": "Florida", "fr": "de la Floride"},
        "abbrev": "FLA",
        "logo": "https://assets.nhle.com/logos/nhl/svg/FLA_light.svg",
        "darkLogo": "https://assets.nhle.com/logos/nhl/svg/FLA_dark.svg",
        "awaySplitSquad": False, "score": 1,
    },
    "homeTeam": {
        "id": 3, "commonName": {"default": "Rangers"}, "placeName": {"default": "New York"},
        "placeNameWithPreposition": {"default": "New York", "fr": "de New York"},
        "abbrev": "NYR",
        "logo": "https://assets.nhle.com/logos/nhl/svg/NYR_light.svg",
        "darkLogo": "https://assets.nhle.com/logos/nhl/svg/NYR_dark.svg",
        "homeSplitSquad": False, "score": 3,
    },
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "gameOutcome": {"lastPeriodType": "REG"},
    "winningGoalie": {"playerId": 8478048, "firstInitial": {"default": "I."}, "lastName": {"default": "Shesterkin"}},
    "winningGoalScorer": {"playerId": 8477839, "firstInitial": {"default": "C."}, "lastName": {"default": "Sheary"}},
    "threeMinRecap": "/video/fla-at-nyr-recap-6392078453112",
    "condensedGame": "/video/fla-at-nyr-condensed-game-6392077472112",
    "gameCenterLink": "/gamecenter/fla-vs-nyr/2026/03/29/2025021167",
}

FUTURE_GAME = {
    "id": 2025021173,
    "season": 20252026,
    "gameType": 2,
    "venue": {"default": "UBS Arena"},
    "neutralSite": False,
    "startTimeUTC": "2026-03-30T23:00:00Z",
    "easternUTCOffset": "-04:00",
    "venueUTCOffset": "-04:00",
    "venueTimezone": "America/New_York",
    "gameState": "FUT",
    "gameScheduleState": "OK",
    "tvBroadcasts": [],
    "awayTeam": {
        "id": 5, "commonName": {"default": "Penguins"}, "placeName": {"default": "Pittsburgh"},
        "placeNameWithPreposition": {"default": "Pittsburgh"}, "abbrev": "PIT",
        "logo": "https://assets.nhle.com/logos/nhl/svg/PIT_light.svg",
        "darkLogo": "https://assets.nhle.com/logos/nhl/svg/PIT_dark.svg",
        "awaySplitSquad": False,
        "radioLink": "https://d2igy0yla8zi0u.cloudfront.net/PIT/20252026/PIT-radio.m3u8",
    },
    "homeTeam": {
        "id": 2, "commonName": {"default": "Islanders"}, "placeName": {"default": "New York"},
        "placeNameWithPreposition": {"default": "New York"}, "abbrev": "NYI",
        "logo": "https://assets.nhle.com/logos/nhl/svg/NYI_light.svg",
        "darkLogo": "https://assets.nhle.com/logos/nhl/svg/NYI_dark.svg",
        "homeSplitSquad": False,
        "radioLink": "https://d2igy0yla8zi0u.cloudfront.net/NYI/20252026/NYI-radio.m3u8",
    },
    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
    "ticketsLink": "https://www.ticketmaster.com/event/300062EEE60433F2",
    "ticketsLinkFr": "https://www.ticketmaster.com/event/300062EEE60433F2?fr=1",
    "gameCenterLink": "/gamecenter/pit-vs-nyi/2026/03/30/2025021173",
}


# ==========================================================================
# GAME DAY
# ==========================================================================

def test_game_day_completed() -> None:
    d = GameDay.from_dict({
        "date": "2026-03-29",
        "dayAbbrev": "SUN",
        "numberOfGames": 6,
        "datePromo": [],
        "games": [COMPLETED_GAME],
    })
    assert d.date == "2026-03-29"
    assert d.day_abbrev == "SUN"
    assert d.number_of_games == 6
    assert d.date_promo == []
    assert len(d.games) == 1
    assert d.games[0].id == 2025021167
    assert d.games[0].game_state == "OFF"
    assert d.games[0].away_team.abbrev == "FLA"
    assert d.games[0].home_team.abbrev == "NYR"
    assert d.games[0].winning_goalie.last_name.default == "Shesterkin"


def test_game_day_future() -> None:
    d = GameDay.from_dict({
        "date": "2026-03-30",
        "dayAbbrev": "MON",
        "numberOfGames": 5,
        "datePromo": [],
        "games": [FUTURE_GAME],
    })
    assert d.date == "2026-03-30"
    assert d.day_abbrev == "MON"
    assert d.number_of_games == 5
    assert len(d.games) == 1
    assert d.games[0].game_state == "FUT"
    assert d.games[0].winning_goalie is None
    assert d.games[0].tickets_link == "https://www.ticketmaster.com/event/300062EEE60433F2"


def test_game_day_no_games() -> None:
    d = GameDay.from_dict({
        "date": "2026-03-29",
        "dayAbbrev": "SUN",
        "numberOfGames": 0,
        "datePromo": [],
        "games": [],
    })
    assert d.games == []


def test_game_day_empty() -> None:
    d = GameDay.from_dict({})
    assert d.date is None
    assert d.day_abbrev is None
    assert d.number_of_games is None
    assert d.date_promo == []
    assert d.games == []


# ==========================================================================
# LEAGUE SCHEDULE RESULT
# ==========================================================================

SCHEDULE_DATA = {
    "nextStartDate": "2026-04-05",
    "previousStartDate": "2026-03-22",
    "gameWeek": [
        {
            "date": "2026-03-29",
            "dayAbbrev": "SUN",
            "numberOfGames": 6,
            "datePromo": [],
            "games": [COMPLETED_GAME],
        },
        {
            "date": "2026-03-30",
            "dayAbbrev": "MON",
            "numberOfGames": 5,
            "datePromo": [],
            "games": [FUTURE_GAME],
        },
    ],
}


def test_league_schedule_result_from_dict() -> None:
    result = LeagueScheduleResult.from_dict(SCHEDULE_DATA)
    assert result.next_start_date == "2026-04-05"
    assert result.previous_start_date == "2026-03-22"
    assert len(result.game_week) == 2
    assert result.game_week[0].date == "2026-03-29"
    assert result.game_week[0].day_abbrev == "SUN"
    assert len(result.game_week[0].games) == 1
    assert result.game_week[1].date == "2026-03-30"


def test_league_schedule_result_game_data_correct() -> None:
    result = LeagueScheduleResult.from_dict(SCHEDULE_DATA)
    completed = result.game_week[0].games[0]
    assert completed.id == 2025021167
    assert completed.season == 20252026
    assert completed.venue.default == "Madison Square Garden"
    assert completed.game_outcome.last_period_type == "REG"
    assert completed.winning_goal_scorer.last_name.default == "Sheary"
    assert len(completed.tv_broadcasts) == 1
    assert completed.tv_broadcasts[0].network == "NHLN"


def test_league_schedule_result_empty_game_week() -> None:
    result = LeagueScheduleResult.from_dict({"nextStartDate": "2026-04-05", "gameWeek": []})
    assert result.next_start_date == "2026-04-05"
    assert result.previous_start_date is None
    assert result.game_week == []


def test_league_schedule_result_empty() -> None:
    result = LeagueScheduleResult.from_dict({})
    assert result.next_start_date is None
    assert result.previous_start_date is None
    assert result.game_week == []


# ==========================================================================
# CALENDAR TEAM
# ==========================================================================

NJD_DATA = {
    "id": 1,
    "seasonId": 20252026,
    "commonName": {"default": "Devils"},
    "abbrev": "NJD",
    "name": {"default": "New Jersey Devils", "fr": "Devils du New Jersey"},
    "placeNameWithPreposition": {"default": "New Jersey", "fr": "du New Jersey"},
    "placeName": {"default": "New Jersey"},
    "logo": "https://assets.nhle.com/logos/nhl/svg/NJD_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/NJD_dark.svg",
    "french": False,
}

MTL_DATA = {
    "id": 8,
    "seasonId": 20252026,
    "commonName": {"default": "Canadiens"},
    "abbrev": "MTL",
    "name": {"default": "Montréal Canadiens", "fr": "Canadiens de Montréal"},
    "placeNameWithPreposition": {"default": "Montréal", "fr": "de Montréal"},
    "placeName": {"default": "Montréal"},
    "logo": "https://assets.nhle.com/logos/nhl/svg/MTL_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/MTL_dark.svg",
    "french": True,
}


def test_calendar_team_english() -> None:
    t = CalendarTeam.from_dict(NJD_DATA)
    assert t.id == 1
    assert t.season_id == 20252026
    assert t.common_name.default == "Devils"
    assert t.abbrev == "NJD"
    assert t.name.default == "New Jersey Devils"
    assert t.name.get_locale("fr") == "Devils du New Jersey"
    assert t.place_name_with_preposition.default == "New Jersey"
    assert t.place_name.default == "New Jersey"
    assert t.logo is not None
    assert t.dark_logo is not None
    assert t.french is False


def test_calendar_team_french() -> None:
    t = CalendarTeam.from_dict(MTL_DATA)
    assert t.id == 8
    assert t.abbrev == "MTL"
    assert t.name.get_locale("fr") == "Canadiens de Montréal"
    assert t.french is True


def test_calendar_team_empty() -> None:
    t = CalendarTeam.from_dict({})
    assert t.id is None
    assert t.season_id is None
    assert t.abbrev is None
    assert t.logo is None
    assert t.french is None
    assert t.common_name.default is None
    assert t.name.default is None


# ==========================================================================
# LEAGUE CALENDAR RESULT
# ==========================================================================

CALENDAR_DATA = {
    "endDate": "2026-04-04",
    "nextStartDate": "2026-04-05",
    "previousStartDate": "2026-03-22",
    "startDate": "2026-03-29",
    "teams": [NJD_DATA, MTL_DATA],
}


def test_league_calendar_result_from_dict() -> None:
    result = LeagueCalendarResult.from_dict(CALENDAR_DATA)
    assert result.start_date == "2026-03-29"
    assert result.end_date == "2026-04-04"
    assert result.next_start_date == "2026-04-05"
    assert result.previous_start_date == "2026-03-22"
    assert len(result.teams) == 2


def test_league_calendar_result_team_data() -> None:
    result = LeagueCalendarResult.from_dict(CALENDAR_DATA)
    njd = result.teams[0]
    assert njd.id == 1
    assert njd.abbrev == "NJD"
    assert njd.french is False
    mtl = result.teams[1]
    assert mtl.id == 8
    assert mtl.abbrev == "MTL"
    assert mtl.french is True


def test_league_calendar_result_no_teams() -> None:
    result = LeagueCalendarResult.from_dict({"startDate": "2026-03-29", "teams": []})
    assert result.start_date == "2026-03-29"
    assert result.teams == []


def test_league_calendar_result_empty() -> None:
    result = LeagueCalendarResult.from_dict({})
    assert result.start_date is None
    assert result.end_date is None
    assert result.next_start_date is None
    assert result.previous_start_date is None
    assert result.teams == []
