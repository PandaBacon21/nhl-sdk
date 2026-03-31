import pytest
pytestmark = pytest.mark.smoke


# ==========================================================================
# CAROUSEL
# ==========================================================================

def test_smoke_carousel(nhl) -> None:
    result = nhl.playoffs.carousel.get_carousel(season=20242025)

    assert result is not None
    assert result.season_id == 20242025
    assert result.current_round is not None
    assert len(result.rounds) > 0
    print(f"Season: {result.season_id} | Current round: {result.current_round} | Rounds: {len(result.rounds)}")

    for rnd in result.rounds:
        print(f"  Round {rnd.round_number} ({rnd.round_abbrev}): {len(rnd.series)} series")
        for s in rnd.series:
            top = s.top_seed
            bot = s.bottom_seed
            winner = f"Winner: {s.winning_team_id}" if s.winning_team_id else "In progress"
            print(f"    {s.series_letter}: {top.abbrev} ({top.wins}) vs {bot.abbrev} ({bot.wins}) — {winner}")


def test_smoke_carousel_cache(nhl) -> None:
    result1 = nhl.playoffs.carousel.get_carousel(season=20242025)
    result2 = nhl.playoffs.carousel.get_carousel(season=20242025)
    assert result1 is result2


# ==========================================================================
# SERIES SCHEDULE
# ==========================================================================

def test_smoke_series_schedule(nhl) -> None:
    result = nhl.playoffs.series_schedule.get_series_schedule(season=20242025, series_letter="A")

    assert result is not None
    assert result.series_letter == "A"
    assert result.round is not None
    assert result.needed_to_win == 4
    assert result.top_seed_team is not None
    assert result.bottom_seed_team is not None
    assert len(result.games) > 0
    top = result.top_seed_team
    bot = result.bottom_seed_team
    print(f"Series A: {top.abbrev} ({top.series_wins}W) vs {bot.abbrev} ({bot.series_wins}W) — {result.length} games")
    print(f"  Top seed record: {top.record} | Conference: {top.conference.name}")

    g = result.games[0]
    print(f"  Game 1: {g.away_team.abbrev} @ {g.home_team.abbrev} | {g.start_time_utc} | {g.game_state}")


def test_smoke_series_schedule_cache(nhl) -> None:
    result1 = nhl.playoffs.series_schedule.get_series_schedule(season=20242025, series_letter="A")
    result2 = nhl.playoffs.series_schedule.get_series_schedule(season=20242025, series_letter="A")
    assert result1 is result2


# ==========================================================================
# BRACKET
# ==========================================================================

def test_smoke_bracket(nhl) -> None:
    result = nhl.playoffs.bracket.get_bracket(year=2024)

    assert result is not None
    assert result.bracket_logo is not None
    assert len(result.series) > 0
    print(f"Bracket logo: {result.bracket_logo}")
    print(f"Total series: {len(result.series)}")

    by_round: dict[int, list] = {}
    for s in result.series:
        by_round.setdefault(s.playoff_round, []).append(s)

    for rnd in sorted(by_round):
        series_list = by_round[rnd]
        print(f"  Round {rnd}: {len(series_list)} series")
        for s in series_list:
            top = s.top_seed_team
            bot = s.bottom_seed_team
            winner = f"→ {s.winning_team_id}" if s.winning_team_id else "TBD"
            print(f"    {s.series_letter} ({s.series_abbrev}): {top.abbrev} ({s.top_seed_wins}W) vs {bot.abbrev} ({s.bottom_seed_wins}W) {winner}")


def test_smoke_bracket_cache(nhl) -> None:
    result1 = nhl.playoffs.bracket.get_bracket(year=2024)
    result2 = nhl.playoffs.bracket.get_bracket(year=2024)
    assert result1 is result2
