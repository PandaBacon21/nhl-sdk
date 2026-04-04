import pytest
pytestmark = pytest.mark.smoke

TEAM_CODE = "COL"


# ==========================================================================
# STANDINGS
# ==========================================================================

def test_smoke_standings(nhl) -> None:
    result = nhl.teams.standings.get_standings()

    assert result is not None
    assert len(result.standings) > 0
    print(f"Standings date: {result.standings_date_time_utc}")
    print(f"Wild card indicator: {result.wild_card_indicator}")
    print(f"Total teams: {len(result.standings)}")

    entry = result.standings[0]
    print(f"First team: {entry.team.name.default} ({entry.team.abbrev})")
    print(f"Points: {entry.record.points} | W: {entry.record.wins} | L: {entry.record.losses} | OTL: {entry.record.ot_losses}")
    print(f"Home: {entry.home.wins}-{entry.home.losses}-{entry.home.ot_losses}")
    print(f"Road: {entry.road.wins}-{entry.road.losses}-{entry.road.ot_losses}")
    print(f"L10: {entry.l10.wins}-{entry.l10.losses}-{entry.l10.ot_losses}")
    print(f"League sequence: {entry.sequences.league}")


def test_smoke_standings_by_season(nhl) -> None:
    result = nhl.teams.standings.get_standings_by_season()

    assert result is not None
    print(f"Seasons with standings: {result}")


# ==========================================================================
# STATS
# ==========================================================================

def test_smoke_team_stats(nhl) -> None:
    team = nhl.teams.get(TEAM_CODE)
    result = team.stats.get_team_stats()

    assert result is not None
    assert len(result.skaters) > 0
    assert len(result.goalies) > 0
    print(f"Season: {result.season} | Game type: {result.game_type}")
    print(f"Skaters: {len(result.skaters)} | Goalies: {len(result.goalies)}")

    top_skater = result.skaters[0]
    print(f"First skater: {top_skater.last_name.default} | Pts: {top_skater.points} | GP: {top_skater.games_played}")

    top_goalie = result.goalies[0]
    print(f"First goalie: {top_goalie.last_name.default} | W: {top_goalie.wins} | SV%: {top_goalie.save_percentage}")

    result_2324 = team.stats.get_team_stats(season=20232024, g_type=2)
    assert result_2324 is not None
    assert len(result_2324.skaters) > 0
    print(f"2023-24 season: {result_2324.season} | Skaters: {len(result_2324.skaters)}")


def test_smoke_team_game_types_per_season(nhl) -> None:
    result = nhl.teams.get(TEAM_CODE).stats.get_game_types_per_season()

    assert result is not None
    assert len(result) > 0
    print(f"Seasons available: {len(result)}")
    print(f"Most recent: {result[0].season} | Game types: {result[0].game_types}")


def test_smoke_team_scoreboard(nhl) -> None:
    result = nhl.teams.get(TEAM_CODE).stats.get_team_scoreboard()

    assert result is not None
    print(f"Focused date: {result.focused_date}")
    print(f"Club timezone: {result.club_time_zone}")
    print(f"Schedule link: {result.club_schedule_link}")
    print(f"Dates with games: {len(result.games_by_date)}")
    for gbd in result.games_by_date:
        for game in gbd.games:
            print(f"  {gbd.date}: {game.away_team.abbrev} @ {game.home_team.abbrev} | game state: {game.game_state}")


# ==========================================================================
# ROSTER
# ==========================================================================

def test_smoke_roster_seasons(nhl) -> None:
    seasons = nhl.teams.get(TEAM_CODE).roster.get_roster_seasons()

    assert isinstance(seasons, list)
    assert len(seasons) > 0
    assert all(isinstance(s, int) for s in seasons)
    print(f"Roster seasons available: {len(seasons)}")
    print(f"Most recent: {seasons[0]} | Oldest: {seasons[-1]}")


def test_smoke_team_roster(nhl) -> None:
    team = nhl.teams.get(TEAM_CODE)
    result = team.roster.get_team_roster()

    assert result is not None
    assert len(result.forwards) > 0
    assert len(result.defensemen) > 0
    assert len(result.goalies) > 0
    print(f"Forwards: {len(result.forwards)} | Defensemen: {len(result.defensemen)} | Goalies: {len(result.goalies)}")

    f = result.forwards[0]
    print(f"First forward: {f.first_name.default} {f.last_name.default} | #{f.sweater_number} | {f.position_code}")
    print(f"  Height: {f.height_in_inches}in | Weight: {f.weight_in_pounds}lbs")
    print(f"  Birth: {f.birth_details.birth_date} | {f.birth_details.city.default}, {f.birth_details.country}")

    result_2324 = team.roster.get_team_roster(season=20232024)
    assert result_2324 is not None
    assert len(result_2324.forwards) > 0
    print(f"2023-24 forwards: {len(result_2324.forwards)}")


def test_smoke_team_prospects(nhl) -> None:
    result = nhl.teams.get(TEAM_CODE).roster.get_team_prospects()

    assert result is not None
    assert len(result.forwards) + len(result.defensemen) + len(result.goalies) > 0
    print(f"Prospects — Forwards: {len(result.forwards)} | Defensemen: {len(result.defensemen)} | Goalies: {len(result.goalies)}")
    if result.forwards:
        p = result.forwards[0]
        print(f"First prospect: {p.first_name.default} {p.last_name.default} | {p.position_code}")


# ==========================================================================
# SCHEDULE
# ==========================================================================

def test_smoke_schedule(nhl) -> None:
    team = nhl.teams.get(TEAM_CODE)
    result = team.schedule.get_schedule()

    assert result is not None
    assert len(result.games) > 0
    print(f"Season: {result.current_season} | Games: {len(result.games)}")
    print(f"Club timezone: {result.club_timezone}")
    g = result.games[0]
    print(f"First game: {g.game_date} | {g.away_team.abbrev} @ {g.home_team.abbrev} | state: {g.game_state}")

    result_2324 = team.schedule.get_schedule(season=20232024)
    assert result_2324 is not None
    assert len(result_2324.games) > 0
    print(f"2023-24 games: {len(result_2324.games)}")


def test_smoke_schedule_month(nhl) -> None:
    team = nhl.teams.get(TEAM_CODE)
    result = team.schedule.get_schedule_month()

    assert result is not None
    assert result.current_month is not None
    print(f"Current month: {result.current_month} | Games: {len(result.games)}")
    print(f"Previous: {result.previous_month} | Next: {result.next_month}")
    if result.games:
        g = result.games[0]
        print(f"First game: {g.game_date} | {g.away_team.abbrev} @ {g.home_team.abbrev}")

    result_specific = team.schedule.get_schedule_month(month="2024-11")
    assert result_specific is not None
    assert len(result_specific.games) > 0
    print(f"Nov 2024 games: {len(result_specific.games)}")


def test_smoke_schedule_week(nhl) -> None:
    team = nhl.teams.get(TEAM_CODE)
    result = team.schedule.get_schedule_week()

    assert result is not None
    print(f"Previous week start: {result.previous_start_date} | Next: {result.next_start_date}")
    print(f"Games this week: {len(result.games)}")
    if result.games:
        g = result.games[0]
        print(f"First game: {g.game_date} | {g.away_team.abbrev} @ {g.home_team.abbrev} | state: {g.game_state}")
        if g.tickets_link:
            print(f"  Tickets: {g.tickets_link}")

    result_specific = team.schedule.get_schedule_week(week="2024-11-04")
    assert result_specific is not None
    assert len(result_specific.games) > 0
    print(f"Week of 2024-11-04 games: {len(result_specific.games)}")
