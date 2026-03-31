from src.models.games.scoreboard import GameScoreboard, ScoreboardResult

from .conftest import ok


def test_get_scoreboard_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_scoreboard_now.return_value = ok({"gamesByDate": []})
    svc = GameScoreboard(mock_client)
    result = svc.get_scoreboard()
    assert isinstance(result, ScoreboardResult)
    mock_client._api.api_web.call_nhl_games.get_scoreboard_now.assert_called_once_with()


def test_get_scoreboard_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_scoreboard_now.return_value = ok({"gamesByDate": []})
    svc = GameScoreboard(mock_client)
    _ = svc.get_scoreboard()
    _ = svc.get_scoreboard()
    mock_client._api.api_web.call_nhl_games.get_scoreboard_now.assert_called_once()


def test_get_scoreboard_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_scoreboard_now.return_value = ok({
        "focusedDate": "2026-03-29",
        "focusedDateCount": 11,
        "gamesByDate": [
            {
                "date": "2026-03-26",
                "games": [
                    {
                        "id": 2025021137,
                        "season": 20252026,
                        "gameType": 2,
                        "gameDate": "2026-03-26",
                        "gameCenterLink": "/gamecenter/cbj-vs-mtl/2026/03/26/2025021137",
                        "venue": {"default": "Centre Bell"},
                        "startTimeUTC": "2026-03-26T23:00:00Z",
                        "easternUTCOffset": "-04:00",
                        "venueUTCOffset": "-04:00",
                        "tvBroadcasts": [],
                        "gameState": "OFF",
                        "gameScheduleState": "OK",
                        "awayTeam": {
                            "id": 29,
                            "name": {"default": "Columbus Blue Jackets"},
                            "commonName": {"default": "Blue Jackets"},
                            "placeNameWithPreposition": {"default": "Columbus"},
                            "abbrev": "CBJ",
                            "score": 1,
                            "logo": "",
                        },
                        "homeTeam": {
                            "id": 8,
                            "name": {"default": "Montréal Canadiens"},
                            "commonName": {"default": "Canadiens"},
                            "placeNameWithPreposition": {"default": "Montréal"},
                            "abbrev": "MTL",
                            "score": 2,
                            "logo": "",
                        },
                        "period": 3,
                        "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
                    }
                ],
            }
        ],
    })
    svc = GameScoreboard(mock_client)
    result = svc.get_scoreboard()
    assert result.focused_date == "2026-03-29"
    assert result.focused_date_count == 11
    assert len(result.games_by_date) == 1
    day = result.games_by_date[0]
    assert day.date == "2026-03-26"
    assert len(day.games) == 1
    g = day.games[0]
    assert g.id == 2025021137
    assert g.away_team.abbrev == "CBJ"
    assert g.home_team.score == 2
    assert g.period_descriptor.period_type == "REG"


def test_get_scoreboard_empty_days(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_scoreboard_now.return_value = ok({
        "focusedDate": "2026-03-29",
        "focusedDateCount": 0,
        "gamesByDate": [],
    })
    svc = GameScoreboard(mock_client)
    result = svc.get_scoreboard()
    assert result.focused_date == "2026-03-29"
    assert result.games_by_date == []
