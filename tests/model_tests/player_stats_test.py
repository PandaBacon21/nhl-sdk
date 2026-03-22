from src.models.players.player.stats.season.season_stats import SeasonStats
from src.models.players.player.stats.season.season_team import SeasonTeam
from src.models.players.player.stats.season.season import Season
from src.models.players.player.stats.season.featured_game_stats import FeaturedGame
from src.models.players.player.stats.career_stats import Career, CareerStats
from src.models.players.player.stats.featured_stats import Featured, FeaturedStats


STAT_DATA = {
    "assists": 70,
    "avgToi": "22:15",
    "faceoffWinningPctg": 0.524,
    "gameWinningGoals": 8,
    "gamesPlayed": 82,
    "goals": 30,
    "otGoals": 2,
    "pim": 14,
    "plusMinus": 22,
    "points": 100,
    "powerPlayGoals": 10,
    "powerPlayPoints": 28,
    "shootingPctg": 0.147,
    "shorthandedGoals": 1,
    "shorthandedPoints": 2,
    "shots": 204,
}


# ==========================================================================
# SEASON STATS
# ==========================================================================

def test_season_stats_from_dict() -> None:
    stats = SeasonStats.from_dict(STAT_DATA)
    assert stats.assists == 70
    assert stats.avg_toi == "22:15"
    assert stats.faceoff_win_pctg == 0.524
    assert stats.game_winning_goals == 8
    assert stats.games_played == 82
    assert stats.goals == 30
    assert stats.ot_goals == 2
    assert stats.pim == 14
    assert stats.plus_minus == 22
    assert stats.points == 100
    assert stats.pp_goals == 10
    assert stats.pp_points == 28
    assert stats.shooting_pctg == 0.147
    assert stats.sh_goals == 1
    assert stats.sh_points == 2
    assert stats.shots == 204

def test_season_stats_empty() -> None:
    stats = SeasonStats.from_dict({})
    assert stats.goals is None
    assert stats.assists is None
    assert stats.points is None
    assert stats.games_played is None

def test_season_stats_to_dict() -> None:
    stats = SeasonStats.from_dict(STAT_DATA)
    d = stats.to_dict()
    assert d["goals"] == 30
    assert d["assists"] == 70
    assert d["pp_goals"] == 10
    assert d["shooting_pctg"] == 0.147


# ==========================================================================
# SEASON TEAM
# ==========================================================================

def test_season_team_from_dict() -> None:
    data = {
        "teamCommonName": {"default": "Oilers"},
        "teamName": {"default": "Edmonton Oilers"},
    }
    team = SeasonTeam.from_dict(data)
    assert team.common_name.default == "Oilers"
    assert team.name.default == "Edmonton Oilers"

def test_season_team_empty() -> None:
    team = SeasonTeam.from_dict({})
    assert team.common_name.default is None
    assert team.name.default is None

def test_season_team_to_dict_uses_str() -> None:
    """to_dict uses str() on LocalizedString, so it returns '' for missing, not None."""
    team = SeasonTeam.from_dict({
        "teamCommonName": {"default": "Oilers"},
        "teamName": {"default": "Edmonton Oilers"},
    })
    d = team.to_dict()
    assert d["common_name"] == "Oilers"
    assert d["name"] == "Edmonton Oilers"

def test_season_team_to_dict_empty_is_empty_string() -> None:
    team = SeasonTeam.from_dict({})
    d = team.to_dict()
    assert d["common_name"] == ""
    assert d["name"] == ""


# ==========================================================================
# SEASON
# ==========================================================================

SEASON_DATA = {
    "season": 20232024,
    "sequence": 1,
    "gameTypeId": 2,
    "leagueAbbrev": "NHL",
    "teamCommonName": {"default": "Oilers"},
    "teamName": {"default": "Edmonton Oilers"},
    **STAT_DATA,
}

def test_season_from_dict() -> None:
    season = Season.from_dict(SEASON_DATA)
    assert season.season == 20232024
    assert season.sequence == 1
    assert season.game_type_id == 2
    assert season.league == "NHL"
    assert season.team.common_name.default == "Oilers"
    assert season.stats.goals == 30
    assert season.stats.points == 100

def test_season_empty() -> None:
    # Season.from_dict({}) is valid — all fields fall back to None/empty
    season = Season.from_dict({})
    assert season.season is None
    assert season.league is None
    assert season.stats.goals is None

def test_season_to_dict() -> None:
    season = Season.from_dict(SEASON_DATA)
    d = season.to_dict()
    assert d["season"] == 20232024
    assert d["league"] == "NHL"
    assert d["team"]["common_name"] == "Oilers"
    assert d["stats"]["goals"] == 30


# ==========================================================================
# FEATURED GAME
# ==========================================================================

