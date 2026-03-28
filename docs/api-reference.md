# API Reference

---

## `NhlClient`

The main entry point for the SDK. All kwargs are optional — defaults are used for any omitted values.

```python
from nhl_stats.src.client import NhlClient

client = NhlClient()
```

### Constructor kwargs

| Parameter            | Type         | Default      | Description                                              |
| -------------------- | ------------ | ------------ | -------------------------------------------------------- |
| `log_name`           | `str`        | `"nhl_sdk"`  | Logger name                                              |
| `log_level`          | `str`        | `"DEBUG"`    | Logging level: `"DEBUG"`, `"INFO"`, `"WARNING"`, `"ERROR"` |
| `log_file`           | `str \| None` | `None`       | File path for log output. `None` writes to stdout only   |
| `lang`               | `str`        | `"en"`       | API response language                                    |
| `cache`              | `BaseCache`  | `MemCache()` | Cache backend. Pass a custom `BaseCache` implementation  |
| `config_from_object` | `BaseConfig` | `None`       | Pass a full config object instead of individual kwargs. Takes precedence over all other kwargs if provided. |

### Top-level properties

| Property   | Returns   | Description          |
| ---------- | --------- | -------------------- |
| `.players` | `Players` | Players namespace    |
| `.teams`   | `Teams`   | Teams namespace      |

---

## `DefaultConfig` / `BaseConfig`

Use a config object to define settings once and reuse across multiple clients, or to keep configuration separate from instantiation.

```python
from nhl_stats.src.core.config import DefaultConfig
from nhl_stats.src.client import NhlClient

config = DefaultConfig(log_level="WARNING", log_file="/tmp/nhl.log")
client = NhlClient(config_from_object=config)
```

`DefaultConfig` extends `BaseConfig` with no additional fields. Subclass `BaseConfig` directly to define a custom config type.

| Field      | Type         | Default      | Description                              |
| ---------- | ------------ | ------------ | ---------------------------------------- |
| `log_name` | `str`        | `"nhl_sdk"`  | Logger name                              |
| `log_level`| `str`        | `"DEBUG"`    | Logging level                            |
| `log_file` | `str \| None` | `None`       | Log file path. `None` = stdout only      |
| `lang`     | `str`        | `"en"`       | API response language                    |
| `cache`    | `BaseCache`  | `MemCache()` | Cache backend                            |

---

## Custom Cache

Implement `BaseCache` to plug in any cache backend (Redis, file-based, etc.). Pass the instance to `NhlClient` via the `cache` kwarg.

```python
from nhl_stats.src.core.cache.base_cache import BaseCache

class MyCache(BaseCache):
    def get(self, key: str): ...
    def set(self, key: str, data, ttl: int): ...
    def delete(self, key: str): ...
    def clear(self): ...

client = NhlClient(cache=MyCache())
```

| Method              | Description                                              |
| ------------------- | -------------------------------------------------------- |
| `.get(key)`         | Return cached value for `key`, or `None` if missing/expired |
| `.set(key, data, ttl)` | Store `data` under `key` with a TTL in seconds        |
| `.delete(key)`      | Remove a single entry                                    |
| `.clear()`          | Purge all cached entries                                 |

The default `MemCache` is an in-process dict-based cache. It does not persist across client instances.

---

## `client.players`

| Method / Property | Returns           | Description                          |
| ----------------- | ----------------- | ------------------------------------ |
| `.get(pid)`       | `Player`          | Player object for a given player ID  |
| `.spotlight`      | `list[Spotlight]` | Currently spotlighted players        |
| `.leaders`        | `Leaders`         | Stat leaders for skaters and goalies |

---

## `Player`

| Property / Method | Returns   | Description                                                    |
| ----------------- | --------- | -------------------------------------------------------------- |
| `.profile`        | `Profile` | Biographical info (name, position, birth, draft, awards, etc.) |
| `.stats`          | `Stats`   | Statistical data                                               |

---

## `Player.stats`

| Attribute / Method             | Returns              | Description                       |
| ------------------------------ | -------------------- | --------------------------------- |
| `.featured`                    | `Featured`           | Current season featured stats     |
| `.career`                      | `Career`             | Career totals                     |
| `.seasons`                     | `list[Season]`       | Per-season stat totals            |
| `.last_5_games`                | `list[FeaturedGame]` | Most recent 5 games               |
| `.game_log(season, game_type)` | `GameLogs`           | Full game log for a season        |
| `.edge()`                      | `SkaterEdge \| GoalieEdge` | NHL Edge stats for the player's position |

`game_log()` parameters:

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

