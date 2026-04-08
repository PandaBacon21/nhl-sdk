from nhl_stats.models.players.player.player_stats.reports import (
    SkaterBioReport, SkaterFaceoffPctReport, SkaterFaceoffWinsReport,
    SkaterGoalsForAgainstReport, SkaterPenaltiesReport, SkaterPenaltyKillReport,
    SkaterPenaltyShotsReport, SkaterPowerPlayReport, SkaterPuckPossessionsReport,
    SkaterRealtimeReport, SkaterShotTypeReport, SkaterTimeOnIceReport,
    SkaterPercentagesReport,
    GoalieBioReport, GoalieAdvancedReport, GoalieDaysRestReport,
    GoaliePenaltyShotsReport, GoalieSavesByStrengthReport,
    GoalieShootoutReport, GoalieStartedVsRelievedReport,
)


# ==========================================================================
# SKATER BIO REPORT
# ==========================================================================

def test_skater_bio_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 944,
        "goals": 418,
        "assists": 719,
        "points": 1137,
        "positionCode": "C",
        "shootsCatches": "R",
        "birthCity": "Halifax",
        "birthCountryCode": "CAN",
        "birthDate": "1995-09-01",
        "birthStateProvinceCode": "NS",
        "currentTeamAbbrev": "COL",
        "currentTeamName": "Colorado Avalanche",
        "draftOverall": 1,
        "draftRound": 1,
        "draftYear": 2013,
        "firstSeasonForGameType": 20132014,
        "height": 72,
        "isInHallOfFameYn": "N",
        "nationalityCode": "CAN",
        "weight": 200,
    }
    r = SkaterBioReport.from_dict(data)
    assert r.player_id == 8477492
    assert r.skater_full_name == "Nathan MacKinnon"
    assert r.goals == 418
    assert r.assists == 719
    assert r.draft_overall == 1
    assert r.birth_city == "Halifax"
    assert r.is_in_hall_of_fame_yn == "N"


def test_skater_bio_report_empty() -> None:
    r = SkaterBioReport.from_dict({})
    assert r.player_id is None
    assert r.goals is None
    assert r.draft_year is None


# ==========================================================================
# SKATER FACEOFF PCT REPORT
# ==========================================================================

def test_skater_faceoff_pct_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "positionCode": "C",
        "shootsCatches": "R",
        "teamAbbrevs": "COL",
        "timeOnIcePerGame": 1325.0,
        "faceoffWinPct": 0.5056,
        "totalFaceoffs": 2199,
        "defensiveZoneFaceoffPct": 0.4876,
        "defensiveZoneFaceoffs": 516,
        "evFaceoffPct": 0.5056,
        "evFaceoffs": 1194,
        "neutralZoneFaceoffPct": 0.4777,
        "neutralZoneFaceoffs": 561,
        "offensiveZoneFaceoffPct": 0.5338,
        "offensiveZoneFaceoffs": 444,
        "ppFaceoffPct": 0.5833,
        "ppFaceoffs": 96,
        "shFaceoffPct": None,
        "shFaceoffs": 0,
    }
    r = SkaterFaceoffPctReport.from_dict(data)
    assert r.player_id == 8477492
    assert r.faceoff_win_pct == 0.5056
    assert r.total_faceoffs == 2199
    assert r.ev_faceoffs == 1194
    assert r.pp_faceoffs == 96


def test_skater_faceoff_pct_report_empty() -> None:
    r = SkaterFaceoffPctReport.from_dict({})
    assert r.player_id is None
    assert r.faceoff_win_pct is None


# ==========================================================================
# SKATER FACEOFF WINS REPORT
# ==========================================================================

