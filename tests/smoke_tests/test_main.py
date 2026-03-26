from src.client import NhlClient

PID = 8477492  # Nathan MacKinnon


def _client() -> NhlClient:
    return NhlClient()


# ==========================================================================
# PROFILE
# ==========================================================================

def test_smoke_profile() -> None:
    nhl = _client()
    player = nhl.players.get(pid=PID)

    assert player.profile.first_name == "Nathan"
    assert player.profile.last_name == "MacKinnon"

    print(player)
    print(f"First name: {player.profile.first_name}")
    print(f"Last name: {player.profile.last_name}")
    print(f"Current team: {player.profile.team}")
    print(f"Weight: {player.profile.weight.weight_lbs}")
    print(f"Height: {player.profile.height}")
    print(f"Draft year: {player.profile.draft.year}")
    print(f"Birth city: {player.profile.birth_details.city}")
    print(f"Birth state/province: {player.profile.birth_details.state_province}")
    print(f"In HHOF: {player.profile.legacy.in_HHOF}")
    print(f"In top 100 all time: {player.profile.legacy.in_top_100_all_time}")
    print(f"Is active: {player.profile.is_active}")
    print(f"Headshot: {player.profile.media.headshot}")
    print(f"Slug: {player.profile.media.slug}")
    print("")
    print("Badges:")
    for badge in player.profile.legacy.badges:
        print(badge)
    print("")
    print("Awards:")
    for award in player.profile.legacy.awards:
        print(award)


# ==========================================================================
# STATS
# ==========================================================================

def test_smoke_stats() -> None:
    nhl = _client()
    player = nhl.players.get(pid=PID)
    stats = player.stats

    assert stats.featured is not None
    assert stats.career is not None
    assert len(stats.seasons) > 0
    assert len(stats.last_5_games) > 0

    print(f"Featured season assists: {stats.featured.season_stats.assists}")
    print(f"Career goals: {stats.career.regular_season.goals}")
    print(f"Career stats: {stats.career.regular_season.to_dict()}")
    print("")
    print("Last 5 games:")
    for game in stats.last_5_games:
        print(f"  {game.game_date} | game: {game.game_id} | toi: {game.toi} | pts: {game.points}")
    print("")
    print("NHL seasons:")
    for season in stats.seasons:
        if season.league == "NHL":
            game_type = {2: "Regular Season", 3: "Playoffs"}.get(season.game_type_id, str(season.game_type_id)) # type: ignore[call-overload]
            print(f"  {season.season} | {game_type} | G: {season.stats.goals} | PPP: {season.stats.pp_points}")


# ==========================================================================
# GAME LOG
# ==========================================================================

def test_smoke_game_log() -> None:
    nhl = _client()
    player = nhl.players.get(pid=PID)

    game_log = player.stats.game_log()
    game_log_2324 = player.stats.game_log(season=20232024, game_type=2)

    assert game_log is not None
    assert len(game_log.games) > 0
    assert game_log_2324 is not None
    assert len(game_log_2324.games) > 0

    print(f"Current season: {game_log.season_id}")
    print(f"2023-24 game type: {game_log_2324.game_type}")
    print(f"First game id (current): {game_log.games[0].game_id}")
    print(f"First game id (2023-24): {game_log_2324.games[0].game_id}")
    print("")
    print("Current season games:")
    for game in game_log.games:
        print(f"  vs {game.opponent_abbrev} | G: {game.goals}")
    print("")
    print("Seasons with playoffs:")
    for season in game_log.seasons:
        if season.playoffs:
            print(f"  {season.season}")


# ==========================================================================
# SPOTLIGHT + LEADERS
# ==========================================================================

def test_smoke_spotlight() -> None:
    nhl = _client()
    spotlight = nhl.players.spotlight

    assert len(spotlight) > 0
    print(f"1st spotlighted player: {spotlight[0].name}")
    print(f"2nd spotlighted player: {spotlight[1].name}")


