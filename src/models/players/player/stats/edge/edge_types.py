"""
SHARED NHL EDGE PRIMITIVE TYPES
"""
from __future__ import annotations
from dataclasses import dataclass

from ......core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class LeaderPlayer:
    """Lite player info included in each leaderboard entry."""
    first_name: LocalizedString
    last_name: LocalizedString
    slug: str | None
    headshot: str | None
    position: str | None
    sweater_number: int | None
    team: dict | None

    @classmethod
    def from_dict(cls, data: dict) -> LeaderPlayer:
        return cls(
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            slug = data.get("slug"),
            headshot = data.get("headshot"),
            position = data.get("position"),
            sweater_number = data.get("sweaterNumber"),
            team = data.get("team"),
        )

    def to_dict(self) -> dict:
        return {
            "first_name": self.first_name.default,
            "last_name": self.last_name.default,
            "slug": self.slug,
            "headshot": self.headshot,
            "position": self.position,
            "sweater_number": self.sweater_number,
            "team": self.team,
        }


@dataclass(slots=True, frozen=True)
class EdgeLeagueAvg:
    """League average values. imperial/metric for measurements, value for counts."""
    imperial: float | None
    metric: float | None
    value: float | None

    @classmethod
    def from_dict(cls, data: dict) -> EdgeLeagueAvg:
        return cls(
            imperial = data.get("imperial"),
            metric = data.get("metric"),
            value = data.get("value"),
        )

    def to_dict(self) -> dict:
        return {
            "imperial": self.imperial,
            "metric": self.metric,
            "value": self.value,
        }


@dataclass(slots=True, frozen=True)
class EdgeMeasurement:
    """
    A physical measurement with imperial/metric values, a league percentile ranking,
    league average, and an optional overlay with context for the peak event.
    """
    imperial: float | None
    metric: float | None
    percentile: float | None
    league_avg: EdgeLeagueAvg
    overlay: EdgeOverlay | None

    @classmethod
    def from_dict(cls, data: dict) -> EdgeMeasurement:
        overlay_data = data.get("overlay")
        return cls(
            imperial = data.get("imperial"),
            metric = data.get("metric"),
            percentile = data.get("percentile"),
            league_avg = EdgeLeagueAvg.from_dict(data.get("leagueAvg") or {}),
            overlay = EdgeOverlay.from_dict(overlay_data) if overlay_data else None,
        )

    def to_dict(self) -> dict:
        return {
            "imperial": self.imperial,
            "metric": self.metric,
            "percentile": self.percentile,
            "league_avg": self.league_avg.to_dict(),
            "overlay": self.overlay.to_dict() if self.overlay else None,
        }


@dataclass(slots=True, frozen=True)
class EdgeCount:
    """A count-based stat with a percentile ranking and league average count."""
    value: int | float | None
    percentile: float | None
    league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> EdgeCount:
        league_avg_raw = data.get("leagueAvg")
        if isinstance(league_avg_raw, dict):
            league_avg = league_avg_raw.get("value")
        elif isinstance(league_avg_raw, (int, float)):
            league_avg = league_avg_raw
        else:
            league_avg = None
        return cls(
            value = data.get("value"),
            percentile = data.get("percentile"),
            league_avg = league_avg,
        )

    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "percentile": self.percentile,
            "league_avg": self.league_avg,
        }


@dataclass(slots=True, frozen=True)
class OverlayTeam:
    """Team abbreviation and score for a game context overlay."""
    abbrev: str | None
    score: int | None

    @classmethod
    def from_dict(cls, data: dict) -> OverlayTeam:
        return cls(
            abbrev = data.get("abbrev"),
            score = data.get("score"),
        )

    def to_dict(self) -> dict:
        return {
            "abbrev": self.abbrev,
            "score": self.score,
        }


@dataclass(slots=True, frozen=True)
class OverlayGameOutcome:
    """Outcome of the game in which a peak stat occurred."""
    last_period_type: str | None
    ot_periods: int | None

    @classmethod
    def from_dict(cls, data: dict) -> OverlayGameOutcome:
        return cls(
            last_period_type = data.get("lastPeriodType"),
            ot_periods = data.get("otPeriods"),
        )

    def to_dict(self) -> dict:
        return {
            "last_period_type": self.last_period_type,
            "ot_periods": self.ot_periods,
        }