def test_skater_faceoff_wins_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "teamAbbrevs": "COL",
        "faceoffWinPct": 0.50558,
        "totalFaceoffs": 2199,
        "totalFaceoffWins": 1111,
        "totalFaceoffLosses": 1088,
        "defensiveZoneFaceoffs": 516,
        "defensiveZoneFaceoffWins": 247,
        "defensiveZoneFaceoffLosses": 269,
        "evFaceoffs": 1194,
        "evFaceoffsWon": 589,
        "evFaceoffsLost": 605,
        "neutralZoneFaceoffs": 561,
        "neutralZoneFaceoffWins": 268,
        "neutralZoneFaceoffLosses": 293,
        "offensiveZoneFaceoffs": 444,
        "offensiveZoneFaceoffWins": 254,
        "offensiveZoneFaceoffLosses": 190,
        "ppFaceoffs": 96,
        "ppFaceoffsWon": 56,
        "ppFaceoffsLost": 40,
        "shFaceoffs": 0,
        "shFaceoffsWon": 0,
        "shFaceoffsLost": 0,
    }
    r = SkaterFaceoffWinsReport.from_dict(data)
    assert r.total_faceoffs == 2199
    assert r.total_faceoff_wins == 1111
    assert r.ev_faceoffs_won == 589
    assert r.defensive_zone_faceoff_losses == 269


def test_skater_faceoff_wins_report_empty() -> None:
    r = SkaterFaceoffWinsReport.from_dict({})
    assert r.total_faceoffs is None
    assert r.ev_faceoffs_won is None


# ==========================================================================
# SKATER GOALS FOR AGAINST REPORT
# ==========================================================================

def test_skater_goals_for_against_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "teamAbbrevs": "COL",
        "positionCode": "C",
        "assists": 69,
        "goals": 51,
        "points": 120,
        "evenStrengthGoalDifference": 28,
        "evenStrengthGoalsAgainst": 62,
        "evenStrengthGoalsFor": 90,
        "evenStrengthGoalsForPct": 0.5921,
        "evenStrengthTimeOnIcePerGame": 1025.0,
        "powerPlayGoalFor": 35,
        "powerPlayGoalsAgainst": 0,
        "powerPlayTimeOnIcePerGame": 264.0,
        "shortHandedGoalsAgainst": 2,
        "shortHandedGoalsFor": 0,
        "shortHandedTimeOnIcePerGame": 5.0,
    }
    r = SkaterGoalsForAgainstReport.from_dict(data)
    assert r.goals == 51
    assert r.even_strength_goals_for == 90
    assert r.even_strength_goal_difference == 28
    assert r.power_play_goal_for == 35


def test_skater_goals_for_against_report_empty() -> None:
    r = SkaterGoalsForAgainstReport.from_dict({})
    assert r.goals is None
    assert r.even_strength_goals_for is None


# ==========================================================================
# SKATER PENALTIES REPORT
# ==========================================================================

def test_skater_penalties_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "positionCode": "C",
        "teamAbbrevs": "COL",
        "assists": 69,
        "goals": 51,
        "points": 120,
        "timeOnIcePerGame": 1339.0,
        "gameMisconductPenalties": 0,
        "majorPenalties": 0,
        "matchPenalties": 0,
        "minorPenalties": 16,
        "misconductPenalties": 0,
        "netPenalties": 22,
        "netPenaltiesPer60": 0.75,
        "penalties": 16,
        "penaltiesDrawn": 38,
        "penaltiesDrawnPer60": 1.30,
        "penaltiesTakenPer60": 0.55,
        "penaltyMinutes": 32,
        "penaltyMinutesPerTimeOnIce": 0.019,
        "penaltySecondsPerGame": 23.0,
    }
    r = SkaterPenaltiesReport.from_dict(data)
    assert r.minor_penalties == 16
    assert r.penalties_drawn == 38
    assert r.net_penalties == 22
    assert r.penalty_minutes == 32


def test_skater_penalties_report_empty() -> None:
    r = SkaterPenaltiesReport.from_dict({})
    assert r.minor_penalties is None
    assert r.penalties_drawn is None


# ==========================================================================
# SKATER PENALTY KILL REPORT
# ==========================================================================

