"""
STANDINGS RESULT MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from .standing_entry import StandingEntry


@dataclass(slots=True, frozen=True)
class StandingsResult:
    """Top-level response from the standings endpoint."""
    wild_card_indicator: bool | None
    standings_date_time_utc: str | None
    standings: list

    @classmethod
    def from_dict(cls, data: dict) -> StandingsResult:
        return cls(
            wild_card_indicator = data.get("wildCardIndicator"),
            standings_date_time_utc = data.get("standingsDateTimeUtc"),
            standings = [StandingEntry.from_dict(e) for e in data.get("standings") or []],
        )
