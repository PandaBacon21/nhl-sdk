"""
Tests for scoreboard models:
  ScoreboardTeam, ScoreboardGame, ScoreboardDate, ScoreboardResult
"""
from src.models.games.scoreboard.scoreboard_result import (
    ScoreboardTeam, ScoreboardGame, ScoreboardDate, ScoreboardResult,
)


AWAY_TEAM = {
    "id": 29,
    "name": {"default": "Columbus Blue Jackets", "fr": "Blue Jackets de Columbus"},
    "commonName": {"default": "Blue Jackets"},
    "placeNameWithPreposition": {"default": "Columbus", "fr": "de Columbus"},
    "abbrev": "CBJ",
    "score": 1,
    "logo": "https://assets.nhle.com/logos/nhl/svg/CBJ_light.svg",
}

HOME_TEAM = {
    "id": 8,
    "name": {"default": "Montréal Canadiens", "fr": "Canadiens de Montréal"},
    "commonName": {"default": "Canadiens"},
    "placeNameWithPreposition": {"default": "Montréal", "fr": "de Montréal"},
    "abbrev": "MTL",
    "score": 2,
    "logo": "https://assets.nhle.com/logos/nhl/svg/MTL_light.svg",
}

GAME_DATA = {
    "id": 2025021137,
    "season": 20252026,
    "gameType": 2,
    "gameDate": "2026-03-26",
    "gameCenterLink": "/gamecenter/cbj-vs-mtl/2026/03/26/2025021137",
    "venue": {"default": "Centre Bell"},
    "startTimeUTC": "2026-03-26T23:00:00Z",
    "easternUTCOffset": "-04:00",
    "venueUTCOffset": "-04:00",
    "tvBroadcasts": [
        {"id": 131, "market": "H", "countryCode": "CA", "network": "TSN2", "sequenceNumber": 112},
    ],
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "awayTeam": AWAY_TEAM,
    "homeTeam": HOME_TEAM,
    "ticketsLink": "https://www.ticketmaster.ca/event/abc123",
    "ticketsLinkFr": "https://www.ticketmaster.ca/event/abc123?lang=fr-ca",
    "period": 3,
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "threeMinRecap": "/video/cbj-at-mtl-recap-6391800336112",
    "threeMinRecapFr": "/fr/video/cbj-vs-mtl-26-03-2026-resume-6391800707112",
}


# ==========================================================================
# SCOREBOARD TEAM
# ==========================================================================

def test_scoreboard_team_away() -> None:
    t = ScoreboardTeam.from_dict(AWAY_TEAM)
    assert t.id == 29
    assert t.name.default == "Columbus Blue Jackets"
    assert t.common_name.default == "Blue Jackets"
    assert t.place_name_with_preposition.default == "Columbus"
    assert t.place_name_with_preposition.get_locale("fr") == "de Columbus"
    assert t.abbrev == "CBJ"
    assert t.score == 1
    assert t.logo is not None


def test_scoreboard_team_home() -> None:
    t = ScoreboardTeam.from_dict(HOME_TEAM)
    assert t.id == 8
    assert t.name.default == "Montréal Canadiens"
    assert t.abbrev == "MTL"
    assert t.score == 2


def test_scoreboard_team_empty() -> None:
    t = ScoreboardTeam.from_dict({})
    assert t.id is None
    assert t.name.default is None
    assert t.common_name.default is None
    assert t.place_name_with_preposition.default is None
    assert t.abbrev is None
    assert t.score is None
    assert t.logo is None


# ==========================================================================
# SCOREBOARD GAME
# ==========================================================================