def test_skater_penalty_kill_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "positionCode": "C",
        "teamAbbrevs": "COL",
        "ppGoalsAgainstPer60": 8.4,
        "shAssists": 1,
        "shGoals": 2,
        "shGoalsPer60": 0.84,
        "shIndividualSatFor": 24,
        "shIndividualSatForPer60": 10.06,
        "shPoints": 3,
        "shPointsPer60": 1.26,
        "shPrimaryAssists": 1,
        "shPrimaryAssistsPer60": 0.42,
        "shSecondaryAssists": 0,
        "shSecondaryAssistsPer60": 0.0,
        "shShootingPct": 0.14,
        "shShots": 14,
        "shShotsPer60": 5.87,
        "shTimeOnIce": 8589,
        "shTimeOnIcePctPerGame": 0.0188,
        "shTimeOnIcePerGame": 104.7,
    }
    r = SkaterPenaltyKillReport.from_dict(data)
    assert r.sh_goals == 2
    assert r.sh_points == 3
    assert r.sh_time_on_ice == 8589


def test_skater_penalty_kill_report_empty() -> None:
    r = SkaterPenaltyKillReport.from_dict({})
    assert r.sh_goals is None
    assert r.sh_time_on_ice is None


# ==========================================================================
# SKATER PENALTY SHOTS REPORT
# ==========================================================================

def test_skater_penalty_shots_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "seasonId": 20202021,
        "positionCode": "C",
        "shootsCatches": "R",
        "teamAbbrevs": "COL",
        "penaltyShotAttempts": 1,
        "penaltyShotShootingPct": 0.0,
        "penaltyShotsFailed": 1,
        "penaltyShotsGoals": 0,
    }
    r = SkaterPenaltyShotsReport.from_dict(data)
    assert r.penalty_shot_attempts == 1
    assert r.penalty_shots_goals == 0
    assert r.penalty_shots_failed == 1


def test_skater_penalty_shots_report_empty() -> None:
    r = SkaterPenaltyShotsReport.from_dict({})
    assert r.penalty_shot_attempts is None
    assert r.penalty_shots_goals is None


# ==========================================================================
# SKATER POWER PLAY REPORT
# ==========================================================================

def test_skater_powerplay_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "positionCode": "C",
        "teamAbbrevs": "COL",
        "ppAssists": 25,
        "ppGoals": 12,
        "ppGoalsForPer60": 9.12,
        "ppGoalsPer60": 2.15,
        "ppIndividualSatFor": 139,
        "ppIndividualSatForPer60": 24.86,
        "ppPoints": 37,
        "ppPointsPer60": 6.62,
        "ppPrimaryAssists": 12,
        "ppPrimaryAssistsPer60": 2.15,
        "ppSecondaryAssists": 13,
        "ppSecondaryAssistsPer60": 2.33,
        "ppShootingPct": 0.109,
        "ppShots": 110,
        "ppShotsPer60": 19.68,
        "ppTimeOnIce": 20126,
        "ppTimeOnIcePctPerGame": 0.696,
        "ppTimeOnIcePerGame": 245.4,
    }
    r = SkaterPowerPlayReport.from_dict(data)
    assert r.pp_goals == 12
    assert r.pp_points == 37
    assert r.pp_time_on_ice == 20126


def test_skater_powerplay_report_empty() -> None:
    r = SkaterPowerPlayReport.from_dict({})
    assert r.pp_goals is None
    assert r.pp_points is None


# ==========================================================================
# SKATER PUCK POSSESSIONS REPORT
# ==========================================================================

def test_skater_puck_possessions_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "positionCode": "C",
        "shootsCatches": "R",
        "teamAbbrevs": "COL",
        "defensiveZoneStartPct": 0.2356,
        "faceoffPct5v5": 0.452,
        "goalsPct": 0.602,
        "individualSatForPer60": 18.84,
        "individualShotsForPer60": 11.02,
        "neutralZoneStartPct": 0.3043,
        "offensiveZoneStartPct": 0.46,
        "offensiveZoneStartRatio": 0.661,
        "onIceShootingPct": 0.116,
        "satPct": 0.562,
        "timeOnIcePerGame5v5": 1016.0,
        "usatPct": 0.562,
    }
    r = SkaterPuckPossessionsReport.from_dict(data)
    assert r.sat_pct == 0.562
    assert r.faceoff_pct5v5 == 0.452
    assert r.time_on_ice_per_game5v5 == 1016.0


def test_skater_puck_possessions_report_empty() -> None:
    r = SkaterPuckPossessionsReport.from_dict({})
    assert r.sat_pct is None
    assert r.faceoff_pct5v5 is None