Omit both for the current season. `season` and `game_type` must be provided together for a historical lookup.

---

## `Player.stats.edge()`

Returns `SkaterEdge` for skaters or `GoalieEdge` for goalies, determined automatically from the player's position parsed at fetch time. No sub-resource selection required — just call `.edge()` and use the returned object.

All methods on both types accept optional `season` and `game_type` parameters. Results are cached with a 1hr TTL. Omit both for current-season data.

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

`season` and `game_type` must be provided together for a historical lookup.

### `SkaterEdge` methods

Returned by `player.stats.edge()` when the player is a skater (any position other than `G`).

| Method                | Returns            | Description                 |
| --------------------- | ------------------ | --------------------------- |
| `.details()`          | `SkaterDetails`    | Ranking and stat summaries  |
| `.comparison()`       | `SkaterComparison` | Drill-down comparison stats |
| `.skating_distance()` | `SkatingDistance`  | Skating distance metrics    |
| `.skating_speed()`    | `SkatingSpeed`     | Skating speed metrics       |
| `.zone_time()`        | `ZoneTime`         | Zone time breakdown         |
| `.shot_speed()`       | `ShotSpeed`        | Shot speed data             |
| `.shot_location()`    | `ShotLocation`     | Shot location data          |
| `.cat_details()`      | `CatSkaterDetails` | CAT endpoint skater details |

### `GoalieEdge` methods

Returned by `player.stats.edge()` when the player is a goalie (`position == "G"`).

| Method             | Returns              | Description                    |
| ------------------ | -------------------- | ------------------------------ |
| `.details()`       | `GoalieDetails`      | Ranking and stat summaries     |
| `.comparison()`    | `GoalieComparison`   | Drill-down comparison stats    |
| `.five_v_five()`   | `GoalieFiveVFive`    | 5v5 save percentage detail     |
| `.shot_location()` | `GoalieShotLocation` | Shot location detail           |
| `.save_pctg()`     | `GoalieSavePctg`     | Overall save percentage detail |
| `.cat_details()`   | `CatGoalieDetails`   | CAT endpoint goalie details    |

---

## `Leaders`

Accessed via `client.players.leaders`.

| Property   | Returns         | Description                     |
| ---------- | --------------- | ------------------------------- |
| `.skaters` | `SkaterLeaders` | Skater leaders namespace        |
| `.goalies` | `GoalieLeaders` | Goalie leaders namespace        |

---

## `SkaterLeaders`

Accessed via `client.players.leaders.skaters`. Provides skater stat leaders and Edge leaderboard access.

| Method / Property                                        | Returns              | Description                        |
| -------------------------------------------------------- | -------------------- | ---------------------------------- |
| `.get_stat_leaders(season, game_type, categories, limit)` | `SkaterStatLeaders` | Skater stat leader lists           |
| `.get_edge_leaders`                                      | `SkaterEdgeLeaders`  | NHL Edge skater leaderboards       |

---

## `GoalieLeaders`

Accessed via `client.players.leaders.goalies`. Provides goalie stat leaders and Edge leaderboard access.

| Method / Property                                        | Returns              | Description                        |
| -------------------------------------------------------- | -------------------- | ---------------------------------- |
| `.get_stat_leaders(season, game_type, categories, limit)` | `GoalieStatLeaders` | Goalie stat leader lists           |
| `.get_edge_leaders`                                      | `GoalieEdgeLeaders`  | NHL Edge goalie leaderboards       |

---

## `SkaterStatLeaders`

Returned by `client.players.leaders.skaters.get_stat_leaders(...)`. Results are cached with a 1hr TTL.

All parameters are optional. `season` and `game_type` must be provided together for a historical lookup, or omitted for current leaders.

- Omitting `categories` returns top 5 players for **all** categories.
- Passing a specific `categories` value returns top 5 for that category only.
- `limit` defaults to `5`. Pass `limit=-1` to return all results.

| Parameter    | Type  | Required | Description                                     |
| ------------ | ----- | -------- | ----------------------------------------------- |
| `season`     | `int` | No       | Season in `YYYYYYYY` format (e.g. `20232024`)   |
| `game_type`  | `int` | No       | `2` = regular season, `3` = playoffs            |
| `categories` | `str` | No       | `"goals"`, `"assists"`, `"points"`, `"plusMinus"`, `"penaltyMins"`, `"goalsPp"`, `"goalsSh"`, `"faceoffLeaders"`, `"toi"` |
| `limit`      | `int` | No       | Results per category. Default: `5`. Pass `-1` for all. |