def test_smoke_leaders() -> None:
    nhl = _client()
    leaders = nhl.players.leaders

    goalie_leaders = leaders.goalies(season=20242025, game_type=2, categories="wins", limit=10)
    assert goalie_leaders.wins is not None
    assert len(goalie_leaders.wins) > 0
    print(f"Goalie wins leader: {goalie_leaders.wins[0].last_name} (pid: {goalie_leaders.wins[0].pid})")
    print(f"Save pct leaders: {goalie_leaders.save_pctg}")

    skater_leaders = leaders.skaters()
    assert skater_leaders.goals is not None
    assert len(skater_leaders.goals) > 0
    print(f"Current goals leader: {skater_leaders.goals[0].last_name}")
    print(f"Current assists leader: {skater_leaders.assists[0].last_name}")

    edge_landing = skater_leaders.edge.landing()
    assert edge_landing is not None
    print(f"Edge seasons: {edge_landing.seasons_with_edge[0].id}")
    print(f"Hardest shot leader: {edge_landing.leaders.hardest_shot.player.last_name}")


# ==========================================================================
# EDGE SKATER
# ==========================================================================

def test_smoke_edge_skater_details() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    details = edge.details()
    assert details is not None
    assert len(details.seasons_with_edge) > 0
    print(f"Edge seasons: {[s.id for s in details.seasons_with_edge]}")
    print(f"Top shot speed (imperial): {details.top_shot_speed.imperial}")
    print(f"Top shot speed percentile: {details.top_shot_speed.percentile}")
    print(f"Total distance skated (imperial): {details.total_distance_skated.imperial}")
    print(f"Zone time - offensive %: {details.zone_time.offensive_zone_pctg}")

    # verify cache — same object returned on second call
    details_2425 = edge.details(season=20242025, game_type=2)
    assert edge.details(season=20242025, game_type=2) is details_2425
    print(f"2024-25 seasons_with_edge count: {len(details_2425.seasons_with_edge)}")


def test_smoke_edge_skater_comparison() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    comparison = edge.comparison()
    assert comparison is not None
    assert len(comparison.seasons_with_edge) > 0
    print(f"Top shot speed (imperial): {comparison.shot_speed.top_shot_speed.imperial}")
    print(f"Max skating speed (imperial): {comparison.skating_speed.max_skating_speed.imperial}")
    print(f"Zone time - offensive %: {comparison.zone_time.offensive_zone_pctg}")
    print(f"Skating distance last 10 count: {len(comparison.skating_distance_last_10)}")


def test_smoke_edge_skater_skating_distance() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    distance = edge.skating_distance()
    assert distance is not None
    assert isinstance(distance.last_10_games, list)
    assert isinstance(distance.distance_by_strength, list)
    print(f"Last 10 games count: {len(distance.last_10_games)}")
    if distance.last_10_games:
        print(f"First game distance (all imperial): {distance.last_10_games[0].distance_skated_all.imperial}")
    print(f"Distance by strength count: {len(distance.distance_by_strength)}")


def test_smoke_edge_skater_skating_speed() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    speed = edge.skating_speed()
    assert speed is not None
    print(f"Max skating speed (imperial): {speed.speed_summary.max_skating_speed.imperial}")
    print(f"Bursts over 22 mph: {speed.speed_summary.bursts_over_22.value}")
    print(f"Top speed instances count: {len(speed.top_speeds)}")
    if speed.top_speeds:
        print(f"Fastest: {speed.top_speeds[0].skating_speed.imperial} on {speed.top_speeds[0].game_date}")


def test_smoke_edge_skater_zone_time() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    zone = edge.zone_time()
    assert zone is not None
    assert len(zone.zone_time_by_strength) > 0
    print(f"Zone time by strength count: {len(zone.zone_time_by_strength)}")
    print(f"Offensive zone starts %: {zone.zone_starts.offensive_zone_starts_pctg}")
    print(f"Defensive zone starts %: {zone.zone_starts.defensive_zone_starts_pctg}")


def test_smoke_edge_skater_shot_speed() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    shot_spd = edge.shot_speed()
    assert shot_spd is not None
    print(f"Top shot speed (imperial): {shot_spd.speed_summary.top_shot_speed.imperial}")
    print(f"Avg shot speed (imperial): {shot_spd.speed_summary.avg_shot_speed.imperial}")
    print(f"Shot attempts over 100 mph: {shot_spd.speed_summary.shot_attempts_over_100.value}")
    if shot_spd.hardest_shots:
        print(f"Hardest shot game date: {shot_spd.hardest_shots[0].game_date}")