# ==========================================================================
# SKATER REALTIME REPORT
# ==========================================================================

def test_skater_realtime_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "positionCode": "C",
        "shootsCatches": "R",
        "teamAbbrevs": "COL",
        "timeOnIcePerGame": 1325.0,
        "blockedShots": 69,
        "blockedShotsPer60": 2.21,
        "emptyNetAssists": 5,
        "emptyNetGoals": 3,
        "emptyNetPoints": 8,
        "firstGoals": 6,
        "giveaways": 82,
        "giveawaysPer60": 2.62,
        "hits": 55,
        "hitsPer60": 1.76,
        "missedShotCrossbar": 2,
        "missedShotFailedBankAttempt": None,
        "missedShotGoalpost": 11,
        "missedShotOverNet": 13,
        "missedShotShort": 2,
        "missedShotWideOfNet": 93,
        "missedShots": 121,
        "otGoals": 2,
        "shotAttemptsBlocked": None,
        "takeaways": 48,
        "takeawaysPer60": 1.58,
        "totalShotAttempts": None,
    }
    r = SkaterRealtimeReport.from_dict(data)
    assert r.blocked_shots == 69
    assert r.hits == 55
    assert r.giveaways == 82
    assert r.takeaways == 48
    assert r.missed_shots == 121


def test_skater_realtime_report_empty() -> None:
    r = SkaterRealtimeReport.from_dict({})
    assert r.blocked_shots is None
    assert r.hits is None


# ==========================================================================
# SKATER SHOT TYPE REPORT
# ==========================================================================

def test_skater_shot_type_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20182019,
        "teamAbbrevs": "COL",
        "goals": 41,
        "shootingPct": 0.112,
        "goalsBackhand": 2,
        "goalsBat": None,
        "goalsBetweenLegs": None,
        "goalsCradle": None,
        "goalsDeflected": 0,
        "goalsPoke": None,
        "goalsSlap": 6,
        "goalsSnap": 6,
        "goalsTipIn": 2,
        "goalsWrapAround": 0,
        "goalsWrist": 25,
        "shootingPctBackhand": 0.05,
        "shootingPctBat": None,
        "shootingPctBetweenLegs": None,
        "shootingPctCradle": None,
        "shootingPctDeflected": 0.0,
        "shootingPctPoke": None,
        "shootingPctSlap": 0.158,
        "shootingPctSnap": 0.182,
        "shootingPctTipIn": 0.125,
        "shootingPctWrapAround": 0.0,
        "shootingPctWrist": 0.108,
        "shotsOnNetBackhand": 40,
        "shotsOnNetBat": None,
        "shotsOnNetBetweenLegs": None,
        "shotsOnNetCradle": None,
        "shotsOnNetDeflected": 2,
        "shotsOnNetPoke": None,
        "shotsOnNetSlap": 38,
        "shotsOnNetSnap": 33,
        "shotsOnNetTipIn": 16,
        "shotsOnNetWrapAround": 4,
        "shotsOnNetWrist": 232,
    }
    r = SkaterShotTypeReport.from_dict(data)
    assert r.goals == 41
    assert r.goals_wrist == 25
    assert r.goals_slap == 6
    assert r.shots_on_net_wrist == 232
    assert r.shooting_pct_snap == 0.182


def test_skater_shot_type_report_empty() -> None:
    r = SkaterShotTypeReport.from_dict({})
    assert r.goals is None
    assert r.goals_wrist is None


# ==========================================================================
# SKATER TIME ON ICE REPORT
# ==========================================================================

def test_skater_toi_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20162017,
        "positionCode": "C",
        "shootsCatches": "R",
        "teamAbbrevs": "COL",
        "evTimeOnIce": 75863,
        "evTimeOnIcePerGame": 925.16,
        "otTimeOnIce": 1058,
        "otTimeOnIcePerOtGame": 88.17,
        "ppTimeOnIce": 13672,
        "ppTimeOnIcePerGame": 166.73,
        "shTimeOnIce": 8589,
        "shTimeOnIcePerGame": 104.74,
        "shifts": 2097,
        "shiftsPerGame": 25.57,
        "timeOnIce": 98124,
        "timeOnIcePerGame": 1196.63,
        "timeOnIcePerShift": 46.79,
    }
    r = SkaterTimeOnIceReport.from_dict(data)
    assert r.time_on_ice == 98124
    assert r.ev_time_on_ice == 75863
    assert r.shifts == 2097
    assert r.shifts_per_game == 25.57


