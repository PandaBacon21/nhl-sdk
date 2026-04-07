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

| Property    | Returns    | Description        |
| ----------- | ---------- | ------------------ |
| `.players`  | `Players`  | Players namespace  |
| `.teams`    | `Teams`    | Teams namespace    |
| `.league`   | `League`   | League namespace   |
| `.games`    | `Games`    | Games namespace    |
| `.draft`    | `Draft`    | Draft namespace    |
| `.playoffs` | `Playoffs` | Playoffs namespace |
| `.misc`     | `Misc`     | Miscellaneous endpoints and reference data |

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

| Method / Property      | Returns              | Description                                        |
| ---------------------- | -------------------- | -------------------------------------------------- |
| `.get(pid)`            | `Player`             | Player object for a given player ID                |
| `.spotlight`           | `list[Spotlight]`    | Currently spotlighted players                      |
| `.leaders`             | `Leaders`            | Stat leaders for skaters and goalies               |
| `.milestones(...)`     | `list[PlayerMilestone]` | League-wide upcoming skater milestones          |

### `.milestones(milestone, game_type, limit)` → `list[PlayerMilestone]`

Returns upcoming statistical milestones being approached by skaters across the league. Results are cached with a 1hr TTL.

| Parameter    | Required | Description                                                        |
| ------------ | -------- | ------------------------------------------------------------------ |
| `milestone`  | No       | Filter by type: `"Goals"`, `"Assists"`, `"Points"`, etc.          |
| `game_type`  | No       | `2` = regular season, `3` = playoffs                               |
| `limit`      | No       | Maximum results. Pass `-1` for all.                                |

---

## `Player`

| Property / Method  | Returns              | Description                                                    |
| ------------------ | -------------------- | -------------------------------------------------------------- |
| `.profile`         | `Profile`            | Biographical info (name, position, birth, draft, media)        |
| `.achievements`    | `PlayerAchievements` | Career recognition — awards, badges, HHOF, milestones          |
| `.stats`           | `PlayerStats`        | Statistical data                                               |

---

## `Player.achievements`

Accessed via `player.achievements`. Exposes career recognition data from the player landing response, and lazily loads upcoming milestone data from the NHL Stats API.

| Property / Method        | Returns                   | Description                                            |
| ------------------------ | ------------------------- | ------------------------------------------------------ |
| `.in_top_100_all_time`   | `bool \| None`            | Whether the player is in the top 100 all-time          |
| `.in_hhof`               | `bool \| None`            | Whether the player is inducted in the Hockey Hall of Fame |
| `.awards`                | `list[Award]`             | NHL awards won by the player                           |
| `.badges`                | `list[Badge]`             | Achievement badges earned by the player                |
| `.milestones(game_type)` | `list[PlayerMilestone] \| None` | Upcoming statistical milestones the player is approaching |

### `.milestones(game_type)` → `list[PlayerMilestone] | None`

Results are cached with a 1hr TTL. Returns `None` if no approaching milestones exist.

| Parameter   | Required | Description                                   |
| ----------- | -------- | --------------------------------------------- |
| `game_type` | No       | `2` = regular season, `3` = playoffs          |

---

## `Player.stats`

| Attribute / Method             | Returns                               | Description                       |
| ------------------------------ | ------------------------------------- | --------------------------------- |
| `.featured`                    | `Featured`                            | Current season featured stats     |
| `.career`                      | `Career`                              | Career totals                     |
| `.seasons`                     | `list[Season]`                        | Per-season stat totals            |
| `.last_5_games`                | `list[FeaturedGame]`                  | Most recent 5 games               |
| `.game_log(season, game_type)` | `GameLogs`                            | Full game log for a season        |
| `.summary(season, game_type)`  | `SkaterSummaryReport \| GoalieSummaryReport \| None` | Season aggregate from api_stats |
| `.report(report_type, ...)`    | `dict`                                | Raw escape hatch for any api_stats report |
| `.edge()`                      | `SkaterEdge \| GoalieEdge`            | NHL Edge stats for the player's position |

### `.game_log(season, game_type)` → `GameLogs`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

Omit both for the current season. `season` and `game_type` must be provided together for a historical lookup.

### `.summary(season, game_type)` → `SkaterSummaryReport | GoalieSummaryReport | None`

Fetches season-level aggregate stats from the NHL Stats API. Includes situational breakdowns (EV/PP/SH goals and points) not available in the player landing response. Returns the position-appropriate model automatically. Results are cached with a 1hr TTL. Returns `None` if no data exists for the requested season.

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20232024`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.report(report_type, ...)` → `dict`

