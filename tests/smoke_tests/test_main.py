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

from nhl_stats.client import NhlClient
from nhl_stats.core.cache.mem_cache import MemCache

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
from test_games import (
    test_smoke_network_tv_schedule_now,
    test_smoke_network_tv_schedule_with_date,
    test_smoke_daily_scores_now,
    test_smoke_daily_scores_with_date,
    test_smoke_scoreboard_now,
    test_smoke_pbp,
    test_smoke_landing,
    test_smoke_boxscore,
    test_smoke_story,
    test_smoke_odds_us,
)
from test_draft import (
    test_smoke_picks_now,
    test_smoke_picks_by_season_and_round,
    test_smoke_picks_all_rounds,
    test_smoke_tracker_now,
    test_smoke_rankings_now,
    test_smoke_rankings_by_season_and_category,
)
from test_playoffs import (
    test_smoke_carousel,
    test_smoke_series_schedule,
    test_smoke_bracket,
)
from test_league import (
    test_smoke_league_schedule_now,
    test_smoke_league_schedule_with_date,
    test_smoke_league_schedule_calendar_now,
    test_smoke_league_schedule_calendar_with_date,
    test_smoke_league_seasons,
)
from test_misc import (
    test_smoke_misc_location,
    test_smoke_misc_countries,
    test_smoke_misc_franchises,
    test_smoke_misc_glossary,
    test_smoke_misc_config,
    test_smoke_misc_ping,
    test_smoke_games_shifts,
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
    time.sleep(1.5)

    test_smoke_network_tv_schedule_now(client)
    test_smoke_network_tv_schedule_with_date(client)
    test_smoke_daily_scores_now(client)
    test_smoke_daily_scores_with_date(client)
    test_smoke_scoreboard_now(client)
    time.sleep(1.5)

    test_smoke_pbp(client)
    test_smoke_landing(client)
    test_smoke_boxscore(client)
    test_smoke_story(client)
    test_smoke_odds_us(client)
    time.sleep(1.5)

    test_smoke_picks_now(client)
    test_smoke_picks_by_season_and_round(client)
    test_smoke_picks_all_rounds(client)
    test_smoke_tracker_now(client)
    test_smoke_rankings_now(client)
    test_smoke_rankings_by_season_and_category(client)
    time.sleep(1.5)

    test_smoke_carousel(client)
    test_smoke_series_schedule(client)
    test_smoke_bracket(client)
    time.sleep(1.5)

    test_smoke_league_schedule_now(client)
    test_smoke_league_schedule_with_date(client)
    test_smoke_league_schedule_calendar_now(client)
    test_smoke_league_schedule_calendar_with_date(client)
    test_smoke_league_seasons(client)
    time.sleep(1.5)

    test_smoke_misc_location(client)
    test_smoke_misc_countries(client)
    test_smoke_misc_franchises(client)
    test_smoke_misc_glossary(client)
    test_smoke_misc_config(client)
    test_smoke_misc_ping(client)
    test_smoke_games_shifts(client)