def test_skater_toi_report_empty() -> None:
    r = SkaterTimeOnIceReport.from_dict({})
    assert r.time_on_ice is None
    assert r.shifts is None


# ==========================================================================
# SKATER PERCENTAGES REPORT
# ==========================================================================

def test_skater_percentages_report_from_dict() -> None:
    data = {
        "playerId": 8477492,
        "skaterFullName": "Nathan MacKinnon",
        "lastName": "MacKinnon",
        "gamesPlayed": 82,
        "seasonId": 20232024,
        "shootsCatches": "R",
        "teamAbbrevs": "COL",
        "satPercentage": 0.582,
        "satPercentageAhead": 0.539,
        "satPercentageBehind": 0.6,
        "satPercentageClose": 0.597,
        "satPercentageTied": 0.604,
        "satRelative": 0.07,
        "usatPercentage": 0.582,
        "usatPercentageAhead": 0.54,
        "usatPercentageBehind": 0.604,
        "usatPercentageTied": 0.6,
        "usatPrecentageClose": 0.595,
        "usatRelative": 0.07,
        "shootingPct5v5": 0.087,
        "skaterSavePct5v5": 0.911,
        "skaterShootingPlusSavePct5v5": 0.998,
        "timeOnIcePerGame5v5": 1025.0,
        "zoneStartPct5v5": 0.645,
    }
    r = SkaterPercentagesReport.from_dict(data)
    assert r.sat_percentage == 0.582
    assert r.usat_percentage == 0.582
    assert r.shooting_pct5v5 == 0.087
    assert r.zone_start_pct5v5 == 0.645
    assert r.usat_precentage_close == 0.595  # API typo preserved


def test_skater_percentages_report_empty() -> None:
    r = SkaterPercentagesReport.from_dict({})
    assert r.sat_percentage is None
    assert r.zone_start_pct5v5 is None


# ==========================================================================
# GOALIE BIO REPORT
# ==========================================================================

def test_goalie_bio_report_from_dict() -> None:
    data = {
        "playerId": 8476883,
        "goalieFullName": "Andrei Vasilevskiy",
        "lastName": "Vasilevskiy",
        "gamesPlayed": 594,
        "shootsCatches": "L",
        "birthCity": "Tyumen",
        "birthCountryCode": "RUS",
        "birthDate": "1994-07-25",
        "birthStateProvinceCode": None,
        "currentTeamAbbrev": "TBL",
        "draftOverall": 19,
        "draftRound": 1,
        "draftYear": 2012,
        "firstSeasonForGameType": 20142015,
        "height": 76,
        "isInHallOfFameYn": "N",
        "losses": 176,
        "nationalityCode": "RUS",
        "otLosses": 39,
        "shutouts": 42,
        "ties": None,
        "weight": 223,
        "wins": 368,
    }
    r = GoalieBioReport.from_dict(data)
    assert r.player_id == 8476883
    assert r.goalie_full_name == "Andrei Vasilevskiy"
    assert r.wins == 368
    assert r.shutouts == 42
    assert r.birth_city == "Tyumen"


def test_goalie_bio_report_empty() -> None:
    r = GoalieBioReport.from_dict({})
    assert r.player_id is None
    assert r.wins is None


# ==========================================================================
# GOALIE ADVANCED REPORT
# ==========================================================================

