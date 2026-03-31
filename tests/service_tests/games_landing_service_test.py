from src.models.games.landing import GameLanding, GameLandingResult

from .conftest import ok

GAME_ID = 2025020417


def test_get_landing_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({})
    svc = GameLanding(mock_client)
    result = svc.get_landing(game_id=GAME_ID)
    assert isinstance(result, GameLandingResult)
    mock_client._api.api_web.call_nhl_games.get_game_landing.assert_called_once_with(game_id=GAME_ID)


def test_get_landing_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({})
    svc = GameLanding(mock_client)
    _ = svc.get_landing(game_id=GAME_ID)
    _ = svc.get_landing(game_id=GAME_ID)
    mock_client._api.api_web.call_nhl_games.get_game_landing.assert_called_once()


def test_get_landing_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({})
    svc = GameLanding(mock_client)
    _ = svc.get_landing(game_id=GAME_ID)
    _ = svc.get_landing(game_id=GAME_ID + 1)
    assert mock_client._api.api_web.call_nhl_games.get_game_landing.call_count == 2


def test_get_landing_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({
        "id": GAME_ID,
        "season": 20252026,
        "gameType": 2,
        "limitedScoring": False,
        "gameDate": "2025-12-02",
        "venue": {"default": "Ball Arena"},
        "venueLocation": {"default": "Denver"},
        "venueTimezone": "America/Denver",
        "startTimeUTC": "2025-12-03T02:00:00Z",
        "easternUTCOffset": "-05:00",
        "venueUTCOffset": "-07:00",
        "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
        "tvBroadcasts": [],
        "gameState": "OFF",
        "gameScheduleState": "OK",
        "awayTeam": {
            "id": 23, "commonName": {"default": "Canucks"}, "abbrev": "VAN",
            "score": 1, "sog": 21, "logo": "", "darkLogo": "",
            "placeName": {"default": "Vancouver"}, "placeNameWithPreposition": {"default": "Vancouver"},
        },
        "homeTeam": {
            "id": 21, "commonName": {"default": "Avalanche"}, "abbrev": "COL",
            "score": 3, "sog": 31, "logo": "", "darkLogo": "",
            "placeName": {"default": "Colorado"}, "placeNameWithPreposition": {"default": "Colorado"},
        },
        "shootoutInUse": True,
        "maxPeriods": 5,
        "regPeriods": 3,
        "otInUse": True,
        "tiesInUse": False,
        "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
        "summary": {
            "scoring": [
                {
                    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
                    "goals": [
                        {
                            "situationCode": "1551",
                            "eventId": 95,
                            "strength": "ev",
                            "playerId": 8481024,
                            "firstName": {"default": "Linus"},
                            "lastName": {"default": "Karlsson"},
                            "name": {"default": "L. Karlsson"},
                            "teamAbbrev": {"default": "VAN"},
                            "goalsToDate": 5,
                            "awayScore": 1,
                            "homeScore": 0,
                            "timeInPeriod": "02:55",
                            "shotType": "backhand",
                            "goalModifier": "none",
                            "assists": [],
                            "isHome": False,
                        }
                    ],
                }
            ],
            "threeStars": [
                {
                    "star": 1,
                    "playerId": 8477492,
                    "teamAbbrev": "COL",
                    "name": {"default": "N. MacKinnon"},
                    "sweaterNo": 29,
                    "position": "C",
                    "goals": 2,
                    "assists": 0,
                    "points": 2,
                }
            ],
            "penalties": [],
        },
    })
    svc = GameLanding(mock_client)
    result = svc.get_landing(game_id=GAME_ID)
    assert result.id == GAME_ID
    assert result.away_team.abbrev == "VAN"
    assert result.home_team.score == 3
    assert result.venue_timezone == "America/Denver"
    assert result.clock.running is False
    assert result.summary is not None
    assert len(result.summary.scoring) == 1
    assert result.summary.scoring[0].goals[0].strength == "ev"
    assert result.summary.three_stars[0].name.default == "N. MacKinnon"
    assert result.summary.penalties == []
