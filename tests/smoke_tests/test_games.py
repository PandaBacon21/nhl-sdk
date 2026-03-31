import pytest
pytestmark = pytest.mark.smoke

DATE = "2026-03-25"
SCORE_DATE = "2026-03-29"


# ==========================================================================
# NETWORK
# ==========================================================================

def test_smoke_network_tv_schedule_now(nhl) -> None:
    result = nhl.games.network.get_tv_schedule()

    assert result is not None
    assert result.date is not None
    assert len(result.broadcasts) > 0
    print(f"Date: {result.date} | Window: {result.start_date} → {result.end_date}")
    print(f"Broadcasts: {len(result.broadcasts)}")

    b = result.broadcasts[0]
    print(f"First: {b.start_time} — {b.title} | status: {b.broadcast_status}")


def test_smoke_network_tv_schedule_with_date(nhl) -> None:
    result = nhl.games.network.get_tv_schedule(date=DATE)

    assert result is not None
    assert result.date == DATE
    assert len(result.broadcasts) > 0
    print(f"Broadcasts for {DATE}: {len(result.broadcasts)}")

    live = [b for b in result.broadcasts if b.broadcast_status == "LIVE"]
    games = [b for b in result.broadcasts if b.title == "NHL Game"]
    print(f"  LIVE: {len(live)} | NHL Games: {len(games)}")
    for b in result.broadcasts[:3]:
        print(f"  {b.start_time} — {b.title} ({b.duration_seconds}s) | status: {b.broadcast_status!r}")


def test_smoke_network_tv_schedule_cache(nhl) -> None:
    result1 = nhl.games.network.get_tv_schedule(date=DATE)
    result2 = nhl.games.network.get_tv_schedule(date=DATE)
    assert result1 is result2


# ==========================================================================
# SCORES
# ==========================================================================

def test_smoke_daily_scores_now(nhl) -> None:
    result = nhl.games.scores.get_daily_scores()

    assert result is not None
    assert result.current_date is not None
    print(f"Date: {result.current_date} | Prev: {result.prev_date} | Next: {result.next_date}")
    print(f"Game week days: {len(result.game_week)} | Games today: {len(result.games)}")
    print(f"Odds partners: {len(result.odds_partners)}")

    for day in result.game_week:
        print(f"  {day.date} ({day.day_abbrev}): {day.number_of_games} games")

    if result.games:
        g = result.games[0]
        print(f"First game: {g.away_team.abbrev} @ {g.home_team.abbrev} | state: {g.game_state}")
        print(f"  Score: {g.away_team.score}-{g.home_team.score} | Period: {g.period}")
        if g.clock:
            print(f"  Clock: {g.clock.time_remaining} | Running: {g.clock.running}")


def test_smoke_daily_scores_with_date(nhl) -> None:
    result = nhl.games.scores.get_daily_scores(date=SCORE_DATE)

    assert result is not None
    assert result.current_date == SCORE_DATE
    assert len(result.games) > 0
    print(f"Scores for {SCORE_DATE}: {len(result.games)} games")

    for g in result.games:
        total_goals = len(g.goals)
        print(f"  {g.away_team.abbrev} {g.away_team.score} @ {g.home_team.abbrev} {g.home_team.score} | goals: {total_goals} | outcome: {g.game_outcome.last_period_type if g.game_outcome else 'N/A'}")

        if g.goals:
            goal = g.goals[0]
            assist_names = [a.name.default for a in goal.assists]
            print(f"    First goal: {goal.name.default} ({goal.strength}) — assists: {assist_names}")


def test_smoke_daily_scores_cache(nhl) -> None:
    result1 = nhl.games.scores.get_daily_scores(date=SCORE_DATE)
    result2 = nhl.games.scores.get_daily_scores(date=SCORE_DATE)
    assert result1 is result2


# ==========================================================================
# SCOREBOARD
# ==========================================================================

def test_smoke_scoreboard_now(nhl) -> None:
    result = nhl.games.scoreboard.get_scoreboard()

    assert result is not None
    assert result.focused_date is not None
    assert result.focused_date_count is not None
    print(f"Focused: {result.focused_date} | Count: {result.focused_date_count}")
    print(f"Days in scoreboard: {len(result.games_by_date)}")

    for day in result.games_by_date:
        print(f"  {day.date}: {len(day.games)} games")

    if result.games_by_date and result.games_by_date[0].games:
        g = result.games_by_date[0].games[0]
        print(f"First game: {g.away_team.abbrev} @ {g.home_team.abbrev} | state: {g.game_state}")
        print(f"  Score: {g.away_team.score}-{g.home_team.score} | Period: {g.period}")
        print(f"  Away full: {g.away_team.name.default} ({g.away_team.common_name.default})")


def test_smoke_scoreboard_cache(nhl) -> None:
    result1 = nhl.games.scoreboard.get_scoreboard()
    result2 = nhl.games.scoreboard.get_scoreboard()
    assert result1 is result2


# ==========================================================================
# PLAY-BY-PLAY
# ==========================================================================

GAME_ID = 2025020417  # VAN @ COL, 2025-12-02


