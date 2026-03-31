"""
Tests for game boxscore models:
  BoxscoreSkater, BoxscoreGoalie, BoxscoreTeam, PlayerByGameStats, GameBoxscoreResult
"""
from src.models.games.boxscore.boxscore_result import (
    BoxscoreSkater,
    BoxscoreGoalie,
    BoxscoreTeam,
    PlayerByGameStats,
    GameBoxscoreResult,
)


SKATER_DATA = {
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

GOALIE_DATA = {
    "playerId": 8475809,
    "sweaterNumber": 41,
    "name": {"default": "S. Wedgewood"},
    "position": "G",
    "evenStrengthShotsAgainst": "25/26",
    "powerPlayShotsAgainst": "3/3",
    "shorthandedShotsAgainst": "1/2",
    "saveShotsAgainst": "29/31",
    "savePctg": 0.935484,
    "evenStrengthGoalsAgainst": 1,
    "powerPlayGoalsAgainst": 0,
    "shorthandedGoalsAgainst": 1,
    "pim": 0,
    "goalsAgainst": 2,
    "toi": "60:00",
    "starter": True,
    "decision": "W",
    "shotsAgainst": 31,
    "saves": 29,
}

BACKUP_GOALIE_DATA = {
    "playerId": 8481529,
    "sweaterNumber": 50,
    "name": {"default": "T. Miner"},
    "position": "G",
    "evenStrengthShotsAgainst": "0/0",
    "powerPlayShotsAgainst": "0/0",
    "shorthandedShotsAgainst": "0/0",
    "saveShotsAgainst": "0/0",
    "evenStrengthGoalsAgainst": 0,
    "powerPlayGoalsAgainst": 0,
    "shorthandedGoalsAgainst": 0,
    "pim": 0,
    "goalsAgainst": 0,
    "toi": "00:00",
    "starter": False,
    "shotsAgainst": 0,
    "saves": 0,
}

TEAM_DATA = {
    "forwards": [SKATER_DATA],
    "defense": [
        {
            "playerId": 8480069,
            "sweaterNumber": 8,
            "name": {"default": "C. Makar"},
            "position": "D",
            "goals": 1,
            "assists": 2,
            "points": 3,
            "plusMinus": 0,
            "pim": 0,
            "hits": 1,
            "powerPlayGoals": 0,
            "sog": 1,
            "faceoffWinningPctg": 0.0,
            "toi": "19:50",
            "blockedShots": 1,
            "shifts": 22,
            "giveaways": 1,
            "takeaways": 0,
        }
    ],
    "goalies": [GOALIE_DATA, BACKUP_GOALIE_DATA],
}

BOXSCORE_DATA = {
    "id": 2025020691,
    "season": 20252026,
    "gameType": 2,
    "limitedScoring": False,
    "gameDate": "2026-01-08",
    "venue": {"default": "Ball Arena"},
    "venueLocation": {"default": "Denver"},
    "startTimeUTC": "2026-01-09T02:00:00Z",
    "easternUTCOffset": "-05:00",
    "venueUTCOffset": "-07:00",
    "tvBroadcasts": [{"id": 294, "market": "A", "countryCode": "CA", "network": "TSN5", "sequenceNumber": 135}],
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
        "awayTeam": TEAM_DATA,
        "homeTeam": TEAM_DATA,
    },
    "gameOutcome": {"lastPeriodType": "REG"},
}


# ==========================================================================
# BoxscoreSkater
# ==========================================================================

def test_skater_fields() -> None:
    s = BoxscoreSkater.from_dict(SKATER_DATA)
    assert s.player_id == 8477492
    assert s.sweater_number == 29
    assert s.name.default == "N. MacKinnon"
    assert s.position == "C"
    assert s.goals == 1
    assert s.assists == 3
    assert s.points == 4
    assert s.plus_minus == 0
    assert s.pim == 0
    assert s.hits == 0
    assert s.power_play_goals == 0
    assert s.sog == 5
    assert s.faceoff_winning_pctg == 0.615385
    assert s.toi == "17:14"
    assert s.blocked_shots == 1
    assert s.shifts == 19
    assert s.giveaways == 1
    assert s.takeaways == 0


def test_skater_empty() -> None:
    s = BoxscoreSkater.from_dict({})
    assert s.player_id is None
    assert s.goals is None
    assert s.toi is None


# ==========================================================================
# BoxscoreGoalie
# ==========================================================================

