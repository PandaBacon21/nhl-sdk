from nhl_stats.models.games.game import Game
from nhl_stats.models.games.pbp.pbp_result import PlayByPlayResult
from nhl_stats.models.games.landing.landing_result import GameLandingResult
from nhl_stats.models.games.boxscore.boxscore_result import GameBoxscoreResult
from nhl_stats.models.games.story.story_result import GameStoryResult
from nhl_stats.models.games.shifts.shift_chart import ShiftChart

from .conftest import ok

GAME_ID = 2025020417


# ==========================================================================
# Games.get()
# ==========================================================================

def test_games_get_returns_game(mock_client) -> None:
    from nhl_stats.services.games import Games
    svc = Games(mock_client)
    game = svc.get(GAME_ID)
    assert isinstance(game, Game)
    assert game.game_id == GAME_ID


# ==========================================================================
# Game.pbp()
# ==========================================================================

def test_pbp_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_play_by_play.return_value = ok({"plays": []})
    game = Game(mock_client, GAME_ID)
    result = game.pbp()
    assert isinstance(result, PlayByPlayResult)
    mock_client._api.api_web.call_nhl_games.get_play_by_play.assert_called_once_with(game_id=GAME_ID)


def test_pbp_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_play_by_play.return_value = ok({"plays": []})
    game = Game(mock_client, GAME_ID)
    _ = game.pbp()
    _ = game.pbp()
    mock_client._api.api_web.call_nhl_games.get_play_by_play.assert_called_once()


def test_pbp_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_play_by_play.return_value = ok({"plays": []})
    _ = Game(mock_client, GAME_ID).pbp()
    _ = Game(mock_client, GAME_ID + 1).pbp()
    assert mock_client._api.api_web.call_nhl_games.get_play_by_play.call_count == 2


def test_pbp_result_populated(mock_client) -> None:
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
    result = Game(mock_client, GAME_ID).pbp()
    assert result.id == GAME_ID
    assert result.away_team.abbrev == "VAN"
    assert result.home_team.score == 3
    assert result.clock.running is False
    assert result.game_outcome.last_period_type == "REG"
    assert len(result.plays) == 1
    assert result.plays[0].type_desc_key == "faceoff"
    assert result.plays[0].details.winning_player_id == 8480012


# ==========================================================================
# Game.landing()
# ==========================================================================

def test_landing_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({})
    game = Game(mock_client, GAME_ID)
    result = game.landing()
    assert isinstance(result, GameLandingResult)
    mock_client._api.api_web.call_nhl_games.get_game_landing.assert_called_once_with(game_id=GAME_ID)


def test_landing_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({})
    game = Game(mock_client, GAME_ID)
    _ = game.landing()
    _ = game.landing()
    mock_client._api.api_web.call_nhl_games.get_game_landing.assert_called_once()


def test_landing_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({})
    _ = Game(mock_client, GAME_ID).landing()
    _ = Game(mock_client, GAME_ID + 1).landing()
    assert mock_client._api.api_web.call_nhl_games.get_game_landing.call_count == 2


def test_landing_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_landing.return_value = ok({
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
        "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
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
        "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
        "summary": {
            "scoring": [
                {
                    "periodDescriptor": {"number": 1, "periodType": "REG", "maxRegulationPeriods": 3},
                    "goals": [
                        {
                            "situationCode": "1551", "eventId": 95, "strength": "ev",
                            "playerId": 8481024,
                            "firstName": {"default": "Linus"}, "lastName": {"default": "Karlsson"},
                            "name": {"default": "L. Karlsson"}, "teamAbbrev": {"default": "VAN"},
                            "goalsToDate": 5, "awayScore": 1, "homeScore": 0,
                            "timeInPeriod": "02:55", "shotType": "backhand",
                            "goalModifier": "none", "assists": [], "isHome": False,
                        }
                    ],
                }
            ],
            "threeStars": [
                {
                    "star": 1, "playerId": 8477492, "teamAbbrev": "COL",
                    "name": {"default": "N. MacKinnon"}, "sweaterNo": 29,
                    "position": "C", "goals": 2, "assists": 0, "points": 2,
                }
            ],
            "penalties": [],
        },
    })
    result = Game(mock_client, GAME_ID).landing()
    assert result.id == GAME_ID
    assert result.away_team.abbrev == "VAN"
    assert result.home_team.score == 3
    assert result.venue_timezone == "America/Denver"
    assert result.clock.running is False
    assert result.summary is not None
    assert result.summary.scoring[0].goals[0].strength == "ev"
    assert result.summary.three_stars[0].name.default == "N. MacKinnon"


