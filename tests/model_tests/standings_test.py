"""
Tests for the NHL standings models:
  StandingsTeam, SplitRecord, StandingsRecord, StandingsSequences,
  StandingEntry, StandingsResult
"""
from src.models.teams.standings.standing_entry import (
    StandingsTeam,
    SplitRecord,
    StandingsRecord,
    StandingsSequences,
    StandingEntry,
)
from src.models.teams.standings.standings_result import StandingsResult


TEAM_DATA = {
    "teamName": {"default": "Colorado Avalanche", "fr": "Avalanche du Colorado"},
    "teamCommonName": {"default": "Avalanche"},
    "teamAbbrev": {"default": "COL"},
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
    "placeName": {"default": "Colorado"},
}

RECORD_DATA = {
    "gamesPlayed": 70,
    "wins": 47,
    "losses": 13,
    "otLosses": 10,
    "points": 104,
    "pointPctg": 0.743,
    "regulationWins": 38,
    "regulationWinPctg": 0.543,
    "regulationPlusOtWins": 44,
    "regulationPlusOtWinPctg": 0.629,
    "winPctg": 0.671,
    "ties": None,
    "shootoutWins": 3,
    "shootoutLosses": 2,
    "goalFor": 242,
    "goalAgainst": 178,
    "goalDifferential": 64,
    "goalDifferentialPctg": 0.576,
    "goalsForPctg": 0.576,
}

HOME_DATA = {
    "homeGamesPlayed": 35,
    "homeWins": 25,
    "homeLosses": 7,
    "homeOtLosses": 3,
    "homePoints": 53,
    "homeRegulationWins": 20,
    "homeRegulationPlusOtWins": 23,
    "homeGoalsFor": 125,
    "homeGoalsAgainst": 88,
    "homeGoalDifferential": 37,
    "homeTies": None,
}

ROAD_DATA = {
    "roadGamesPlayed": 35,
    "roadWins": 22,
    "roadLosses": 6,
    "roadOtLosses": 7,
    "roadPoints": 51,
    "roadRegulationWins": 18,
    "roadRegulationPlusOtWins": 21,
    "roadGoalsFor": 117,
    "roadGoalsAgainst": 90,
    "roadGoalDifferential": 27,
    "roadTies": None,
}

L10_DATA = {
    "l10GamesPlayed": 10,
    "l10Wins": 7,
    "l10Losses": 1,
    "l10OtLosses": 2,
    "l10Points": 16,
    "l10RegulationWins": 6,
    "l10RegulationPlusOtWins": 7,
    "l10GoalsFor": 38,
    "l10GoalsAgainst": 24,
    "l10GoalDifferential": 14,
    "l10Ties": None,
}

SEQUENCE_DATA = {
    "leagueSequence": 1,
    "leagueHomeSequence": 2,
    "leagueRoadSequence": 1,
    "leagueL10Sequence": 3,
    "conferenceSequence": 1,
    "conferenceHomeSequence": 1,
    "conferenceRoadSequence": 1,
    "conferenceL10Sequence": 2,
    "divisionSequence": 1,
    "divisionHomeSequence": 1,
    "divisionRoadSequence": 1,
    "divisionL10Sequence": 1,
    "wildcardSequence": None,
    "waiversSequence": None,
}

ENTRY_DATA = {
    **TEAM_DATA,
    **RECORD_DATA,
    **HOME_DATA,
    **ROAD_DATA,
    **L10_DATA,
    **SEQUENCE_DATA,
    "seasonId": 20252026,
    "date": "2026-03-26",
    "gameTypeId": 2,
    "clinchIndicator": "x",
    "conferenceAbbrev": "W",
    "conferenceName": "Western",
    "divisionAbbrev": "C",
    "divisionName": "Central",
    "streakCode": "W",
    "streakCount": 3,
}


# ==========================================================================
# STANDINGS TEAM
# ==========================================================================

def test_standings_team_from_dict() -> None:
    team = StandingsTeam.from_dict(TEAM_DATA)
    assert team.name.default == "Colorado Avalanche"
    assert team.common_name.default == "Avalanche"
    assert team.abbrev == "COL"
    assert team.logo == "https://assets.nhle.com/logos/nhl/svg/COL_light.svg"
    assert team.place_name.default == "Colorado"

def test_standings_team_empty() -> None:
    team = StandingsTeam.from_dict({})
    assert team.name.default is None
    assert team.common_name.default is None
    assert team.abbrev is None
    assert team.logo is None
    assert team.place_name.default is None


# ==========================================================================
# SPLIT RECORD
# ==========================================================================

