from src.models.players.player.achievements.player_achievements import PlayerAchievements
from src.models.players.player.achievements.player_milestone import PlayerMilestone
from tests.service_tests.conftest import ok

PID = 8477492
POS_SKATER = "C"
POS_GOALIE = "G"

LANDING_DATA = {
    "inTop100AllTime": 1,
    "inHHOF": 0,
    "awards": [],
    "featuredStats": {},
}

MILESTONE_ROW = {
    "id": 1,
    "playerId": PID,
    "milestone": "Goals",
    "milestoneAmount": 500,
    "goals": 473,
    "assists": 789,
    "points": 1262,
    "gamesPlayed": 1040,
    "gameTypeId": 2,
    "currentTeamId": 21,
    "teamAbbrev": "COL",
    "teamCommonName": "Avalanche",
    "teamFullName": "Colorado Avalanche",
    "teamPlaceName": "Colorado",
    "playerFullName": "Nathan MacKinnon",
}


def _skater(mock_client) -> PlayerAchievements:
    return PlayerAchievements(pid=PID, pos=POS_SKATER, data=LANDING_DATA, client=mock_client)


def _goalie(mock_client) -> PlayerAchievements:
    return PlayerAchievements(pid=PID, pos=POS_GOALIE, data=LANDING_DATA, client=mock_client)


# ==========================================================================
# milestones()
# ==========================================================================

def test_milestones_skater_calls_skater_endpoint(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok(
        {"data": [MILESTONE_ROW], "total": 1}
    )
    pa = _skater(mock_client)
    result = pa.milestones()
    assert result is not None
    assert len(result) == 1
    assert isinstance(result[0], PlayerMilestone)
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.assert_called_once()
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.assert_not_called()


def test_milestones_goalie_calls_goalie_endpoint(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.return_value = ok(
        {"data": [MILESTONE_ROW], "total": 1}
    )
    pa = _goalie(mock_client)
    result = pa.milestones()
    assert result is not None
    assert len(result) == 1
    assert isinstance(result[0], PlayerMilestone)
    mock_client._api.api_stats.call_nhl_stats_players.get_goalie_milestones.assert_called_once()
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.assert_not_called()


def test_milestones_with_game_type(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok(
        {"data": [MILESTONE_ROW], "total": 1}
    )
    pa = _skater(mock_client)
    result = pa.milestones(game_type=2)
    assert result is not None
    call_kwargs = mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.call_args
    assert "gameTypeId=2" in call_kwargs.kwargs["cayenne_exp"]


def test_milestones_cache_hit(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok(
        {"data": [MILESTONE_ROW], "total": 1}
    )
    pa = _skater(mock_client)
    _ = pa.milestones()
    _ = pa.milestones()
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.assert_called_once()


def test_milestones_returns_none_when_empty(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok(
        {"data": [], "total": 0}
    )
    pa = _skater(mock_client)
    result = pa.milestones()
    assert result is None


def test_milestones_milestone_fields(mock_client) -> None:
    mock_client._api.api_stats.call_nhl_stats_players.get_skater_milestones.return_value = ok(
        {"data": [MILESTONE_ROW], "total": 1}
    )
    pa = _skater(mock_client)
    result = pa.milestones()
    m = result[0]
    assert m.player_id == PID
    assert m.milestone == "Goals"
    assert m.milestone_amount == 500
    assert m.goals == 473
    assert m.team_abbrev == "COL"