def test_smoke_pbp(nhl) -> None:
    result = nhl.games.pbp.get_play_by_play(game_id=GAME_ID)

    assert result is not None
    assert result.id == GAME_ID
    assert result.game_date is not None
    assert result.away_team is not None
    assert result.home_team is not None
    assert isinstance(result.plays, list)
    print(f"Game: {result.away_team.abbrev} @ {result.home_team.abbrev} | {result.game_date}")
    print(f"Score: {result.away_team.score}-{result.home_team.score} | state: {result.game_state}")
    print(f"Plays: {len(result.plays)}")

    if result.plays:
        p = result.plays[0]
        print(f"First play: [{p.type_desc_key}] period {p.period_descriptor.number if p.period_descriptor else '?'} @ {p.time_in_period}")


def test_smoke_pbp_cache(nhl) -> None:
    result1 = nhl.games.pbp.get_play_by_play(game_id=GAME_ID)
    result2 = nhl.games.pbp.get_play_by_play(game_id=GAME_ID)
    assert result1 is result2


# ==========================================================================
# LANDING
# ==========================================================================

def test_smoke_landing(nhl) -> None:
    result = nhl.games.landing.get_landing(game_id=GAME_ID)

    assert result is not None
    assert result.id == GAME_ID
    assert result.game_date is not None
    assert result.away_team is not None
    assert result.home_team is not None
    print(f"Game: {result.away_team.abbrev} @ {result.home_team.abbrev} | {result.game_date}")
    print(f"Score: {result.away_team.score}-{result.home_team.score} | state: {result.game_state}")

    if result.summary:
        total_goals = sum(len(sp.goals) for sp in result.summary.scoring)
        print(f"Goals: {total_goals} | 3 stars: {len(result.summary.three_stars)}")

        if result.summary.three_stars:
            star1 = result.summary.three_stars[0]
            print(f"1st star: {star1.name.default} ({star1.team_abbrev}) — {star1.points}pts")


def test_smoke_landing_cache(nhl) -> None:
    result1 = nhl.games.landing.get_landing(game_id=GAME_ID)
    result2 = nhl.games.landing.get_landing(game_id=GAME_ID)
    assert result1 is result2


# ==========================================================================
# BOXSCORE
# ==========================================================================

BOXSCORE_GAME_ID = 2025020691  # OTT @ COL, 2026-01-08


def test_smoke_boxscore(nhl) -> None:
    result = nhl.games.boxscore.get_boxscore(game_id=BOXSCORE_GAME_ID)

    assert result is not None
    assert result.id == BOXSCORE_GAME_ID
    assert result.game_date is not None
    assert result.away_team is not None
    assert result.home_team is not None
    print(f"Game: {result.away_team.abbrev} @ {result.home_team.abbrev} | {result.game_date}")
    print(f"Score: {result.away_team.score}-{result.home_team.score}")

    if result.player_by_game_stats:
        home = result.player_by_game_stats.home_team
        away = result.player_by_game_stats.away_team
        print(f"Home: {len(home.forwards)}F {len(home.defense)}D {len(home.goalies)}G")
        print(f"Away: {len(away.forwards)}F {len(away.defense)}D {len(away.goalies)}G")

        if home.goalies:
            g = home.goalies[0]
            print(f"Home starter: {g.name.default} | {g.saves}/{g.shots_against} | decision: {g.decision}")


def test_smoke_boxscore_cache(nhl) -> None:
    result1 = nhl.games.boxscore.get_boxscore(game_id=BOXSCORE_GAME_ID)
    result2 = nhl.games.boxscore.get_boxscore(game_id=BOXSCORE_GAME_ID)
    assert result1 is result2


# ==========================================================================
# STORY
# ==========================================================================

def test_smoke_story(nhl) -> None:
    result = nhl.games.story.get_game_story(game_id=GAME_ID)

    assert result is not None
    assert result.id == GAME_ID
    assert result.game_date is not None
    assert result.away_team is not None
    assert result.home_team is not None
    print(f"Game: {result.away_team.abbrev} @ {result.home_team.abbrev} | {result.game_date}")
    print(f"Score: {result.away_team.score}-{result.home_team.score} | state: {result.game_state}")

    if result.summary:
        total_goals = sum(len(sp.goals) for sp in result.summary.scoring)
        print(f"Goals: {total_goals} | 3 stars: {len(result.summary.three_stars)}")
        print(f"Team stats: {len(result.summary.team_game_stats)} categories")

        if result.summary.three_stars:
            star1 = result.summary.three_stars[0]
            print(f"1st star: {star1.name} ({star1.team_abbrev}) — {star1.points}pts")


def test_smoke_story_cache(nhl) -> None:
    result1 = nhl.games.story.get_game_story(game_id=GAME_ID)
    result2 = nhl.games.story.get_game_story(game_id=GAME_ID)
    assert result1 is result2


# ==========================================================================
# PARTNER ODDS
# ==========================================================================

def test_smoke_odds_us(nhl) -> None:
    result = nhl.games.odds.get_odds(country_code="US")

    assert result is not None
    assert result.current_odds_date is not None
    assert result.last_updated_utc is not None
    print(f"Odds date: {result.current_odds_date} | Updated: {result.last_updated_utc}")
    print(f"Games with odds: {len(result.games)}")

    # Canary: this endpoint currently returns no games regardless of country.
    # If this assertion starts failing, the API is now returning real odds data
    # and the games structure should be modelled properly.
    assert result.games == [], (
        f"Partner odds API returned {len(result.games)} games — "
        "the endpoint appears to be active. Model the game structure in PartnerOddsResult."
    )


def test_smoke_odds_cache(nhl) -> None:
    result1 = nhl.games.odds.get_odds(country_code="US")
    result2 = nhl.games.odds.get_odds(country_code="US")
    assert result1 is result2
