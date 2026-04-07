# NHL Stats SDK

An unofficial Python SDK for the NHL API. Personal side project built for fun — no guarantees on cadence, but actively maintained.

> Only possible due to the great work by Zmalski documenting the [NHL API](https://github.com/Zmalski/NHL-API-Reference).
> Full Postman collection for manual testing available [here](https://josh-personal.postman.co/workspace/My-Personal-Workspace~1a09e9af-597c-4eb3-806e-860262a49125/collection/19505270-dfda07ab-2c76-4c1e-9682-296f91049732?action=share&creator=19505270&active-environment=19505270-97cd10c3-3bf7-4101-b0b2-569cd2507fed).

---

## Requirements

- Python 3.13+

---

## Installation

> while in dev

```bash
pip install -e .
```

---

## Quick Start

```python
from nhl_stats.src.client import NhlClient

client = NhlClient()

# --- Players ---
player = client.players.get(8477492)  # Nathan MacKinnon

# Profile
print(player.profile.first_name)
print(player.profile.position)

# Achievements (awards, badges, HHOF, top-100 status)
print(player.achievements.in_hhof)
print(player.achievements.in_top_100_all_time)
print(player.achievements.awards)
print(player.achievements.badges)

# Upcoming milestones for this player
milestones = player.achievements.milestones()
milestones = player.achievements.milestones(game_type=2)

# Stats
print(player.stats.career)
print(player.stats.seasons)
print(player.stats.last_5_games)

# Season summary (api_stats — includes EV/PP/SH splits)
summary = player.stats.summary()
summary = player.stats.summary(season=20232024, game_type=2)

# Game log
logs = player.stats.game_log()
logs = player.stats.game_log(season=20232024, game_type=2)

# Named api_stats reports — all accept optional season + game_type
# Shared (skater and goalie)
stats_bio    = player.stats.stats_bio()
pen_shots    = player.stats.penalty_shots(season=20232024, game_type=2)

# Skater-only (returns None for goalies)
faceoff_pct  = player.stats.faceoff_pct()
faceoff_wins = player.stats.faceoff_wins()
gfa          = player.stats.goals_for_against()
penalties    = player.stats.penalties()
pk           = player.stats.penalty_kill()
pp           = player.stats.powerplay()
puck_poss    = player.stats.puck_possessions()
realtime     = player.stats.realtime()
shot_type    = player.stats.shot_type()
toi          = player.stats.time_on_ice()
pct          = player.stats.percentages()

# Goalie-only (returns None for skaters)
advanced     = player.stats.advanced()
days_rest    = player.stats.days_rest()
saves_str    = player.stats.saves_by_strength()
shootout     = player.stats.shootout()
svr          = player.stats.started_vs_relieved()

# Raw escape hatch — any api_stats report type by name
raw          = player.stats.report("realtime", season=20232024, game_type=2)

# NHL Edge — position-aware (returns SkaterEdge or GoalieEdge automatically)
details = player.stats.edge().details()
speed   = player.stats.edge().skating_speed()

# League-wide player milestones (skaters + goalies combined by default)
milestones = client.players.milestones()
milestones = client.players.milestones(milestone="Goals", game_type=2)
milestones = client.players.milestones(position="s")   # skaters only
milestones = client.players.milestones(position="g")   # goalies only

# Raw player list query (api_stats escape hatch)
players    = client.players.query(cayenne_exp="currentTeamId>0")   # all active players with a team

# Spotlight + leaders
spotlight = client.players.spotlight
leaders   = client.players.leaders
skater_leaders = leaders.skaters.get_stat_leaders(categories="goals", limit=10)

# --- Teams ---
# Standings
standings = client.teams.standings.get_standings()
standings_by_date = client.teams.standings.get_standings(date="2025-01-15")

# Get a team object (identifier baked in)
team = client.teams.get("COL")

# Stats
team_stats = team.stats.get_team_stats()
scoreboard = team.stats.get_team_scoreboard()

# Aggregate summary (api_stats — goals for/against, PP%, PK%, faceoff%, etc.)
summary = team.stats.get_summary()
summary = team.stats.get_summary(season=20232024, g_type=2)

# Team reference data from api_stats
ref = team.stats.get_team_ref()    # TeamRef for this team

# All teams reference list (includes historical)
all_teams = client.teams.all()

# Roster
roster = team.roster.get_team_roster()

# Schedule
schedule      = team.schedule.get_schedule()
month_sched   = team.schedule.get_schedule_month(month="2025-01")
week_sched    = team.schedule.get_schedule_week(week="2025-01-06")

# NHL Edge — team-specific (via team.stats.edge)
edge          = team.stats.edge
details       = edge.details.get_details()
comparison    = edge.comparison.get_comparison()
distance      = edge.skating_distance.get_skating_distance()
speed         = edge.skating_speed.get_skating_speed()
zone          = edge.zone_time.get_zone_time()
shot_speed    = edge.shot_speed.get_shot_speed()
shot_loc      = edge.shot_location.get_shot_location()

# NHL Edge — league-wide leaderboards (via client.teams.edge)
landing       = client.teams.edge.landing.get_landing()
dist_top_10   = client.teams.edge.skating_distance_top_10.get_top_10(strength="all", sort="per-60")
speed_top_10  = client.teams.edge.skating_speed_top_10.get_top_10(sort="max")
zone_top_10   = client.teams.edge.zone_time_top_10.get_top_10(strength="all", sort="offensive")
shot_spd_top  = client.teams.edge.shot_speed_top_10.get_top_10(sort="max")
shot_loc_top  = client.teams.edge.shot_location_top_10.get_top_10(category="sog", sort="all")

# --- League ---
league_schedule  = client.league.get_schedule()
league_calendar  = client.league.get_schedule_calendar(date="2025-01-06")
seasons          = client.league.get_seasons()
season_details   = client.league.get_season_details()
component_season = client.league.get_component_season()

# --- Games ---
tv_schedule  = client.games.network.get_tv_schedule()
daily_scores = client.games.scores.get_daily_scores(date="2025-01-15")
scoreboard   = client.games.scoreboard.get_scoreboard()
pbp          = client.games.pbp.get_play_by_play(game_id=2024020001)
landing      = client.games.landing.get_landing(game_id=2024020001)
boxscore     = client.games.boxscore.get_boxscore(game_id=2024020001)
story        = client.games.story.get_game_story(game_id=2024020001)
odds         = client.games.odds.get_odds(country_code="US")
shifts       = client.games.shifts.get(game_id=2024020001)
streams      = client.games.streams.get()                    # may be region-restricted
game_records = client.games.query(cayenne_exp="season=20242025", limit=10)

# --- Draft ---
rankings     = client.draft.rankings.get_rankings()
rankings_by  = client.draft.rankings.get_rankings(season=2024, category=1)
tracker      = client.draft.tracker.get_tracker_now()
picks        = client.draft.picks.get_picks()
picks_by     = client.draft.picks.get_picks(season=2025, round="1")
all_picks    = client.draft.picks.get_all(year=2024)

# api_stats draft query
draft_data   = client.draft.query(cayenne_exp="draftYear=2023")

# --- Playoffs ---
carousel        = client.playoffs.carousel.get_carousel(season=20242025)
series_schedule = client.playoffs.series_schedule.get_series_schedule(season=20242025, series_letter="A")
bracket         = client.playoffs.bracket.get_bracket(year=2024)

# --- Misc ---
location     = client.misc.location()
postal       = client.misc.postal_lookup(postal_code="80202")
meta         = client.misc.meta()
game_meta    = client.misc.game_meta(game_id=2024020001)
game_rail    = client.misc.game_rail(game_id=2024020001)
goal_replay  = client.misc.goal_replay(game_id=2024020001, event_number=3)
play_replay  = client.misc.play_replay(game_id=2024020001, event_number=3)
wsc          = client.misc.wsc_play_by_play(game_id=2024020001)
countries    = client.misc.countries
franchises   = client.misc.franchises
glossary     = client.misc.glossary
config       = client.misc.config
ping         = client.misc.ping()
```

---

## Configuration

`NhlClient` accepts optional keyword arguments. All fields have defaults and can be overridden individually or via a `BaseConfig` object.

```python
from nhl_stats.src.client import NhlClient

client = NhlClient(
    log_name="my_app",        # logger name              (default: "nhl_sdk")
    log_level="INFO",         # DEBUG|INFO|WARNING|ERROR  (default: "DEBUG")
    log_file="/tmp/nhl.log",  # log file path; None = stdout only (default: None)
    lang="en",                # response language         (default: "en")
    cache=my_cache,           # custom BaseCache impl     (default: MemCache)
)
```

By default, logs are written to stdout only (`log_file=None`). Pass any file path string to write to a file instead.

### Custom Config Object

```python
from nhl_stats.src.core.config import DefaultConfig
from nhl_stats.src.client import NhlClient

config = DefaultConfig(log_level="WARNING", log_file=None)
client = NhlClient(config_from_object=config)
```

### Custom Cache

Implement `BaseCache` to plug in any backend (Redis, file-based, etc.):

```python
from nhl_stats.src.core.cache.base_cache import BaseCache

class MyCache(BaseCache):
    def get(self, key): ...
    def set(self, key, data, ttl): ...
    def delete(self, key): ...
    def clear(self): ...
```

---

## API Reference

Full method and property documentation is in [docs/api-reference.md](docs/api-reference.md).

---

## Error Handling

The NHL API is public and requires no authentication. As this is an unofficial SDK against an undocumented API, there is no guarantee that endpoints or response structures won't change, and unexpected errors outside those listed below may occur.

On HTTP 429, the SDK automatically retries up to 3 times with exponential backoff. The `Retry-After` response header is respected when present, capped at 60s with a minimum of 1s per retry. `RateLimitError` is raised only after all retries are exhausted. In practice, the NHL API returns `Retry-After: 60` on rate limit and counts it down across successive 429 responses in the same window.

```python
from nhl_stats.src.core.errors import NotFoundError, RateLimitError, NhlApiError

try:
    player = client.players.get(9999999)
    _ = player.profile
except NotFoundError as e:
    print(f"Player not found: {e} (status {e.status_code})")
except RateLimitError:
    print("Rate limited — retries exhausted")
except NhlApiError as e:
    print(f"API error: {e}")
```

| Exception        | HTTP Status        |
| ---------------- | ------------------ |
| `NotFoundError`  | 404                |
| `RateLimitError` | 429                |
| `ServerError`    | 5xx                |
| `NhlApiError`    | Base class / other |

---

## Roadmap

- [x] Player profile (bio, draft, media)
- [x] Player achievements (awards, badges, HHOF, top-100, milestones)
- [x] Player stats (career, season, game log, featured)
- [x] Player season summary from api_stats (EV/PP/SH splits)
- [x] Player api_stats named report methods (20 reports: stats_bio, faceoff, penalties, TOI, etc.)
- [x] Player spotlight
- [x] Stat leaders (skaters + goalies)
- [x] League-wide player milestones (skaters + goalies, filterable by position)
- [x] Player list query escape hatch (api_stats)
- [x] NHL Edge — skater stats
- [x] NHL Edge — goalie stats
- [x] NHL Edge — team stats (team-specific detail + league-wide leaderboards)
- [x] Teams namespace (standings, stats, roster, schedule)
- [x] Team aggregate summary from api_stats (PP%, PK%, goals for/against, etc.)
- [x] Team reference data via api_stats (TeamRef, teams.all, get_team_ref)
- [x] League (schedule, calendar, seasons, season details, component season)
- [x] Games (network schedule, daily scores, scoreboard, PBP, landing, boxscore, story, odds, shift charts)
- [x] Games query + streams escape hatches (api_stats)
- [x] Draft (prospect rankings, live tracker, picks, all-picks, api_stats query)
- [x] Playoffs (series carousel, series schedule, bracket)
- [x] Misc (location, postal lookup, meta, game rail, replays, WSC play-by-play)
- [x] Reference data via api_stats (countries, franchises, glossary, config, ping)

---

## License

MIT License. See [LICENSE](LICENSE) for details.
