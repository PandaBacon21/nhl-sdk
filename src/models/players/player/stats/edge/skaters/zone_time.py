"""
SKATER ZONE TIME MODEL
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ZoneTimeStrength:
    """Zone time percentages, percentile rankings, and league averages for a strength situation."""
    strength_code: str | None
    offensive_zone_pctg: float | None
    offensive_zone_percentile: float | None
    offensive_zone_league_avg: float | None
    neutral_zone_pctg: float | None
    neutral_zone_percentile: float | None
    neutral_zone_league_avg: float | None
    defensive_zone_pctg: float | None
    defensive_zone_percentile: float | None
    defensive_zone_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneTimeStrength:
        return cls(
            strength_code = data.get("strengthCode"),
            offensive_zone_pctg = data.get("offensiveZonePctg"),
            offensive_zone_percentile = data.get("offensiveZonePercentile"),
            offensive_zone_league_avg = data.get("offensiveZoneLeagueAvg"),
            neutral_zone_pctg = data.get("neutralZonePctg"),
            neutral_zone_percentile = data.get("neutralZonePercentile"),
            neutral_zone_league_avg = data.get("neutralZoneLeagueAvg"),
            defensive_zone_pctg = data.get("defensiveZonePctg"),
            defensive_zone_percentile = data.get("defensiveZonePercentile"),
            defensive_zone_league_avg = data.get("defensiveZoneLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "strength_code": self.strength_code,
            "offensive_zone_pctg": self.offensive_zone_pctg,
            "offensive_zone_percentile": self.offensive_zone_percentile,
            "offensive_zone_league_avg": self.offensive_zone_league_avg,
            "neutral_zone_pctg": self.neutral_zone_pctg,
            "neutral_zone_percentile": self.neutral_zone_percentile,
            "neutral_zone_league_avg": self.neutral_zone_league_avg,
            "defensive_zone_pctg": self.defensive_zone_pctg,
            "defensive_zone_percentile": self.defensive_zone_percentile,
            "defensive_zone_league_avg": self.defensive_zone_league_avg,
        }


@dataclass(slots=True, frozen=True)
class ZoneStartsDetail:
    """Zone start percentages and percentile rankings."""
    offensive_zone_starts_pctg: float | None
    offensive_zone_starts_percentile: float | None
    neutral_zone_starts_pctg: float | None
    neutral_zone_starts_percentile: float | None
    defensive_zone_starts_pctg: float | None
    defensive_zone_starts_percentile: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneStartsDetail:
        return cls(
            offensive_zone_starts_pctg = data.get("offensiveZoneStartsPctg"),
            offensive_zone_starts_percentile = data.get("offensiveZoneStartsPctgPercentile"),
            neutral_zone_starts_pctg = data.get("neutralZoneStartsPctg"),
            neutral_zone_starts_percentile = data.get("neutralZoneStartsPctgPercentile"),
            defensive_zone_starts_pctg = data.get("defensiveZoneStartsPctg"),
            defensive_zone_starts_percentile = data.get("defensiveZoneStartsPctgPercentile"),
        )

    def to_dict(self) -> dict:
        return {
            "offensive_zone_starts_pctg": self.offensive_zone_starts_pctg,
            "offensive_zone_starts_percentile": self.offensive_zone_starts_percentile,
            "neutral_zone_starts_pctg": self.neutral_zone_starts_pctg,
            "neutral_zone_starts_percentile": self.neutral_zone_starts_percentile,
            "defensive_zone_starts_pctg": self.defensive_zone_starts_pctg,
            "defensive_zone_starts_percentile": self.defensive_zone_starts_percentile,
        }


@dataclass(slots=True, frozen=True)
class ZoneTime:
    """
    Per-player zone time detail.

    Provides zone time percentages with percentile rankings for all/even/power-play/penalty-kill
    situations, plus zone start percentages.

    Instances of this class are accessed via `Stats.edge.skater.zone_time()`.
    """
    zone_time_by_strength: list
    zone_starts: ZoneStartsDetail

    @classmethod
    def from_dict(cls, data: dict) -> ZoneTime:
        return cls(
            zone_time_by_strength = [ZoneTimeStrength.from_dict(z) for z in data.get("zoneTimeDetails") or []],
            zone_starts = ZoneStartsDetail.from_dict(data.get("zoneStarts") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "zone_time_by_strength": [z.to_dict() for z in self.zone_time_by_strength],
            "zone_starts": self.zone_starts.to_dict(),
        }
