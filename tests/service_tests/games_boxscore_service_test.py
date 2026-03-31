from src.models.games.boxscore import GameBoxscore, GameBoxscoreResult

from .conftest import ok

GAME_ID = 2025020691


def test_get_boxscore_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_boxscore.return_value = ok({})
    svc = GameBoxscore(mock_client)
    result = svc.get_boxscore(game_id=GAME_ID)
    assert isinstance(result, GameBoxscoreResult)
    mock_client._api.api_web.call_nhl_games.get_boxscore.assert_called_once_with(game_id=GAME_ID)


def test_get_boxscore_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_boxscore.return_value = ok({})
    svc = GameBoxscore(mock_client)
    _ = svc.get_boxscore(game_id=GAME_ID)
    _ = svc.get_boxscore(game_id=GAME_ID)
    mock_client._api.api_web.call_nhl_games.get_boxscore.assert_called_once()


def test_get_boxscore_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_boxscore.return_value = ok({})
    svc = GameBoxscore(mock_client)
    _ = svc.get_boxscore(game_id=GAME_ID)
    _ = svc.get_boxscore(game_id=GAME_ID + 1)
    assert mock_client._api.api_web.call_nhl_games.get_boxscore.call_count == 2


def test_get_boxscore_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_boxscore.return_value = ok({
        "id": GAME_ID,
        "season": 20252026,
        "gameType": 2,
        "gameDate": "2026-01-08",
        "venue": {"default": "Ball Arena"},
        "venueLocation": {"default": "Denver"},
        "startTimeUTC": "2026-01-09T02:00:00Z",
        "easternUTCOffset": "-05:00",
        "venueUTCOffset": "-07:00",
        "tvBroadcasts": [],
        "gameState": "OFF",
        "gameScheduleState": "OK",
        "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
        "regPeriods": 3,
        "awayTeam": {
            "id": 9, "commonName": {"default": "Senators"}, "abbrev": "OTT",
            "score": 2, "sog": 31, "logo": "", "darkLogo": "",
            "placeName": {"default": "Ottawa"}, "placeNameWithPreposition": {"default": "Ottawa"},
        },
        "homeTeam": {
            "id": 21, "commonName": {"default": "Avalanche"}, "abbrev": "COL",
            "score": 8, "sog": 34, "logo": "", "darkLogo": "",
            "placeName": {"default": "Colorado"}, "placeNameWithPreposition": {"default": "Colorado"},
        },
        "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
        "playerByGameStats": {
            "awayTeam": {
                "forwards": [],
                "defense": [],
                "goalies": [
                    {
                        "playerId": 8482447,
                        "sweaterNumber": 1,
                        "name": {"default": "L. Meriläinen"},
                        "position": "G",
                        "evenStrengthShotsAgainst": "9/12",
                        "powerPlayShotsAgainst": "5/5",
                        "shorthandedShotsAgainst": "1/1",
                        "saveShotsAgainst": "15/18",
                        "savePctg": 0.833333,
                        "evenStrengthGoalsAgainst": 3,
                        "powerPlayGoalsAgainst": 0,
                        "shorthandedGoalsAgainst": 0,
                        "pim": 0,
                        "goalsAgainst": 3,
                        "toi": "42:35",
                        "starter": True,
                        "decision": "L",
                        "shotsAgainst": 18,
                        "saves": 15,
                    }
                ],
            },
            "homeTeam": {
                "forwards": [
                    {
                        "playerId": 8477492,
                        "sweaterNumber": 29,
                        "name": {"default": "N. MacKinnon"},
                        "position": "C",
                        "goals": 1,
                        "assists": 3,
                        "points": 4,
                        "plusMinus": 0,
                        "pim": 0,
                        "hits": 0,
                        "powerPlayGoals": 0,
                        "sog": 5,
                        "faceoffWinningPctg": 0.615385,
                        "toi": "17:14",
                        "blockedShots": 1,
                        "shifts": 19,
                        "giveaways": 1,
                        "takeaways": 0,
                    }
                ],
                "defense": [],
                "goalies": [],
            },
        },
        "gameOutcome": {"lastPeriodType": "REG"},
    })
    svc = GameBoxscore(mock_client)
    result = svc.get_boxscore(game_id=GAME_ID)
    assert result.id == GAME_ID
    assert result.away_team.abbrev == "OTT"
    assert result.home_team.score == 8
    assert result.clock.running is False
    assert result.game_outcome.last_period_type == "REG"
    assert result.player_by_game_stats is not None
    away_goalie = result.player_by_game_stats.away_team.goalies[0]
    assert away_goalie.decision == "L"
    assert away_goalie.saves == 15
    home_fwd = result.player_by_game_stats.home_team.forwards[0]
    assert home_fwd.name.default == "N. MacKinnon"
    assert home_fwd.points == 4
