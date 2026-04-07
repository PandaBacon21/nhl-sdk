"""
Service tests for the named report methods on PlayerStats.
"""
from src.models.players.player.player_stats.player_stats import PlayerStats
from src.models.players.player.player_stats.reports import (
    SkaterBioReport, SkaterFaceoffPctReport, SkaterFaceoffWinsReport,
    SkaterGoalsForAgainstReport, SkaterPenaltiesReport, SkaterPenaltyKillReport,
    SkaterPenaltyShotsReport, SkaterPowerPlayReport, SkaterPuckPossessionsReport,
    SkaterRealtimeReport, SkaterShotTypeReport, SkaterTimeOnIceReport,
    SkaterPercentagesReport,
    GoalieBioReport, GoalieAdvancedReport, GoalieDaysRestReport,
    GoaliePenaltyShotsReport, GoalieSavesByStrengthReport,
    GoalieShootoutReport, GoalieStartedVsRelievedReport,
)

from .conftest import ok

PID = 8477492
GOALIE_PID = 8476883

LANDING = {
    "featuredStats": {},
    "careerTotals": {},
    "seasonTotals": [],
    "last5Games": [],
}

SKATER_ROW = {"playerId": PID, "skaterFullName": "Nathan MacKinnon"}
GOALIE_ROW = {"playerId": GOALIE_PID, "goalieFullName": "Andrei Vasilevskiy"}


def _skater(mock_client) -> PlayerStats:
    return PlayerStats(pos="C", pid=PID, data=LANDING, client=mock_client)


def _goalie(mock_client) -> PlayerStats:
    return PlayerStats(pos="G", pid=GOALIE_PID, data=LANDING, client=mock_client)


def _set_skater_response(mock_client, row=None):
    data = {"data": [row or SKATER_ROW], "total": 1}
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.return_value = ok(data)


def _set_goalie_response(mock_client, row=None):
    data = {"data": [row or GOALIE_ROW], "total": 1}
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_stats.return_value = ok(data)


# ==========================================================================
# bio()
# ==========================================================================

def test_bio_skater_cache_miss(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    result = ps.bio()
    assert isinstance(result, SkaterBioReport)
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.assert_called_once()


def test_bio_skater_cache_hit(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    _ = ps.bio()
    _ = ps.bio()
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.assert_called_once()


def test_bio_goalie_cache_miss(mock_client) -> None:
    _set_goalie_response(mock_client)
    ps = _goalie(mock_client)
    result = ps.bio()
    assert isinstance(result, GoalieBioReport)
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_stats.assert_called_once()


def test_bio_returns_none_on_empty_data(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.return_value = ok({"data": []})
    ps = _skater(mock_client)
    assert ps.bio() is None


# ==========================================================================
# penalty_shots() — both positions
# ==========================================================================

def test_penalty_shots_skater(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    result = ps.penalty_shots()
    assert isinstance(result, SkaterPenaltyShotsReport)


def test_penalty_shots_goalie(mock_client) -> None:
    _set_goalie_response(mock_client)
    ps = _goalie(mock_client)
    result = ps.penalty_shots()
    assert isinstance(result, GoaliePenaltyShotsReport)


def test_penalty_shots_cache_hit(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    _ = ps.penalty_shots(season=20232024, game_type=2)
    _ = ps.penalty_shots(season=20232024, game_type=2)
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.assert_called_once()


# ==========================================================================
# Skater-only methods return None for goalies
# ==========================================================================

def test_skater_only_methods_return_none_for_goalie(mock_client) -> None:
    ps = _goalie(mock_client)
    assert ps.faceoff_pct() is None
    assert ps.faceoff_wins() is None
    assert ps.goals_for_against() is None
    assert ps.penalties() is None
    assert ps.penalty_kill() is None
    assert ps.powerplay() is None
    assert ps.puck_possessions() is None
    assert ps.realtime() is None
    assert ps.shot_type() is None
    assert ps.time_on_ice() is None
    assert ps.percentages() is None
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.assert_not_called()
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_stats.assert_not_called()


# ==========================================================================
# Goalie-only methods return None for skaters
# ==========================================================================

def test_goalie_only_methods_return_none_for_skater(mock_client) -> None:
    ps = _skater(mock_client)
    assert ps.advanced() is None
    assert ps.days_rest() is None
    assert ps.saves_by_strength() is None
    assert ps.shootout() is None
    assert ps.started_vs_relieved() is None
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.assert_not_called()
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_stats.assert_not_called()


# ==========================================================================
# Skater report methods — cache miss / hit / return type
# ==========================================================================

def test_faceoff_pct_cache_miss(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    result = ps.faceoff_pct(season=20232024, game_type=2)
    assert isinstance(result, SkaterFaceoffPctReport)
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.assert_called_once()


def test_faceoff_pct_cache_hit(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    _ = ps.faceoff_pct(season=20232024, game_type=2)
    _ = ps.faceoff_pct(season=20232024, game_type=2)
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.assert_called_once()


def test_faceoff_wins_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).faceoff_wins(season=20232024)
    assert isinstance(result, SkaterFaceoffWinsReport)


def test_goals_for_against_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).goals_for_against(season=20232024)
    assert isinstance(result, SkaterGoalsForAgainstReport)


def test_penalties_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).penalties(season=20232024)
    assert isinstance(result, SkaterPenaltiesReport)


def test_penalty_kill_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).penalty_kill(season=20232024)
    assert isinstance(result, SkaterPenaltyKillReport)


def test_powerplay_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).powerplay(season=20232024)
    assert isinstance(result, SkaterPowerPlayReport)


def test_puck_possessions_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).puck_possessions(season=20232024)
    assert isinstance(result, SkaterPuckPossessionsReport)


def test_realtime_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).realtime(season=20232024)
    assert isinstance(result, SkaterRealtimeReport)


