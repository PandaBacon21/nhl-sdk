# ==========================================================================
# SPOTLIGHT
# ==========================================================================

def test_smoke_spotlight(nhl) -> None:
    spotlight = nhl.players.spotlight

    assert len(spotlight) > 0
    print(f"1st spotlighted player: {spotlight[0].name}")
    print(f"2nd spotlighted player: {spotlight[1].name}")


# ==========================================================================
# LEADERS
# ==========================================================================

def test_smoke_leaders(nhl) -> None:
    leaders = nhl.players.leaders

    goalie_leaders = leaders.goalies.get_stat_leaders(season=20242025, game_type=2, categories="wins", limit=10)
    assert goalie_leaders.wins is not None
    assert len(goalie_leaders.wins) > 0
    print(f"Goalie wins leader: {goalie_leaders.wins[0].last_name} (pid: {goalie_leaders.wins[0].pid})")
    print(f"Save pct leaders: {goalie_leaders.save_pctg}")

    skater_leaders = leaders.skaters.get_stat_leaders()
    assert skater_leaders.goals is not None
    assert len(skater_leaders.goals) > 0
    print(f"Current goals leader: {skater_leaders.goals[0].last_name}")
    print(f"Current assists leader: {skater_leaders.assists[0].last_name}")

    edge_landing = leaders.skaters.get_edge_leaders.landing()
    assert edge_landing is not None
    print(f"Edge seasons: {edge_landing.seasons_with_edge[0].id}")
    print(f"Hardest shot leader: {edge_landing.leaders.hardest_shot.player.last_name}")
