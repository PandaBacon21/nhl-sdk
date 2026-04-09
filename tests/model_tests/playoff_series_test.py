"""
Tests for playoff series schedule models
"""
from nhl_sdk.models.playoffs.series.series_result import (
    SeriesConference,
    SeriesScheduleSeriesTeam,
    SeriesScheduleGameTeam,
    SeriesStatus,
    SeriesGameOutcome,
    SeriesScheduleGame,
    SeriesScheduleResult,
)


CONFERENCE_DATA = {"name": "Eastern", "abbrev": "E"}

SERIES_TEAM_DATA = {
    "id": 10,
    "name": {"default": "Maple Leafs"},
    "abbrev": "TOR",
    "placeName": {"default": "Toronto"},
    "placeNameWithPreposition": {"default": "Toronto", "fr": "de Toronto"},
    "conference": CONFERENCE_DATA,
    "record": "7-6",
    "seriesWins": 4,
    "divisionAbbrev": "A",
    "seed": 1,
    "logo": "https://assets.nhle.com/logos/nhl/svg/TOR_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/TOR_dark.svg",
}

BOTTOM_TEAM_DATA = {
    "id": 9,
    "name": {"default": "Senators", "fr": "Sénateurs"},
    "abbrev": "OTT",
    "placeName": {"default": "Ottawa"},
    "placeNameWithPreposition": {"default": "Ottawa", "fr": "d'Ottawa"},
    "conference": CONFERENCE_DATA,
    "record": "2-4",
    "seriesWins": 2,
    "divisionAbbrev": "A",
    "seed": 4,
    "logo": "https://assets.nhle.com/logos/nhl/svg/OTT_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/OTT_dark.svg",
}

GAME_TEAM_DATA = {
    "id": 9,
    "commonName": {"default": "Senators", "fr": "Sénateurs"},
    "placeName": {"default": "Ottawa"},
    "placeNameWithPreposition": {"default": "Ottawa", "fr": "d'Ottawa"},
    "abbrev": "OTT",
    "score": 2,
}

GAME_DATA = {
    "id": 2024030111,
    "season": 20242025,
    "gameType": 3,
    "gameNumber": 1,
    "ifNecessary": False,
    "venue": {"default": "Scotiabank Arena"},
    "neutralSite": False,
    "startTimeUTC": "2025-04-20T23:00:00Z",
    "easternUTCOffset": "-04:00",
    "venueUTCOffset": "-04:00",
    "venueTimezone": "America/Toronto",
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "tvBroadcasts": [{"id": 4, "market": "N", "countryCode": "CA", "network": "CBC", "sequenceNumber": 101}],
    "awayTeam": GAME_TEAM_DATA,
    "homeTeam": {**GAME_TEAM_DATA, "id": 10, "commonName": {"default": "Maple Leafs"}, "abbrev": "TOR", "score": 6},
    "gameCenterLink": "/gamecenter/ott-vs-tor/2025/04/20/2024030111",
    "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
    "seriesStatus": {"topSeedWins": 1, "bottomSeedWins": 0},
    "gameOutcome": {"lastPeriodType": "REG"},
}

SERIES_DATA = {
    "round": 1,
    "roundAbbrev": "R1",
    "roundLabel": "1st-round",
    "seriesLetter": "A",
    "seriesLogo": "https://assets.nhle.com/logos/playoffs/png/stanley_cup_playoffs_secondary_wordmark_dark.png",
    "seriesLogoFr": "https://assets.nhle.com/logos/playoffs/png/stanley_cup_playoffs_secondary_wordmark_fr_dark.png",
    "neededToWin": 4,
    "length": 7,
    "topSeedTeam": SERIES_TEAM_DATA,
    "bottomSeedTeam": BOTTOM_TEAM_DATA,
    "games": [GAME_DATA],
    "fullCoverageUrl": {"en": "https://www.nhl.com/playoffs/2025/series-a-coverage", "fr": "https://www.nhl.com/fr/playoffs/2025/series-a-coverage"},
}