def test_shot_type_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).shot_type(season=20232024)
    assert isinstance(result, SkaterShotTypeReport)


def test_time_on_ice_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).time_on_ice(season=20232024)
    assert isinstance(result, SkaterTimeOnIceReport)


def test_percentages_returns_report(mock_client) -> None:
    _set_skater_response(mock_client)
    result = _skater(mock_client).percentages(season=20232024)
    assert isinstance(result, SkaterPercentagesReport)


# ==========================================================================
# Goalie report methods — cache miss / hit / return type
# ==========================================================================

def test_advanced_cache_miss(mock_client) -> None:
    _set_goalie_response(mock_client)
    ps = _goalie(mock_client)
    result = ps.advanced(season=20232024, game_type=2)
    assert isinstance(result, GoalieAdvancedReport)
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_stats.assert_called_once()


def test_advanced_cache_hit(mock_client) -> None:
    _set_goalie_response(mock_client)
    ps = _goalie(mock_client)
    _ = ps.advanced(season=20232024, game_type=2)
    _ = ps.advanced(season=20232024, game_type=2)
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_stats.assert_called_once()


def test_days_rest_returns_report(mock_client) -> None:
    _set_goalie_response(mock_client)
    result = _goalie(mock_client).days_rest(season=20232024)
    assert isinstance(result, GoalieDaysRestReport)


def test_saves_by_strength_returns_report(mock_client) -> None:
    _set_goalie_response(mock_client)
    result = _goalie(mock_client).saves_by_strength(season=20232024)
    assert isinstance(result, GoalieSavesByStrengthReport)


def test_shootout_returns_report(mock_client) -> None:
    _set_goalie_response(mock_client)
    result = _goalie(mock_client).shootout(season=20232024)
    assert isinstance(result, GoalieShootoutReport)


def test_started_vs_relieved_returns_report(mock_client) -> None:
    _set_goalie_response(mock_client)
    result = _goalie(mock_client).started_vs_relieved(season=20232024)
    assert isinstance(result, GoalieStartedVsRelievedReport)


# ==========================================================================
# Different season/game_type combos use separate cache keys
# ==========================================================================

def test_different_seasons_use_separate_cache_keys(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    _ = ps.realtime(season=20232024, game_type=2)
    _ = ps.realtime(season=20222023, game_type=2)
    assert mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.call_count == 2


def test_different_game_types_use_separate_cache_keys(mock_client) -> None:
    _set_skater_response(mock_client)
    ps = _skater(mock_client)
    _ = ps.powerplay(season=20232024, game_type=2)
    _ = ps.powerplay(season=20232024, game_type=3)
    assert mock_client._api.api_stats.call_nhl_stats_players.get_skater_stats.call_count == 2