def test_split_record_home() -> None:
    rec = SplitRecord.home(HOME_DATA)
    assert rec.games_played == 35
    assert rec.wins == 25
    assert rec.losses == 7
    assert rec.ot_losses == 3
    assert rec.points == 53
    assert rec.goals_for == 125
    assert rec.goals_against == 88
    assert rec.goal_differential == 37

def test_split_record_road() -> None:
    rec = SplitRecord.road(ROAD_DATA)
    assert rec.games_played == 35
    assert rec.wins == 22
    assert rec.losses == 6
    assert rec.ot_losses == 7
    assert rec.goals_for == 117

def test_split_record_l10() -> None:
    rec = SplitRecord.l10(L10_DATA)
    assert rec.games_played == 10
    assert rec.wins == 7
    assert rec.losses == 1
    assert rec.ot_losses == 2
    assert rec.points == 16

def test_split_record_empty() -> None:
    rec = SplitRecord.home({})
    assert rec.games_played is None
    assert rec.wins is None
    assert rec.losses is None


# ==========================================================================
# STANDINGS RECORD
# ==========================================================================

def test_standings_record_from_dict() -> None:
    rec = StandingsRecord.from_dict(RECORD_DATA)
    assert rec.games_played == 70
    assert rec.wins == 47
    assert rec.losses == 13
    assert rec.ot_losses == 10
    assert rec.points == 104
    assert rec.point_pctg == 0.743
    assert rec.regulation_wins == 38
    assert rec.shootout_wins == 3
    assert rec.shootout_losses == 2
    assert rec.goals_for == 242
    assert rec.goals_against == 178
    assert rec.goal_differential == 64

def test_standings_record_empty() -> None:
    rec = StandingsRecord.from_dict({})
    assert rec.games_played is None
    assert rec.wins is None
    assert rec.points is None


# ==========================================================================
# STANDINGS SEQUENCES
# ==========================================================================

def test_standings_sequences_from_dict() -> None:
    seq = StandingsSequences.from_dict(SEQUENCE_DATA)
    assert seq.league == 1
    assert seq.league_home == 2
    assert seq.league_road == 1
    assert seq.conference == 1
    assert seq.division == 1
    assert seq.wildcard is None
    assert seq.waivers is None

def test_standings_sequences_empty() -> None:
    seq = StandingsSequences.from_dict({})
    assert seq.league is None
    assert seq.conference is None
    assert seq.division is None


# ==========================================================================
# STANDING ENTRY
# ==========================================================================

def test_standing_entry_from_dict() -> None:
    entry = StandingEntry.from_dict(ENTRY_DATA)
    assert entry.team.name.default == "Colorado Avalanche"
    assert entry.team.abbrev == "COL"
    assert entry.season_id == 20252026
    assert entry.date == "2026-03-26"
    assert entry.game_type_id == 2
    assert entry.clinch_indicator == "x"
    assert entry.conference_abbrev == "W"
    assert entry.division_name == "Central"
    assert entry.streak_code == "W"
    assert entry.streak_count == 3

def test_standing_entry_record() -> None:
    entry = StandingEntry.from_dict(ENTRY_DATA)
    assert entry.record.wins == 47
    assert entry.record.points == 104
    assert entry.record.goals_for == 242

def test_standing_entry_splits() -> None:
    entry = StandingEntry.from_dict(ENTRY_DATA)
    assert entry.home.wins == 25
    assert entry.road.wins == 22
    assert entry.l10.wins == 7

def test_standing_entry_sequences() -> None:
    entry = StandingEntry.from_dict(ENTRY_DATA)
    assert entry.sequences.league == 1
    assert entry.sequences.division == 1

def test_standing_entry_empty() -> None:
    entry = StandingEntry.from_dict({})
    assert entry.team.name.default is None
    assert entry.season_id is None
    assert entry.record.wins is None
    assert entry.home.wins is None


# ==========================================================================
# STANDINGS RESULT
# ==========================================================================

def test_standings_result_from_dict() -> None:
    data = {
        "wildCardIndicator": True,
        "standingsDateTimeUtc": "2026-03-26T12:00:00Z",
        "standings": [ENTRY_DATA, ENTRY_DATA],
    }
    result = StandingsResult.from_dict(data)
    assert result.wild_card_indicator is True
    assert result.standings_date_time_utc == "2026-03-26T12:00:00Z"
    assert len(result.standings) == 2
    assert result.standings[0].team.abbrev == "COL"

def test_standings_result_empty_standings() -> None:
    result = StandingsResult.from_dict({"wildCardIndicator": False})
    assert result.wild_card_indicator is False
    assert result.standings == []

def test_standings_result_empty() -> None:
    result = StandingsResult.from_dict({})
    assert result.wild_card_indicator is None
    assert result.standings_date_time_utc is None
    assert result.standings == []
