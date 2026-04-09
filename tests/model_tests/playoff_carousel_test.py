"""
Tests for playoff carousel models: PlayoffTeamSeed, PlayoffSeries, PlayoffRound, PlayoffCarouselResult
"""
from nhl_sdk.models.playoffs.carousel.carousel_result import (
    PlayoffTeamSeed,
    PlayoffSeries,
    PlayoffRound,
    PlayoffCarouselResult,
)


TOP_SEED_DATA = {
    "id": 10,
    "abbrev": "TOR",
    "wins": 4,
    "logo": "https://assets.nhle.com/logos/nhl/svg/TOR_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/TOR_dark.svg",
}

BOTTOM_SEED_DATA = {
    "id": 13,
    "abbrev": "FLA",
    "wins": 2,
    "logo": "https://assets.nhle.com/logos/nhl/svg/FLA_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/FLA_dark.svg",
}

SERIES_DATA = {
    "seriesLetter": "A",
    "roundNumber": 1,
    "seriesLabel": "A vs B",
    "seriesLink": "playoff-series/carousel/20242025/A",
    "topSeed": TOP_SEED_DATA,
    "bottomSeed": BOTTOM_SEED_DATA,
    "neededToWin": 4,
    "winningTeamId": 10,
    "losingTeamId": 13,
}

ROUND_DATA = {
    "roundNumber": 1,
    "roundLabel": "1st-round",
    "roundAbbrev": "R1",
    "series": [SERIES_DATA],
}

CAROUSEL_DATA = {
    "seasonId": 20242025,
    "currentRound": 4,
    "rounds": [ROUND_DATA],
}


# --------------------------------------------------------------------------
# PlayoffTeamSeed
# --------------------------------------------------------------------------

def test_team_seed_fields() -> None:
    s = PlayoffTeamSeed.from_dict(TOP_SEED_DATA)
    assert s.id == 10
    assert s.abbrev == "TOR"
    assert s.wins == 4
    assert s.logo is not None
    assert s.dark_logo is not None


def test_team_seed_empty() -> None:
    s = PlayoffTeamSeed.from_dict({})
    assert s.id is None
    assert s.abbrev is None
    assert s.wins is None
    assert s.logo is None
    assert s.dark_logo is None


# --------------------------------------------------------------------------
# PlayoffSeries
# --------------------------------------------------------------------------

def test_series_fields() -> None:
    s = PlayoffSeries.from_dict(SERIES_DATA)
    assert s.series_letter == "A"
    assert s.round_number == 1
    assert s.series_label == "A vs B"
    assert s.series_link is not None
    assert s.needed_to_win == 4
    assert s.winning_team_id == 10
    assert s.losing_team_id == 13


def test_series_seeds() -> None:
    s = PlayoffSeries.from_dict(SERIES_DATA)
    assert isinstance(s.top_seed, PlayoffTeamSeed)
    assert isinstance(s.bottom_seed, PlayoffTeamSeed)
    assert s.top_seed.abbrev == "TOR"
    assert s.bottom_seed.abbrev == "FLA"


def test_series_no_winner() -> None:
    s = PlayoffSeries.from_dict({**SERIES_DATA, "winningTeamId": None, "losingTeamId": None})
    assert s.winning_team_id is None
    assert s.losing_team_id is None


def test_series_empty() -> None:
    s = PlayoffSeries.from_dict({})
    assert s.series_letter is None
    assert s.round_number is None
    assert s.winning_team_id is None
    assert s.top_seed.id is None
    assert s.bottom_seed.id is None


# --------------------------------------------------------------------------
# PlayoffRound
# --------------------------------------------------------------------------

def test_round_fields() -> None:
    r = PlayoffRound.from_dict(ROUND_DATA)
    assert r.round_number == 1
    assert r.round_label == "1st-round"
    assert r.round_abbrev == "R1"
    assert len(r.series) == 1


def test_round_series_parsed() -> None:
    r = PlayoffRound.from_dict(ROUND_DATA)
    assert isinstance(r.series[0], PlayoffSeries)
    assert r.series[0].series_letter == "A"


def test_round_empty() -> None:
    r = PlayoffRound.from_dict({})
    assert r.round_number is None
    assert r.round_label is None
    assert r.series == []


# --------------------------------------------------------------------------
# PlayoffCarouselResult
# --------------------------------------------------------------------------

def test_carousel_fields() -> None:
    c = PlayoffCarouselResult.from_dict(CAROUSEL_DATA)
    assert c.season_id == 20242025
    assert c.current_round == 4
    assert len(c.rounds) == 1


def test_carousel_rounds_parsed() -> None:
    c = PlayoffCarouselResult.from_dict(CAROUSEL_DATA)
    assert isinstance(c.rounds[0], PlayoffRound)
    assert c.rounds[0].round_number == 1


def test_carousel_empty() -> None:
    c = PlayoffCarouselResult.from_dict({})
    assert c.season_id is None
    assert c.current_round is None
    assert c.rounds == []


def test_carousel_multiple_rounds() -> None:
    round2 = {**ROUND_DATA, "roundNumber": 2, "roundLabel": "2nd-round", "roundAbbrev": "R2", "series": []}
    c = PlayoffCarouselResult.from_dict({**CAROUSEL_DATA, "rounds": [ROUND_DATA, round2]})
    assert len(c.rounds) == 2
    assert c.rounds[1].round_abbrev == "R2"
