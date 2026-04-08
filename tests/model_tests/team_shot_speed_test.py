"""
Tests for TeamShotSpeedResult and sub-models.
"""
from nhl_stats.models.teams.team.edge.team_shot_speed_details.team_shot_speed_detail import (
    TeamShotSpeedResult, TeamHardestShotEntry, TeamShotSpeedDetail,
)


OVERLAY = {
    "player": {"firstName": {"default": "Cale"}, "lastName": {"default": "Makar"}},
    "gameDate": "2026-03-18",
    "awayTeam": {"abbrev": "DAL", "score": 2},
    "homeTeam": {"abbrev": "COL", "score": 1},
    "gameOutcome": {"lastPeriodType": "SO"},
    "periodDescriptor": {"maxRegulationPeriods": 3, "number": 2, "periodType": "REG"},
    "timeInPeriod": "10:39",
    "gameType": 2,
}

COL_TEAM_REF = {
    "commonName": {"default": "Avalanche"},
    "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
    "teamLogo": {
        "light": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
        "dark": "https://assets.nhle.com/logos/nhl/svg/COL_dark.svg",
    },
}

DAL_TEAM_REF = {
    "commonName": {"default": "Stars"},
    "placeNameWithPreposition": {"default": "Dallas", "fr": "de Dallas"},
    "teamLogo": {
        "light": "https://assets.nhle.com/logos/nhl/svg/DAL_light.svg",
        "dark": "https://assets.nhle.com/logos/nhl/svg/DAL_dark.svg",
    },
}

HARDEST_SHOT_ENTRY = {
    "player": {
        "id": 8480069,
        "firstName": {"default": "Cale"},
        "lastName": {"default": "Makar"},
        "slug": "cale-makar-8480069",
    },
    "gameCenterLink": "/gamecenter/dal-vs-col/2026/03/18/2025021080",
    "gameDate": "2026-03-18",
    "gameType": 2,
    "isHomeTeam": True,
    "shotSpeed": {"imperial": 98.21, "metric": 158.0537},
    "timeInPeriod": "10:39",
    "periodDescriptor": {"number": 2, "periodType": "REG", "maxRegulationPeriods": 3},
    "homeTeam": COL_TEAM_REF,
    "awayTeam": DAL_TEAM_REF,
}

SPEED_DETAIL_ALL = {
    "position": "all",
    "topShotSpeed": {
        "imperial": 98.21, "metric": 158.0537, "rank": 23,
        "leagueAvg": {"imperial": 99.3481, "metric": 159.8853},
        "overlay": OVERLAY,
    },
    "avgShotSpeed": {
        "imperial": 60.4652, "metric": 97.3094, "rank": 1,
        "leagueAvg": {"imperial": 58.1684, "metric": 93.613},
    },
    "shotAttemptsOver100": {"value": 0, "rank": 12, "leagueAvg": 0.7813},
    "shotAttempts90To100": {"value": 57, "rank": 10, "leagueAvg": 49.9375},
    "shotAttempts80To90": {"value": 525, "leagueAvg": 368.75},
    "shotAttempts70To80": {"value": 1320, "leagueAvg": 925.875},
}

SPEED_DETAIL_D = {
    "position": "D",
    "topShotSpeed": {
        "imperial": 98.21, "metric": 158.0537, "rank": 20,
        "leagueAvg": {"imperial": 98.8134, "metric": 159.0248},
        "overlay": OVERLAY,
    },
    "avgShotSpeed": {
        "imperial": 69.5475, "metric": 111.9258, "rank": 3,
        "leagueAvg": {"imperial": 67.8156, "metric": 109.1387},
    },
    "shotAttemptsOver100": {"value": 0, "rank": 11, "leagueAvg": 0.6875},
    "shotAttempts90To100": {"value": 46, "rank": 10, "leagueAvg": 38.875},
    "shotAttempts80To90": {"value": 322, "leagueAvg": 196.9688},
    "shotAttempts70To80": {"value": 724, "leagueAvg": 439.0},
}

FULL_RESPONSE = {
    "hardestShots": [HARDEST_SHOT_ENTRY],
    "shotSpeedDetails": [SPEED_DETAIL_ALL, SPEED_DETAIL_D],
}


# --------------------------------------------------------------------------
# TeamHardestShotEntry
# --------------------------------------------------------------------------

def test_hardest_shot_entry_fields() -> None:
    entry = TeamHardestShotEntry.from_dict(HARDEST_SHOT_ENTRY)
    assert entry.game_center_link == "/gamecenter/dal-vs-col/2026/03/18/2025021080"
    assert entry.game_date == "2026-03-18"
    assert entry.game_type == 2
    assert entry.is_home_team is True
    assert entry.time_in_period == "10:39"


def test_hardest_shot_entry_player() -> None:
    entry = TeamHardestShotEntry.from_dict(HARDEST_SHOT_ENTRY)
    assert entry.player.id == 8480069
    assert entry.player.first_name.default == "Cale"
    assert entry.player.slug == "cale-makar-8480069"


def test_hardest_shot_entry_shot_speed() -> None:
    entry = TeamHardestShotEntry.from_dict(HARDEST_SHOT_ENTRY)
    assert entry.shot_speed.imperial == 98.21
    assert entry.shot_speed.metric == 158.0537