# --------------------------------------------------------------------------
# SeriesConference
# --------------------------------------------------------------------------

def test_conference_fields() -> None:
    c = SeriesConference.from_dict(CONFERENCE_DATA)
    assert c.name == "Eastern"
    assert c.abbrev == "E"


def test_conference_empty() -> None:
    c = SeriesConference.from_dict({})
    assert c.name is None
    assert c.abbrev is None


# --------------------------------------------------------------------------
# SeriesScheduleSeriesTeam
# --------------------------------------------------------------------------

def test_series_team_fields() -> None:
    t = SeriesScheduleSeriesTeam.from_dict(SERIES_TEAM_DATA)
    assert t.id == 10
    assert t.abbrev == "TOR"
    assert t.name.default == "Maple Leafs"
    assert t.record == "7-6"
    assert t.series_wins == 4
    assert t.seed == 1
    assert t.division_abbrev == "A"
    assert t.logo is not None
    assert t.dark_logo is not None


def test_series_team_conference() -> None:
    t = SeriesScheduleSeriesTeam.from_dict(SERIES_TEAM_DATA)
    assert isinstance(t.conference, SeriesConference)
    assert t.conference.name == "Eastern"
    assert t.conference.abbrev == "E"


def test_series_team_localized() -> None:
    t = SeriesScheduleSeriesTeam.from_dict(BOTTOM_TEAM_DATA)
    assert t.name.default == "Senators"
    assert t.name.get_locale("fr") == "Sénateurs"
    assert t.place_name_with_preposition.get_locale("fr") == "d'Ottawa"


def test_series_team_empty() -> None:
    t = SeriesScheduleSeriesTeam.from_dict({})
    assert t.id is None
    assert t.abbrev is None
    assert t.record is None
    assert t.series_wins is None
    assert t.seed is None
    assert t.name.default is None
    assert t.conference.name is None


# --------------------------------------------------------------------------
# SeriesScheduleGameTeam
# --------------------------------------------------------------------------

def test_game_team_fields() -> None:
    t = SeriesScheduleGameTeam.from_dict(GAME_TEAM_DATA)
    assert t.id == 9
    assert t.abbrev == "OTT"
    assert t.common_name.default == "Senators"
    assert t.score == 2


def test_game_team_empty() -> None:
    t = SeriesScheduleGameTeam.from_dict({})
    assert t.id is None
    assert t.score is None
    assert t.common_name.default is None


# --------------------------------------------------------------------------
# SeriesStatus
# --------------------------------------------------------------------------

def test_series_status_fields() -> None:
    s = SeriesStatus.from_dict({"topSeedWins": 1, "bottomSeedWins": 0})
    assert s.top_seed_wins == 1
    assert s.bottom_seed_wins == 0


def test_series_status_empty() -> None:
    s = SeriesStatus.from_dict({})
    assert s.top_seed_wins is None
    assert s.bottom_seed_wins is None


# --------------------------------------------------------------------------
# SeriesGameOutcome
# --------------------------------------------------------------------------

def test_game_outcome_reg() -> None:
    o = SeriesGameOutcome.from_dict({"lastPeriodType": "REG"})
    assert o.last_period_type == "REG"
    assert o.ot_periods is None


def test_game_outcome_ot() -> None:
    o = SeriesGameOutcome.from_dict({"lastPeriodType": "OT", "otPeriods": 1})
    assert o.last_period_type == "OT"
    assert o.ot_periods == 1


def test_game_outcome_empty() -> None:
    o = SeriesGameOutcome.from_dict({})
    assert o.last_period_type is None
    assert o.ot_periods is None


# --------------------------------------------------------------------------
# SeriesScheduleGame
# --------------------------------------------------------------------------