# ==========================================================================
# Game.boxscore()
# ==========================================================================

BOXSCORE_GAME_ID = 2025020691


def test_boxscore_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_boxscore.return_value = ok({})
    game = Game(mock_client, BOXSCORE_GAME_ID)
    result = game.boxscore()
    assert isinstance(result, GameBoxscoreResult)
    mock_client._api.api_web.call_nhl_games.get_boxscore.assert_called_once_with(game_id=BOXSCORE_GAME_ID)


def test_boxscore_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_boxscore.return_value = ok({})
    game = Game(mock_client, BOXSCORE_GAME_ID)
    _ = game.boxscore()
    _ = game.boxscore()
    mock_client._api.api_web.call_nhl_games.get_boxscore.assert_called_once()


def test_boxscore_result_populated(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_boxscore.return_value = ok({
        "id": BOXSCORE_GAME_ID,
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
                "forwards": [], "defense": [],
                "goalies": [
                    {
                        "playerId": 8482447, "sweaterNumber": 1,
                        "name": {"default": "L. Meriläinen"}, "position": "G",
                        "evenStrengthShotsAgainst": "9/12", "powerPlayShotsAgainst": "5/5",
                        "shorthandedShotsAgainst": "1/1", "saveShotsAgainst": "15/18",
                        "savePctg": 0.833333, "evenStrengthGoalsAgainst": 3,
                        "powerPlayGoalsAgainst": 0, "shorthandedGoalsAgainst": 0,
                        "pim": 0, "goalsAgainst": 3, "toi": "42:35",
                        "starter": True, "decision": "L", "shotsAgainst": 18, "saves": 15,
                    }
                ],
            },
            "homeTeam": {
                "forwards": [
                    {
                        "playerId": 8477492, "sweaterNumber": 29,
                        "name": {"default": "N. MacKinnon"}, "position": "C",
                        "goals": 1, "assists": 3, "points": 4,
                        "plusMinus": 0, "pim": 0, "hits": 0,
                        "powerPlayGoals": 0, "sog": 5, "faceoffWinningPctg": 0.615385,
                        "toi": "17:14", "blockedShots": 1, "shifts": 19,
                        "giveaways": 1, "takeaways": 0,
                    }
                ],
                "defense": [], "goalies": [],
            },
        },
        "gameOutcome": {"lastPeriodType": "REG"},
    })
    result = Game(mock_client, BOXSCORE_GAME_ID).boxscore()
    assert result.id == BOXSCORE_GAME_ID
    assert result.away_team.abbrev == "OTT"
    assert result.home_team.score == 8
    assert result.game_outcome.last_period_type == "REG"
    away_goalie = result.player_by_game_stats.away_team.goalies[0]
    assert away_goalie.decision == "L"
    assert away_goalie.saves == 15
    home_fwd = result.player_by_game_stats.home_team.forwards[0]
    assert home_fwd.name.default == "N. MacKinnon"
    assert home_fwd.points == 4


# ==========================================================================
# Game.story()
# ==========================================================================

