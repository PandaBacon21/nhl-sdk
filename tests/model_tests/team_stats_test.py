"""
Tests for the team stats models:
  TeamSkaterStat, TeamGoalieStat, TeamStatsResult,
  TeamSeasonGameTypes, TeamScoreboard and its nested types
"""
from nhl_stats.models.teams.team.team_stats.team_skater_stat import TeamSkaterStat
from nhl_stats.models.teams.team.team_stats.team_goalie_stat import TeamGoalieStat
from nhl_stats.models.teams.team.team_stats.team_stats_result import TeamStatsResult
from nhl_stats.models.teams.team.team_stats.team_season_game_types import TeamSeasonGameTypes
from nhl_stats.models.teams.team.team_stats.team_scoreboard import (
    TeamScoreboard,
    ScoreboardGamesByDate,
    ScoreboardGame,
    ScoreboardTeam,
    ScoreboardTvBroadcast,
    ScoreboardPeriodDescriptor,
)


SKATER_DATA = {
    "playerId": 8477492,
    "headshot": "https://assets.nhle.com/mugs/nhl/20252026/COL/8477492.png",
    "firstName": {"default": "Nathan"},
    "lastName": {"default": "MacKinnon"},
    "positionCode": "C",
    "gamesPlayed": 70,
    "goals": 35,
    "assists": 65,
    "points": 100,
    "plusMinus": 28,
    "penaltyMinutes": 18,
    "powerPlayGoals": 12,
    "shorthandedGoals": 1,
    "gameWinningGoals": 8,
    "overtimeGoals": 2,
    "shots": 220,
    "shootingPctg": 0.159,
    "avgTimeOnIcePerGame": 21.5,
    "avgShiftsPerGame": 24.3,
    "faceoffWinPctg": 0.524,
}

GOALIE_DATA = {
    "playerId": 8480366,
    "headshot": "https://assets.nhle.com/mugs/nhl/20252026/COL/8480366.png",
    "firstName": {"default": "Mackenzie"},
    "lastName": {"default": "Blackwood"},
    "gamesPlayed": 45,
    "gamesStarted": 43,
    "wins": 30,
    "losses": 10,
    "overtimeLosses": 5,
    "goalsAgainstAverage": 2.41,
    "savePercentage": 0.916,
    "shotsAgainst": 1250,
    "saves": 1145,
    "goalsAgainst": 105,
    "shutouts": 4,
    "goals": 0,
    "assists": 2,
    "points": 2,
    "penaltyMinutes": 2,
    "timeOnIce": "2580:00",
}

BROADCAST_DATA = {
    "id": 2,
    "market": "A",
    "countryCode": "US",
    "network": "ALT",
    "sequenceNumber": 385,
}

