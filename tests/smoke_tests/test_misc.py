import pytest
pytestmark = pytest.mark.smoke

GAME_ID = 2025020417  # VAN @ COL, 2025-12-02
POSTAL_CODE = "80202"  # Denver, CO


# ==========================================================================
# LOCATION
# ==========================================================================

def test_smoke_misc_location(nhl) -> None:
    result = nhl.misc.location()

    assert result is not None
    assert result.country_code is not None
    print(f"Detected country: {result.country_code}")


# ==========================================================================
# REFERENCE DATA
# ==========================================================================

def test_smoke_misc_countries(nhl) -> None:
    result = nhl.misc.countries

    assert result is not None
    assert len(result) > 0
    print(f"Countries: {len(result)}")

    ca = next((c for c in result if c.country_code == "CA"), None)
    assert ca is not None
    assert ca.country_name is not None
    assert ca.country3_code == "CAN"
    print(f"Canada: {ca.country_name} | 3-code: {ca.country3_code} | active: {ca.is_active}")


def test_smoke_misc_countries_cache(nhl) -> None:
    result1 = nhl.misc.countries
    result2 = nhl.misc.countries
    assert result1 is result2


def test_smoke_misc_franchises(nhl) -> None:
    result = nhl.misc.franchises

    assert result is not None
    assert len(result) > 0
    print(f"Franchises: {len(result)}")

    first = result[0]
    assert first.franchise_id is not None
    assert first.full_name is not None
    print(f"First franchise: [{first.franchise_id}] {first.full_name}")


def test_smoke_misc_franchises_cache(nhl) -> None:
    result1 = nhl.misc.franchises
    result2 = nhl.misc.franchises
    assert result1 is result2


def test_smoke_misc_glossary(nhl) -> None:
    result = nhl.misc.glossary

    assert result is not None
    assert len(result) > 0
    print(f"Glossary entries: {len(result)}")

    first = result[0]
    assert first.id is not None
    assert first.abbreviation is not None
    print(f"First entry: [{first.abbreviation}] {first.full_name}")


def test_smoke_misc_glossary_cache(nhl) -> None:
    result1 = nhl.misc.glossary
    result2 = nhl.misc.glossary
    assert result1 is result2


def test_smoke_misc_config(nhl) -> None:
    result = nhl.misc.config

    assert result is not None
    assert isinstance(result.player_report_data, dict)
    assert isinstance(result.goalie_report_data, dict)
    assert isinstance(result.team_report_data, dict)
    assert isinstance(result.aggregated_columns, list)
    assert isinstance(result.individual_columns, list)
    print(f"Player reports: {len(result.player_report_data)} | Goalie reports: {len(result.goalie_report_data)}")
    print(f"Team reports: {len(result.team_report_data)}")
    print(f"Aggregated columns: {len(result.aggregated_columns)} | Individual: {len(result.individual_columns)}")


def test_smoke_misc_config_cache(nhl) -> None:
    result1 = nhl.misc.config
    result2 = nhl.misc.config
    assert result1 is result2


def test_smoke_misc_ping(nhl) -> None:
    result = nhl.misc.ping()

    assert result is True
    print("Ping: OK")


# ==========================================================================
# SHIFTS (via games.get(game_id).shifts())
# ==========================================================================

def test_smoke_games_shifts(nhl) -> None:
    result = nhl.games.get(GAME_ID).shifts()

    assert result is not None
    assert result.game_id == GAME_ID
    assert result.total > 0
    assert len(result.shifts) > 0
    print(f"Shifts for game {GAME_ID}: {result.total} total")

    first = result.shifts[0]
    assert first.player_id is not None
    assert first.team_abbrev is not None
    assert first.period is not None
    assert first.start_time is not None
    print(f"First shift: {first.first_name} {first.last_name} ({first.team_abbrev}) "
          f"P{first.period} {first.start_time}–{first.end_time}")


def test_smoke_games_shifts_cache(nhl) -> None:
    result1 = nhl.games.get(GAME_ID).shifts()
    result2 = nhl.games.get(GAME_ID).shifts()
    assert result1 is result2