Raw escape hatch for any api_stats report type not covered by named methods. Returns `{"data": [...], "total": N}`.

| Parameter      | Required | Description                                                         |
| -------------- | -------- | ------------------------------------------------------------------- |
| `report_type`  | Yes      | e.g. `"summary"`, `"bios"`, `"realtime"`, `"faceoffwins"`          |
| `season`       | No       | Season in `YYYYYYYY` format. Merged into cayenneExp automatically.  |
| `game_type`    | No       | Game type. Merged into cayenneExp automatically.                    |
| `is_aggregate` | No       | Aggregate stats across seasons/teams.                               |
| `cayenne_exp`  | No       | Custom filter expression. Overrides auto-built expression.          |
| `sort`         | No       | Field to sort by.                                                   |
| `dir`          | No       | Sort direction: `"ASC"` or `"DESC"`.                                |
| `start`        | No       | Pagination offset.                                                  |
| `limit`        | No       | Maximum results (`-1` for all).                                     |

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

Accessed via `client.players.leaders.skaters`. Provides skater stat leaders and Edge leaderboards. Results are cached with a 1hr TTL.

| Method                                                    | Returns                  | Description                          |
| --------------------------------------------------------- | ------------------------ | ------------------------------------ |
| `.get_stat_leaders(season, game_type, categories, limit)` | `SkaterStatLeaders`      | Skater stat leader lists             |
| `.edge_landing(season, game_type)`                        | `SkaterLanding`          | Edge landing page leaders summary    |
| `.edge_distance_top_10(pos, strength, sort, ...)`         | `list[DistanceLeaderEntry]`     | Top 10 skaters by skating distance   |
| `.edge_speed_top_10(pos, sort, ...)`                      | `list[SpeedLeaderEntry]`        | Top 10 fastest skaters               |
| `.edge_zone_time_top_10(pos, strength, sort, ...)`        | `list[ZoneTimeLeaderEntry]`     | Top 10 skaters by zone time          |
| `.edge_shot_speed_top_10(pos, sort, ...)`                 | `list[ShotSpeedLeaderEntry]`    | Top 10 skaters by shot speed         |
| `.edge_shot_location_top_10(category, sort, ...)`         | `list[ShotLocationLeaderEntry]` | Top 10 skaters by shot location      |

All Edge methods accept optional `season` and `game_type` parameters. `season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

---

## `GoalieLeaders`

Accessed via `client.players.leaders.goalies`. Provides goalie stat leaders and Edge leaderboards. Results are cached with a 1hr TTL.

| Method                                                    | Returns             | Description                          |
| --------------------------------------------------------- | ------------------- | ------------------------------------ |
| `.get_stat_leaders(season, game_type, categories, limit)` | `GoalieStatLeaders` | Goalie stat leader lists             |
| `.edge_landing(season, game_type)`                        | `GoalieLanding`     | Edge landing page leaders summary    |
| `.edge_five_v_five_top_10(sort, ...)`                     | `list[GoalieFiveVFiveLeaderEntry]`    | Top 10 goalies by 5v5 save pctg      |
| `.edge_shot_location_top_10(category, sort, ...)`         | `list[GoalieShotLocationLeaderEntry]` | Top 10 goalies by shot location      |
| `.edge_save_pctg_top_10(sort, ...)`                       | `list[GoalieSavePctgLeaderEntry]`     | Top 10 goalies by save percentage    |

All Edge methods accept optional `season` and `game_type` parameters. `season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

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

## `SkaterLeaders` — Edge method parameters

