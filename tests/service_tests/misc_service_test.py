from nhl_sdk.services.misc import Misc
from nhl_sdk.models.misc import (
    LocationResult, PostalLookupResult, MiscMeta,
    GameMetaResult, PlayoffSeriesMetaResult,
    GoalReplayResult, PlayReplayResult,
    GameRailResult, WscPlay, StatsConfig,
    Country, Franchise, GlossaryEntry,
)

from .conftest import ok

GAME_ID = 2025020417
YEAR = 2024
SERIES_LETTER = "A"
EVENT_NUM = 3
POSTAL_CODE = "80202"


# ==========================================================================
# META
# ==========================================================================

def test_misc_meta(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_meta.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.meta()
    assert isinstance(result, MiscMeta)
    mock_client._api.api_web.call_nhl_misc.get_meta.assert_called_once_with(
        players=None, teams=None, season_states=None
    )


def test_misc_meta_with_params(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_meta.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.meta(players="8477492", teams="COL")
    assert isinstance(result, MiscMeta)
    mock_client._api.api_web.call_nhl_misc.get_meta.assert_called_once_with(
        players="8477492", teams="COL", season_states=None
    )


def test_misc_game_meta(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_game_info.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.game_meta(game_id=GAME_ID)
    assert isinstance(result, GameMetaResult)
    mock_client._api.api_web.call_nhl_misc.get_game_info.assert_called_once_with(game_id=GAME_ID)


def test_misc_playoff_series_meta(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_playoff_series_meta.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.playoff_series_meta(year=YEAR, series_letter=SERIES_LETTER)
    assert isinstance(result, PlayoffSeriesMetaResult)
    mock_client._api.api_web.call_nhl_misc.get_playoff_series_meta.assert_called_once_with(
        year=YEAR, series_letter=SERIES_LETTER
    )


# ==========================================================================
# LOCATION & POSTAL
# ==========================================================================

def test_misc_location(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_location.return_value = ok({"country": "US"})
    svc = Misc(mock_client)
    result = svc.location()
    assert isinstance(result, LocationResult)
    assert result.country_code == "US"
    mock_client._api.api_web.call_nhl_misc.get_location.assert_called_once()


def test_misc_postal_lookup(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_postal_lookup.return_value = ok([
        {"postalCode": POSTAL_CODE, "country": "US", "city": "Denver"}
    ])
    svc = Misc(mock_client)
    result = svc.postal_lookup(postal_code=POSTAL_CODE)
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], PostalLookupResult)
    assert result[0].postal_code == POSTAL_CODE
    mock_client._api.api_web.call_nhl_misc.get_postal_lookup.assert_called_once_with(
        postal_code=POSTAL_CODE
    )


def test_misc_postal_lookup_empty(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_postal_lookup.return_value = ok([])
    svc = Misc(mock_client)
    result = svc.postal_lookup(postal_code=POSTAL_CODE)
    assert result == []


# ==========================================================================
# GAME CONTENT
# ==========================================================================

def test_misc_game_rail(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_game_rail.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.game_rail(game_id=GAME_ID)
    assert isinstance(result, GameRailResult)
    mock_client._api.api_web.call_nhl_misc.get_game_rail.assert_called_once_with(game_id=GAME_ID)


def test_misc_goal_replay(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_goal_replay.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.goal_replay(game_id=GAME_ID, event_number=EVENT_NUM)
    assert isinstance(result, GoalReplayResult)
    mock_client._api.api_web.call_nhl_misc.get_goal_replay.assert_called_once_with(
        game_id=GAME_ID, event_number=EVENT_NUM
    )


def test_misc_play_replay(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_play_replay.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.play_replay(game_id=GAME_ID, event_number=EVENT_NUM)
    assert isinstance(result, PlayReplayResult)
    mock_client._api.api_web.call_nhl_misc.get_play_replay.assert_called_once_with(
        game_id=GAME_ID, event_number=EVENT_NUM
    )


def test_misc_wsc_play_by_play(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_wsc.return_value = ok([
        {"id": 1, "eventId": 10, "period": 1, "typeDescKey": "faceoff"}
    ])
    svc = Misc(mock_client)
    result = svc.wsc_play_by_play(game_id=GAME_ID)
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], WscPlay)
    mock_client._api.api_web.call_nhl_misc.get_wsc.assert_called_once_with(game_id=GAME_ID)


def test_misc_wsc_play_by_play_empty(mock_client) -> None:
    mock_client._api.api_web.call_nhl_misc.get_wsc.return_value = ok([])
    svc = Misc(mock_client)
    result = svc.wsc_play_by_play(game_id=GAME_ID)
    assert result == []


# ==========================================================================
# REFERENCE DATA (cached properties)
# ==========================================================================

def test_misc_countries_cache_miss(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_misc.get_countries.return_value = ok({
        "data": [{"id": "CA", "countryCode": "CA", "countryName": "Canada"}],
        "total": 1,
    })
    svc = Misc(mock_client)
    result = svc.countries
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Country)
    assert result[0].country_code == "CA"
    mock_client._api.api_stats.call_nhl_sdk_misc.get_countries.assert_called_once()


def test_misc_countries_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_misc.get_countries.return_value = ok({
        "data": [{"id": "CA", "countryCode": "CA"}],
        "total": 1,
    })
    svc = Misc(mock_client)
    _ = svc.countries
    _ = svc.countries
    mock_client._api.api_stats.call_nhl_sdk_misc.get_countries.assert_called_once()


def test_misc_franchises_cache_miss(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_teams.get_franchise.return_value = ok({
        "data": [{"id": 1, "fullName": "Montreal Canadiens"}],
        "total": 1,
    })
    svc = Misc(mock_client)
    result = svc.franchises
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Franchise)
    assert result[0].franchise_id == 1
    mock_client._api.api_stats.call_nhl_sdk_teams.get_franchise.assert_called_once()


def test_misc_franchises_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_teams.get_franchise.return_value = ok({
        "data": [{"id": 1, "fullName": "Montreal Canadiens"}],
        "total": 1,
    })
    svc = Misc(mock_client)
    _ = svc.franchises
    _ = svc.franchises
    mock_client._api.api_stats.call_nhl_sdk_teams.get_franchise.assert_called_once()


def test_misc_glossary_cache_miss(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_misc.get_glossary.return_value = ok({
        "data": [{"id": 1, "abbreviation": "G", "fullName": "Goals"}],
        "total": 1,
    })
    svc = Misc(mock_client)
    result = svc.glossary
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], GlossaryEntry)
    assert result[0].abbreviation == "G"
    mock_client._api.api_stats.call_nhl_sdk_misc.get_glossary.assert_called_once()


def test_misc_glossary_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_misc.get_glossary.return_value = ok({
        "data": [{"id": 1, "abbreviation": "G"}],
        "total": 1,
    })
    svc = Misc(mock_client)
    _ = svc.glossary
    _ = svc.glossary
    mock_client._api.api_stats.call_nhl_sdk_misc.get_glossary.assert_called_once()


def test_misc_config_cache_miss(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_misc.get_config.return_value = ok({
        "playerReportData": {},
        "goalieReportData": {},
        "teamReportData": {},
        "aggregatedColumns": ["goals"],
        "individualColumns": ["assists"],
    })
    svc = Misc(mock_client)
    result = svc.config
    assert isinstance(result, StatsConfig)
    assert result.aggregated_columns == ["goals"]
    mock_client._api.api_stats.call_nhl_sdk_misc.get_config.assert_called_once()


def test_misc_config_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_misc.get_config.return_value = ok({
        "playerReportData": {},
        "goalieReportData": {},
        "teamReportData": {},
    })
    svc = Misc(mock_client)
    _ = svc.config
    _ = svc.config
    mock_client._api.api_stats.call_nhl_sdk_misc.get_config.assert_called_once()


def test_misc_ping_true(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_sdk_misc.ping.return_value = ok({})
    svc = Misc(mock_client)
    result = svc.ping()
    assert result is True
    mock_client._api.api_stats.call_nhl_sdk_misc.ping.assert_called_once()


def test_misc_ping_false(mock_client) -> None:
    from nhl_sdk.core.transport import APIResponse
    mock_client._api.api_stats.call_nhl_sdk_misc.ping.return_value = APIResponse(
        ok=False, data={}, status_code=503
    )
    svc = Misc(mock_client)
    result = svc.ping()
    assert result is False
