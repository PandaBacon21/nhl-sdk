import pytest
pytestmark = pytest.mark.smoke


# ==========================================================================
# PICKS
# ==========================================================================

def test_smoke_picks_now(nhl) -> None:
    result = nhl.draft.picks.get_picks()

    assert result is not None
    assert result.draft_year is not None
    assert result.state is not None
    assert len(result.selectable_rounds) > 0
    assert len(result.picks) > 0
    print(f"Draft year: {result.draft_year} | State: {result.state} | Rounds: {result.selectable_rounds}")

    p = result.picks[0]
    print(f"  Pick #{p.overall_pick} (R{p.round}): {p.first_name} {p.last_name} ({p.position_code}, {p.country_code}) → {p.team_abbrev}")
    print(f"    Club: {p.amateur_club_name} ({p.amateur_league}) | {p.height}\" {p.weight}lbs")
    print(f"    Pick history: {p.team_pick_history}")


def test_smoke_picks_cache(nhl) -> None:
    result1 = nhl.draft.picks.get_picks()
    result2 = nhl.draft.picks.get_picks()
    assert result1 is result2


def test_smoke_picks_by_season_and_round(nhl) -> None:
    result = nhl.draft.picks.get_picks(season=2025, round="1")

    assert result is not None
    assert result.draft_year == 2025
    assert len(result.picks) > 0
    print(f"2025 Round 1 picks: {len(result.picks)}")

    for p in result.picks[:5]:
        print(f"  #{p.overall_pick}: {p.first_name} {p.last_name} ({p.position_code}) → {p.team_abbrev} | {p.amateur_club_name} ({p.amateur_league})")


def test_smoke_picks_all_rounds(nhl) -> None:
    result = nhl.draft.picks.get_picks(season=2025, round="all")

    assert result is not None
    assert result.draft_year == 2025
    assert len(result.picks) > 0
    print(f"2025 all rounds: {len(result.picks)} total picks")


# ==========================================================================
# TRACKER
# ==========================================================================

def test_smoke_tracker_now(nhl) -> None:
    result = nhl.draft.tracker.get_tracker_now()

    assert result is not None
    assert result.current_draft_date is not None
    assert result.state is not None
    print(f"Draft date: {result.current_draft_date} | Round: {result.round} | State: {result.state}")
    print(f"Broadcasts: {[b.network for b in result.tv_broadcasts]}")
    print(f"Picks: {len(result.picks)}")

    if result.picks:
        p = result.picks[0]
        print(f"  Pick #1 overall: {p.first_name} {p.last_name} ({p.position_code}) → {p.team_abbrev} ({p.state})")


def test_smoke_tracker_cache(nhl) -> None:
    result1 = nhl.draft.tracker.get_tracker_now()
    result2 = nhl.draft.tracker.get_tracker_now()
    assert result1 is result2


# ==========================================================================
# RANKINGS
# ==========================================================================

def test_smoke_rankings_now(nhl) -> None:
    result = nhl.draft.rankings.get_rankings()

    assert result is not None
    assert result.draft_year is not None
    assert len(result.draft_years) > 0
    assert len(result.categories) > 0
    assert len(result.rankings) > 0
    print(f"Draft year: {result.draft_year} | Category: {result.category_key}")
    print(f"Draft years available: {result.draft_years}")
    print(f"Categories: {[c.name for c in result.categories]}")

    p = result.rankings[0]
    print(f"#1 ({result.category_key}): {p.first_name} {p.last_name} | {p.position_code} | {p.last_amateur_club} ({p.last_amateur_league})")
    print(f"  Born: {p.birth_date} | {p.birth_city}, {p.birth_country} | {p.height_in_inches}\" {p.weight_in_pounds}lbs")


def test_smoke_rankings_cache(nhl) -> None:
    result1 = nhl.draft.rankings.get_rankings()
    result2 = nhl.draft.rankings.get_rankings()
    assert result1 is result2


def test_smoke_rankings_by_season_and_category(nhl) -> None:
    result = nhl.draft.rankings.get_rankings(season=2024, category=1)

    assert result is not None
    assert result.draft_year == 2024
    assert len(result.rankings) > 0
    print(f"2024 NA Skater rankings: {len(result.rankings)} prospects")

    for p in result.rankings[:5]:
        state = f", {p.birth_state_province}" if p.birth_state_province else ""
        rank = f"MT#{p.midterm_rank} → F#{p.final_rank}" if p.midterm_rank else f"F#{p.final_rank}"
        print(f"  {rank}: {p.first_name} {p.last_name} ({p.position_code}) — {p.last_amateur_club} | {p.birth_city}{state}, {p.birth_country}")