@dataclass(slots=True, frozen=True)
class OverlayPeriodDescriptor:
    """Period details for when a peak stat occurred."""
    number: int | None
    period_type: str | None
    max_regulation_periods: int | None

    @classmethod
    def from_dict(cls, data: dict) -> OverlayPeriodDescriptor:
        return cls(
            number = data.get("number"),
            period_type = data.get("periodType"),
            max_regulation_periods = data.get("maxRegulationPeriods"),
        )

    def to_dict(self) -> dict:
        return {
            "number": self.number,
            "period_type": self.period_type,
            "max_regulation_periods": self.max_regulation_periods,
        }


@dataclass(slots=True, frozen=True)
class EdgeOverlay:
    """Game context for the peak event of a measurement."""
    first_name: LocalizedString
    last_name: LocalizedString
    game_date: str | None
    away_team: OverlayTeam
    home_team: OverlayTeam
    game_outcome: OverlayGameOutcome
    period_descriptor: OverlayPeriodDescriptor
    time_in_period: str | None
    game_type: int | None

    @classmethod
    def from_dict(cls, data: dict) -> EdgeOverlay:
        player_data: dict = data.get("player") or {}
        return cls(
            first_name = LocalizedString(player_data.get("firstName")),
            last_name = LocalizedString(player_data.get("lastName")),
            game_date = data.get("gameDate"),
            away_team = OverlayTeam.from_dict(data.get("awayTeam") or {}),
            home_team = OverlayTeam.from_dict(data.get("homeTeam") or {}),
            game_outcome = OverlayGameOutcome.from_dict(data.get("gameOutcome") or {}),
            period_descriptor = OverlayPeriodDescriptor.from_dict(data.get("periodDescriptor") or {}),
            time_in_period = data.get("timeInPeriod"),
            game_type = data.get("gameType"),
        )

    def to_dict(self) -> dict:
        return {
            "first_name": self.first_name.default,
            "last_name": self.last_name.default,
            "game_date": self.game_date,
            "away_team": self.away_team.to_dict(),
            "home_team": self.home_team.to_dict(),
            "game_outcome": self.game_outcome.to_dict(),
            "period_descriptor": self.period_descriptor.to_dict(),
            "time_in_period": self.time_in_period,
            "game_type": self.game_type,
        }


@dataclass(slots=True, frozen=True)
class EdgeValue:
    """A simple imperial/metric measurement with no ranking data."""
    imperial: float | None
    metric: float | None

    @classmethod
    def from_dict(cls, data: dict) -> EdgeValue:
        return cls(
            imperial = data.get("imperial"),
            metric = data.get("metric"),
        )

    def to_dict(self) -> dict:
        return {
            "imperial": self.imperial,
            "metric": self.metric,
        }


@dataclass(slots=True, frozen=True)
class EdgePeak:
    """An imperial/metric measurement with context overlay for the peak event, but no ranking data."""
    imperial: float | None
    metric: float | None
    overlay: EdgeOverlay | None

    @classmethod
    def from_dict(cls, data: dict) -> EdgePeak:
        overlay_data = data.get("overlay")
        return cls(
            imperial = data.get("imperial"),
            metric = data.get("metric"),
            overlay = EdgeOverlay.from_dict(overlay_data) if overlay_data else None,
        )

    def to_dict(self) -> dict:
        return {
            "imperial": self.imperial,
            "metric": self.metric,
            "overlay": self.overlay.to_dict() if self.overlay else None,
        }


@dataclass(slots=True, frozen=True)
class EdgeSeason:
    """A season for which NHL Edge stats are available."""
    id: int | None
    game_types: list

    @classmethod
    def from_dict(cls, data: dict) -> EdgeSeason:
        return cls(
            id = data.get("id"),
            game_types = data.get("gameTypes") or [],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "game_types": self.game_types,
        }