| Attribute          | Returns              | Description                    |
| ------------------ | -------------------- | ------------------------------ |
| `.goals`           | `list[LeaderPlayer]` | Goals leaders                  |
| `.goals_pp`        | `list[LeaderPlayer]` | Power-play goals leaders       |
| `.goals_sh`        | `list[LeaderPlayer]` | Short-handed goals leaders     |
| `.assists`         | `list[LeaderPlayer]` | Assists leaders                |
| `.points`          | `list[LeaderPlayer]` | Points leaders                 |
| `.plus_minus`      | `list[LeaderPlayer]` | Plus/minus leaders             |
| `.penalty_min`     | `list[LeaderPlayer]` | Penalty minutes leaders        |
| `.faceoff_leaders` | `list[LeaderPlayer]` | Faceoff percentage leaders     |
| `.toi`             | `list[LeaderPlayer]` | Time-on-ice leaders            |

---

## `GoalieStatLeaders`

Returned by `client.players.leaders.goalies.get_stat_leaders(...)`. Results are cached with a 1hr TTL.

All parameters are optional. `season` and `game_type` must be provided together for a historical lookup, or omitted for current leaders.

- Omitting `categories` returns top 5 goalies for **all** categories.
- Passing a specific `categories` value returns top 5 for that category only.
- `limit` defaults to `5`. Pass `limit=-1` to return all results.

| Parameter    | Type  | Required | Description                                     |
| ------------ | ----- | -------- | ----------------------------------------------- |
| `season`     | `int` | No       | Season in `YYYYYYYY` format (e.g. `20232024`)   |
| `game_type`  | `int` | No       | `2` = regular season, `3` = playoffs            |
| `categories` | `str` | No       | `"wins"`, `"shutouts"`, `"savePctg"`, `"goalsAgainstAverage"` |
| `limit`      | `int` | No       | Results per category. Default: `5`. Pass `-1` for all. |

| Attribute            | Returns              | Description                      |
| -------------------- | -------------------- | -------------------------------- |
| `.wins`              | `list[LeaderPlayer]` | Wins leaders                     |
| `.shutouts`          | `list[LeaderPlayer]` | Shutouts leaders                 |
| `.save_pctg`         | `list[LeaderPlayer]` | Save percentage leaders          |
| `.goals_against_avg` | `list[LeaderPlayer]` | Goals against average leaders    |

---

## `SkaterEdgeLeaders`

Accessed via `client.players.leaders.skaters.get_edge_leaders`. No player ID required — these are league-wide leaderboards. Results are cached with a 1hr TTL.

### `.landing(season, game_type)` → `SkaterLanding`

Edge landing page leaders summary.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.distance_top_10(pos, strength, sort, season, game_type)` → `SkaterDistanceTop10`

Top 10 skaters by skating distance.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                         |
| `strength`  | Yes      | `"all"`, `"es"`, `"pp"`, `"pk"`               |
| `sort`      | Yes      | `"total"`, `"per-60"`, `"max-game"`, `"max-period"` |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.speed_top_10(pos, sort, season, game_type)` → `SkaterSpeedTop10`

Top 10 fastest skaters.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                         |
| `sort`      | Yes      | `"max"`, `"over-22"`, `"20-22"`, `"18-20"`    |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.zone_time_top_10(pos, strength, sort, season, game_type)` → `SkaterZoneTimeTop10`

Top 10 skaters by zone time.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                         |
| `strength`  | Yes      | `"all"`, `"es"`, `"pp"`, `"pk"`               |
| `sort`      | Yes      | `"offensive"`, `"neutral"`, `"defensive"`     |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.shot_speed_top_10(pos, sort, season, game_type)` → `SkaterShotSpeedTop10`

Top 10 skaters by shot speed.

| Parameter   | Required | Valid values                                         |
| ----------- | -------- | ---------------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                                |
| `sort`      | Yes      | `"max"`, `"over-100"`, `"90-99"`, `"80-89"`, `"70-79"` |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)         |
| `game_type` | No       | `2` = regular season, `3` = playoffs                 |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.shot_location_top_10(category, sort, season, game_type)` → `SkaterShotLocationTop10`

Top 10 skaters by shot location category.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `category`  | Yes      | `"sog"`, `"goals"`, `"shooting-pctg"`         |
| `sort`      | Yes      | `"all"`, `"high"`, `"mid"`, `"long"`          |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

---

## `GoalieEdgeLeaders`

Accessed via `client.players.leaders.goalies.get_edge_leaders`. No player ID required — these are league-wide leaderboards. Results are cached with a 1hr TTL.

### `.landing(season, game_type)` → `GoalieLanding`

Edge landing page leaders summary.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.five_v_five_top_10(sort, season, game_type)` → `list`