def test_story_cache_miss(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_story.return_value = ok({})
    game = Game(mock_client, GAME_ID)
    result = game.story()
    assert isinstance(result, GameStoryResult)
    mock_client._api.api_web.call_nhl_games.get_game_story.assert_called_once_with(game_id=GAME_ID)


def test_story_cache_hit(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_story.return_value = ok({})
    game = Game(mock_client, GAME_ID)
    _ = game.story()
    _ = game.story()
    mock_client._api.api_web.call_nhl_games.get_game_story.assert_called_once()


def test_story_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_web.call_nhl_games.get_game_story.return_value = ok({})
    _ = Game(mock_client, GAME_ID).story()
    _ = Game(mock_client, GAME_ID + 1).story()
    assert mock_client._api.api_web.call_nhl_games.get_game_story.call_count == 2


def test_story_result_populated(mock_client) -> None:
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
        "periodDescriptor": {"number": 3, "periodType": "REG", "maxRegulationPeriods": 3},
        "clock": {"timeRemaining": "00:00", "secondsRemaining": 0, "running": False, "inIntermission": False},
        "summary": {
            "scoring": [],
            "threeStars": [
                {
                    "star": 1, "playerId": 8477492, "teamAbbrev": "COL",
                    "name": "N. MacKinnon", "sweaterNo": 29,
                    "position": "C", "goals": 2, "assists": 0, "points": 2,
                }
            ],
            "teamGameStats": [
                {"category": "sog", "awayValue": 21, "homeValue": 31},
                {"category": "powerPlay", "awayValue": "0/1", "homeValue": "0/1"},
            ],
        },
    })
    result = Game(mock_client, GAME_ID).story()
    assert result.id == GAME_ID
    assert result.away_team.abbrev == "VAN"
    assert result.home_team.score == 3
    assert result.venue_timezone == "America/Denver"
    assert result.summary.three_stars[0].name == "N. MacKinnon"
    assert result.summary.team_game_stats[0].category == "sog"
    assert result.summary.team_game_stats[1].away_value == "0/1"


# ==========================================================================
# Game.shifts()
# ==========================================================================

def test_shifts_cache_miss(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok(
        {"data": [], "total": 0}
    )
    game = Game(mock_client, GAME_ID)
    result = game.shifts()
    assert isinstance(result, ShiftChart)
    assert result.game_id == GAME_ID
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.assert_called_once_with(
        game_id=GAME_ID
    )


def test_shifts_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok(
        {"data": [], "total": 0}
    )
    game = Game(mock_client, GAME_ID)
    _ = game.shifts()
    _ = game.shifts()
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.assert_called_once()


def test_shifts_different_game_ids_separate_cache_keys(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok(
        {"data": [], "total": 0}
    )
    _ = Game(mock_client, GAME_ID).shifts()
    _ = Game(mock_client, GAME_ID + 1).shifts()
    assert mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.call_count == 2


def test_shifts_result_populated(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_misc.get_shift_charts.return_value = ok({
        "total": 2,
        "data": [
            {
                "id": 101, "gameId": GAME_ID, "playerId": 8477492,
                "period": 1, "shiftNumber": 1, "startTime": "00:00",
                "endTime": "01:23", "duration": "01:23",
                "firstName": "Ryan", "lastName": "Johansen",
                "teamId": 21, "teamAbbrev": "COL", "teamName": "Colorado Avalanche",
                "hexValue": "#236192", "detailCode": 0,
                "eventDescription": None, "eventDetails": None,
                "eventNumber": None, "typeCode": 517,
            },
            {
                "id": 102, "gameId": GAME_ID, "playerId": 8478402,
                "period": 1, "shiftNumber": 2, "startTime": "01:30",
                "endTime": "03:00", "duration": "01:30",
                "firstName": "Nathan", "lastName": "MacKinnon",
                "teamId": 21, "teamAbbrev": "COL", "teamName": "Colorado Avalanche",
                "hexValue": "#236192", "detailCode": 0,
                "eventDescription": None, "eventDetails": None,
                "eventNumber": None, "typeCode": 517,
            },
        ],
    })
    result = Game(mock_client, GAME_ID).shifts()
    assert result.game_id == GAME_ID
    assert result.total == 2
    assert len(result.shifts) == 2
    first = result.shifts[0]
    assert first.player_id == 8477492
    assert first.team_abbrev == "COL"
    assert first.start_time == "00:00"
    assert first.shift_number == 1
