PID = 8477492  # Nathan MacKinnon


# ==========================================================================
# PROFILE
# ==========================================================================

def test_smoke_profile(nhl) -> None:
    player = nhl.players.get(pid=PID)

    assert player.profile.first_name == "Nathan"
    assert player.profile.last_name == "MacKinnon"

    print(player)
    print(f"First name: {player.profile.first_name}")
    print(f"Last name: {player.profile.last_name}")
    print(f"Current team: {player.profile.team}")
    print(f"Weight: {player.profile.weight_in_pounds}")
    print(f"Height: {player.profile.height_in_inches}")
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

def test_smoke_stats(nhl) -> None:
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

def test_smoke_game_log(nhl) -> None:
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
