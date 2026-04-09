from nhl_sdk.models.games.scores.scores import GameScores
from nhl_sdk.models.games.scores.daily_score import DailyScoreResult

from .conftest import ok

DATE = "2026-03-29"


def test_get_daily_scores_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_daily_scores.return_value = ok({"games": []})
    svc = GameScores(mock_client)
    result = svc.get_daily_scores()
    assert isinstance(result, DailyScoreResult)
    mock_client._api.api_web.call_nhl_games.get_daily_scores.assert_called_once_with(date=None)


def test_get_daily_scores_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_daily_scores.return_value = ok({"games": []})
    svc = GameScores(mock_client)
    _ = svc.get_daily_scores()
    _ = svc.get_daily_scores()
    mock_client._api.api_web.call_nhl_games.get_daily_scores.assert_called_once()


def test_get_daily_scores_with_date(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_daily_scores.return_value = ok({"games": []})
    svc = GameScores(mock_client)
    result = svc.get_daily_scores(date=DATE)
    assert isinstance(result, DailyScoreResult)
    mock_client._api.api_web.call_nhl_games.get_daily_scores.assert_called_once_with(date=DATE)


def test_get_daily_scores_date_and_now_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_daily_scores.return_value = ok({"games": []})
    svc = GameScores(mock_client)
    _ = svc.get_daily_scores()
    _ = svc.get_daily_scores(date=DATE)
    assert mock_client._api.api_web.call_nhl_games.get_daily_scores.call_count == 2


def test_get_daily_scores_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_daily_scores.return_value = ok({
        "prevDate": "2026-03-28",
        "currentDate": DATE,
        "nextDate": "2026-03-30",
        "gameWeek": [
            {"date": "2026-03-29", "dayAbbrev": "SUN", "numberOfGames": 6},
        ],
        "oddsPartners": [],
        "games": [
            {
                "id": 2025021167,
                "season": 20252026,
                "gameType": 2,
                "gameDate": DATE,
                "venue": {"default": "Madison Square Garden"},
                "startTimeUTC": f"{DATE}T17:00:00Z",
                "easternUTCOffset": "-04:00",
                "venueUTCOffset": "-04:00",
                "tvBroadcasts": [],
                "gameState": "OFF",
                "gameScheduleState": "OK",
                "awayTeam": {"id": 13, "name": {"default": "Panthers"}, "abbrev": "FLA", "score": 1, "sog": 27, "logo": ""},
                "homeTeam": {"id": 3, "name": {"default": "Rangers"}, "abbrev": "NYR", "score": 3, "sog": 21, "logo": ""},
                "gameCenterLink": "/gamecenter/fla-vs-nyr/2026/03/29/2025021167",
                "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
                "neutralSite": False,
                "venueTimezone": "America/New_York",
                "period": 3,
                "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
                "gameOutcome": {"lastPeriodType": "REG"},
                "goals": [],
            }
        ],
    })
    svc = GameScores(mock_client)
    result = svc.get_daily_scores(date=DATE)
    assert result.current_date == DATE
    assert result.prev_date == "2026-03-28"
    assert result.next_date == "2026-03-30"
    assert len(result.game_week) == 1
    assert result.game_week[0].number_of_games == 6
    assert len(result.games) == 1
    g = result.games[0]
    assert g.id == 2025021167
    assert g.away_team.abbrev == "FLA"
    assert g.home_team.score == 3
    assert g.clock.running is False
    assert g.game_outcome.last_period_type == "REG"
