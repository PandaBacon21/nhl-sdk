from src.models.playoffs.carousel import PlayoffCarousel, PlayoffCarouselResult

from .conftest import ok


CAROUSEL_RESPONSE = {
    "seasonId": 20242025,
    "currentRound": 4,
    "rounds": [
        {
            "roundNumber": 1,
            "roundLabel": "1st-round",
            "roundAbbrev": "R1",
            "series": [
                {
                    "seriesLetter": "A",
                    "roundNumber": 1,
                    "seriesLabel": "A vs B",
                    "seriesLink": "playoff-series/carousel/20242025/A",
                    "topSeed": {"id": 10, "abbrev": "TOR", "wins": 4, "logo": "", "darkLogo": ""},
                    "bottomSeed": {"id": 13, "abbrev": "FLA", "wins": 2, "logo": "", "darkLogo": ""},
                    "neededToWin": 4,
                    "winningTeamId": 10,
                    "losingTeamId": 13,
                }
            ],
        }
    ],
}


def test_get_carousel_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_carousel.return_value = ok(CAROUSEL_RESPONSE)
    svc = PlayoffCarousel(mock_client)
    result = svc.get_carousel(season=20242025)
    assert isinstance(result, PlayoffCarouselResult)
    mock_client._api.api_web.call_nhl_playoffs.get_carousel.assert_called_once_with(season=20242025)


def test_get_carousel_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_carousel.return_value = ok(CAROUSEL_RESPONSE)
    svc = PlayoffCarousel(mock_client)
    _ = svc.get_carousel(season=20242025)
    _ = svc.get_carousel(season=20242025)
    mock_client._api.api_web.call_nhl_playoffs.get_carousel.assert_called_once()


def test_get_carousel_different_seasons_separate_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_carousel.return_value = ok(CAROUSEL_RESPONSE)
    svc = PlayoffCarousel(mock_client)
    _ = svc.get_carousel(season=20242025)
    _ = svc.get_carousel(season=20232024)
    assert mock_client._api.api_web.call_nhl_playoffs.get_carousel.call_count == 2


def test_get_carousel_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_carousel.return_value = ok(CAROUSEL_RESPONSE)
    svc = PlayoffCarousel(mock_client)
    result = svc.get_carousel(season=20242025)
    assert result.season_id == 20242025
    assert result.current_round == 4
    assert len(result.rounds) == 1
    assert result.rounds[0].series[0].top_seed.abbrev == "TOR"


def test_get_carousel_series_wins(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_carousel.return_value = ok(CAROUSEL_RESPONSE)
    svc = PlayoffCarousel(mock_client)
    result = svc.get_carousel(season=20242025)
    series = result.rounds[0].series[0]
    assert series.top_seed.wins == 4
    assert series.bottom_seed.wins == 2
    assert series.winning_team_id == 10
