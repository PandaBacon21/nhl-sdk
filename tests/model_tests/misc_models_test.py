from src.models.misc import (
    Country, Franchise, GlossaryEntry,
    LocationResult, PostalLookupResult,
    WscPlay, WscPlayDetails,
    StatsConfig, ReportConfig, ReportContextConfig,
)
from src.models.games.shifts import ShiftChart, ShiftEntry


# ==========================================================================
# LOCATION RESULT
# ==========================================================================

def test_location_result_from_dict() -> None:
    data = {"country": "US"}
    result = LocationResult.from_dict(data)
    assert result.country_code == "US"


def test_location_result_empty() -> None:
    result = LocationResult.from_dict({})
    assert result.country_code is None


# ==========================================================================
# POSTAL LOOKUP RESULT
# ==========================================================================

def test_postal_lookup_result_from_dict() -> None:
    data = {
        "postalCode": "80202",
        "country": "US",
        "stateProvince": "CO",
        "city": "Denver",
        "county": "Denver",
        "networkType": "cable",
        "teamName": {"default": "Colorado Avalanche"},
    }
    result = PostalLookupResult.from_dict(data)
    assert result.postal_code == "80202"
    assert result.country == "US"
    assert result.state_province == "CO"
    assert result.city == "Denver"
    assert result.county == "Denver"
    assert result.network_type == "cable"
    assert result.team_name.default == "Colorado Avalanche"


def test_postal_lookup_result_empty() -> None:
    result = PostalLookupResult.from_dict({})
    assert result.postal_code is None
    assert result.country is None
    assert result.state_province is None
    assert result.city is None
    assert result.county is None
    assert result.network_type is None
    assert result.team_name.default is None


# ==========================================================================
# COUNTRY
# ==========================================================================

def test_country_from_dict() -> None:
    data = {
        "id": "CA",
        "countryCode": "CA",
        "country3Code": "CAN",
        "countryName": "Canada",
        "nationalityName": "Canadian",
        "iocCode": "CAN",
        "hasPlayerStats": 1,
        "isActive": 1,
        "imageUrl": "https://example.com/ca.png",
        "thumbnailUrl": "https://example.com/ca_thumb.png",
        "olympicUrl": "https://example.com/ca_olympic.png",
    }
    result = Country.from_dict(data)
    assert result.id == "CA"
    assert result.country_code == "CA"
    assert result.country3_code == "CAN"
    assert result.country_name == "Canada"
    assert result.nationality_name == "Canadian"
    assert result.ioc_code == "CAN"
    assert result.has_player_stats is True
    assert result.is_active is True
    assert result.image_url == "https://example.com/ca.png"
    assert result.thumbnail_url == "https://example.com/ca_thumb.png"
    assert result.olympic_url == "https://example.com/ca_olympic.png"


def test_country_from_dict_bool_false() -> None:
    data = {"id": "XX", "hasPlayerStats": 0, "isActive": 0}
    result = Country.from_dict(data)
    assert result.has_player_stats is False
    assert result.is_active is False


def test_country_empty() -> None:
    result = Country.from_dict({})
    assert result.id is None
    assert result.country_code is None
    assert result.country3_code is None
    assert result.country_name is None
    assert result.nationality_name is None
    assert result.ioc_code is None
    assert result.has_player_stats is None
    assert result.is_active is None
    assert result.image_url is None
    assert result.thumbnail_url is None
    assert result.olympic_url is None


# ==========================================================================
# FRANCHISE
# ==========================================================================

def test_franchise_from_dict() -> None:
    data = {
        "id": 1,
        "fullName": "Montreal Canadiens",
        "teamCommonName": "Canadiens",
        "teamPlaceName": "Montréal",
    }
    result = Franchise.from_dict(data)
    assert result.franchise_id == 1
    assert result.full_name == "Montreal Canadiens"
    assert result.team_common_name == "Canadiens"
    assert result.team_place_name == "Montréal"


def test_franchise_empty() -> None:
    result = Franchise.from_dict({})
    assert result.franchise_id is None
    assert result.full_name is None
    assert result.team_common_name is None
    assert result.team_place_name is None


# ==========================================================================
# GLOSSARY ENTRY
# ==========================================================================

def test_glossary_entry_from_dict() -> None:
    data = {
        "id": 42,
        "abbreviation": "G",
        "fullName": "Goals",
        "definition": "Number of goals scored.",
        "languageCode": "en",
        "firstSeasonForStat": 19171918,
        "lastUpdated": "2024-01-15",
    }
    result = GlossaryEntry.from_dict(data)
    assert result.id == 42
    assert result.abbreviation == "G"
    assert result.full_name == "Goals"
    assert result.definition == "Number of goals scored."
    assert result.language_code == "en"
    assert result.first_season_for_stat == 19171918
    assert result.last_updated == "2024-01-15"


def test_glossary_entry_empty() -> None:
    result = GlossaryEntry.from_dict({})
    assert result.id is None
    assert result.abbreviation is None
    assert result.full_name is None
    assert result.definition is None
    assert result.language_code is None
    assert result.first_season_for_stat is None
    assert result.last_updated is None


