import pytest
pytestmark = pytest.mark.smoke

DATE = "2026-03-29"


def test_smoke_league_schedule_now(nhl) -> None:
    result = nhl.league.get_schedule()

    assert result is not None
    assert len(result.game_week) > 0
    print(f"Previous week start: {result.previous_start_date} | Next: {result.next_start_date}")
    print(f"Days in response: {len(result.game_week)}")

    day = result.game_week[0]
    print(f"First day: {day.date} ({day.day_abbrev}) | Games: {day.number_of_games}")
    if day.games:
        g = day.games[0]
        print(f"  First game: {g.away_team.abbrev} @ {g.home_team.abbrev} | state: {g.game_state}")
        print(f"  Start UTC: {g.start_time_utc} | Venue: {g.venue.default}")


def test_smoke_league_schedule_with_date(nhl) -> None:
    result = nhl.league.get_schedule(date=DATE)

    assert result is not None
    assert len(result.game_week) > 0
    print(f"Schedule for {DATE} — days: {len(result.game_week)}")

    for day in result.game_week:
        total_broadcasts = sum(len(g.tv_broadcasts) for g in day.games)
        print(f"  {day.date} ({day.day_abbrev}): {day.number_of_games} games | broadcasts: {total_broadcasts}")


def test_smoke_league_schedule_cache(nhl) -> None:
    result1 = nhl.league.get_schedule(date=DATE)
    result2 = nhl.league.get_schedule(date=DATE)
    assert result1 is result2


def test_smoke_league_schedule_calendar_now(nhl) -> None:
    result = nhl.league.get_schedule_calendar()

    assert result is not None
    assert len(result.teams) > 0
    print(f"Window: {result.start_date} → {result.end_date}")
    print(f"Previous: {result.previous_start_date} | Next: {result.next_start_date}")
    print(f"Teams playing: {len(result.teams)}")

    t = result.teams[0]
    print(f"First team: {t.name.default} ({t.abbrev}) | Season: {t.season_id} | French: {t.french}")


def test_smoke_league_schedule_calendar_with_date(nhl) -> None:
    result = nhl.league.get_schedule_calendar(date=DATE)

    assert result is not None
    assert len(result.teams) > 0
    print(f"Calendar for {DATE} — teams: {len(result.teams)}")
    abbrevs = [t.abbrev for t in result.teams]
    print(f"  Abbrevs: {abbrevs}")


def test_smoke_league_calendar_cache(nhl) -> None:
    result1 = nhl.league.get_schedule_calendar(date=DATE)
    result2 = nhl.league.get_schedule_calendar(date=DATE)
    assert result1 is result2


def test_smoke_league_seasons(nhl) -> None:
    result = nhl.league.get_seasons()

    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(s, int) for s in result)
    assert 19171918 in result
    assert 20252026 in result
    print(f"Total seasons: {len(result)}")
    print(f"First: {result[0]} | Last: {result[-1]}")


def test_smoke_league_seasons_cache(nhl) -> None:
    result1 = nhl.league.get_seasons()
    result2 = nhl.league.get_seasons()
    assert result1 is result2