def test_goalie_advanced_report_from_dict() -> None:
    data = {
        "playerId": 8476883,
        "goalieFullName": "Andrei Vasilevskiy",
        "lastName": "Vasilevskiy",
        "gamesPlayed": 65,
        "gamesStarted": 64,
        "seasonId": 20172018,
        "teamAbbrevs": "TBL",
        "shootsCatches": "L",
        "completeGamePct": 0.96875,
        "completeGames": 62,
        "goalsAgainst": 167,
        "goalsAgainstAverage": 2.619,
        "goalsFor": 224,
        "goalsForAverage": 3.514,
        "incompleteGames": 2,
        "qualityStart": 37,
        "qualityStartsPct": 0.578,
        "regulationLosses": 19,
        "regulationWins": 39,
        "savePct": 0.9195,
        "shotsAgainstPer60": 32.55,
        "timeOnIce": 229511,
    }
    r = GoalieAdvancedReport.from_dict(data)
    assert r.complete_games == 62
    assert r.quality_start == 37
    assert r.regulation_wins == 39
    assert r.save_pct == 0.9195


def test_goalie_advanced_report_empty() -> None:
    r = GoalieAdvancedReport.from_dict({})
    assert r.complete_games is None
    assert r.quality_start is None


# ==========================================================================
# GOALIE DAYS REST REPORT
# ==========================================================================

def test_goalie_days_rest_report_from_dict() -> None:
    data = {
        "playerId": 8476883,
        "goalieFullName": "Andrei Vasilevskiy",
        "lastName": "Vasilevskiy",
        "gamesPlayed": 65,
        "gamesStarted": 64,
        "seasonId": 20172018,
        "teamAbbrevs": "TBL",
        "shootsCatches": "L",
        "ties": None,
        "losses": 17,
        "otLosses": 3,
        "wins": 44,
        "savePct": 0.9195,
        "gamesPlayedDaysRest0": 3,
        "gamesPlayedDaysRest1": 29,
        "gamesPlayedDaysRest2": 17,
        "gamesPlayedDaysRest3": 9,
        "gamesPlayedDaysRest4Plus": 7,
        "savePctDaysRest0": 0.909,
        "savePctDaysRest1": 0.920,
        "savePctDaysRest2": 0.927,
        "savePctDaysRest3": 0.926,
        "savePctDaysRest4Plus": 0.895,
    }
    r = GoalieDaysRestReport.from_dict(data)
    assert r.games_played_days_rest1 == 29
    assert r.save_pct_days_rest0 == 0.909
    assert r.save_pct_days_rest4_plus == 0.895
    assert r.wins == 44


def test_goalie_days_rest_report_empty() -> None:
    r = GoalieDaysRestReport.from_dict({})
    assert r.games_played_days_rest1 is None
    assert r.save_pct_days_rest0 is None


# ==========================================================================
# GOALIE PENALTY SHOTS REPORT
# ==========================================================================

def test_goalie_penalty_shots_report_from_dict() -> None:
    data = {
        "playerId": 8476883,
        "goalieFullName": "Andrei Vasilevskiy",
        "lastName": "Vasilevskiy",
        "gamesPlayed": 2,
        "seasonId": 20172018,
        "teamAbbrevs": "TBL",
        "shootsCatches": "L",
        "goalsAgainst": 5,
        "savePct": 0.918,
        "saves": 56,
        "shotsAgainst": 61,
        "penaltyShotSavePct": 0.5,
        "penaltyShotsAgainst": 2,
        "penaltyShotsGoalsAgainst": 1,
        "penaltyShotsSaves": 1,
    }
    r = GoaliePenaltyShotsReport.from_dict(data)
    assert r.penalty_shots_against == 2
    assert r.penalty_shot_save_pct == 0.5
    assert r.penalty_shots_saves == 1


def test_goalie_penalty_shots_report_empty() -> None:
    r = GoaliePenaltyShotsReport.from_dict({})
    assert r.penalty_shots_against is None
    assert r.penalty_shot_save_pct is None


# ==========================================================================
# GOALIE SAVES BY STRENGTH REPORT
# ==========================================================================

