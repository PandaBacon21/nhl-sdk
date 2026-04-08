"""
NETWORK TV SCHEDULE MODELS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class NetworkBroadcast:
    start_time: str | None
    end_time: str | None
    duration_seconds: int | None
    title: str | None
    description: str | None
    house_number: str | None
    broadcast_type: str | None
    broadcast_status: str | None
    broadcast_image_url: str | None

    @classmethod
    def from_dict(cls, data: dict) -> NetworkBroadcast:
        return cls(
            start_time = data.get("startTime"),
            end_time = data.get("endTime"),
            duration_seconds = data.get("durationSeconds"),
            title = data.get("title"),
            description = data.get("description"),
            house_number = data.get("houseNumber"),
            broadcast_type = data.get("broadcastType"),
            broadcast_status = data.get("broadcastStatus") or None,
            broadcast_image_url = data.get("broadcastImageUrl") or None,
        )


@dataclass(slots=True, frozen=True)
class NetworkScheduleResult:
    date: str | None
    start_date: str | None
    end_date: str | None
    broadcasts: list[NetworkBroadcast]

    @classmethod
    def from_dict(cls, data: dict) -> NetworkScheduleResult:
        return cls(
            date = data.get("date"),
            start_date = data.get("startDate"),
            end_date = data.get("endDate"),
            broadcasts = [NetworkBroadcast.from_dict(b) for b in data.get("broadcasts") or []],
        )