TEAM_IN_GAME_DATA = {
    "id": 21,
    "name": {"default": "Colorado Avalanche", "fr": "Avalanche du Colorado"},
    "commonName": {"default": "Avalanche"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
    "abbrev": "COL",
    "score": 4,
    "logo": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
}

PERIOD_DESCRIPTOR_DATA = {
    "number": 3,
    "periodType": "REG",
    "maxRegulationPeriods": 3,
}

GAME_DATA = {
    "id": 2025021096,
    "season": 20252026,
    "gameType": 2,
    "gameDate": "2026-03-20",
    "gameCenterLink": "/gamecenter/col-vs-chi/2026/03/20/2025021096",
    "venue": {"default": "United Center"},
    "startTimeUTC": "2026-03-21T00:30:00Z",
    "easternUTCOffset": "-04:00",
    "venueUTCOffset": "-05:00",
    "tvBroadcasts": [BROADCAST_DATA],
    "gameState": "OFF",
    "gameScheduleState": "OK",
    "awayTeam": TEAM_IN_GAME_DATA,
    "homeTeam": {**TEAM_IN_GAME_DATA, "id": 16, "abbrev": "CHI", "score": 1},
    "ticketsLink": "https://www.ticketmaster.com/event/040062F0F4B538CC",
    "period": 3,
    "periodDescriptor": PERIOD_DESCRIPTOR_DATA,
    "threeMinRecapFr": "/fr/video/col-vs-chi-resume",
}

SCOREBOARD_DATA = {
    "focusedDate": "2026-03-25",
    "focusedDateCount": 10,
    "clubTimeZone": "America/Denver",
    "clubUTCOffset": "-06:00",
    "clubScheduleLink": "/avalanche/schedule",
    "gamesByDate": [
        {"date": "2026-03-20", "games": [GAME_DATA]},
    ],
}


# ==========================================================================
# TEAM SKATER STAT
# ==========================================================================

def test_team_skater_stat_from_dict() -> None:
    s = TeamSkaterStat.from_dict(SKATER_DATA)
    assert s.player_id == 8477492
    assert s.first_name.default == "Nathan"
    assert s.last_name.default == "MacKinnon"
    assert s.position_code == "C"
    assert s.games_played == 70
    assert s.goals == 35
    assert s.assists == 65
    assert s.points == 100
    assert s.plus_minus == 28
    assert s.power_play_goals == 12
    assert s.shorthanded_goals == 1
    assert s.game_winning_goals == 8
    assert s.overtime_goals == 2
    assert s.shots == 220
    assert s.shooting_pctg == 0.159
    assert s.avg_shifts_per_game == 24.3
    assert s.faceoff_win_pctg == 0.524

def test_team_skater_stat_empty() -> None:
    s = TeamSkaterStat.from_dict({})
    assert s.player_id is None
    assert s.first_name.default is None
    assert s.goals is None
    assert s.points is None


# ==========================================================================
# TEAM GOALIE STAT
# ==========================================================================

def test_team_goalie_stat_from_dict() -> None:
    g = TeamGoalieStat.from_dict(GOALIE_DATA)
    assert g.player_id == 8480366
    assert g.first_name.default == "Mackenzie"
    assert g.last_name.default == "Blackwood"
    assert g.games_played == 45
    assert g.games_started == 43
    assert g.wins == 30
    assert g.losses == 10
    assert g.overtime_losses == 5
    assert g.goals_against_average == 2.41
    assert g.save_percentage == 0.916
    assert g.shots_against == 1250
    assert g.saves == 1145
    assert g.goals_against == 105
    assert g.shutouts == 4
    assert g.time_on_ice == "2580:00"

def test_team_goalie_stat_empty() -> None:
    g = TeamGoalieStat.from_dict({})
    assert g.player_id is None
    assert g.wins is None
    assert g.save_percentage is None


# ==========================================================================
# TEAM STATS RESULT
# ==========================================================================

def test_team_stats_result_from_dict() -> None:
    data = {
        "season": "20252026",
        "gameType": 2,
        "skaters": [SKATER_DATA],
        "goalies": [GOALIE_DATA],
    }
    result = TeamStatsResult.from_dict(data)
    assert result.season == "20252026"
    assert result.game_type == 2
    assert len(result.skaters) == 1
    assert len(result.goalies) == 1
    assert result.skaters[0].last_name.default == "MacKinnon"
    assert result.goalies[0].last_name.default == "Blackwood"

def test_team_stats_result_empty_lists() -> None:
    result = TeamStatsResult.from_dict({"season": "20252026", "gameType": 2})
    assert result.season == "20252026"
    assert result.skaters == []
    assert result.goalies == []

def test_team_stats_result_empty() -> None:
    result = TeamStatsResult.from_dict({})
    assert result.season is None
    assert result.game_type is None
    assert result.skaters == []
    assert result.goalies == []


# ==========================================================================
# TEAM SEASON GAME TYPES
# ==========================================================================

def test_team_season_game_types_from_dict() -> None:
    s = TeamSeasonGameTypes.from_dict({"season": 20252026, "gameTypes": [2, 3]})
    assert s.season == 20252026
    assert s.game_types == [2, 3]

def test_team_season_game_types_single() -> None:
    s = TeamSeasonGameTypes.from_dict({"season": 20242025, "gameTypes": [2]})
    assert s.season == 20242025
    assert s.game_types == [2]

def test_team_season_game_types_empty() -> None:
    s = TeamSeasonGameTypes.from_dict({})
    assert s.season is None
    assert s.game_types == []


# ==========================================================================
# SCOREBOARD NESTED TYPES
# ==========================================================================

def test_scoreboard_tv_broadcast_from_dict() -> None:
    b = ScoreboardTvBroadcast.from_dict(BROADCAST_DATA)
    assert b.id == 2
    assert b.market == "A"
    assert b.country_code == "US"
    assert b.network == "ALT"
    assert b.sequence_number == 385

def test_scoreboard_tv_broadcast_empty() -> None:
    b = ScoreboardTvBroadcast.from_dict({})
    assert b.id is None
    assert b.network is None

def test_scoreboard_team_from_dict() -> None:
    t = ScoreboardTeam.from_dict(TEAM_IN_GAME_DATA)
    assert t.id == 21
    assert t.name.default == "Colorado Avalanche"
    assert t.common_name.default == "Avalanche"
    assert t.abbrev == "COL"
    assert t.score == 4
    assert t.record is None

def test_scoreboard_team_future_game() -> None:
    data = {**TEAM_IN_GAME_DATA, "score": None, "record": "47-13-10"}
    t = ScoreboardTeam.from_dict(data)
    assert t.score is None
    assert t.record == "47-13-10"

def test_scoreboard_team_empty() -> None:
    t = ScoreboardTeam.from_dict({})
    assert t.id is None
    assert t.name.default is None
    assert t.abbrev is None

def test_scoreboard_period_descriptor_from_dict() -> None:
    pd = ScoreboardPeriodDescriptor.from_dict(PERIOD_DESCRIPTOR_DATA)
    assert pd.number == 3
    assert pd.period_type == "REG"
    assert pd.max_regulation_periods == 3

def test_scoreboard_period_descriptor_ot() -> None:
    pd = ScoreboardPeriodDescriptor.from_dict({"number": 4, "periodType": "OT", "maxRegulationPeriods": 3})
    assert pd.number == 4
    assert pd.period_type == "OT"


# ==========================================================================
# SCOREBOARD GAME
# ==========================================================================

def test_scoreboard_game_from_dict() -> None:
    game = ScoreboardGame.from_dict(GAME_DATA)
    assert game.id == 2025021096
    assert game.season == 20252026
    assert game.game_type == 2
    assert game.game_date == "2026-03-20"
    assert game.venue.default == "United Center"
    assert game.start_time_utc == "2026-03-21T00:30:00Z"
    assert game.game_state == "OFF"
    assert game.away_team.abbrev == "COL"
    assert game.home_team.abbrev == "CHI"
    assert game.period == 3
    assert game.period_descriptor is not None
    assert game.period_descriptor.period_type == "REG"
    assert game.three_min_recap_fr == "/fr/video/col-vs-chi-resume"
    assert len(game.tv_broadcasts) == 1
    assert game.tv_broadcasts[0].network == "ALT"

def test_scoreboard_game_future_no_period() -> None:
    data = {**GAME_DATA, "gameState": "FUT", "period": None, "periodDescriptor": None}
    game = ScoreboardGame.from_dict(data)
    assert game.game_state == "FUT"
    assert game.period is None
    assert game.period_descriptor is None

def test_scoreboard_game_empty() -> None:
    game = ScoreboardGame.from_dict({})
    assert game.id is None
    assert game.game_state is None
    assert game.period_descriptor is None
    assert game.tv_broadcasts == []


# ==========================================================================
# SCOREBOARD GAMES BY DATE
# ==========================================================================

def test_scoreboard_games_by_date_from_dict() -> None:
    data = {"date": "2026-03-20", "games": [GAME_DATA]}
    gbd = ScoreboardGamesByDate.from_dict(data)
    assert gbd.date == "2026-03-20"
    assert len(gbd.games) == 1
    assert gbd.games[0].id == 2025021096

def test_scoreboard_games_by_date_empty() -> None:
    gbd = ScoreboardGamesByDate.from_dict({})
    assert gbd.date is None
    assert gbd.games == []


# ==========================================================================
# TEAM SCOREBOARD
# ==========================================================================

def test_team_scoreboard_from_dict() -> None:
    sb = TeamScoreboard.from_dict(SCOREBOARD_DATA)
    assert sb.focused_date == "2026-03-25"
    assert sb.focused_date_count == 10
    assert sb.club_time_zone == "America/Denver"
    assert sb.club_utc_offset == "-06:00"
    assert sb.club_schedule_link == "/avalanche/schedule"
    assert len(sb.games_by_date) == 1
    assert sb.games_by_date[0].date == "2026-03-20"
    assert sb.games_by_date[0].games[0].away_team.abbrev == "COL"

def test_team_scoreboard_empty() -> None:
    sb = TeamScoreboard.from_dict({})
    assert sb.focused_date is None
    assert sb.club_time_zone is None
    assert sb.games_by_date == []
