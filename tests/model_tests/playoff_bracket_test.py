"""
Tests for playoff bracket models: BracketTeam, BracketSeries, PlayoffBracketResult
"""
from src.models.playoffs.bracket.bracket_result import (
    BracketTeam,
    BracketSeries,
    PlayoffBracketResult,
)


TEAM_DATA = {
    "id": 13,
    "abbrev": "FLA",
    "name": {"default": "Florida Panthers", "fr": "Panthers de la Floride"},
    "commonName": {"default": "Panthers"},
    "placeNameWithPreposition": {"default": "Florida", "fr": "de la Floride"},
    "logo": "https://assets.nhle.com/logos/nhl/svg/FLA_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/FLA_dark.svg",
}

BOTTOM_TEAM_DATA = {
    "id": 14,
    "abbrev": "TBL",
    "name": {"default": "Tampa Bay Lightning", "fr": "Lightning de Tampa Bay"},
    "commonName": {"default": "Lightning"},
    "placeNameWithPreposition": {"default": "Tampa Bay", "fr": "de Tampa Bay"},
    "logo": "https://assets.nhle.com/logos/nhl/svg/TBL_light.svg",
    "darkLogo": "https://assets.nhle.com/logos/nhl/svg/TBL_dark.svg",
}

R1_SERIES_DATA = {
    "seriesUrl": "/schedule/playoff-series/2024/series-a/lightning-vs-panthers",
    "seriesTitle": "1st Round",
    "seriesAbbrev": "R1",
    "seriesLetter": "A",
    "playoffRound": 1,
    "topSeedRank": 1,
    "topSeedRankAbbrev": "D1",
    "topSeedWins": 4,
    "bottomSeedRank": 4,
    "bottomSeedRankAbbrev": "WC1",
    "bottomSeedWins": 1,
    "winningTeamId": 13,
    "losingTeamId": 14,
    "topSeedTeam": TEAM_DATA,
    "bottomSeedTeam": BOTTOM_TEAM_DATA,
}

SCF_SERIES_DATA = {
    "seriesUrl": "/schedule/playoff-series/2024/series-o/oilers-vs-panthers",
    "seriesLogo": "https://assets.nhle.com/logos/playoffs/png/sc-banner.png",
    "seriesLogoFr": "https://assets.nhle.com/logos/playoffs/png/sc-banner.png",
    "seriesTitle": "Stanley Cup Final",
    "seriesAbbrev": "SCF",
    "seriesLetter": "O",
    "playoffRound": 4,
    "topSeedRank": 1,
    "topSeedRankAbbrev": "D1",
    "topSeedWins": 4,
    "bottomSeedRank": 2,
    "bottomSeedRankAbbrev": "D2",
    "bottomSeedWins": 3,
    "winningTeamId": 13,
    "losingTeamId": 22,
    "topSeedTeam": TEAM_DATA,
    "bottomSeedTeam": {**BOTTOM_TEAM_DATA, "id": 22, "abbrev": "EDM"},
}

CF_SERIES_DATA = {
    **R1_SERIES_DATA,
    "seriesLogo": "https://assets.nhle.com/logos/playoffs/png/ecf-20232024-wordmark-en.png",
    "seriesLogoFr": "https://assets.nhle.com/logos/playoffs/png/ecf-20232024-wordmark-fr.png",
    "seriesTitle": "Eastern Conference Finals",
    "seriesAbbrev": "ECF",
    "seriesLetter": "M",
    "conferenceAbbrev": "E",
    "conferenceName": "Eastern",
    "playoffRound": 3,
}

BRACKET_DATA = {
    "bracketLogo": "https://assets.nhle.com/logos/playoffs/png/scp-20232024-horizontal-banner-en.png",
    "bracketLogoFr": "https://assets.nhle.com/logos/playoffs/png/scp-20232024-horizontal-banner-fr.png",
    "series": [R1_SERIES_DATA, CF_SERIES_DATA, SCF_SERIES_DATA],
}


# --------------------------------------------------------------------------
# BracketTeam
# --------------------------------------------------------------------------