# ==========================================================================
# WSC PLAY DETAILS
# ==========================================================================

def test_wsc_play_details_from_dict() -> None:
    data = {
        "eventOwnerTeamId": 21,
        "xCoord": -10,
        "yCoord": 5,
        "zoneCode": "D",
        "losingPlayerId": 111,
        "winningPlayerId": 222,
        "shotType": "wrist",
        "shootingPlayerId": 333,
        "goalieInNetId": 444,
        "awaySOG": 10,
        "homeSOG": 12,
        "reason": "blocked",
        "blockingPlayerId": 555,
        "hittingPlayerId": 666,
        "hitteePlayerId": 777,
        "playerId": 888,
        "goalModifier": "none",
        "strength": "ev",
        "strengthCode": 1551,
        "goalCode": 1,
        "scoringPlayerId": 999,
        "scoringPlayerTotal": 10,
        "assist1PlayerId": 1000,
        "assist1PlayerTotal": 20,
        "assist2PlayerId": 1001,
        "assist2PlayerTotal": 15,
        "awayScore": 1,
        "homeScore": 2,
        "penaltyTypeCode": "MAJ",
        "descKey": "slashing",
        "duration": 5,
        "committedByPlayerId": 1002,
        "drawnByPlayerId": 1003,
    }
    result = WscPlayDetails.from_dict(data)
    assert result.event_owner_team_id == 21
    assert result.x_coord == -10
    assert result.y_coord == 5
    assert result.zone_code == "D"
    assert result.losing_player_id == 111
    assert result.winning_player_id == 222
    assert result.shot_type == "wrist"
    assert result.shooting_player_id == 333
    assert result.goalie_in_net_id == 444
    assert result.away_sog == 10
    assert result.home_sog == 12
    assert result.reason == "blocked"
    assert result.blocking_player_id == 555
    assert result.hitting_player_id == 666
    assert result.hittee_player_id == 777
    assert result.player_id == 888
    assert result.scoring_player_id == 999
    assert result.scoring_player_total == 10
    assert result.assist1_player_id == 1000
    assert result.assist2_player_id == 1001
    assert result.away_score == 1
    assert result.home_score == 2
    assert result.penalty_type_code == "MAJ"
    assert result.penalty_desc_key == "slashing"
    assert result.duration == 5
    assert result.committed_by_player_id == 1002
    assert result.drawn_by_player_id == 1003


def test_wsc_play_details_empty() -> None:
    result = WscPlayDetails.from_dict({})
    assert result.event_owner_team_id is None
    assert result.x_coord is None
    assert result.scoring_player_id is None


# ==========================================================================
# WSC PLAY
# ==========================================================================

def test_wsc_play_from_dict() -> None:
    data = {
        "id": 1,
        "eventId": 53,
        "period": 1,
        "timeInPeriod": "00:00",
        "secondsRemaining": 1200,
        "situationCode": "1551",
        "typeCode": 502,
        "typeDescKey": "faceoff",
        "homeTeamDefendingSide": "right",
        "sortOrder": 11,
        "utc": "2025-12-03T02:00:00Z",
        "eventOwnerTeamId": 23,
        "losingPlayerId": 111,
        "winningPlayerId": 222,
    }
    result = WscPlay.from_dict(data)
    assert result.id == 1
    assert result.event_id == 53
    assert result.period == 1
    assert result.time_in_period == "00:00"
    assert result.seconds_remaining == 1200
    assert result.situation_code == "1551"
    assert result.type_code == 502
    assert result.type_desc_key == "faceoff"
    assert result.home_team_defending_side == "right"
    assert result.sort_order == 11
    assert result.utc == "2025-12-03T02:00:00Z"
    assert isinstance(result.details, WscPlayDetails)
    assert result.details.event_owner_team_id == 23
    assert result.details.winning_player_id == 222


def test_wsc_play_empty() -> None:
    result = WscPlay.from_dict({})
    assert result.id is None
    assert result.event_id is None
    assert result.type_desc_key is None
    assert isinstance(result.details, WscPlayDetails)


# ==========================================================================
# REPORT CONTEXT CONFIG
# ==========================================================================

def test_report_context_config_from_dict() -> None:
    data = {
        "displayItems": ["goals", "assists"],
        "resultFilters": ["season"],
        "sortKeys": ["points"],
    }
    result = ReportContextConfig.from_dict(data)
    assert result.display_items == ["goals", "assists"]
    assert result.result_filters == ["season"]
    assert result.sort_keys == ["points"]


def test_report_context_config_empty() -> None:
    result = ReportContextConfig.from_dict({})
    assert result.display_items == []
    assert result.result_filters == []
    assert result.sort_keys == []


# ==========================================================================
# REPORT CONFIG
# ==========================================================================