def test_hardest_shot_entry_period_descriptor() -> None:
    entry = TeamHardestShotEntry.from_dict(HARDEST_SHOT_ENTRY)
    assert entry.period_descriptor.number == 2
    assert entry.period_descriptor.period_type == "REG"
    assert entry.period_descriptor.max_regulation_periods == 3


def test_hardest_shot_entry_teams() -> None:
    entry = TeamHardestShotEntry.from_dict(HARDEST_SHOT_ENTRY)
    assert entry.home_team.common_name.default == "Avalanche"
    assert entry.away_team.common_name.default == "Stars"


def test_hardest_shot_entry_empty() -> None:
    entry = TeamHardestShotEntry.from_dict({})
    assert entry.game_center_link is None
    assert entry.shot_speed.imperial is None
    assert entry.period_descriptor.number is None
    assert entry.home_team.common_name.default is None


# --------------------------------------------------------------------------
# TeamShotSpeedDetail
# --------------------------------------------------------------------------

def test_team_shot_speed_detail_all_positions() -> None:
    detail = TeamShotSpeedDetail.from_dict(SPEED_DETAIL_ALL)
    assert detail.position == "all"
    assert detail.top_shot_speed.imperial == 98.21
    assert detail.top_shot_speed.rank == 23
    assert detail.top_shot_speed.league_avg.imperial == 99.3481
    assert detail.top_shot_speed.overlay is not None
    assert detail.top_shot_speed.overlay.game_date == "2026-03-18"


def test_team_shot_speed_detail_avg_speed() -> None:
    detail = TeamShotSpeedDetail.from_dict(SPEED_DETAIL_ALL)
    assert detail.avg_shot_speed.imperial == 60.4652
    assert detail.avg_shot_speed.rank == 1
    assert detail.avg_shot_speed.overlay is None


def test_team_shot_speed_detail_attempt_buckets_with_rank() -> None:
    detail = TeamShotSpeedDetail.from_dict(SPEED_DETAIL_ALL)
    assert detail.shot_attempts_over_100.value == 0
    assert detail.shot_attempts_over_100.rank == 12
    assert detail.shot_attempts_over_100.league_avg == 0.7813
    assert detail.shot_attempts_90_to_100.value == 57
    assert detail.shot_attempts_90_to_100.rank == 10


def test_team_shot_speed_detail_attempt_buckets_no_rank() -> None:
    detail = TeamShotSpeedDetail.from_dict(SPEED_DETAIL_ALL)
    assert detail.shot_attempts_80_to_90.value == 525
    assert detail.shot_attempts_80_to_90.rank is None
    assert detail.shot_attempts_80_to_90.league_avg == 368.75
    assert detail.shot_attempts_70_to_80.value == 1320
    assert detail.shot_attempts_70_to_80.rank is None


def test_team_shot_speed_detail_defensemen() -> None:
    detail = TeamShotSpeedDetail.from_dict(SPEED_DETAIL_D)
    assert detail.position == "D"
    assert detail.top_shot_speed.rank == 20
    assert detail.avg_shot_speed.rank == 3
    assert detail.shot_attempts_90_to_100.value == 46


def test_team_shot_speed_detail_empty() -> None:
    detail = TeamShotSpeedDetail.from_dict({})
    assert detail.position is None
    assert detail.top_shot_speed.imperial is None
    assert detail.top_shot_speed.rank is None
    assert detail.top_shot_speed.overlay is None
    assert detail.shot_attempts_over_100.value is None


# --------------------------------------------------------------------------
# TeamShotSpeedResult (top-level)
# --------------------------------------------------------------------------

def test_team_shot_speed_result_from_dict() -> None:
    result = TeamShotSpeedResult.from_dict(FULL_RESPONSE)
    assert isinstance(result, TeamShotSpeedResult)


def test_team_shot_speed_result_hardest_shots() -> None:
    result = TeamShotSpeedResult.from_dict(FULL_RESPONSE)
    assert len(result.hardest_shots) == 1
    assert result.hardest_shots[0].player.id == 8480069
    assert result.hardest_shots[0].shot_speed.imperial == 98.21


def test_team_shot_speed_result_details() -> None:
    result = TeamShotSpeedResult.from_dict(FULL_RESPONSE)
    assert len(result.shot_speed_details) == 2
    assert result.shot_speed_details[0].position == "all"
    assert result.shot_speed_details[1].position == "D"


def test_team_shot_speed_result_empty() -> None:
    result = TeamShotSpeedResult.from_dict({})
    assert result.hardest_shots == []
    assert result.shot_speed_details == []


def test_team_shot_speed_result_to_dict() -> None:
    result = TeamShotSpeedResult.from_dict(FULL_RESPONSE)
    d = result.to_dict()
    assert len(d["hardest_shots"]) == 1
    assert d["hardest_shots"][0]["player"]["id"] == 8480069
    assert d["hardest_shots"][0]["shot_speed"]["imperial"] == 98.21
    assert d["hardest_shots"][0]["is_home_team"] is True
    assert len(d["shot_speed_details"]) == 2
    assert d["shot_speed_details"][0]["position"] == "all"
    assert d["shot_speed_details"][0]["top_shot_speed"]["rank"] == 23
    assert d["shot_speed_details"][0]["shot_attempts_80_to_90"]["value"] == 525
    assert d["shot_speed_details"][0]["shot_attempts_80_to_90"]["rank"] is None