GAME_DATA = {
    "assists": 2,
    "gameDate": "2024-01-15",
    "gameId": 2023020500,
    "gameTypeId": 2,
    "goals": 1,
    "homeRoadFlag": "H",
    "opponentAbbrev": "TOR",
    "pim": 0,
    "plusMinus": 2,
    "points": 3,
    "powerPlayGoals": 1,
    "shifts": 22,
    "shorthandedGoals": 0,
    "shots": 5,
    "teamAbbrev": "EDM",
    "toi": "22:15",
}

def test_featured_game_from_dict() -> None:
    game = FeaturedGame.from_dict(GAME_DATA)
    assert game.assists == 2
    assert game.game_date == "2024-01-15"
    assert game.game_id == 2023020500
    assert game.game_type_id == 2
    assert game.goals == 1
    assert game.home_road_flag == "H"
    assert game.opponent_abbrev == "TOR"
    assert game.pim == 0
    assert game.plus_minus == 2
    assert game.points == 3
    assert game.pp_goals == 1
    assert game.shifts == 22
    assert game.sh_goals == 0
    assert game.shots == 5
    assert game.team_abbrev == "EDM"
    assert game.toi == "22:15"

def test_featured_game_empty() -> None:
    game = FeaturedGame.from_dict({})
    assert game.goals is None
    assert game.assists is None
    assert game.game_date is None

def test_featured_game_to_dict() -> None:
    game = FeaturedGame.from_dict(GAME_DATA)
    d = game.to_dict()
    assert d["goals"] == 1
    assert d["assists"] == 2
    assert d["game_date"] == "2024-01-15"
    assert d["pp_goals"] == 1


# ==========================================================================
# CAREER STATS
# ==========================================================================

def test_career_stats_from_dict() -> None:
    stats = CareerStats.from_dict(STAT_DATA)
    assert stats.goals == 30
    assert stats.assists == 70
    assert stats.points == 100
    assert stats.games_played == 82
    assert stats.pp_goals == 10
    assert stats.sh_goals == 1

def test_career_stats_empty() -> None:
    stats = CareerStats.from_dict({})
    assert stats.goals is None
    assert stats.assists is None

def test_career_from_dict() -> None:
    data = {
        "regularSeason": STAT_DATA,
        "playoffs": {**STAT_DATA, "gamesPlayed": 14, "goals": 5, "assists": 12, "points": 17},
    }
    career = Career.from_dict(data)
    assert career.regular_season.goals == 30
    assert career.regular_season.games_played == 82
    assert career.playoffs.goals == 5
    assert career.playoffs.games_played == 14
    assert career.playoffs.points == 17

def test_career_empty() -> None:
    career = Career.from_dict({})
    assert career.regular_season.goals is None
    assert career.playoffs.goals is None


# ==========================================================================
# FEATURED STATS
# ==========================================================================

FEATURED_STAT_DATA = {
    "assists": 70,
    "gameWinningGoals": 8,
    "gamesPlayed": 82,
    "goals": 30,
    "otGoals": 2,
    "pim": 14,
    "plusMinus": 22,
    "points": 100,
    "powerPlayGoals": 10,
    "powerPlayPoints": 28,
    "shootingPctg": 0.147,
    "shorthandedGoals": 1,
    "shorthandedPoints": 2,
    "shots": 204,
}

def test_featured_stats_from_dict() -> None:
    stats = FeaturedStats.from_dict(FEATURED_STAT_DATA)
    assert stats.goals == 30
    assert stats.assists == 70
    assert stats.points == 100
    assert stats.games_played == 82
    assert stats.pp_goals == 10
    assert stats.shooting_pctg == 0.147

def test_featured_stats_empty() -> None:
    stats = FeaturedStats.from_dict({})
    assert stats.goals is None
    assert stats.assists is None

def test_featured_from_dict() -> None:
    data = {
        "season": 20232024,
        "regularSeason": {
            "subSeason": FEATURED_STAT_DATA,
            "career": {**FEATURED_STAT_DATA, "goals": 300, "gamesPlayed": 600},
        }
    }
    featured = Featured.from_dict(data)
    assert featured.season == 20232024
    assert featured.season_stats.goals == 30
    assert featured.season_stats.games_played == 82
    assert featured.career_stats.goals == 300
    assert featured.career_stats.games_played == 600

def test_featured_empty() -> None:
    featured = Featured.from_dict({})
    assert featured.season is None
    assert featured.season_stats.goals is None
    assert featured.career_stats.goals is None

def test_featured_to_dict() -> None:
    data = {
        "season": 20232024,
        "regularSeason": {
            "subSeason": FEATURED_STAT_DATA,
            "career": {**FEATURED_STAT_DATA, "goals": 300},
        }
    }
    featured = Featured.from_dict(data)
    d = featured.to_dict()
    assert d["season"] == 20232024
    assert d["season_stats"]["goals"] == 30
    assert d["career_stats"]["goals"] == 300
