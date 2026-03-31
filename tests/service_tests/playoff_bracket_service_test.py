from src.models.playoffs.bracket import PlayoffBracket, PlayoffBracketResult

from .conftest import ok


BRACKET_RESPONSE = {
    "bracketLogo": "https://assets.nhle.com/logos/playoffs/png/scp-20232024-horizontal-banner-en.png",
    "bracketLogoFr": "https://assets.nhle.com/logos/playoffs/png/scp-20232024-horizontal-banner-fr.png",
    "series": [
        {
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
            "topSeedTeam": {"id": 13, "abbrev": "FLA", "name": {"default": "Florida Panthers"}, "commonName": {"default": "Panthers"}, "placeNameWithPreposition": {"default": "Florida"}, "logo": "", "darkLogo": ""},
            "bottomSeedTeam": {"id": 14, "abbrev": "TBL", "name": {"default": "Tampa Bay Lightning"}, "commonName": {"default": "Lightning"}, "placeNameWithPreposition": {"default": "Tampa Bay"}, "logo": "", "darkLogo": ""},
        }
    ],
}


def test_get_bracket_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_bracket.return_value = ok(BRACKET_RESPONSE)
    svc = PlayoffBracket(mock_client)
    result = svc.get_bracket(year=2024)
    assert isinstance(result, PlayoffBracketResult)
    mock_client._api.api_web.call_nhl_playoffs.get_bracket.assert_called_once_with(year=2024)


def test_get_bracket_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_bracket.return_value = ok(BRACKET_RESPONSE)
    svc = PlayoffBracket(mock_client)
    _ = svc.get_bracket(year=2024)
    _ = svc.get_bracket(year=2024)
    mock_client._api.api_web.call_nhl_playoffs.get_bracket.assert_called_once()


def test_get_bracket_different_years_separate_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_bracket.return_value = ok(BRACKET_RESPONSE)
    svc = PlayoffBracket(mock_client)
    _ = svc.get_bracket(year=2024)
    _ = svc.get_bracket(year=2023)
    assert mock_client._api.api_web.call_nhl_playoffs.get_bracket.call_count == 2


def test_get_bracket_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_bracket.return_value = ok(BRACKET_RESPONSE)
    svc = PlayoffBracket(mock_client)
    result = svc.get_bracket(year=2024)
    assert result.bracket_logo is not None
    assert len(result.series) == 1
    assert result.series[0].series_letter == "A"
    assert result.series[0].top_seed_team.abbrev == "FLA"
    assert result.series[0].winning_team_id == 13
