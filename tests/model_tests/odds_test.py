"""
Tests for partner odds models: OddsEntry, OddsTeam, OddsGame, PartnerOddsResult
"""
from src.models.games.odds.odds_result import (
    PartnerOddsResult, OddsGame, OddsTeam, OddsEntry,
)


ODDS_ENTRY_ML = {"description": "MONEY_LINE_2_WAY", "value": -110.0, "qualifier": ""}
ODDS_ENTRY_PL = {"description": "PUCK_LINE", "value": -500.0, "qualifier": "+1.5"}
ODDS_ENTRY_OU = {"description": "OVER_UNDER", "value": -130.0, "qualifier": "O6.5"}

HOME_TEAM = {
    "id": 6,
    "name": {"default": "Bruins"},
    "abbrev": "BOS",
    "logo": "https://assets.nhle.com/logos/nhl/svg/BOS_light.svg",
    "odds": [ODDS_ENTRY_ML, ODDS_ENTRY_PL, ODDS_ENTRY_OU],
}

AWAY_TEAM = {
    "id": 25,
    "name": {"default": "Stars"},
    "abbrev": "DAL",
    "logo": "https://assets.nhle.com/logos/nhl/svg/DAL_light.svg",
    "odds": [
        {"description": "MONEY_LINE_2_WAY", "value": -120.0, "qualifier": ""},
        {"description": "PUCK_LINE", "value": 340.0, "qualifier": "-1.5"},
        {"description": "OVER_UNDER", "value": 100.0, "qualifier": "U6.5"},
    ],
}

GAME_DATA = {
    "gameId": 2025021178,
    "gameType": 2,
    "startTimeUTC": "2026-03-31T23:00:00Z",
    "homeTeam": HOME_TEAM,
    "awayTeam": AWAY_TEAM,
}

FULL_RESPONSE = {
    "currentOddsDate": "2026-03-31",
    "lastUpdatedUTC": "2026-04-01T01:00:39Z",
    "games": [GAME_DATA],
}


# --------------------------------------------------------------------------
# OddsEntry
# --------------------------------------------------------------------------

def test_odds_entry_fields() -> None:
    entry = OddsEntry.from_dict(ODDS_ENTRY_ML)
    assert entry.description == "MONEY_LINE_2_WAY"
    assert entry.value == -110.0
    assert entry.qualifier == ""


def test_odds_entry_with_qualifier() -> None:
    entry = OddsEntry.from_dict(ODDS_ENTRY_OU)
    assert entry.description == "OVER_UNDER"
    assert entry.value == -130.0
    assert entry.qualifier == "O6.5"


def test_odds_entry_empty() -> None:
    entry = OddsEntry.from_dict({})
    assert entry.description is None
    assert entry.value is None
    assert entry.qualifier is None


# --------------------------------------------------------------------------
# OddsTeam
# --------------------------------------------------------------------------

def test_odds_team_fields() -> None:
    team = OddsTeam.from_dict(HOME_TEAM)
    assert team.id == 6
    assert team.name.default == "Bruins"
    assert team.abbrev == "BOS"
    assert team.logo == "https://assets.nhle.com/logos/nhl/svg/BOS_light.svg"
    assert len(team.odds) == 3


def test_odds_team_odds_entries() -> None:
    team = OddsTeam.from_dict(HOME_TEAM)
    assert team.odds[0].description == "MONEY_LINE_2_WAY"
    assert team.odds[0].value == -110.0
    assert team.odds[1].description == "PUCK_LINE"
    assert team.odds[1].qualifier == "+1.5"
    assert team.odds[2].description == "OVER_UNDER"
    assert team.odds[2].qualifier == "O6.5"


def test_odds_team_empty() -> None:
    team = OddsTeam.from_dict({})
    assert team.id is None
    assert team.name.default is None
    assert team.abbrev is None
    assert team.logo is None
    assert team.odds == []


# --------------------------------------------------------------------------
# OddsGame
# --------------------------------------------------------------------------

def test_odds_game_fields() -> None:
    game = OddsGame.from_dict(GAME_DATA)
    assert game.game_id == 2025021178
    assert game.game_type == 2
    assert game.start_time_utc == "2026-03-31T23:00:00Z"


def test_odds_game_teams() -> None:
    game = OddsGame.from_dict(GAME_DATA)
    assert game.home_team.abbrev == "BOS"
    assert game.home_team.id == 6
    assert len(game.home_team.odds) == 3
    assert game.away_team.abbrev == "DAL"
    assert game.away_team.id == 25
    assert len(game.away_team.odds) == 3


def test_odds_game_empty() -> None:
    game = OddsGame.from_dict({})
    assert game.game_id is None
    assert game.game_type is None
    assert game.start_time_utc is None
    assert game.home_team.id is None
    assert game.home_team.odds == []


# --------------------------------------------------------------------------
# PartnerOddsResult
# --------------------------------------------------------------------------

def test_odds_result_fields() -> None:
    r = PartnerOddsResult.from_dict(FULL_RESPONSE)
    assert r.current_odds_date == "2026-03-31"
    assert r.last_updated_utc == "2026-04-01T01:00:39Z"
    assert len(r.games) == 1


def test_odds_result_game_populated() -> None:
    r = PartnerOddsResult.from_dict(FULL_RESPONSE)
    game = r.games[0]
    assert game.game_id == 2025021178
    assert game.home_team.abbrev == "BOS"
    assert game.away_team.abbrev == "DAL"


def test_odds_result_empty() -> None:
    r = PartnerOddsResult.from_dict({})
    assert r.current_odds_date is None
    assert r.last_updated_utc is None
    assert r.games == []


def test_odds_result_empty_games_list() -> None:
    r = PartnerOddsResult.from_dict({"currentOddsDate": "2026-03-31", "games": []})
    assert r.games == []


def test_odds_result_to_dict() -> None:
    r = PartnerOddsResult.from_dict(FULL_RESPONSE)
    d = r.to_dict()
    assert d["current_odds_date"] == "2026-03-31"
    assert len(d["games"]) == 1
    assert d["games"][0]["game_id"] == 2025021178
    assert d["games"][0]["home_team"]["abbrev"] == "BOS"
    assert d["games"][0]["home_team"]["odds"][0]["description"] == "MONEY_LINE_2_WAY"
