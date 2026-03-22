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

# Get a player
player = client.players.get(8477492)  # Nathan MacKinnon

# Profile
print(player.profile.first_name)
print(player.profile.position)

# Stats
print(player.stats.career)
print(player.stats.featured)
print(player.stats.seasons)
print(player.stats.last_5_games)

# Game log (current season)
logs = player.stats.game_log()

# Game log (specific season + game type)
logs = player.stats.game_log(season=20232024, game_type=2)

# Edge stats (skaters)
details  = player.stats.edge.skater.details()
speed    = player.stats.edge.skater.skating_speed()
distance = player.stats.edge.skater.skating_distance()
```

---

## Configuration

`NhlClient` accepts optional keyword arguments. All fields have defaults and can be overridden individually or via a `BaseConfig` object.

```python
from nhl_stats.src.client import NhlClient

client = NhlClient(
    log_name="my_app",        # logger name              (default: "nhl_sdk")
    log_level="INFO",         # DEBUG|INFO|WARNING|ERROR  (default: "DEBUG")
    log_file="/tmp/nhl.log",  # log file path; None = stdout only
    lang="en",                # response language         (default: "en")
    cache=my_cache,           # custom BaseCache impl     (default: MemCache)
)
```

### Log File Default

By default, logs are written to the platform-appropriate directory resolved by [`platformdirs`](https://github.com/platformdirs/platformdirs):

| Platform | Default Path                          |
| -------- | ------------------------------------- |
| macOS    | `~/Library/Logs/nhl_sdk/nhl.log`      |
| Linux    | `~/.cache/nhl_sdk/log/nhl.log`        |
| Windows  | `%LOCALAPPDATA%\nhl_sdk\Logs\nhl.log` |

Set `log_file=None` to write to stdout only.

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

### `client.players`

| Method / Property | Returns           | Description                               |
| ----------------- | ----------------- | ----------------------------------------- |
| `.get(pid)`       | `Player`          | Player object for the given NHL player ID |
| `.spotlight`      | `list[Spotlight]` | Currently spotlighted players             |
| `.leaders`        | `Leaders`         | Stat leaders for skaters and goalies      |

---

### `Player`

| Property / Method | Returns   | Description                                                    |
| ----------------- | --------- | -------------------------------------------------------------- |
| `.profile`        | `Profile` | Biographical info (name, position, birth, draft, awards, etc.) |
| `.stats`          | `Stats`   | Statistical data                                               |
| `.refresh()`      | `None`    | Clears cache and re-fetches latest data                        |

---

### `Player.stats`

| Attribute / Method             | Returns              | Description                       |
| ------------------------------ | -------------------- | --------------------------------- |
| `.featured`                    | `Featured`           | Current season featured stats     |
| `.career`                      | `Career`             | Career totals                     |
| `.seasons`                     | `list[Season]`       | Per-season stat totals            |
| `.last_5_games`                | `list[FeaturedGame]` | Most recent 5 games               |
| `.game_log(season, game_type)` | `GameLogs`           | Full game log for a season        |
| `.edge`                        | `EdgeStats`          | NHL Edge tracking stats container |

---

### `Player.stats.edge`

| Sub-resource | Status      | Description                |
| ------------ | ----------- | -------------------------- |
| `.skater`    | Implemented | Skater-specific Edge stats |
| `.goalie`    | Coming soon | —                          |
| `.team`      | Coming soon | —                          |

#### `edge.skater` methods

All methods accept optional `season` and `game_type` parameters. Results are cached (1hr TTL).

| Method                | Description                   |
| --------------------- | ----------------------------- |
| `.details()`          | Full skater Edge detail stats |
| `.comparison()`       | Skater comparison stats       |
| `.skating_distance()` | Skating distance metrics      |
| `.skating_speed()`    | Skating speed metrics         |
| `.zone_time()`        | Zone time breakdown           |
| `.shot_speed()`       | Shot speed data               |
| `.shot_location()`    | Shot location data            |
| `.cat_details()`      | Category-based skater details |

---

## Error Handling

The NHL API is public and requires no authentication. As this is an unofficial SDK against an undocumented API, there is no guarantee that endpoints or response structures won't change, and unexpected errors outside those listed below may occur. Errors you may encounter:

```python
from nhl_stats.src.core.errors import NotFoundError, RateLimitError, NhlApiError

try:
    player = client.players.get(9999999)
    _ = player.profile
except NotFoundError as e:
    print(f"Player not found: {e} (status {e.status_code})")
except RateLimitError:
    print("Rate limited")
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
- [ ] NHL Edge — goalie stats
- [ ] NHL Edge — team stats
- [ ] Teams namespace
- [ ] League / schedule / standings

---

## License

MIT License. See [LICENSE](LICENSE) for details.
