# NHL Stats SDK

[![PyPI version](https://img.shields.io/pypi/v/nhl-sdk)](https://pypi.org/project/nhl-sdk)

An unofficial Python SDK for the NHL API. Personal side project built for fun — no guarantees on cadence, but actively maintained.

> Only possible due to the great work by Zmalski documenting the [NHL API](https://github.com/Zmalski/NHL-API-Reference).
> Full Postman collection for manual testing available [here](https://www.postman.com/josh-a/workspace/nhl-api-unofficial-collection/collection/19505270-dfda07ab-2c76-4c1e-9682-296f91049732?action=share&creator=19505270).

---

## Requirements

- Python 3.13+

---

## Installation

```bash
pip install nhl-sdk
```

Or clone the repo and install in editable mode for local development:

```bash
git clone https://github.com/PandaBacon21/nhl-sdk.git
cd nhl-sdk/nhl_sdk
pip install -e .
```

---

## Quick Start

```python
from nhl_sdk.client import NhlClient

client = NhlClient()

# --- Players ---
player = client.players.get(8477492)   # Nathan MacKinnon — gateway object, player ID baked in

print(player.profile.first_name)       # biographical info
print(player.stats.career)             # career totals from landing
pp  = player.stats.powerplay()         # one of 20+ named api_stats reports (season, game_type optional)
log = player.stats.game_log(season=20242025, game_type=2)

print(player.achievements.awards)      # awards, badges, HHOF status, top-100
milestones = player.achievements.milestones()

# Collection-level — spotlight, stat leaders, league-wide milestones
spotlight  = client.players.spotlight
leaders    = client.players.leaders
milestones = client.players.milestones(milestone="Goals", position="s")  # skaters only

# --- Teams ---
team = client.teams.get("COL")         # Team gateway — abbreviation and team ID baked in

stats    = team.stats.get_team_stats()
summary  = team.stats.get_summary()    # api_stats aggregate (PP%, PK%, goals for/against, etc.)
roster   = team.roster.get_team_roster()
schedule = team.schedule.get_schedule()

standings = client.teams.standings.get_standings()

# --- League ---
schedule       = client.league.get_schedule(date="2025-01-15")
seasons        = client.league.get_seasons()
season_details = client.league.get_season_details()

# --- Games ---
game    = client.games.get(2024020001)  # Game gateway — game ID baked in
pbp     = game.pbp()
landing = game.landing()
shifts  = game.shifts()

scores     = client.games.scores.get_daily_scores(date="2025-01-15")
scoreboard = client.games.scoreboard.get_scoreboard()

# --- Draft ---
rankings = client.draft.rankings.get_rankings()
picks    = client.draft.picks.get_all(year=2024)
tracker  = client.draft.tracker.get_tracker_now()

# --- Playoffs ---
carousel = client.playoffs.carousel.get_carousel(season=20242025)
bracket  = client.playoffs.bracket.get_bracket(year=2024)

# --- Misc ---
meta      = client.misc.meta()
location  = client.misc.location()
countries = client.misc.countries
ping      = client.misc.ping()

# --- NHL Edge ---
# Player edge — returns SkaterEdge or GoalieEdge based on position
edge  = player.stats.edge()
speed = edge.skating_speed()

# Team edge — per-team detail
distance = team.stats.edge.skating_distance.get_skating_distance()

# Team edge — league-wide leaderboards
dist_top = client.teams.edge.skating_distance_top_10.get_top_10()
```

---

## What's Included

| Namespace | What it covers |
| --------- | -------------- |
| [`client.players`](docs/api-reference.md#clientplayers) | Player gateway (`profile`, `stats`, `achievements`), stat leaders, spotlight, league-wide milestones, player list query |
| [`client.teams`](docs/api-reference.md#clientteams) | Team gateway (`stats`, `roster`, `schedule`), standings, all-teams reference list |
| [`client.league`](docs/api-reference.md#clientleague) | League schedule, schedule calendar, season list, season details, component season |
| [`client.games`](docs/api-reference.md#clientgames) | Game gateway (`pbp`, `landing`, `boxscore`, `story`, `shifts`), daily scores, scoreboard, TV schedule, odds, streams |
| [`client.draft`](docs/api-reference.md#clientdraft) | Prospect rankings, live draft tracker, picks, all-picks, draft query |
| [`client.playoffs`](docs/api-reference.md#clientplayoffs) | Series carousel, per-series schedule, full bracket |
| [`client.misc`](docs/api-reference.md#clientmisc) | Location, postal lookup, meta, game rail, replays, WSC play-by-play, reference data (countries, franchises, glossary, config) |

**Player stats** — [`Player.stats`](docs/api-reference.md#playerstats) exposes career totals, season splits, and game logs from the landing endpoint, plus 20 named per-player reports sourced from the NHL Stats API (summary, bio, faceoff, penalties, TOI, power play, penalty kill, realtime, and more). NHL Edge per-player data is available via [`Player.stats.edge()`](docs/api-reference.md#playerstatse).

**Team stats** — [`TeamStats`](docs/api-reference.md#teamstats) covers per-player skater/goalie stats, aggregate team summaries (PP%, PK%, goals for/against), and team reference data. NHL Edge per-team detail is via [`TeamEdge`](docs/api-reference.md#teamedge) and league-wide leaderboards via [`TeamsEdge`](docs/api-reference.md#teamsedge).

---

## Configuration

`NhlClient` accepts optional keyword arguments. All fields have defaults and can be overridden individually or via a `BaseConfig` object.

```python
from nhl_sdk.client import NhlClient

client = NhlClient(
    log_name="my_app",        # logger name              (default: "nhl_sdk")
    log_level="INFO",         # DEBUG|INFO|WARNING|ERROR  (default: "WARNING")
    log_file="/tmp/nhl.log",  # log file path; None = stdout only (default: None)
    lang="en",                # response language         (default: "en")
    cache=my_cache,           # custom BaseCache impl     (default: MemCache)
)
```

By default, logs are written to stdout only (`log_file=None`). Pass any file path string to write to a file instead.

### Custom Config Object

```python
from nhl_sdk.core.config import DefaultConfig
from nhl_sdk.client import NhlClient

config = DefaultConfig(log_level="WARNING", log_file=None)
client = NhlClient(config_from_object=config)
```

### Custom Cache

Implement `BaseCache` to plug in any backend (Redis, file-based, etc.):

```python
from nhl_sdk.core.cache.base_cache import BaseCache

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
from nhl_sdk.core.errors import NotFoundError, RateLimitError, NhlApiError

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

## License

MIT License. See [LICENSE](LICENSE) for details.