def test_goalie_saves_by_strength_report_from_dict() -> None:
    data = {
        "playerId": 8476883,
        "goalieFullName": "Andrei Vasilevskiy",
        "lastName": "Vasilevskiy",
        "gamesPlayed": 50,
        "gamesStarted": 47,
        "seasonId": 20162017,
        "teamAbbrevs": "TBL",
        "shootsCatches": "L",
        "ties": None,
        "goalsAgainst": 123,
        "losses": 17,
        "otLosses": 7,
        "savePct": 0.9169,
        "saves": 1357,
        "shotsAgainst": 1480,
        "wins": 23,
        "evGoalsAgainst": 94,
        "evSavePct": 0.9216,
        "evSaves": 1105,
        "evShotsAgainst": 1199,
        "ppGoalsAgainst": 26,
        "ppSavePct": 0.8947,
        "ppSaves": 221,
        "ppShotsAgainst": 247,
        "shGoalsAgainst": 3,
        "shSavePct": 0.9118,
        "shSaves": 31,
        "shShotsAgainst": 34,
    }
    r = GoalieSavesByStrengthReport.from_dict(data)
    assert r.ev_saves == 1105
    assert r.ev_save_pct == 0.9216
    assert r.pp_goals_against == 26
    assert r.sh_saves == 31


def test_goalie_saves_by_strength_report_empty() -> None:
    r = GoalieSavesByStrengthReport.from_dict({})
    assert r.ev_saves is None
    assert r.pp_goals_against is None


# ==========================================================================
# GOALIE SHOOTOUT REPORT
# ==========================================================================

def test_goalie_shootout_report_from_dict() -> None:
    data = {
        "playerId": 8476883,
        "goalieFullName": "Andrei Vasilevskiy",
        "lastName": "Vasilevskiy",
        "gamesPlayed": 3,
        "seasonId": 20212022,
        "shootsCatches": "L",
        "teamAbbrevs": "TBL",
        "careerShootoutGamesPlayed": 36,
        "careerShootoutGoalsAllowed": 31,
        "careerShootoutLosses": 9,
        "careerShootoutSavePct": 0.765,
        "careerShootoutSaves": 101,
        "careerShootoutShotsAgainst": 132,
        "careerShootoutWins": 27,
        "shootoutGoalsAgainst": 7,
        "shootoutLosses": 2,
        "shootoutSavePct": 0.533,
        "shootoutSaves": 8,
        "shootoutShotsAgainst": 15,
        "shootoutWins": 1,
    }
    r = GoalieShootoutReport.from_dict(data)
    assert r.career_shootout_wins == 27
    assert r.shootout_save_pct == 0.533
    assert r.shootout_shots_against == 15


def test_goalie_shootout_report_empty() -> None:
    r = GoalieShootoutReport.from_dict({})
    assert r.career_shootout_wins is None
    assert r.shootout_save_pct is None


# ==========================================================================
# GOALIE STARTED VS RELIEVED REPORT
# ==========================================================================

def test_goalie_started_vs_relieved_report_from_dict() -> None:
    data = {
        "playerId": 8476883,
        "goalieFullName": "Andrei Vasilevskiy",
        "lastName": "Vasilevskiy",
        "gamesPlayed": 53,
        "seasonId": 20182019,
        "teamAbbrevs": "TBL",
        "shootsCatches": "L",
        "ties": None,
        "gamesRelieved": 0,
        "gamesStarted": 53,
        "losses": 10,
        "otLosses": 4,
        "savePct": 0.9253,
        "wins": 39,
        "gamesRelievedGoalsAgainst": 0,
        "gamesRelievedLosses": 0,
        "gamesRelievedOtLosses": 0,
        "gamesRelievedSavePct": None,
        "gamesRelievedSaves": 0,
        "gamesRelievedShotsAgainst": 0,
        "gamesRelievedTies": None,
        "gamesRelievedWins": 0,
        "gamesStartedGoalsAgainst": 128,
        "gamesStartedLosses": 10,
        "gamesStartedOtLosses": 4,
        "gamesStartedSavePct": 0.9253,
        "gamesStartedSaves": 1585,
        "gamesStartedShotsAgainst": 1713,
        "gamesStartedTies": None,
        "gamesStartedWins": 39,
    }
    r = GoalieStartedVsRelievedReport.from_dict(data)
    assert r.games_started == 53
    assert r.games_relieved == 0
    assert r.games_started_wins == 39
    assert r.games_started_save_pct == 0.9253
    assert r.games_relieved_save_pct is None


def test_goalie_started_vs_relieved_report_empty() -> None:
    r = GoalieStartedVsRelievedReport.from_dict({})
    assert r.games_started is None
    assert r.games_started_wins is None