def test_team_fields() -> None:
    t = BracketTeam.from_dict(TEAM_DATA)
    assert t.id == 13
    assert t.abbrev == "FLA"
    assert t.name.default == "Florida Panthers"
    assert t.common_name.default == "Panthers"
    assert t.logo is not None
    assert t.dark_logo is not None


def test_team_localized() -> None:
    t = BracketTeam.from_dict(TEAM_DATA)
    assert t.name.get_locale("fr") == "Panthers de la Floride"
    assert t.place_name_with_preposition.get_locale("fr") == "de la Floride"


def test_team_empty() -> None:
    t = BracketTeam.from_dict({})
    assert t.id is None
    assert t.abbrev is None
    assert t.name.default is None
    assert t.common_name.default is None
    assert t.logo is None
    assert t.dark_logo is None


# --------------------------------------------------------------------------
# BracketSeries
# --------------------------------------------------------------------------

def test_series_r1_fields() -> None:
    s = BracketSeries.from_dict(R1_SERIES_DATA)
    assert s.series_letter == "A"
    assert s.series_title == "1st Round"
    assert s.series_abbrev == "R1"
    assert s.playoff_round == 1
    assert s.top_seed_rank == 1
    assert s.top_seed_rank_abbrev == "D1"
    assert s.top_seed_wins == 4
    assert s.bottom_seed_rank == 4
    assert s.bottom_seed_rank_abbrev == "WC1"
    assert s.bottom_seed_wins == 1
    assert s.winning_team_id == 13
    assert s.losing_team_id == 14
    assert s.series_logo is None
    assert s.conference_abbrev is None
    assert s.conference_name is None


def test_series_teams() -> None:
    s = BracketSeries.from_dict(R1_SERIES_DATA)
    assert isinstance(s.top_seed_team, BracketTeam)
    assert isinstance(s.bottom_seed_team, BracketTeam)
    assert s.top_seed_team.abbrev == "FLA"
    assert s.bottom_seed_team.abbrev == "TBL"


def test_series_cf_has_conference_fields() -> None:
    s = BracketSeries.from_dict(CF_SERIES_DATA)
    assert s.series_abbrev == "ECF"
    assert s.conference_abbrev == "E"
    assert s.conference_name == "Eastern"
    assert s.series_logo is not None
    assert s.series_logo_fr is not None


def test_series_scf_fields() -> None:
    s = BracketSeries.from_dict(SCF_SERIES_DATA)
    assert s.series_letter == "O"
    assert s.series_abbrev == "SCF"
    assert s.series_title == "Stanley Cup Final"
    assert s.playoff_round == 4
    assert s.bottom_seed_team.abbrev == "EDM"


def test_series_empty() -> None:
    s = BracketSeries.from_dict({})
    assert s.series_letter is None
    assert s.playoff_round is None
    assert s.winning_team_id is None
    assert s.top_seed_team.id is None
    assert s.bottom_seed_team.id is None


# --------------------------------------------------------------------------
# PlayoffBracketResult
# --------------------------------------------------------------------------

def test_bracket_fields() -> None:
    r = PlayoffBracketResult.from_dict(BRACKET_DATA)
    assert r.bracket_logo is not None
    assert r.bracket_logo_fr is not None
    assert len(r.series) == 3


def test_bracket_series_parsed() -> None:
    r = PlayoffBracketResult.from_dict(BRACKET_DATA)
    assert isinstance(r.series[0], BracketSeries)
    assert r.series[0].series_letter == "A"
    assert r.series[2].series_abbrev == "SCF"


def test_bracket_empty() -> None:
    r = PlayoffBracketResult.from_dict({})
    assert r.bracket_logo is None
    assert r.bracket_logo_fr is None
    assert r.series == []


def test_bracket_all_rounds_present() -> None:
    r = PlayoffBracketResult.from_dict(BRACKET_DATA)
    rounds = {s.playoff_round for s in r.series}
    assert 1 in rounds
    assert 3 in rounds
    assert 4 in rounds
