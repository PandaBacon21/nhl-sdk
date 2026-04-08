from nhl_stats.models.players.player.achievements.player_milestone import PlayerMilestone
from nhl_stats.models.players.player.player_stats.reports.skater_summary_report import SkaterSummaryReport
from nhl_stats.models.players.player.player_stats.reports.goalie_summary_report import GoalieSummaryReport


# ==========================================================================
# PlayerMilestone
# ==========================================================================

MILESTONE_ROW = {
    "id": 101,
    "assists": 789,
    "currentTeamId": 21,
    "gameTypeId": 2,
    "gamesPlayed": 1040,
    "goals": 473,
    "milestone": "Goals",
    "milestoneAmount": 500,
    "playerFullName": "Nathan MacKinnon",
    "playerId": 8477492,
    "points": 1262,
    "teamAbbrev": "COL",
    "teamCommonName": "Avalanche",
    "teamFullName": "Colorado Avalanche",
    "teamPlaceName": "Colorado",
}


def test_player_milestone_from_dict() -> None:
    m = PlayerMilestone.from_dict(MILESTONE_ROW)
    assert m.id == 101
    assert m.assists == 789
    assert m.current_team_id == 21
    assert m.game_type_id == 2
    assert m.games_played == 1040
    assert m.goals == 473
    assert m.milestone == "Goals"
    assert m.milestone_amount == 500
    assert m.player_full_name == "Nathan MacKinnon"
    assert m.player_id == 8477492
    assert m.points == 1262
    assert m.team_abbrev == "COL"
    assert m.team_common_name == "Avalanche"
    assert m.team_full_name == "Colorado Avalanche"
    assert m.team_place_name == "Colorado"


def test_player_milestone_empty() -> None:
    m = PlayerMilestone.from_dict({})
    assert m.id is None
    assert m.goals is None
    assert m.milestone is None
    assert m.player_id is None
    assert m.team_abbrev is None


# ==========================================================================
# SkaterSummaryReport
# ==========================================================================

SKATER_SUMMARY_ROW = {
    "playerId": 8477492,
    "seasonId": 20232024,
    "gameTypeId": 2,
    "skaterFullName": "Nathan MacKinnon",
    "teamAbbrevs": "COL",
    "positionCode": "C",
    "gamesPlayed": 82,
    "goals": 51,
    "assists": 89,
    "points": 140,
    "plusMinus": 37,
    "penaltyMinutes": 44,
    "shots": 300,
    "shootingPctg": 17.0,
    "evGoals": 35,
    "evPoints": 100,
    "ppGoals": 14,
    "ppPoints": 36,
    "shGoals": 2,
    "shPoints": 4,
    "otGoals": 3,
    "gameWinningGoals": 9,
    "faceoffWinPctg": 56.5,
    "timeOnIcePerGame": "22:05",
}


def test_skater_summary_report_from_dict() -> None:
    r = SkaterSummaryReport.from_dict(SKATER_SUMMARY_ROW)
    assert r.player_id == 8477492
    assert r.season_id == 20232024
    assert r.game_type_id == 2
    assert r.skater_full_name == "Nathan MacKinnon"
    assert r.team_abbrevs == "COL"
    assert r.position_code == "C"
    assert r.games_played == 82
    assert r.goals == 51
    assert r.assists == 89
    assert r.points == 140
    assert r.plus_minus == 37
    assert r.penalty_minutes == 44
    assert r.shots == 300
    assert r.shooting_pctg == 17.0
    assert r.ev_goals == 35
    assert r.ev_points == 100
    assert r.pp_goals == 14
    assert r.pp_points == 36
    assert r.sh_goals == 2
    assert r.sh_points == 4
    assert r.ot_goals == 3
    assert r.game_winning_goals == 9
    assert r.faceoff_win_pctg == 56.5
    assert r.time_on_ice_per_game == "22:05"


def test_skater_summary_report_empty() -> None:
    r = SkaterSummaryReport.from_dict({})
    assert r.player_id is None
    assert r.goals is None
    assert r.pp_goals is None
    assert r.faceoff_win_pctg is None
    assert r.time_on_ice_per_game is None


# ==========================================================================
# GoalieSummaryReport
# ==========================================================================

GOALIE_SUMMARY_ROW = {
    "playerId": 8476883,
    "seasonId": 20232024,
    "gameTypeId": 2,
    "goalieFullName": "Connor Hellebuyck",
    "teamAbbrevs": "WPG",
    "gamesPlayed": 60,
    "gamesStarted": 59,
    "wins": 37,
    "losses": 19,
    "otLosses": 4,
    "shotsAgainst": 1700,
    "saves": 1573,
    "goalsAgainst": 127,
    "goalsAgainstAverage": 2.10,
    "savePctg": 0.925,
    "shutouts": 6,
    "timeOnIce": "3540:00",
    "goals": 0,
    "assists": 2,
    "penaltyMinutes": 4,
}


def test_goalie_summary_report_from_dict() -> None:
    r = GoalieSummaryReport.from_dict(GOALIE_SUMMARY_ROW)
    assert r.player_id == 8476883
    assert r.season_id == 20232024
    assert r.game_type_id == 2
    assert r.goalie_full_name == "Connor Hellebuyck"
    assert r.team_abbrevs == "WPG"
    assert r.games_played == 60
    assert r.games_started == 59
    assert r.wins == 37
    assert r.losses == 19
    assert r.ot_losses == 4
    assert r.shots_against == 1700
    assert r.saves == 1573
    assert r.goals_against == 127
    assert r.goals_against_avg == 2.10
    assert r.save_pctg == 0.925
    assert r.shutouts == 6
    assert r.time_on_ice == "3540:00"
    assert r.goals == 0
    assert r.assists == 2
    assert r.penalty_minutes == 4


def test_goalie_summary_report_empty() -> None:
    r = GoalieSummaryReport.from_dict({})
    assert r.player_id is None
    assert r.wins is None
    assert r.save_pctg is None
    assert r.goals_against_avg is None
    assert r.time_on_ice is None