def test_report_config_from_dict() -> None:
    data = {
        "game": {"displayItems": ["goals"], "resultFilters": [], "sortKeys": []},
        "season": {"displayItems": ["assists"], "resultFilters": ["season"], "sortKeys": ["points"]},
    }
    result = ReportConfig.from_dict(data)
    assert isinstance(result.game, ReportContextConfig)
    assert result.game.display_items == ["goals"]
    assert isinstance(result.season, ReportContextConfig)
    assert result.season.display_items == ["assists"]


def test_report_config_empty() -> None:
    result = ReportConfig.from_dict({})
    assert result.game is None
    assert result.season is None


# ==========================================================================
# STATS CONFIG
# ==========================================================================

def test_stats_config_from_dict() -> None:
    data = {
        "playerReportData": {
            "summary": {
                "game": {"displayItems": ["goals"], "resultFilters": [], "sortKeys": []},
                "season": {"displayItems": ["assists"], "resultFilters": [], "sortKeys": []},
            }
        },
        "goalieReportData": {},
        "teamReportData": {},
        "aggregatedColumns": ["goals", "assists"],
        "individualColumns": ["penaltyMinutes"],
    }
    result = StatsConfig.from_dict(data)
    assert "summary" in result.player_report_data
    assert isinstance(result.player_report_data["summary"], ReportConfig)
    assert result.player_report_data["summary"].game.display_items == ["goals"]
    assert result.goalie_report_data == {}
    assert result.team_report_data == {}
    assert result.aggregated_columns == ["goals", "assists"]
    assert result.individual_columns == ["penaltyMinutes"]


def test_stats_config_empty() -> None:
    result = StatsConfig.from_dict({})
    assert result.player_report_data == {}
    assert result.goalie_report_data == {}
    assert result.team_report_data == {}
    assert result.aggregated_columns == []
    assert result.individual_columns == []


# ==========================================================================
# SHIFT ENTRY
# ==========================================================================

def test_shift_entry_from_dict() -> None:
    data = {
        "id": 101,
        "gameId": 2025020417,
        "playerId": 8477492,
        "period": 1,
        "shiftNumber": 1,
        "startTime": "00:00",
        "endTime": "01:23",
        "duration": "01:23",
        "firstName": "Ryan",
        "lastName": "Johansen",
        "teamId": 21,
        "teamAbbrev": "COL",
        "teamName": "Colorado Avalanche",
        "hexValue": "#236192",
        "detailCode": 0,
        "eventDescription": None,
        "eventDetails": None,
        "eventNumber": None,
        "typeCode": 517,
    }
    result = ShiftEntry.from_dict(data)
    assert result.id == 101
    assert result.game_id == 2025020417
    assert result.player_id == 8477492
    assert result.period == 1
    assert result.shift_number == 1
    assert result.start_time == "00:00"
    assert result.end_time == "01:23"
    assert result.duration == "01:23"
    assert result.first_name == "Ryan"
    assert result.last_name == "Johansen"
    assert result.team_id == 21
    assert result.team_abbrev == "COL"
    assert result.team_name == "Colorado Avalanche"
    assert result.hex_value == "#236192"
    assert result.detail_code == 0
    assert result.event_description is None
    assert result.type_code == 517


def test_shift_entry_empty() -> None:
    result = ShiftEntry.from_dict({})
    assert result.id is None
    assert result.game_id is None
    assert result.player_id is None
    assert result.shift_number is None
    assert result.hex_value is None
    assert result.team_name is None


# ==========================================================================
# SHIFT CHART
# ==========================================================================

def test_shift_chart_from_dict() -> None:
    game_id = 2025020417
    data = {
        "total": 2,
        "data": [
            {
                "id": 101, "gameId": game_id, "playerId": 8477492,
                "period": 1, "shiftNumber": 1, "startTime": "00:00",
                "endTime": "01:23", "duration": "01:23",
                "firstName": "Ryan", "lastName": "Johansen",
                "teamId": 21, "teamAbbrev": "COL", "teamName": "Colorado Avalanche",
                "hexValue": "#236192", "detailCode": 0,
                "eventDescription": None, "eventDetails": None,
                "eventNumber": None, "typeCode": 517,
            },
            {
                "id": 102, "gameId": game_id, "playerId": 8478402,
                "period": 1, "shiftNumber": 2, "startTime": "01:30",
                "endTime": "03:00", "duration": "01:30",
                "firstName": "Nathan", "lastName": "MacKinnon",
                "teamId": 21, "teamAbbrev": "COL", "teamName": "Colorado Avalanche",
                "hexValue": "#236192", "detailCode": 0,
                "eventDescription": None, "eventDetails": None,
                "eventNumber": None, "typeCode": 517,
            },
        ],
    }
    result = ShiftChart.from_dict(game_id=game_id, data=data)
    assert result.game_id == game_id
    assert result.total == 2
    assert len(result.shifts) == 2
    assert isinstance(result.shifts[0], ShiftEntry)
    assert result.shifts[0].player_id == 8477492
    assert result.shifts[1].first_name == "Nathan"


def test_shift_chart_empty() -> None:
    result = ShiftChart.from_dict(game_id=999, data={})
    assert result.game_id == 999
    assert result.total == 0
    assert result.shifts == []
