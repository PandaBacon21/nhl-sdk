"""
Tests for games network models:
  NetworkBroadcast, NetworkScheduleResult
"""
from src.models.games.network.network_schedule import NetworkBroadcast, NetworkScheduleResult


LIVE_BROADCAST = {
    "startTime": "2026-03-25T00:00:00",
    "endTime": "2026-03-25T01:00:00",
    "durationSeconds": 3600,
    "title": "On The Fly With Bonus Coverage",
    "description": "Missed the game? On The Fly conveniently recaps all games, every night.",
    "houseNumber": "H60ANAVAN03242026",
    "broadcastType": "HD",
    "broadcastStatus": "LIVE",
    "broadcastImageUrl": "onthefly.png",
}

COMPLETED_BROADCAST = {
    "startTime": "2026-03-25T12:00:00",
    "endTime": "2026-03-25T14:00:00",
    "durationSeconds": 7200,
    "title": "NHL Game",
    "description": "Minnesota Wild at Tampa Bay Lightning on 3/24/2026 From Benchmark International Arena",
    "houseNumber": "H120MINTBL03242026",
    "broadcastType": "HD",
    "broadcastStatus": "",
    "broadcastImageUrl": "nhl.png",
}


# ==========================================================================
# NETWORK BROADCAST
# ==========================================================================

def test_network_broadcast_live() -> None:
    b = NetworkBroadcast.from_dict(LIVE_BROADCAST)
    assert b.start_time == "2026-03-25T00:00:00"
    assert b.end_time == "2026-03-25T01:00:00"
    assert b.duration_seconds == 3600
    assert b.title == "On The Fly With Bonus Coverage"
    assert b.description is not None
    assert b.house_number == "H60ANAVAN03242026"
    assert b.broadcast_type == "HD"
    assert b.broadcast_status == "LIVE"
    assert b.broadcast_image_url == "onthefly.png"


def test_network_broadcast_empty_status_normalized_to_none() -> None:
    """Empty string broadcastStatus should normalize to None."""
    b = NetworkBroadcast.from_dict(COMPLETED_BROADCAST)
    assert b.broadcast_status is None


def test_network_broadcast_empty_image_url_normalized_to_none() -> None:
    data = {**LIVE_BROADCAST, "broadcastImageUrl": ""}
    b = NetworkBroadcast.from_dict(data)
    assert b.broadcast_image_url is None


def test_network_broadcast_game_entry() -> None:
    b = NetworkBroadcast.from_dict(COMPLETED_BROADCAST)
    assert b.title == "NHL Game"
    assert b.duration_seconds == 7200
    assert b.house_number == "H120MINTBL03242026"
    assert b.broadcast_status is None


def test_network_broadcast_empty() -> None:
    b = NetworkBroadcast.from_dict({})
    assert b.start_time is None
    assert b.end_time is None
    assert b.duration_seconds is None
    assert b.title is None
    assert b.description is None
    assert b.house_number is None
    assert b.broadcast_type is None
    assert b.broadcast_status is None
    assert b.broadcast_image_url is None


# ==========================================================================
# NETWORK SCHEDULE RESULT
# ==========================================================================

SCHEDULE_DATA = {
    "date": "2026-03-25",
    "startDate": "2026-03-11",
    "endDate": "2026-04-12",
    "broadcasts": [LIVE_BROADCAST, COMPLETED_BROADCAST],
}


def test_network_schedule_result_from_dict() -> None:
    result = NetworkScheduleResult.from_dict(SCHEDULE_DATA)
    assert result.date == "2026-03-25"
    assert result.start_date == "2026-03-11"
    assert result.end_date == "2026-04-12"
    assert len(result.broadcasts) == 2


def test_network_schedule_result_broadcast_data() -> None:
    result = NetworkScheduleResult.from_dict(SCHEDULE_DATA)
    live = result.broadcasts[0]
    assert live.broadcast_status == "LIVE"
    assert live.title == "On The Fly With Bonus Coverage"
    game = result.broadcasts[1]
    assert game.title == "NHL Game"
    assert game.duration_seconds == 7200


def test_network_schedule_result_no_broadcasts() -> None:
    result = NetworkScheduleResult.from_dict({"date": "2026-03-25", "broadcasts": []})
    assert result.date == "2026-03-25"
    assert result.broadcasts == []


def test_network_schedule_result_empty() -> None:
    result = NetworkScheduleResult.from_dict({})
    assert result.date is None
    assert result.start_date is None
    assert result.end_date is None
    assert result.broadcasts == []