def test_goalie_starter_fields() -> None:
    g = BoxscoreGoalie.from_dict(GOALIE_DATA)
    assert g.player_id == 8475809
    assert g.sweater_number == 41
    assert g.name.default == "S. Wedgewood"
    assert g.position == "G"
    assert g.even_strength_shots_against == "25/26"
    assert g.power_play_shots_against == "3/3"
    assert g.shorthanded_shots_against == "1/2"
    assert g.save_shots_against == "29/31"
    assert g.save_pctg == 0.935484
    assert g.even_strength_goals_against == 1
    assert g.power_play_goals_against == 0
    assert g.shorthanded_goals_against == 1
    assert g.goals_against == 2
    assert g.toi == "60:00"
    assert g.starter is True
    assert g.decision == "W"
    assert g.shots_against == 31
    assert g.saves == 29


def test_goalie_backup_no_decision() -> None:
    g = BoxscoreGoalie.from_dict(BACKUP_GOALIE_DATA)
    assert g.starter is False
    assert g.decision is None
    assert g.saves == 0
    assert g.shots_against == 0


def test_goalie_empty() -> None:
    g = BoxscoreGoalie.from_dict({})
    assert g.player_id is None
    assert g.starter is None
    assert g.decision is None


# ==========================================================================
# BoxscoreTeam
# ==========================================================================

def test_boxscore_team_fields() -> None:
    t = BoxscoreTeam.from_dict(TEAM_DATA)
    assert len(t.forwards) == 1
    assert len(t.defense) == 1
    assert len(t.goalies) == 2
    assert t.forwards[0].name.default == "N. MacKinnon"
    assert t.defense[0].name.default == "C. Makar"
    assert t.goalies[0].decision == "W"
    assert t.goalies[1].decision is None


def test_boxscore_team_empty() -> None:
    t = BoxscoreTeam.from_dict({})
    assert t.forwards == []
    assert t.defense == []
    assert t.goalies == []


# ==========================================================================
# PlayerByGameStats
# ==========================================================================

def test_player_by_game_stats_fields() -> None:
    p = PlayerByGameStats.from_dict({"awayTeam": TEAM_DATA, "homeTeam": TEAM_DATA})
    assert len(p.away_team.forwards) == 1
    assert len(p.home_team.goalies) == 2
    assert p.away_team.forwards[0].player_id == 8477492


def test_player_by_game_stats_empty() -> None:
    p = PlayerByGameStats.from_dict({})
    assert p.away_team.forwards == []
    assert p.home_team.goalies == []


# ==========================================================================
# GameBoxscoreResult
# ==========================================================================

def test_boxscore_result_fields() -> None:
    r = GameBoxscoreResult.from_dict(BOXSCORE_DATA)
    assert r.id == 2025020691
    assert r.season == 20252026
    assert r.game_type == 2
    assert r.limited_scoring is False
    assert r.game_date == "2026-01-08"
    assert r.venue.default == "Ball Arena"
    assert r.venue_location.default == "Denver"
    assert r.game_state == "OFF"
    assert r.reg_periods == 3


def test_boxscore_result_teams() -> None:
    r = GameBoxscoreResult.from_dict(BOXSCORE_DATA)
    assert r.away_team.abbrev == "OTT"
    assert r.away_team.score == 2
    assert r.home_team.abbrev == "COL"
    assert r.home_team.score == 8


def test_boxscore_result_clock() -> None:
    r = GameBoxscoreResult.from_dict(BOXSCORE_DATA)
    assert r.clock.time_remaining == "00:00"
    assert r.clock.running is False


def test_boxscore_result_game_outcome() -> None:
    r = GameBoxscoreResult.from_dict(BOXSCORE_DATA)
    assert r.game_outcome.last_period_type == "REG"


def test_boxscore_result_player_stats() -> None:
    r = GameBoxscoreResult.from_dict(BOXSCORE_DATA)
    assert r.player_by_game_stats is not None
    assert len(r.player_by_game_stats.home_team.forwards) == 1
    assert r.player_by_game_stats.home_team.forwards[0].points == 4
    assert r.player_by_game_stats.home_team.goalies[0].starter is True


def test_boxscore_result_no_player_stats() -> None:
    data = {k: v for k, v in BOXSCORE_DATA.items() if k != "playerByGameStats"}
    r = GameBoxscoreResult.from_dict(data)
    assert r.player_by_game_stats is None


def test_boxscore_result_empty() -> None:
    r = GameBoxscoreResult.from_dict({})
    assert r.id is None
    assert r.player_by_game_stats is None
    assert r.game_outcome is None