All Edge methods accept optional `season` and `game_type`. `season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.edge_landing(season, game_type)` → `SkaterLanding`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.edge_distance_top_10(pos, strength, sort, season, game_type)` → `list[DistanceLeaderEntry]`

| Parameter   | Required | Valid values                                        |
| ----------- | -------- | --------------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                               |
| `strength`  | Yes      | `"all"`, `"es"`, `"pp"`, `"pk"`                     |
| `sort`      | Yes      | `"total"`, `"per-60"`, `"max-game"`, `"max-period"` |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)        |
| `game_type` | No       | `2` = regular season, `3` = playoffs                |

### `.edge_speed_top_10(pos, sort, season, game_type)` → `list[SpeedLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                        |
| `sort`      | Yes      | `"max"`, `"over-22"`, `"20-22"`, `"18-20"`   |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.edge_zone_time_top_10(pos, strength, sort, season, game_type)` → `list[ZoneTimeLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                        |
| `strength`  | Yes      | `"all"`, `"es"`, `"pp"`, `"pk"`              |
| `sort`      | Yes      | `"offensive"`, `"neutral"`, `"defensive"`    |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.edge_shot_speed_top_10(pos, sort, season, game_type)` → `list[ShotSpeedLeaderEntry]`

| Parameter   | Required | Valid values                                            |
| ----------- | -------- | ------------------------------------------------------- |
| `pos`       | Yes      | `"all"`, `"F"`, `"D"`                                   |
| `sort`      | Yes      | `"max"`, `"over-100"`, `"90-99"`, `"80-89"`, `"70-79"` |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)            |
| `game_type` | No       | `2` = regular season, `3` = playoffs                    |

### `.edge_shot_location_top_10(category, sort, season, game_type)` → `list[ShotLocationLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `category`  | Yes      | `"sog"`, `"goals"`, `"shooting-pctg"`        |
| `sort`      | Yes      | `"all"`, `"high"`, `"mid"`, `"long"`         |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

---

## `GoalieLeaders` — Edge method parameters

All Edge methods accept optional `season` and `game_type`. `season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

### `.edge_landing(season, game_type)` → `GoalieLanding`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.edge_five_v_five_top_10(sort, season, game_type)` → `list[GoalieFiveVFiveLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `sort`      | Yes      | `"savePctg"`                                 |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.edge_shot_location_top_10(category, sort, season, game_type)` → `list[GoalieShotLocationLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `category`  | Yes      | `"sog"`, `"goals"`, `"shooting-pctg"`        |
| `sort`      | Yes      | `"all"`, `"high"`, `"mid"`, `"long"`         |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.edge_save_pctg_top_10(sort, season, game_type)` → `list[GoalieSavePctgLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `sort`      | Yes      | `"savePctg"`                                 |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

`season` and `game_type` must be provided together for a historical lookup, or omitted for current-season data.

---

## `client.teams`

| Method / Property     | Returns     | Description                                    |
| --------------------- | ----------- | ---------------------------------------------- |
| `.get(abbrev)`        | `Team`      | Team gateway object with identifier baked in   |
| `.standings`          | `Standings` | NHL standings sub-resource                     |
| `.edge`               | `TeamsEdge` | League-wide NHL Edge leaderboards sub-resource |

`abbrev` is the three-letter team code (e.g. `"COL"`). Case-insensitive. Raises `ValueError` for unknown codes. Supports all current franchises and historical relocations (`"ARI"`, `"PHX"`, `"ATL"`).

---

## `Team`

Returned by `client.teams.get("COL")`. The team abbreviation and ID are baked in — sub-resource methods require no team identifier.

| Property    | Returns        | Description                                       |
| ----------- | -------------- | ------------------------------------------------- |
| `.stats`    | `TeamStats`    | Per-team stats and NHL Edge sub-resource          |
| `.roster`   | `TeamRoster`   | Per-team roster sub-resource                      |
| `.schedule` | `TeamSchedule` | Per-team schedule sub-resource                    |

---

## `TeamStats`

Accessed via `team.stats` on a `Team` object. Results are cached with a 1hr TTL.

| Method                              | Returns                     | Description                                   |
| ----------------------------------- | --------------------------- | --------------------------------------------- |
| `.get_team_stats(season, g_type)`   | `TeamStatsResult`           | Club skater and goalie stats                  |
| `.get_game_types_per_season()`      | `list[TeamSeasonGameTypes]` | Seasons and game types available for the club |
| `.get_team_scoreboard()`            | `TeamScoreboard`            | Current scoreboard for the club               |
| `.get_summary(season, g_type)`      | `TeamAggregateSummary \| None` | Aggregate team stats from api_stats         |
| `.edge`                             | `TeamEdge`                  | Team-specific NHL Edge sub-resource           |

### `.get_team_stats(season, g_type)` parameters

| Parameter | Required | Valid values                                 |
| --------- | -------- | -------------------------------------------- |
| `season`  | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `g_type`  | No       | `2` = regular season, `3` = playoffs         |

`season` and `g_type` must be provided together for a historical lookup, or omitted for current stats.

### `.get_summary(season, g_type)` → `TeamAggregateSummary | None`

Fetches team-level aggregate metrics from the NHL Stats API (goals for/against, power play %, penalty kill %, faceoff win %, and more). Returns `None` if no data exists for the requested season. Results are cached with a 1hr TTL.

| Parameter | Required | Valid values                                 |
| --------- | -------- | -------------------------------------------- |
| `season`  | No       | `int` in `YYYYYYYY` format (e.g. `20232024`) |
| `g_type`  | No       | `2` = regular season, `3` = playoffs         |

`season` and `g_type` must be provided together for a historical lookup, or omitted for current data.

---

## `TeamEdge`

Accessed via `team.stats.edge` on a `Team` object. The team ID is baked in. Each property returns a sub-resource with a single method. All methods accept optional `season` and `game_type` — omit both for current-season data, or provide both for a historical lookup. Results are cached with a 1hr TTL.

| Property            | Sub-resource             | Method                                   | Returns                     | Description                                        |
| ------------------- | ------------------------ | ---------------------------------------- | --------------------------- | -------------------------------------------------- |
| `.details`          | `TeamDetails`            | `.get_details(season, game_type)`        | `TeamDetailResult`          | Full Edge stat summary for the team                |
| `.comparison`       | `TeamComparison`         | `.get_comparison(season, game_type)`     | `TeamComparisonResult`      | Shot/skating speed, distance, zone time, shot diff |
| `.skating_distance` | `TeamSkatingDistance`    | `.get_skating_distance(season, game_type)` | `TeamSkatingDistanceResult` | Per-situation distance breakdowns by strength/pos  |
| `.skating_speed`    | `TeamSkatingSpeedDetails`| `.get_skating_speed(season, game_type)`  | `TeamSkatingSpeedResult`    | Top speed instances and burst count breakdowns     |
| `.zone_time`        | `TeamZoneDetails`        | `.get_zone_time(season, game_type)`      | `TeamZoneDetailResult`      | Zone time percentages by strength, shot diffs      |
| `.shot_speed`       | `TeamShotSpeedDetails`   | `.get_shot_speed(season, game_type)`     | `TeamShotSpeedResult`       | Hardest shot instances and attempt bucket breakdown|
| `.shot_location`    | `TeamShotLocationDetails`| `.get_shot_location(season, game_type)`  | `TeamShotLocationResult`    | Per-area shot breakdowns and totals by location    |

All methods share the same parameter signature:

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

---

## `TeamsEdge`

Accessed via `client.teams.edge`. Provides league-wide NHL Edge leaderboards. Each property returns a sub-resource. Results are cached with a 1hr TTL.

| Property                   | Sub-resource          | Description                                       |
| -------------------------- | --------------------- | ------------------------------------------------- |
| `.landing`                 | `TeamLanding`         | League-leading team per Edge category             |
| `.skating_distance_top_10` | `TeamSkatingDistance10` | Top 10 teams by skating distance                |
| `.skating_speed_top_10`    | `TeamSkatingSpeed10`  | Top 10 teams by skating speed                     |
| `.zone_time_top_10`        | `TeamZoneTime10`      | Top 10 teams by zone time                         |
| `.shot_speed_top_10`       | `TeamShotSpeed10`     | Top 10 teams by shot speed                        |
| `.shot_location_top_10`    | `TeamShotLocation10`  | Top 10 teams by shot location                     |

All `get_top_10()` methods accept optional `season` and `game_type`. Omit both for current-season data; provide both for a historical lookup.

### `.landing.get_landing(season, game_type)` → `TeamEdgeLandingResult`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.skating_distance_top_10.get_top_10(strength, sort, pos, season, game_type)` → `list[TeamDistanceLeaderEntry]`

| Parameter   | Required | Valid values                                        |
| ----------- | -------- | --------------------------------------------------- |
| `strength`  | Yes      | `"all"`, `"es"`, `"pp"`, `"pk"`                     |
| `sort`      | Yes      | `"total"`, `"per-60"`, `"max-game"`, `"max-period"` |
| `pos`       | No       | `"all"`, `"F"`, `"D"`. Defaults to `"all"`          |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)        |
| `game_type` | No       | `2` = regular season, `3` = playoffs                |

### `.skating_speed_top_10.get_top_10(sort, pos, season, game_type)` → `list[TeamSpeedLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `sort`      | Yes      | `"max"`, `"over-22"`, `"20-22"`, `"18-20"`   |
| `pos`       | No       | `"all"`, `"F"`, `"D"`. Defaults to `"all"`   |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

### `.zone_time_top_10.get_top_10(strength, sort, season, game_type)` → `list[TeamZoneTimeLeaderEntry]`

| Parameter   | Required | Valid values                              |
| ----------- | -------- | ----------------------------------------- |
| `strength`  | Yes      | `"all"`, `"es"`, `"pp"`, `"pk"`           |
| `sort`      | Yes      | `"offensive"`, `"neutral"`, `"defensive"` |
| `season`    | No       | `int` in `YYYYYYYY` format                |
| `game_type` | No       | `2` = regular season, `3` = playoffs      |

### `.shot_speed_top_10.get_top_10(sort, pos, season, game_type)` → `list[TeamShotSpeedLeaderEntry]`

| Parameter   | Required | Valid values                                            |
| ----------- | -------- | ------------------------------------------------------- |
| `sort`      | Yes      | `"max"`, `"over-100"`, `"90-99"`, `"80-89"`, `"70-79"` |
| `pos`       | No       | `"all"`, `"F"`, `"D"`. Defaults to `"all"`              |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`)            |
| `game_type` | No       | `2` = regular season, `3` = playoffs                    |

### `.shot_location_top_10.get_top_10(category, sort, season, game_type)` → `list[TeamShotLocationLeaderEntry]`

| Parameter   | Required | Valid values                                 |
| ----------- | -------- | -------------------------------------------- |
| `category`  | Yes      | `"sog"`, `"goals"`, `"shooting-pctg"`        |
| `sort`      | Yes      | `"all"`, `"high"`, `"mid"`, `"long"`         |
| `season`    | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |
| `game_type` | No       | `2` = regular season, `3` = playoffs         |

---

## `Standings`

Accessed via `client.teams.standings`. Results are cached with a 1hr TTL.

| Method                       | Returns           | Description                                   |
| ---------------------------- | ----------------- | --------------------------------------------- |
| `.get_standings(date)`       | `StandingsResult` | Current or date-specific standings            |
| `.get_standings_by_season()` | `list`            | Seasons for which standings data is available |

`date` is optional; format `YYYY-MM-DD` (e.g. `"2025-01-15"`). Defaults to current standings.

---

## `TeamRoster`

Accessed via `team.roster` on a `Team` object. Results are cached with a 6hr TTL.

| Method                     | Returns            | Description                                |
| -------------------------- | ------------------ | ------------------------------------------ |
| `.get_team_roster(season)` | `TeamRosterResult` | Current or historical roster for the team  |
| `.get_roster_seasons()`    | `list[int]`        | Seasons for which roster data is available |
| `.get_team_prospects()`    | `ProspectsResult`  | Prospect list for the team                 |

`get_team_roster()` parameters:

| Parameter | Required | Valid values                                 |
| --------- | -------- | -------------------------------------------- |
| `season`  | No       | `int` in `YYYYYYYY` format (e.g. `20242025`) |

`season` defaults to the current roster.

---

## `TeamSchedule`

Accessed via `team.schedule` on a `Team` object. Results are cached with a 1hr TTL.

| Method                       | Returns                   | Description                      |
| ---------------------------- | ------------------------- | -------------------------------- |
| `.get_schedule(season)`      | `TeamScheduleResult`      | Full-season schedule for the team |
| `.get_schedule_month(month)` | `TeamMonthScheduleResult` | Monthly schedule for the team    |
| `.get_schedule_week(week)`   | `TeamWeekScheduleResult`  | Weekly schedule for the team     |

| Parameter | Required | Format       | Example        |
| --------- | -------- | ------------ | -------------- |
| `season`  | No       | `YYYYYYYY`   | `20242025`     |
| `month`   | No       | `YYYY-MM`    | `"2025-01"`    |
| `week`    | No       | `YYYY-MM-DD` | `"2025-01-06"` |

`season`, `month`, and `week` are optional and default to the current period.

---

## `client.league`

Accessed directly as `client.league`. Results are cached with a 1hr TTL.

| Method                            | Returns                  | Description                                                    |
| --------------------------------- | ------------------------ | -------------------------------------------------------------- |
| `.get_schedule(date)`             | `LeagueScheduleResult`   | League-wide game schedule for the current week or a specific date |
| `.get_schedule_calendar(date)`    | `LeagueCalendarResult`   | Calendar of scheduled game dates for the current window or a specific date |
| `.get_seasons()`                  | `list[int]`              | All NHL season IDs, past and present                           |
| `.get_season_details()`           | `list[dict]`             | Detailed season metadata from api_stats (start/end dates, etc.) |
| `.get_component_season()`         | `list[dict]`             | Component season metadata from api_stats                       |

| Parameter | Required | Format       | Example        |
| --------- | -------- | ------------ | -------------- |
| `date`    | No       | `YYYY-MM-DD` | `"2025-01-06"` |

`date` is optional for both schedule methods. Omit for the current period.

---

## `client.games`

| Property      | Returns          | Description                          |
| ------------- | ---------------- | ------------------------------------ |
| `.network`    | `GameNetwork`    | TV broadcast schedule sub-resource   |
| `.scores`     | `GameScores`     | Daily scores sub-resource            |
| `.scoreboard` | `GameScoreboard` | Current scoreboard sub-resource      |
| `.pbp`        | `GamePlayByPlay` | Play-by-play sub-resource            |
| `.landing`    | `GameLanding`    | Game landing sub-resource            |
| `.boxscore`   | `GameBoxscore`   | Boxscore sub-resource                |
| `.story`      | `GameStory`      | Game story sub-resource              |
| `.odds`       | `PartnerOdds`    | Partner betting odds sub-resource    |
| `.shifts`     | `GameShifts`     | Shift chart sub-resource             |

---

## `GameNetwork`

Accessed via `client.games.network`. Results are cached with a 1hr TTL.

| Method                      | Returns                 | Description                                         |
| --------------------------- | ----------------------- | --------------------------------------------------- |
| `.get_tv_schedule(date)`    | `NetworkScheduleResult` | TV broadcast schedule for the current date or a specific date |

| Parameter | Required | Format       | Example        |
| --------- | -------- | ------------ | -------------- |
| `date`    | No       | `YYYY-MM-DD` | `"2025-01-15"` |

---

## `GameScores`

Accessed via `client.games.scores`. Results are cached with a 1hr TTL.

| Method                        | Returns           | Description                                         |
| ----------------------------- | ----------------- | --------------------------------------------------- |
| `.get_daily_scores(date)`     | `DailyScoreResult` | Game scores including goals and clock state for the current date or a specific date |

| Parameter | Required | Format       | Example        |
| --------- | -------- | ------------ | -------------- |
| `date`    | No       | `YYYY-MM-DD` | `"2025-01-15"` |

---

## `GameScoreboard`

Accessed via `client.games.scoreboard`. Results are cached with a 1hr TTL.

| Method               | Returns            | Description                              |
| -------------------- | ------------------ | ---------------------------------------- |
| `.get_scoreboard()`  | `ScoreboardResult` | Current NHL scoreboard grouped by date   |

---

## `GamePlayByPlay`

Accessed via `client.games.pbp`. Results are cached with a 1hr TTL.

| Method                          | Returns           | Description                          |
| ------------------------------- | ----------------- | ------------------------------------ |
| `.get_play_by_play(game_id)`    | `PlayByPlayResult` | Full event-by-event play-by-play for a game |

| Parameter | Required | Description                                      |
| --------- | -------- | ------------------------------------------------ |
| `game_id` | Yes      | NHL game ID (e.g. `2024020001`)                  |

---

## `GameLanding`

Accessed via `client.games.landing`. Results are cached with a 1hr TTL.

| Method                   | Returns             | Description                                                  |
| ------------------------ | ------------------- | ------------------------------------------------------------ |
| `.get_landing(game_id)`  | `GameLandingResult` | Scoring by period, three stars, and penalties for a game     |

| Parameter | Required | Description                      |
| --------- | -------- | -------------------------------- |
| `game_id` | Yes      | NHL game ID (e.g. `2024020001`)  |

---

## `GameBoxscore`

Accessed via `client.games.boxscore`. Results are cached with a 1hr TTL.

| Method                      | Returns               | Description                                               |
| --------------------------- | --------------------- | --------------------------------------------------------- |
| `.get_boxscore(game_id)`    | `GameBoxscoreResult`  | Per-player stats for forwards, defense, and goalies for both teams |

| Parameter | Required | Description                      |
| --------- | -------- | -------------------------------- |
| `game_id` | Yes      | NHL game ID (e.g. `2024020001`)  |

---

## `GameStory`

Accessed via `client.games.story`. Results are cached with a 1hr TTL.

| Method                        | Returns           | Description                                                        |
| ----------------------------- | ----------------- | ------------------------------------------------------------------ |
| `.get_game_story(game_id)`    | `GameStoryResult` | Scoring summary, three stars, and team game stats for a game       |

| Parameter | Required | Description                      |
| --------- | -------- | -------------------------------- |
| `game_id` | Yes      | NHL game ID (e.g. `2024020001`)  |

---

## `PartnerOdds`

Accessed via `client.games.odds`. Results are cached with a 1hr TTL.

| Method                          | Returns             | Description                                          |
| ------------------------------- | ------------------- | ---------------------------------------------------- |
| `.get_odds(country_code)`       | `PartnerOddsResult` | Current partner betting odds for the given country   |

| Parameter      | Required | Description                                   |
| -------------- | -------- | --------------------------------------------- |
| `country_code` | Yes      | Two-letter country code (e.g. `"US"`, `"CA"`) |

---

## `GameShifts`

Accessed via `client.games.shifts`. Results are cached with a 1hr TTL.

| Method          | Returns      | Description                              |
| --------------- | ------------ | ---------------------------------------- |
| `.get(game_id)` | `ShiftChart` | Shift chart data for a specific game     |

| Parameter | Required | Description                      |
| --------- | -------- | -------------------------------- |
| `game_id` | Yes      | NHL game ID (e.g. `2024020001`)  |

`ShiftChart` contains a `total` count and a `shifts` list of `ShiftEntry` objects. Each `ShiftEntry` includes player identity, team, period, start/end times, duration, hex color, and event details when applicable.

---

## `client.draft`

| Property     | Returns          | Description                        |
| ------------ | ---------------- | ---------------------------------- |
| `.rankings`  | `DraftRankings`  | Prospect rankings sub-resource     |
| `.tracker`   | `DraftTracker`   | Live draft tracker sub-resource    |
| `.picks`     | `DraftPicks`     | Draft picks sub-resource           |

| Method          | Returns      | Description                               |
| --------------- | ------------ | ----------------------------------------- |
| `.query(...)`   | `list[dict]` | Raw api_stats draft query                 |

### `.query(cayenne_exp, sort, dir, start, limit)` → `list[dict]`

Queries draft data from the NHL Stats API. Useful for filtering historical draft records by year, round, team, etc. Results are cached with a 6hr TTL.

| Parameter     | Required | Description                                                    |
| ------------- | -------- | -------------------------------------------------------------- |
| `cayenne_exp` | No       | Filter expression (e.g. `"draftYear=2023 and roundNumber=1"`) |
| `sort`        | No       | Field to sort by.                                              |
| `dir`         | No       | Sort direction: `"ASC"` or `"DESC"`.                           |
| `start`       | No       | Pagination offset.                                             |
| `limit`       | No       | Maximum results (`-1` for all).                                |

---

## `DraftRankings`

Accessed via `client.draft.rankings`. Results are cached with a 6hr TTL.

| Method                                    | Returns               | Description                                                    |
| ----------------------------------------- | --------------------- | -------------------------------------------------------------- |
| `.get_rankings(season, category)`         | `DraftRankingsResult` | Current midterm rankings, or rankings for a specific draft year and category |

| Parameter  | Required | Description                                                                          |
| ---------- | -------- | ------------------------------------------------------------------------------------ |
| `season`   | No       | Draft year as `int` (e.g. `2024`). Must be paired with `category`.                  |
| `category` | No       | Category as `int`: `1` = NA Skaters, `2` = Intl Skaters, `3` = NA Goalies, `4` = Intl Goalies |

Omit both for the current midterm rankings. `season` and `category` must be provided together.

---

## `DraftTracker`

Accessed via `client.draft.tracker`. Results are cached with a 1min TTL.

| Method                  | Returns              | Description                                         |
| ----------------------- | -------------------- | --------------------------------------------------- |
| `.get_tracker_now()`    | `DraftTrackerResult` | Current draft round state, picks, and TV broadcasts |

---

## `DraftPicks`

Accessed via `client.draft.picks`. Results are cached with a 6hr TTL.

| Method                          | Returns           | Description                                                         |
| ------------------------------- | ----------------- | ------------------------------------------------------------------- |
| `.get_picks(season, round)`     | `DraftPicksResult` | Picks for the current draft cycle, or for a specific season and round |

| Parameter | Required | Description                                                                       |
| --------- | -------- | --------------------------------------------------------------------------------- |
| `season`  | No       | Draft year as `int` (e.g. `2025`). Must be paired with `round`.                   |
| `round`   | No       | Round as `str`: `"1"`–`"7"` for a specific round, or `"all"` for all rounds. Must be paired with `season`. |

Omit both for the current draft cycle's picks.

---

## `client.playoffs`

| Property          | Returns                 | Description                               |
| ----------------- | ----------------------- | ----------------------------------------- |
| `.carousel`       | `PlayoffCarousel`       | Series carousel sub-resource              |
| `.series_schedule` | `PlayoffSeriesSchedule` | Series game schedule sub-resource         |
| `.bracket`        | `PlayoffBracket`        | Full playoff bracket sub-resource         |

---

## `PlayoffCarousel`

Accessed via `client.playoffs.carousel`. Results are cached with a 1hr TTL.

| Method                       | Returns                  | Description                                                   |
| ---------------------------- | ------------------------ | ------------------------------------------------------------- |
| `.get_carousel(season)`      | `PlayoffCarouselResult`  | Overview of all series in a season with win counts and seeds  |

| Parameter | Required | Description                                      |
| --------- | -------- | ------------------------------------------------ |
| `season`  | Yes      | Season in `YYYYYYYY` format (e.g. `20242025`)    |

---

## `PlayoffSeriesSchedule`

Accessed via `client.playoffs.series_schedule`. Results are cached with a 1hr TTL.

| Method                                           | Returns                  | Description                                               |
| ------------------------------------------------ | ------------------------ | --------------------------------------------------------- |
| `.get_series_schedule(season, series_letter)`    | `SeriesScheduleResult`   | Game-by-game schedule and results for a specific series   |

| Parameter       | Required | Description                                                   |
| --------------- | -------- | ------------------------------------------------------------- |
| `season`        | Yes      | Season in `YYYYYYYY` format (e.g. `20242025`)                 |
| `series_letter` | Yes      | Series letter (e.g. `"A"`, `"B"`, ..., `"O"`). Round 1 uses A–H, Round 2 uses I–L, Conference Finals use M–N, Stanley Cup Final uses O. |

---

## `PlayoffBracket`

Accessed via `client.playoffs.bracket`. Results are cached with a 6hr TTL.

| Method                  | Returns                 | Description                                                          |
| ----------------------- | ----------------------- | -------------------------------------------------------------------- |
| `.get_bracket(year)`    | `PlayoffBracketResult`  | Full bracket for a playoff year — all series across all rounds as a flat list |

| Parameter | Required | Description                          |
| --------- | -------- | ------------------------------------ |
| `year`    | Yes      | Year in `YYYY` format (e.g. `2024`)  |

---

## `client.misc`

Accessed directly as `client.misc`. Provides access to miscellaneous api-web endpoints and reference data from api_stats. Methods without caching note are uncached (live API call each time). Reference properties are cached with a 24hr TTL.

### Game & Location Methods

| Method / Property                          | Returns                        | Description                                                     |
| ------------------------------------------ | ------------------------------ | --------------------------------------------------------------- |
| `.location()`                              | `LocationResult`               | Country code detected for the current request                   |
| `.postal_lookup(postal_code)`              | `list[PostalLookupResult]`     | Geographic info for a postal code                               |
| `.meta(players, teams, season_states)`     | `MiscMeta`                     | Meta info for players, teams, or season states                  |
| `.game_meta(game_id)`                      | `GameMetaResult`               | Metadata for a specific game                                    |
| `.playoff_series_meta(year, series_letter)`| `PlayoffSeriesMetaResult`      | Metadata for a specific playoff series                          |
| `.game_rail(game_id)`                      | `GameRailResult`               | Sidebar content for the game center view                        |
| `.goal_replay(game_id, event_number)`      | `GoalReplayResult`             | Goal replay data for a game event                               |
| `.play_replay(game_id, event_number)`      | `PlayReplayResult`             | Play replay data for a game event                               |
| `.wsc_play_by_play(game_id)`               | `list[WscPlay]`                | WSC play-by-play data for a game                                |

### Reference Data (cached 24hr)

| Property        | Returns              | Description                                      |
| --------------- | -------------------- | ------------------------------------------------ |
| `.countries`    | `list[Country]`      | All countries with a hockey presence             |
| `.franchises`   | `list[Franchise]`    | All NHL franchises, past and present             |
| `.glossary`     | `list[GlossaryEntry]`| Statistical term definitions                     |
| `.config`       | `StatsConfig`        | NHL Stats API configuration and report metadata  |

### Connectivity

| Method    | Returns | Description                                   |
| --------- | ------- | --------------------------------------------- |
| `.ping()` | `bool`  | `True` if the Stats API server responds successfully |

### Parameter details

`.postal_lookup(postal_code)`:

| Parameter     | Required | Description                         |
| ------------- | -------- | ----------------------------------- |
| `postal_code` | Yes      | Postal / ZIP code string            |

`.meta(players, teams, season_states)` — all parameters optional:

| Parameter       | Required | Description                                  |
| --------------- | -------- | -------------------------------------------- |
| `players`       | No       | Player ID string                             |
| `teams`         | No       | Three-letter team code                       |
| `season_states` | No       | Season state filter                          |

`.game_meta(game_id)`, `.game_rail(game_id)`, `.goal_replay(game_id, event_number)`, `.play_replay(game_id, event_number)`, `.wsc_play_by_play(game_id)`:

| Parameter      | Required | Description                      |
| -------------- | -------- | -------------------------------- |
| `game_id`      | Yes      | NHL game ID (e.g. `2024020001`)  |
| `event_number` | Yes (replays only) | Event number within the game |

`.playoff_series_meta(year, series_letter)`:

| Parameter       | Required | Description                                        |
| --------------- | -------- | -------------------------------------------------- |
| `year`          | Yes      | Season year in `YYYY` format (e.g. `2024`)         |
| `series_letter` | Yes      | Series letter (e.g. `"A"`)                         |
