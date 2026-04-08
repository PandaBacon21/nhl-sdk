from nhl_stats.models.players.player.player_stats.games.player_season_game_type import SeasonGameType
from nhl_stats.models.players.player.player_stats.games.player_game import Game
from nhl_stats.models.players.player.player_stats.games.player_game_logs import GameLogs


# ==========================================================================
# SEASON GAME TYPE
# ==========================================================================

def test_season_game_type_with_playoffs() -> None:
    data = {"season": 20232024, "gameTypes": [2, 3]}
    sgt = SeasonGameType.from_dict(data)
    assert sgt.season == 20232024
    assert sgt.game_types == [2, 3]
    assert sgt.playoffs is True

def test_season_game_type_regular_only() -> None:
    data = {"season": 20232024, "gameTypes": [2]}
    sgt = SeasonGameType.from_dict(data)
    assert sgt.season == 20232024
    assert sgt.game_types == [2]
    assert sgt.playoffs is False

def test_season_game_type_empty() -> None:
    sgt = SeasonGameType.from_dict({})
    assert sgt.season is None
    assert sgt.game_types == []
    assert sgt.playoffs is False


# ==========================================================================
# GAME
# ==========================================================================

GAME_DATA = {
    "gameId": 2023020500,
    "teamAbbrev": "EDM",
    "homeRoadFlag": "H",
    "gameDate": "2024-01-15",
    "goals": 1,
    "assists": 2,
    "commonName": {"default": "Oilers"},
    "opponentCommonName": {"default": "Leafs"},
    "points": 3,
    "plusMinus": 2,
    "powerPlayGoals": 1,
    "powerPlayPoints": 2,
    "gameWinningGoals": 0,
    "otGoals": 0,
    "shots": 5,
    "shifts": 22,
    "shorthandedGoals": 0,
    "shorthandedPoints": 0,
    "opponentAbbrev": "TOR",
    "pim": 0,
    "toi": "22:15",
}

def test_game_from_dict() -> None:
    game = Game.from_dict(GAME_DATA)
    assert game.game_id == 2023020500
    assert game.team_abbrev == "EDM"
    assert game.home_road_flag == "H"
    assert game.game_date == "2024-01-15"
    assert game.goals == 1
    assert game.assists == 2
    assert game.team_name.default == "Oilers"
    assert game.opponent_name.default == "Leafs"
    assert game.points == 3
    assert game.plus_minus == 2
    assert game.pp_goals == 1
    assert game.pp_points == 2
    assert game.gw_goals == 0
    assert game.shots == 5
    assert game.shifts == 22
    assert game.sh_goals == 0
    assert game.opponent_abbrev == "TOR"
    assert game.pim == 0
    assert game.toi == "22:15"

def test_game_empty() -> None:
    game = Game.from_dict({})
    assert game.game_id is None
    assert game.goals is None
    assert game.team_name.default is None
    assert game.toi is None

def test_game_to_dict() -> None:
    game = Game.from_dict(GAME_DATA)
    d = game.to_dict()
    assert d["game_id"] == 2023020500
    assert d["goals"] == 1
    assert d["assists"] == 2
    assert d["team_name"] == "Oilers"
    assert d["opponent_name"] == "Leafs"
    assert d["power_play_goals"] == 1
    assert d["time_on_ice"] == "22:15"
    assert d["penalty_minutes"] == 0

def test_game_to_dict_keys_renamed() -> None:
    """to_dict renames several keys from the model field names."""
    game = Game.from_dict(GAME_DATA)
    d = game.to_dict()
    # Verify the renamed keys exist with correct values
    assert "power_play_goals" in d       # pp_goals → power_play_goals
    assert "power_play_points" in d      # pp_points → power_play_points
    assert "game_winning_goals" in d     # gw_goals → game_winning_goals
    assert "overtime_goals" in d         # ot_goals → overtime_goals
    assert "shorthanded_goals" in d      # sh_goals → shorthanded_goals
    assert "shorthanded_points" in d     # sh_points → shorthanded_points
    assert "penalty_minutes" in d        # pim → penalty_minutes
    assert "time_on_ice" in d            # toi → time_on_ice


# ==========================================================================
# GAME LOGS
# ==========================================================================

def test_game_logs_from_dict(capsys) -> None:
    data = {
        "seasonId": 20232024,
        "gameTypeId": 2,
        "playerStatsSeasons": [
            {"season": 20232024, "gameTypes": [2, 3]},
            {"season": 20222023, "gameTypes": [2]},
        ],
        "gameLog": [GAME_DATA],
    }
    logs = GameLogs.from_dict(data)
    assert logs.season_id == 20232024
    assert logs.game_type == 2
    assert len(logs.seasons) == 2
    assert logs.seasons[0].season == 20232024
    assert logs.seasons[0].playoffs is True
    assert logs.seasons[1].playoffs is False
    assert len(logs.games) == 1
    assert logs.games[0].game_date == "2024-01-15"

def test_game_logs_empty(capsys) -> None:
    logs = GameLogs.from_dict({})
    assert logs.season_id is None
    assert logs.game_type is None
    assert logs.seasons == []
    assert logs.games == []
