from src.models.playoffs.series import PlayoffSeriesSchedule, SeriesScheduleResult

from .conftest import ok


SERIES_RESPONSE = {
    "round": 1,
    "roundAbbrev": "R1",
    "roundLabel": "1st-round",
    "seriesLetter": "A",
    "seriesLogo": "https://assets.nhle.com/logos/playoffs/png/stanley_cup_playoffs_secondary_wordmark_dark.png",
    "seriesLogoFr": "https://assets.nhle.com/logos/playoffs/png/stanley_cup_playoffs_secondary_wordmark_fr_dark.png",
    "neededToWin": 4,
    "length": 7,
    "topSeedTeam": {"id": 10, "name": {"default": "Maple Leafs"}, "abbrev": "TOR", "placeName": {"default": "Toronto"}, "placeNameWithPreposition": {"default": "Toronto"}, "conference": {"name": "Eastern", "abbrev": "E"}, "record": "7-6", "seriesWins": 4, "divisionAbbrev": "A", "seed": 1, "logo": "", "darkLogo": ""},
    "bottomSeedTeam": {"id": 9, "name": {"default": "Senators"}, "abbrev": "OTT", "placeName": {"default": "Ottawa"}, "placeNameWithPreposition": {"default": "Ottawa"}, "conference": {"name": "Eastern", "abbrev": "E"}, "record": "2-4", "seriesWins": 2, "divisionAbbrev": "A", "seed": 4, "logo": "", "darkLogo": ""},
    "games": [
        {
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
            "tvBroadcasts": [],
            "awayTeam": {"id": 9, "commonName": {"default": "Senators"}, "placeName": {"default": "Ottawa"}, "placeNameWithPreposition": {"default": "Ottawa"}, "abbrev": "OTT", "score": 2},
            "homeTeam": {"id": 10, "commonName": {"default": "Maple Leafs"}, "placeName": {"default": "Toronto"}, "placeNameWithPreposition": {"default": "Toronto"}, "abbrev": "TOR", "score": 6},
            "gameCenterLink": "/gamecenter/ott-vs-tor/2025/04/20/2024030111",
            "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
            "seriesStatus": {"topSeedWins": 1, "bottomSeedWins": 0},
            "gameOutcome": {"lastPeriodType": "REG"},
        }
    ],
    "fullCoverageUrl": {"en": "https://www.nhl.com/playoffs/2025/series-a-coverage"},
}


def test_get_series_schedule_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.return_value = ok(SERIES_RESPONSE)
    svc = PlayoffSeriesSchedule(mock_client)
    result = svc.get_series_schedule(season=20242025, series_letter="A")
    assert isinstance(result, SeriesScheduleResult)
    mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.assert_called_once_with(
        season=20242025, series_letter="A"
    )


def test_get_series_schedule_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.return_value = ok(SERIES_RESPONSE)
    svc = PlayoffSeriesSchedule(mock_client)
    _ = svc.get_series_schedule(season=20242025, series_letter="A")
    _ = svc.get_series_schedule(season=20242025, series_letter="A")
    mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.assert_called_once()


def test_get_series_schedule_different_letters_separate_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.return_value = ok(SERIES_RESPONSE)
    svc = PlayoffSeriesSchedule(mock_client)
    _ = svc.get_series_schedule(season=20242025, series_letter="A")
    _ = svc.get_series_schedule(season=20242025, series_letter="B")
    assert mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.call_count == 2


def test_get_series_schedule_different_seasons_separate_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.return_value = ok(SERIES_RESPONSE)
    svc = PlayoffSeriesSchedule(mock_client)
    _ = svc.get_series_schedule(season=20242025, series_letter="A")
    _ = svc.get_series_schedule(season=20232024, series_letter="A")
    assert mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.call_count == 2


def test_get_series_schedule_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_playoffs.get_series_schedule.return_value = ok(SERIES_RESPONSE)
    svc = PlayoffSeriesSchedule(mock_client)
    result = svc.get_series_schedule(season=20242025, series_letter="A")
    assert result.round == 1
    assert result.series_letter == "A"
    assert result.top_seed_team.abbrev == "TOR"
    assert result.bottom_seed_team.abbrev == "OTT"
    assert len(result.games) == 1
    assert result.games[0].id == 2024030111
