from src.models.games.story import GameStory, GameStoryResult

from .conftest import ok

GAME_ID = 2025020417


def test_get_story_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_story.return_value = ok({})
    svc = GameStory(mock_client)
    result = svc.get_game_story(game_id=GAME_ID)
    assert isinstance(result, GameStoryResult)
    mock_client._api.api_web.call_nhl_games.get_game_story.assert_called_once_with(game_id=GAME_ID)


def test_get_story_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_story.return_value = ok({})
    svc = GameStory(mock_client)
    _ = svc.get_game_story(game_id=GAME_ID)
    _ = svc.get_game_story(game_id=GAME_ID)
    mock_client._api.api_web.call_nhl_games.get_game_story.assert_called_once()


def test_get_story_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_story.return_value = ok({})
    svc = GameStory(mock_client)
    _ = svc.get_game_story(game_id=GAME_ID)
    _ = svc.get_game_story(game_id=GAME_ID + 1)
    assert mock_client._api.api_web.call_nhl_games.get_game_story.call_count == 2


def test_get_story_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_story.return_value = ok({
        "id": GAME_ID,
        "season": 20252026,
        "gameType": 2,
        "gameDate": "2025-12-02",
        "venue": {"default": "Ball Arena"},
        "venueLocation": {"default": "Denver"},
        "venueTimezone": "America/Denver",
        "startTimeUTC": "2025-12-03T02:00:00Z",
        "easternUTCOffset": "-05:00",
        "venueUTCOffset": "-07:00",
        "tvBroadcasts": [],
        "gameState": "OFF",
        "gameScheduleState": "OK",
        "awayTeam": {
            "id": 23, "name": {"default": "Canucks"}, "abbrev": "VAN",
            "placeName": {"default": "Vancouver"}, "score": 1, "sog": 21, "logo": "",
        },
        "homeTeam": {
            "id": 21, "name": {"default": "Avalanche"}, "abbrev": "COL",
            "placeName": {"default": "Colorado"}, "score": 3, "sog": 31, "logo": "",
        },
        "shootoutInUse": True,
        "maxPeriods": 5,
        "regPeriods": 3,
        "otInUse": True,
        "tiesInUse": False,
        "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
        "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
        "summary": {
            "scoring": [],
            "threeStars": [
                {
                    "star": 1,
                    "playerId": 8477492,
                    "teamAbbrev": "COL",
                    "name": "N. MacKinnon",
                    "sweaterNo": 29,
                    "position": "C",
                    "goals": 2,
                    "assists": 0,
                    "points": 2,
                }
            ],
            "teamGameStats": [
                {"category": "sog", "awayValue": 21, "homeValue": 31},
                {"category": "powerPlay", "awayValue": "0/1", "homeValue": "0/1"},
            ],
        },
    })
    svc = GameStory(mock_client)
    result = svc.get_game_story(game_id=GAME_ID)
    assert result.id == GAME_ID
    assert result.away_team.abbrev == "VAN"
    assert result.away_team.name.default == "Canucks"
    assert result.home_team.score == 3
    assert result.venue_timezone == "America/Denver"
    assert result.clock.running is False
    assert result.summary is not None
    assert result.summary.three_stars[0].name == "N. MacKinnon"
    assert result.summary.team_game_stats[0].category == "sog"
    assert result.summary.team_game_stats[1].away_value == "0/1"
