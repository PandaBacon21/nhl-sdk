PID = 8477492  # Nathan MacKinnon


# ==========================================================================
# EDGE SKATER
# ==========================================================================

def test_smoke_edge_skater_details(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

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


def test_smoke_edge_skater_comparison(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

    comparison = edge.comparison()
    assert comparison is not None
    assert len(comparison.seasons_with_edge) > 0
    print(f"Top shot speed (imperial): {comparison.shot_speed.top_shot_speed.imperial}")
    print(f"Max skating speed (imperial): {comparison.skating_speed.max_skating_speed.imperial}")
    print(f"Zone time - offensive %: {comparison.zone_time.offensive_zone_pctg}")
    print(f"Skating distance last 10 count: {len(comparison.skating_distance_last_10)}")


def test_smoke_edge_skater_skating_distance(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

    distance = edge.skating_distance()
    assert distance is not None
    assert isinstance(distance.last_10_games, list)
    assert isinstance(distance.distance_by_strength, list)
    print(f"Last 10 games count: {len(distance.last_10_games)}")
    if distance.last_10_games:
        print(f"First game distance (all imperial): {distance.last_10_games[0].distance_skated_all.imperial}")
    print(f"Distance by strength count: {len(distance.distance_by_strength)}")


def test_smoke_edge_skater_skating_speed(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

    speed = edge.skating_speed()
    assert speed is not None
    print(f"Max skating speed (imperial): {speed.speed_summary.max_skating_speed.imperial}")
    print(f"Bursts over 22 mph: {speed.speed_summary.bursts_over_22.value}")
    print(f"Top speed instances count: {len(speed.top_speeds)}")
    if speed.top_speeds:
        print(f"Fastest: {speed.top_speeds[0].skating_speed.imperial} on {speed.top_speeds[0].game_date}")


def test_smoke_edge_skater_zone_time(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

    zone = edge.zone_time()
    assert zone is not None
    assert len(zone.zone_time_by_strength) > 0
    print(f"Zone time by strength count: {len(zone.zone_time_by_strength)}")
    print(f"Offensive zone starts %: {zone.zone_starts.offensive_zone_starts_pctg}")
    print(f"Defensive zone starts %: {zone.zone_starts.defensive_zone_starts_pctg}")


def test_smoke_edge_skater_shot_speed(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

    shot_spd = edge.shot_speed()
    assert shot_spd is not None
    print(f"Top shot speed (imperial): {shot_spd.speed_summary.top_shot_speed.imperial}")
    print(f"Avg shot speed (imperial): {shot_spd.speed_summary.avg_shot_speed.imperial}")
    print(f"Shot attempts over 100 mph: {shot_spd.speed_summary.shot_attempts_over_100.value}")
    if shot_spd.hardest_shots:
        print(f"Hardest shot game date: {shot_spd.hardest_shots[0].game_date}")


def test_smoke_edge_skater_shot_location(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

    shot_loc = edge.shot_location()
    assert shot_loc is not None
    assert len(shot_loc.area_details) > 0
    print(f"Area count: {len(shot_loc.area_details)}")
    print(f"First area: {shot_loc.area_details[0].area} | SOG: {shot_loc.area_details[0].sog}")
    print(f"Zone totals count: {len(shot_loc.zone_totals)}")


def test_smoke_edge_skater_cat_details(nhl) -> None:
    edge = nhl.players.get(pid=PID).stats.edge()

    cat = edge.cat_details()
    assert cat is not None
    cat_dict = cat.to_dict()
    print(f"Cat details: {cat_dict}")
