"""
Master smoke test runner — run directly with: uv run tests/smoke_tests/test_main.py
For pytest, run: uv run pytest tests/smoke_tests/
"""
import pytest
pytestmark = pytest.mark.smoke

import sys
import os
import time

sys.path.insert(0, os.path.dirname(__file__))

from src.client import NhlClient
from src.core.cache.mem_cache import MemCache

from test_player import test_smoke_profile, test_smoke_stats, test_smoke_game_log
from test_leaders import test_smoke_spotlight, test_smoke_leaders
from test_edge import (
    test_smoke_edge_skater_details,
    test_smoke_edge_skater_comparison,
    test_smoke_edge_skater_skating_distance,
    test_smoke_edge_skater_skating_speed,
    test_smoke_edge_skater_zone_time,
    test_smoke_edge_skater_shot_speed,
    test_smoke_edge_skater_shot_location,
    test_smoke_edge_skater_cat_details,
    test_smoke_edge_goalie_details,
    test_smoke_edge_goalie_comparison,
    test_smoke_edge_goalie_five_v_five,
    test_smoke_edge_goalie_shot_location,
    test_smoke_edge_goalie_save_pctg,
    test_smoke_edge_goalie_cat_details,
)
from test_teams import (
    test_smoke_standings,
    test_smoke_standings_by_season,
    test_smoke_team_stats,
    test_smoke_team_game_types_per_season,
    test_smoke_team_scoreboard,
    test_smoke_roster_seasons,
    test_smoke_team_roster,
    test_smoke_team_prospects,
    test_smoke_schedule,
    test_smoke_schedule_month,
    test_smoke_schedule_week,
)


if __name__ == "__main__":
    client = NhlClient(log_file="logs/nhl.log", log_level="DEBUG", cache=MemCache())

    test_smoke_profile(client)
    test_smoke_stats(client)
    test_smoke_game_log(client)
    test_smoke_spotlight(client)
    test_smoke_leaders(client)
    time.sleep(1.5)

    test_smoke_edge_skater_details(client)
    test_smoke_edge_skater_comparison(client)
    test_smoke_edge_skater_skating_distance(client)
    test_smoke_edge_skater_skating_speed(client)
    test_smoke_edge_skater_zone_time(client)
    test_smoke_edge_skater_shot_speed(client)
    test_smoke_edge_skater_shot_location(client)
    test_smoke_edge_skater_cat_details(client)
    time.sleep(1.5)

    test_smoke_edge_goalie_details(client)
    test_smoke_edge_goalie_comparison(client)
    test_smoke_edge_goalie_five_v_five(client)
    test_smoke_edge_goalie_shot_location(client)
    test_smoke_edge_goalie_save_pctg(client)
    test_smoke_edge_goalie_cat_details(client)
    time.sleep(1.5)

    test_smoke_standings(client)
    test_smoke_standings_by_season(client)
    test_smoke_team_stats(client)
    test_smoke_team_game_types_per_season(client)
    test_smoke_team_scoreboard(client)
    test_smoke_roster_seasons(client)
    test_smoke_team_roster(client)
    test_smoke_team_prospects(client)
    test_smoke_schedule(client)
    test_smoke_schedule_month(client)
    test_smoke_schedule_week(client)
