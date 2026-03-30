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

# Stats
print(player.stats.career)
print(player.stats.seasons)
print(player.stats.last_5_games)

# Game log (current season)
logs = player.stats.game_log()

# Game log (specific season + game type)
logs = player.stats.game_log(season=20232024, game_type=2)

# NHL Edge — position-aware (returns SkaterEdge or GoalieEdge automatically)
details = player.stats.edge().details()
speed   = player.stats.edge().skating_speed()

# Spotlight + leaders
spotlight = client.players.spotlight
leaders   = client.players.leaders
skater_leaders = leaders.skaters.get_stat_leaders(categories="goals", limit=10)

# --- Teams ---
# Standings
standings = client.teams.standings.get_standings()
standings_by_date = client.teams.standings.get_standings(date="2025-01-15")

# Stats
team_stats = client.teams.stats.get_team_stats("COL")
scoreboard = client.teams.stats.get_team_scoreboard("COL")

# Roster
roster = client.teams.roster.get_team_roster("COL")

# Schedule
schedule      = client.teams.schedule.get_schedule("COL")
month_sched   = client.teams.schedule.get_schedule_month("COL", month="2025-01")
week_sched    = client.teams.schedule.get_schedule_week("COL", week="2025-01-06")
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

- [x] Player profile (bio, awards, draft, media)
- [x] Player stats (career, season, game log, featured)
- [x] Player spotlight
- [x] Stat leaders (skaters + goalies)
- [x] NHL Edge — skater stats
- [x] NHL Edge — goalie stats
- [x] Teams namespace (standings, stats, roster, schedule)
- [ ] NHL Edge — team stats
- [ ] League / schedule / standings

---

## License

MIT License. See [LICENSE](LICENSE) for details.
