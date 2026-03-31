from src.models.games.pbp import GamePlayByPlay, PlayByPlayResult

from .conftest import ok

GAME_ID = 2025020417


def test_get_pbp_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_play_by_play.return_value = ok({"plays": []})
    svc = GamePlayByPlay(mock_client)
    result = svc.get_play_by_play(game_id=GAME_ID)
    assert isinstance(result, PlayByPlayResult)
    mock_client._api.api_web.call_nhl_games.get_play_by_play.assert_called_once_with(game_id=GAME_ID)


def test_get_pbp_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_play_by_play.return_value = ok({"plays": []})
    svc = GamePlayByPlay(mock_client)
    _ = svc.get_play_by_play(game_id=GAME_ID)
    _ = svc.get_play_by_play(game_id=GAME_ID)
    mock_client._api.api_web.call_nhl_games.get_play_by_play.assert_called_once()


def test_get_pbp_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_play_by_play.return_value = ok({"plays": []})
    svc = GamePlayByPlay(mock_client)
    _ = svc.get_play_by_play(game_id=GAME_ID)
    _ = svc.get_play_by_play(game_id=GAME_ID + 1)
    assert mock_client._api.api_web.call_nhl_games.get_play_by_play.call_count == 2


def test_get_pbp_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_play_by_play.return_value = ok({
        "id": GAME_ID,
        "season": 20252026,
        "gameType": 2,
        "limitedScoring": False,
        "gameDate": "2025-12-02",
        "venue": {"default": "Ball Arena"},
        "venueLocation": {"default": "Denver"},
        "startTimeUTC": "2025-12-03T02:00:00Z",
        "easternUTCOffset": "-05:00",
        "venueUTCOffset": "-07:00",
        "tvBroadcasts": [],
        "gameState": "OFF",
        "gameScheduleState": "OK",
        "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
        "awayTeam": {
            "id": 23, "commonName": {"default": "Canucks"}, "abbrev": "VAN",
            "score": 1, "sog": 21, "logo": "", "darkLogo": "",
            "placeName": {"default": "Vancouver"},
            "placeNameWithPreposition": {"default": "Vancouver"},
        },
        "homeTeam": {
            "id": 21, "commonName": {"default": "Avalanche"}, "abbrev": "COL",
            "score": 3, "sog": 31, "logo": "", "darkLogo": "",
            "placeName": {"default": "Colorado"},
            "placeNameWithPreposition": {"default": "Colorado"},
        },
        "shootoutInUse": True,
        "otInUse": True,
        "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
        "displayPeriod": 1,
        "maxPeriods": 5,
        "gameOutcome": {"lastPeriodType": "REG"},
        "plays": [
            {
                "eventId": 53,
                "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
                "timeInPeriod": "00:00",
                "timeRemaining": "20:00",
                "situationCode": "1551",
                "homeTeamDefendingSide": "right",
                "typeCode": 502,
                "typeDescKey": "faceoff",
                "sortOrder": 11,
                "details": {
                    "eventOwnerTeamId": 23,
                    "losingPlayerId": 8477492,
                    "winningPlayerId": 8480012,
                    "xCoord": 0, "yCoord": 0, "zoneCode": "N",
                },
            },
        ],
    })
    svc = GamePlayByPlay(mock_client)
    result = svc.get_play_by_play(game_id=GAME_ID)
    assert result.id == GAME_ID
    assert result.away_team.abbrev == "VAN"
    assert result.home_team.score == 3
    assert result.clock.running is False
    assert result.game_outcome.last_period_type == "REG"
    assert len(result.plays) == 1
    assert result.plays[0].type_desc_key == "faceoff"
    assert result.plays[0].details.winning_player_id == 8480012
