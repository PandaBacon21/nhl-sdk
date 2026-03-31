"""
PARTNER ODDS MODELS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PartnerOddsResult:
    current_odds_date: str | None
    last_updated_utc: str | None
    games: list

    @classmethod
    def from_dict(cls, data: dict) -> PartnerOddsResult:
        return cls(
            current_odds_date = data.get("currentOddsDate"),
            last_updated_utc = data.get("lastUpdatedUTC"),
            games = data.get("games") or [],
        )