def test_scoreboard_game_completed() -> None:
    g = ScoreboardGame.from_dict(GAME_DATA)
    assert g.id == 2025021137
    assert g.season == 20252026
    assert g.game_type == 2
    assert g.game_date == "2026-03-26"
    assert g.game_center_link == "/gamecenter/cbj-vs-mtl/2026/03/26/2025021137"
    assert g.venue.default == "Centre Bell"
    assert g.start_time_utc == "2026-03-26T23:00:00Z"
    assert g.game_state == "OFF"
    assert len(g.tv_broadcasts) == 1
    assert g.tv_broadcasts[0].network == "TSN2"
    assert g.away_team.abbrev == "CBJ"
    assert g.away_team.score == 1
    assert g.home_team.abbrev == "MTL"
    assert g.home_team.score == 2
    assert g.tickets_link is not None
    assert g.tickets_link_fr is not None
    assert g.period == 3
    assert g.period_descriptor is not None
    assert g.period_descriptor.period_type == "REG"
    assert g.three_min_recap is not None
    assert g.three_min_recap_fr is not None


def test_scoreboard_game_so() -> None:
    data = {
        **GAME_DATA,
        "period": 5,
        "periodDescriptor": {"number": 5, "periodType": "SO", "maxRegulationPeriods": 3},
    }
    g = ScoreboardGame.from_dict(data)
    assert g.period == 5
    assert g.period_descriptor.period_type == "SO"


def test_scoreboard_game_no_period_descriptor() -> None:
    data = {**GAME_DATA}
    data.pop("periodDescriptor", None)
    g = ScoreboardGame.from_dict(data)
    assert g.period_descriptor is None


def test_scoreboard_game_no_tickets() -> None:
    data = {**GAME_DATA}
    data.pop("ticketsLink", None)
    data.pop("ticketsLinkFr", None)
    g = ScoreboardGame.from_dict(data)
    assert g.tickets_link is None
    assert g.tickets_link_fr is None


def test_scoreboard_game_empty() -> None:
    g = ScoreboardGame.from_dict({})
    assert g.id is None
    assert g.tv_broadcasts == []
    assert g.period_descriptor is None
    assert g.tickets_link is None
    assert g.three_min_recap is None


# ==========================================================================
# SCOREBOARD DATE
# ==========================================================================

def test_scoreboard_date_from_dict() -> None:
    d = ScoreboardDate.from_dict({"date": "2026-03-26", "games": [GAME_DATA]})
    assert d.date == "2026-03-26"
    assert len(d.games) == 1
    assert d.games[0].id == 2025021137


def test_scoreboard_date_empty_games() -> None:
    d = ScoreboardDate.from_dict({"date": "2026-03-26", "games": []})
    assert d.date == "2026-03-26"
    assert d.games == []


def test_scoreboard_date_empty() -> None:
    d = ScoreboardDate.from_dict({})
    assert d.date is None
    assert d.games == []


# ==========================================================================
# SCOREBOARD RESULT
# ==========================================================================

SCOREBOARD_DATA = {
    "focusedDate": "2026-03-29",
    "focusedDateCount": 11,
    "gamesByDate": [
        {"date": "2026-03-26", "games": [GAME_DATA]},
        {"date": "2026-03-29", "games": []},
    ],
}


def test_scoreboard_result_from_dict() -> None:
    result = ScoreboardResult.from_dict(SCOREBOARD_DATA)
    assert result.focused_date == "2026-03-29"
    assert result.focused_date_count == 11
    assert len(result.games_by_date) == 2
    assert result.games_by_date[0].date == "2026-03-26"
    assert len(result.games_by_date[0].games) == 1
    assert result.games_by_date[1].date == "2026-03-29"
    assert result.games_by_date[1].games == []


def test_scoreboard_result_game_fields() -> None:
    result = ScoreboardResult.from_dict(SCOREBOARD_DATA)
    g = result.games_by_date[0].games[0]
    assert g.away_team.common_name.default == "Blue Jackets"
    assert g.home_team.name.default == "Montréal Canadiens"
    assert g.period_descriptor.period_type == "REG"


def test_scoreboard_result_empty() -> None:
    result = ScoreboardResult.from_dict({})
    assert result.focused_date is None
    assert result.focused_date_count is None
    assert result.games_by_date == []
