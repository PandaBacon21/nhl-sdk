from nhl_stats.client import NhlClient



# Currently only for testing purposes
def main() -> None: 
    nhl = NhlClient()
    players = nhl.players

    player = players.get(pid=8477492) # MacKinnon
    # player = players.get(pid=8478550) # Panarin
    # player = players.get(pid=8451101) # Sakic

    """BIO TESTING"""
    print(player)
    print(f"Player first name: {player.bio.first_name}")
    print(f"Player last name: {player.bio.last_name}")
    print(f"Current Team: {player.bio.team}")
    print(f"Weight: {player.bio.weight.weight_lbs}")
    print(f"Height: {player.bio.height}")
    print(f"Player draft year: {player.bio.draft.year}")
    print(f"Player home city: {player.bio.birth_details.city}")
    print(f"Player home state/Province: {player.bio.birth_details.state_province}")
    print(f"In Hockey Hall of Fame: {player.bio.legacy.in_HHOF}")
    print(f"In top 100 All Time: {player.bio.legacy.in_top_100_all_time}")
    print(f"Is actively playing: {player.bio.is_active}")
    print(f"Player headshot: {player.bio.media.headshot}")
    print(f"Player Slug: {player.bio.media.slug}")
    print("")
    badges = player.bio.legacy.badges
    print("Player Badges:")
    for badge in badges: 
        print(badge)
    awards = player.bio.legacy.awards
    print("")
    print("Player Awards:")
    for award in awards:
        print(award)
    print("")

    """STATS TESTING"""
    player_stats = player.stats
    featured_stats = player_stats.featured
    career_stats = player_stats.career
    last_five_games = player_stats.last_5_games

    print("")
    print(f"Featured Season Assists: {featured_stats.season_stats.assists}")
    print("")
    print("Career stats to dict: ")
    print(career_stats.regular_season.to_dict())
    print("")
    print(f"Career goals: {career_stats.regular_season.goals}")
    print("")
    print("Last 5 games: ")
    for game in last_five_games: 
        print(f"Data: {game.game_date}, Game: {game.game_id}")
        print(f"Time on ice: {game.toi}")
        print(f"Points: {game.points}")

    print("")
    for season in player_stats.seasons:
        if season.league == "NHL": 
            print(f"Season: {season.season}, League: {season.league}")
            if season.game_type == 2: 
                print("Game type: Regular Season")
            elif season.game_type == 3: 
                print("Game type: Playoffs")
            else: 
                print(f"Game type: {season.game_type}")
            print(f"Goals: {season.stats.goals}")
            print(f"PowerPlay Points: {season.stats.pp_points}")
            print("")

    # print(player.raw())
    # player.refresh()
    # print(player.bio.first_name)
    # # print(player.bio.last_name)

    game_log = player.stats.game_log()
    game_log_2 = player.stats.game_log(season=20232024, game_type=2)
    # print(game_log)
    print(f"Game Log - Season: {game_log.season_id}")
    print(f"Game Type: {game_log_2.game_type}")
    game = game_log.games[0]
    game_2 = game_log_2.games[0]
    print(f"Game ID - Log 2: {game_2.game_id}")
    print(f"Game ID - Log 1: {game.game_id}")
    # print(game.to_dict())
    for game in game_log.games:
        print(f"Opponent: {game.opponent_abbrev}, Goals: {game.goals}")
    print("")
    print("Seasons with Playoffs:")
    for season in game_log.seasons: 
        if season.playoffs: 
            print(season.season)

    print("")
    print(f"1st Spotlighted Player: {players.spotlight[0].name}")
    print(f"2nd Spotlighted Player: {players.spotlight[1].name}")
    print("")
    goal_leaders = players.leaders.goalies(season=20242025, game_type=2, categories="wins", limit=10)
    wins = goal_leaders.wins
    save_pct = goal_leaders.save_pctg
    print(f"Goalie wins leader: {wins[0].last_name}")
    print(f"Goalie wins leader id: {wins[0].pid}")
    print(save_pct)

    skater_leaders = players.leaders.skaters()
    print(f"Current Goals Leader: {skater_leaders.goals[0].last_name}")



if __name__ == "__main__": 
    main()