def test_smoke_edge_skater_shot_location() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    shot_loc = edge.shot_location()
    assert shot_loc is not None
    assert len(shot_loc.area_details) > 0
    print(f"Area count: {len(shot_loc.area_details)}")
    print(f"First area: {shot_loc.area_details[0].area} | SOG: {shot_loc.area_details[0].sog}")
    print(f"Zone totals count: {len(shot_loc.zone_totals)}")


def test_smoke_edge_skater_cat_details() -> None:
    nhl = _client()
    edge = nhl.players.get(pid=PID).stats.edge.skater

    cat = edge.cat_details()
    assert cat is not None
    cat_dict = cat.to_dict()
    print(f"Cat details: {cat_dict}")


# ==========================================================================
# TEAMS — STANDINGS
# ==========================================================================

TEAM_CODE = "COL"


def test_smoke_standings() -> None:
    nhl = _client()
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


def test_smoke_standings_by_season() -> None:
    nhl = _client()
    result = nhl.teams.standings.get_standings_by_season()

    assert result is not None
    print(f"Seasons with standings: {result}")


# ==========================================================================
# TEAMS — STATS
# ==========================================================================

def test_smoke_team_stats() -> None:
    nhl = _client()
    result = nhl.teams.stats.get_team_stats(team=TEAM_CODE)

    assert result is not None
    assert len(result.skaters) > 0
    assert len(result.goalies) > 0
    print(f"Season: {result.season} | Game type: {result.game_type}")
    print(f"Skaters: {len(result.skaters)} | Goalies: {len(result.goalies)}")

    top_skater = result.skaters[0]
    print(f"First skater: {top_skater.last_name.default} | Pts: {top_skater.points} | GP: {top_skater.games_played}")

    top_goalie = result.goalies[0]
    print(f"First goalie: {top_goalie.last_name.default} | W: {top_goalie.wins} | SV%: {top_goalie.save_percentage}")

    result_2324 = nhl.teams.stats.get_team_stats(team=TEAM_CODE, season=20232024, g_type=2)
    assert result_2324 is not None
    assert len(result_2324.skaters) > 0
    print(f"2023-24 season: {result_2324.season} | Skaters: {len(result_2324.skaters)}")


def test_smoke_team_game_types_per_season() -> None:
    nhl = _client()
    result = nhl.teams.stats.get_game_types_per_season(team=TEAM_CODE)

    assert result is not None
    assert len(result) > 0
    print(f"Seasons available: {len(result)}")
    print(f"Most recent: {result[0].season} | Game types: {result[0].game_types}")


def test_smoke_team_scoreboard() -> None:
    nhl = _client()
    result = nhl.teams.stats.get_team_scoreboard(team=TEAM_CODE)

    assert result is not None
    print(f"Focused date: {result.focused_date}")
    print(f"Club timezone: {result.club_time_zone}")
    print(f"Schedule link: {result.club_schedule_link}")
    print(f"Dates with games: {len(result.games_by_date)}")
    for gbd in result.games_by_date:
        for game in gbd.games:
            print(f"  {gbd.date}: {game.away_team.abbrev} @ {game.home_team.abbrev} | state: {game.game_state}")


if __name__ == "__main__":
    test_smoke_profile()
    test_smoke_stats()
    test_smoke_game_log()
    test_smoke_spotlight()
    test_smoke_leaders()
    test_smoke_edge_skater_details()
    test_smoke_edge_skater_comparison()
    test_smoke_edge_skater_skating_distance()
    test_smoke_edge_skater_skating_speed()
    test_smoke_edge_skater_zone_time()
    test_smoke_edge_skater_shot_speed()
    test_smoke_edge_skater_shot_location()
    test_smoke_edge_skater_cat_details()
    test_smoke_standings()
    test_smoke_standings_by_season()
    test_smoke_team_stats()
    test_smoke_team_game_types_per_season()
    test_smoke_team_scoreboard()