def test_game_fields() -> None:
    g = SeriesScheduleGame.from_dict(GAME_DATA)
    assert g.id == 2024030111
    assert g.season == 20242025
    assert g.game_type == 3
    assert g.game_number == 1
    assert g.if_necessary is False
    assert g.venue.default == "Scotiabank Arena"
    assert g.neutral_site is False
    assert g.start_time_utc == "2025-04-20T23:00:00Z"
    assert g.game_state == "OFF"
    assert g.game_center_link is not None


def test_game_teams() -> None:
    g = SeriesScheduleGame.from_dict(GAME_DATA)
    assert isinstance(g.away_team, SeriesScheduleGameTeam)
    assert isinstance(g.home_team, SeriesScheduleGameTeam)
    assert g.away_team.abbrev == "OTT"
    assert g.home_team.abbrev == "TOR"
    assert g.home_team.score == 6


def test_game_broadcasts() -> None:
    g = SeriesScheduleGame.from_dict(GAME_DATA)
    assert len(g.tv_broadcasts) == 1
    assert g.tv_broadcasts[0].network == "CBC"


def test_game_period_descriptor() -> None:
    g = SeriesScheduleGame.from_dict(GAME_DATA)
    assert g.period_descriptor is not None
    assert g.period_descriptor.number == 3
    assert g.period_descriptor.period_type == "REG"


def test_game_series_status() -> None:
    g = SeriesScheduleGame.from_dict(GAME_DATA)
    assert isinstance(g.series_status, SeriesStatus)
    assert g.series_status.top_seed_wins == 1
    assert g.series_status.bottom_seed_wins == 0


def test_game_outcome_present() -> None:
    g = SeriesScheduleGame.from_dict(GAME_DATA)
    assert g.game_outcome is not None
    assert g.game_outcome.last_period_type == "REG"


def test_game_no_outcome() -> None:
    g = SeriesScheduleGame.from_dict({**GAME_DATA, "gameOutcome": None})
    assert g.game_outcome is None


def test_game_no_period_descriptor() -> None:
    g = SeriesScheduleGame.from_dict({**GAME_DATA, "periodDescriptor": None})
    assert g.period_descriptor is None


# --------------------------------------------------------------------------
# SeriesScheduleResult
# --------------------------------------------------------------------------

def test_result_fields() -> None:
    r = SeriesScheduleResult.from_dict(SERIES_DATA)
    assert r.round == 1
    assert r.round_abbrev == "R1"
    assert r.round_label == "1st-round"
    assert r.series_letter == "A"
    assert r.series_logo is not None
    assert r.series_logo_fr is not None
    assert r.needed_to_win == 4
    assert r.length == 7


def test_result_teams() -> None:
    r = SeriesScheduleResult.from_dict(SERIES_DATA)
    assert isinstance(r.top_seed_team, SeriesScheduleSeriesTeam)
    assert isinstance(r.bottom_seed_team, SeriesScheduleSeriesTeam)
    assert r.top_seed_team.abbrev == "TOR"
    assert r.bottom_seed_team.abbrev == "OTT"


def test_result_games() -> None:
    r = SeriesScheduleResult.from_dict(SERIES_DATA)
    assert len(r.games) == 1
    assert isinstance(r.games[0], SeriesScheduleGame)
    assert r.games[0].id == 2024030111


def test_result_full_coverage_url() -> None:
    r = SeriesScheduleResult.from_dict(SERIES_DATA)
    assert "en" in r.full_coverage_url
    assert "fr" in r.full_coverage_url
    assert "nhl.com" in r.full_coverage_url["en"]


def test_result_empty() -> None:
    r = SeriesScheduleResult.from_dict({})
    assert r.round is None
    assert r.series_letter is None
    assert r.needed_to_win is None
    assert r.games == []
    assert r.full_coverage_url == {}
    assert r.top_seed_team.id is None
    assert r.bottom_seed_team.id is None
