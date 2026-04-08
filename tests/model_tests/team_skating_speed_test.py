"""
Tests for TeamSkatingSpeedResult and sub-models.
"""
from nhl_stats.models.teams.team.edge.team_skating_speed_details.team_skating_speed_detail import (
    TeamSkatingSpeedResult, TopSpeedPlayer,
    TeamTopSpeedEntry, TeamSpeedDetail,
)


OVERLAY = {
    "player": {"firstName": {"default": "Nathan"}, "lastName": {"default": "MacKinnon"}},
    "gameDate": "2026-03-28",
    "awayTeam": {"abbrev": "WPG", "score": 4},
    "homeTeam": {"abbrev": "COL", "score": 2},
    "gameOutcome": {"lastPeriodType": "REG"},
    "periodDescriptor": {"maxRegulationPeriods": 3, "number": 2, "periodType": "REG"},
    "timeInPeriod": "06:42",
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

WPG_TEAM_REF = {
    "commonName": {"default": "Jets"},
    "placeNameWithPreposition": {"default": "Winnipeg", "fr": "de Winnipeg"},
    "teamLogo": {
        "light": "https://assets.nhle.com/logos/nhl/svg/WPG_light.svg",
        "dark": "https://assets.nhle.com/logos/nhl/svg/WPG_dark.svg",
    },
}

TOP_SPEED_ENTRY = {
    "player": {
        "id": 8477492,
        "firstName": {"default": "Nathan"},
        "lastName": {"default": "MacKinnon"},
        "slug": "nathan-mackinnon-8477492",
    },
    "gameCenterLink": "/gamecenter/wpg-vs-col/2026/03/28/2025021162",
    "gameDate": "2026-03-28",
    "gameType": 2,
    "isHomeTeam": True,
    "skatingSpeed": {"imperial": 24.0129, "metric": 38.6450},
    "timeInPeriod": "06:42",
    "periodDescriptor": {"number": 2, "periodType": "REG", "maxRegulationPeriods": 3},
    "homeTeam": COL_TEAM_REF,
    "awayTeam": WPG_TEAM_REF,
}

SPEED_DETAIL_ALL = {
    "positionCode": "all",
    "maxSkatingSpeed": {
        "imperial": 24.0129, "metric": 38.6450, "rank": 8,
        "leagueAvg": {"imperial": 23.7365, "metric": 38.2002},
        "overlay": OVERLAY,
    },
    "burstsOver22": {"value": 152, "rank": 2, "leagueAvg": 77.75},
    "bursts20To22": {"value": 2242, "rank": 1, "leagueAvg": 1516.1875},
    "bursts18To20": {"value": 8206, "rank": 2, "leagueAvg": 7059.625},
}

SPEED_DETAIL_D = {
    "positionCode": "D",
    "maxSkatingSpeed": {
        "imperial": 23.6795, "metric": 38.1083, "rank": 4,
        "leagueAvg": {"imperial": 23.0207, "metric": 37.0482},
        "overlay": OVERLAY,
    },
    "burstsOver22": {"value": 35, "rank": 3, "leagueAvg": 11.0625},
    "bursts20To22": {"value": 467, "rank": 1, "leagueAvg": 277.0938},
    "bursts18To20": {"value": 1941, "rank": 4, "leagueAvg": 1633.6875},
}

FULL_RESPONSE = {
    "topSkatingSpeeds": [TOP_SPEED_ENTRY],
    "skatingSpeedDetails": [SPEED_DETAIL_ALL, SPEED_DETAIL_D],
}


# --------------------------------------------------------------------------
# TopSpeedPlayer
# --------------------------------------------------------------------------

def test_top_speed_player_fields() -> None:
    player = TopSpeedPlayer.from_dict(TOP_SPEED_ENTRY["player"])
    assert player.id == 8477492
    assert player.first_name.default == "Nathan"
    assert player.last_name.default == "MacKinnon"
    assert player.slug == "nathan-mackinnon-8477492"


def test_top_speed_player_empty() -> None:
    player = TopSpeedPlayer.from_dict({})
    assert player.id is None
    assert player.first_name.default is None
    assert player.last_name.default is None
    assert player.slug is None


# --------------------------------------------------------------------------
# TeamTopSpeedEntry
# --------------------------------------------------------------------------

def test_team_top_speed_entry_fields() -> None:
    entry = TeamTopSpeedEntry.from_dict(TOP_SPEED_ENTRY)
    assert entry.game_center_link == "/gamecenter/wpg-vs-col/2026/03/28/2025021162"
    assert entry.game_date == "2026-03-28"
    assert entry.game_type == 2
    assert entry.is_home_team is True
    assert entry.time_in_period == "06:42"


def test_team_top_speed_entry_player() -> None:
    entry = TeamTopSpeedEntry.from_dict(TOP_SPEED_ENTRY)
    assert entry.player.id == 8477492
    assert entry.player.first_name.default == "Nathan"
    assert entry.player.slug == "nathan-mackinnon-8477492"


def test_team_top_speed_entry_skating_speed() -> None:
    entry = TeamTopSpeedEntry.from_dict(TOP_SPEED_ENTRY)
    assert entry.skating_speed.imperial == 24.0129
    assert entry.skating_speed.metric == 38.6450


def test_team_top_speed_entry_period_descriptor() -> None:
    entry = TeamTopSpeedEntry.from_dict(TOP_SPEED_ENTRY)
    assert entry.period_descriptor.number == 2
    assert entry.period_descriptor.period_type == "REG"
    assert entry.period_descriptor.max_regulation_periods == 3


def test_team_top_speed_entry_teams() -> None:
    entry = TeamTopSpeedEntry.from_dict(TOP_SPEED_ENTRY)
    assert entry.home_team.common_name.default == "Avalanche"
    assert entry.home_team.team_logo.light == "https://assets.nhle.com/logos/nhl/svg/COL_light.svg"
    assert entry.away_team.common_name.default == "Jets"


def test_team_top_speed_entry_empty() -> None:
    entry = TeamTopSpeedEntry.from_dict({})
    assert entry.game_center_link is None
    assert entry.game_date is None
    assert entry.is_home_team is None
    assert entry.skating_speed.imperial is None
    assert entry.period_descriptor.number is None
    assert entry.home_team.common_name.default is None


# --------------------------------------------------------------------------
# TeamSpeedDetail
# --------------------------------------------------------------------------

def test_team_speed_detail_all_positions() -> None:
    detail = TeamSpeedDetail.from_dict(SPEED_DETAIL_ALL)
    assert detail.position_code == "all"
    assert detail.max_skating_speed.imperial == 24.0129
    assert detail.max_skating_speed.rank == 8
    assert detail.max_skating_speed.league_avg.imperial == 23.7365
    assert detail.max_skating_speed.overlay is not None
    assert detail.max_skating_speed.overlay.game_date == "2026-03-28"


def test_team_speed_detail_burst_counts() -> None:
    detail = TeamSpeedDetail.from_dict(SPEED_DETAIL_ALL)
    assert detail.bursts_over_22.value == 152
    assert detail.bursts_over_22.rank == 2
    assert detail.bursts_over_22.league_avg == 77.75
    assert detail.bursts_20_to_22.value == 2242
    assert detail.bursts_20_to_22.rank == 1
    assert detail.bursts_18_to_20.value == 8206
    assert detail.bursts_18_to_20.rank == 2


def test_team_speed_detail_defensemen() -> None:
    detail = TeamSpeedDetail.from_dict(SPEED_DETAIL_D)
    assert detail.position_code == "D"
    assert detail.max_skating_speed.imperial == 23.6795
    assert detail.max_skating_speed.rank == 4
    assert detail.bursts_over_22.value == 35


def test_team_speed_detail_empty() -> None:
    detail = TeamSpeedDetail.from_dict({})
    assert detail.position_code is None
    assert detail.max_skating_speed.imperial is None
    assert detail.max_skating_speed.rank is None
    assert detail.max_skating_speed.overlay is None
    assert detail.bursts_over_22.value is None


# --------------------------------------------------------------------------
# TeamSkatingSpeedResult (top-level)
# --------------------------------------------------------------------------

def test_team_skating_speed_result_from_dict() -> None:
    result = TeamSkatingSpeedResult.from_dict(FULL_RESPONSE)
    assert isinstance(result, TeamSkatingSpeedResult)


def test_team_skating_speed_result_top_speeds() -> None:
    result = TeamSkatingSpeedResult.from_dict(FULL_RESPONSE)
    assert len(result.top_skating_speeds) == 1
    assert result.top_skating_speeds[0].player.id == 8477492
    assert result.top_skating_speeds[0].skating_speed.imperial == 24.0129


def test_team_skating_speed_result_details() -> None:
    result = TeamSkatingSpeedResult.from_dict(FULL_RESPONSE)
    assert len(result.skating_speed_details) == 2
    assert result.skating_speed_details[0].position_code == "all"
    assert result.skating_speed_details[1].position_code == "D"


def test_team_skating_speed_result_empty() -> None:
    result = TeamSkatingSpeedResult.from_dict({})
    assert result.top_skating_speeds == []
    assert result.skating_speed_details == []


def test_team_skating_speed_result_to_dict() -> None:
    result = TeamSkatingSpeedResult.from_dict(FULL_RESPONSE)
    d = result.to_dict()
    assert len(d["top_skating_speeds"]) == 1
    assert d["top_skating_speeds"][0]["player"]["id"] == 8477492
    assert d["top_skating_speeds"][0]["skating_speed"]["imperial"] == 24.0129
    assert d["top_skating_speeds"][0]["is_home_team"] is True
    assert len(d["skating_speed_details"]) == 2
    assert d["skating_speed_details"][0]["position_code"] == "all"
    assert d["skating_speed_details"][0]["max_skating_speed"]["rank"] == 8
    assert d["skating_speed_details"][0]["bursts_over_22"]["value"] == 152
