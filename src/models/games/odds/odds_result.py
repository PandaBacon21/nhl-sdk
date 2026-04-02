"""
PARTNER ODDS MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class OddsEntry:
    """A single odds line: type, American-format value, and qualifier (e.g. 'O6.5')."""
    description: str | None
    value: float | None
    qualifier: str | None

    @classmethod
    def from_dict(cls, data: dict) -> OddsEntry:
        return cls(
            description = data.get("description"),
            value = data.get("value"),
            qualifier = data.get("qualifier"),
        )

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "value": self.value,
            "qualifier": self.qualifier,
        }


@dataclass(slots=True, frozen=True)
class OddsTeam:
    """Team info with associated partner odds lines."""
    id: int | None
    name: LocalizedString
    abbrev: str | None
    logo: str | None
    odds: list[OddsEntry]

    @classmethod
    def from_dict(cls, data: dict) -> OddsTeam:
        return cls(
            id = data.get("id"),
            name = LocalizedString(data.get("name")),
            abbrev = data.get("abbrev"),
            logo = data.get("logo"),
            odds = [OddsEntry.from_dict(o) for o in data.get("odds") or []],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name.default,
            "abbrev": self.abbrev,
            "logo": self.logo,
            "odds": [o.to_dict() for o in self.odds],
        }


@dataclass(slots=True, frozen=True)
class OddsGame:
    """A game with partner odds for both the home and away team."""
    game_id: int | None
    game_type: int | None
    start_time_utc: str | None
    home_team: OddsTeam
    away_team: OddsTeam

    @classmethod
    def from_dict(cls, data: dict) -> OddsGame:
        return cls(
            game_id = data.get("gameId"),
            game_type = data.get("gameType"),
            start_time_utc = data.get("startTimeUTC"),
            home_team = OddsTeam.from_dict(data.get("homeTeam") or {}),
            away_team = OddsTeam.from_dict(data.get("awayTeam") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "game_id": self.game_id,
            "game_type": self.game_type,
            "start_time_utc": self.start_time_utc,
            "home_team": self.home_team.to_dict(),
            "away_team": self.away_team.to_dict(),
        }


@dataclass(slots=True, frozen=True)
class PartnerOddsResult:
    """
    Partner odds for all games on the current odds date.

    Instances of this class are accessed via `client.games.odds.get_odds()`.
    """
    current_odds_date: str | None
    last_updated_utc: str | None
    games: list[OddsGame]

    @classmethod
    def from_dict(cls, data: dict) -> PartnerOddsResult:
        return cls(
            current_odds_date = data.get("currentOddsDate"),
            last_updated_utc = data.get("lastUpdatedUTC"),
            games = [OddsGame.from_dict(g) for g in data.get("games") or []],
        )

    def to_dict(self) -> dict:
        return {
            "current_odds_date": self.current_odds_date,
            "last_updated_utc": self.last_updated_utc,
            "games": [g.to_dict() for g in self.games],
        }