Top 10 goalies by 5v5 save percentage.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `sort`      | Yes      | `"savePctg"`                                  |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.shot_location_top_10(category, sort, season, game_type)` → `list`

Top 10 goalies by shot location.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `category`  | Yes      | `"sog"`, `"goals"`, `"shooting-pctg"`         |
| `sort`      | Yes      | `"all"`, `"high"`, `"mid"`, `"long"`          |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.save_pctg_top_10(sort, season, game_type)` → `list`

Top 10 goalies by overall save percentage.

| Parameter   | Required | Valid values                                  |
| ----------- | -------- | --------------------------------------------- |
| `sort`      | Yes      | `"savePctg"`                                  |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)  |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

---

## `client.teams`

| Property     | Returns        | Description                    |
| ------------ | -------------- | ------------------------------ |
| `.standings` | `Standings`    | NHL standings sub-resource     |
| `.stats`     | `TeamStats`    | Per-team stats sub-resource    |
| `.roster`    | `TeamRoster`   | Per-team roster sub-resource   |
| `.schedule`  | `TeamSchedule` | Per-team schedule sub-resource |

---

## `Standings`

Accessed via `client.teams.standings`. Results are cached with a 1hr TTL.

| Method                       | Returns           | Description                                   |
| ---------------------------- | ----------------- | --------------------------------------------- |
| `.get_standings(date)`       | `StandingsResult` | Current or date-specific standings            |
| `.get_standings_by_season()` | `list`            | Seasons for which standings data is available |

`date` is optional; format `YYYY-MM-DD` (e.g. `"2025-01-15"`). Defaults to current standings.

---

## `TeamStats`

Accessed via `client.teams.stats`. Results are cached with a 1hr TTL.

| Method                                  | Returns                     | Description                                   |
| --------------------------------------- | --------------------------- | --------------------------------------------- |
| `.get_team_stats(team, season, g_type)` | `TeamStatsResult`           | Club skater and goalie stats                  |
| `.get_game_types_per_season(team)`      | `list[TeamSeasonGameTypes]` | Seasons and game types available for the club |
| `.get_team_scoreboard(team)`            | `TeamScoreboard`            | Current scoreboard for the club               |

`get_team_stats()` parameters:

| Parameter | Required | Valid values                                 |
| --------- | -------- | -------------------------------------------- |
| `team`    | Yes      | Three-letter team code (e.g. `"COL"`)        |
| `season`  | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `g_type`  | No       | `2` = regular season, `3` = playoffs         |

`season` and `g_type` must be provided together for a historical lookup, or omitted for current stats. `team` is required for all three methods.

---

## `TeamRoster`

Accessed via `client.teams.roster`. Results are cached with a 6hr TTL.

| Method                           | Returns            | Description                                |
| -------------------------------- | ------------------ | ------------------------------------------ |
| `.get_team_roster(team, season)` | `TeamRosterResult` | Current or historical roster for a club    |
| `.get_roster_seasons(team)`      | `list[int]`        | Seasons for which roster data is available |
| `.get_team_prospects(team)`      | `ProspectsResult`  | Prospect list for a club                   |

`get_team_roster()` parameters:

| Parameter | Required | Valid values                                 |
| --------- | -------- | -------------------------------------------- |
| `team`    | Yes      | Three-letter team code (e.g. `"COL"`)        |
| `season`  | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |

`season` defaults to the current roster. `team` is required for all three methods.

---

## `TeamSchedule`

Accessed via `client.teams.schedule`. Results are cached with a 1hr TTL.

| Method                             | Returns                   | Description                     |
| ---------------------------------- | ------------------------- | ------------------------------- |
| `.get_schedule(team, season)`      | `TeamScheduleResult`      | Full-season schedule for a club |
| `.get_schedule_month(team, month)` | `TeamMonthScheduleResult` | Monthly schedule for a club     |
| `.get_schedule_week(team, week)`   | `TeamWeekScheduleResult`  | Weekly schedule for a club      |

| Parameter | Required | Format       | Example        |
| --------- | -------- | ------------ | -------------- |
| `team`    | Yes      | Three-letter code | `"COL"`   |
| `season`  | No       | `YYYYYYYY`   | `20242025`     |
| `month`   | No       | `YYYY-MM`    | `"2025-01"`    |
| `week`    | No       | `YYYY-MM-DD` | `"2025-01-06"` |

`season`, `month`, and `week` are optional and default to the current period. `team` is required for all three methods.
