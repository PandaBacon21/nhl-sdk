"""
TEAM ZONE TIME DETAIL RESULT
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ZoneTimeEntry:
    """Zone time percentages, ranks, and league averages for one strength code."""
    strength_code: str | None
    offensive_zone_pctg: float | None
    offensive_zone_rank: int | None
    offensive_zone_league_avg: float | None
    neutral_zone_pctg: float | None
    neutral_zone_rank: int | None
    neutral_zone_league_avg: float | None
    defensive_zone_pctg: float | None
    defensive_zone_rank: int | None
    defensive_zone_league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneTimeEntry:
        return cls(
            strength_code = data.get("strengthCode"),
            offensive_zone_pctg = data.get("offensiveZonePctg"),
            offensive_zone_rank = data.get("offensiveZoneRank"),
            offensive_zone_league_avg = data.get("offensiveZoneLeagueAvg"),
            neutral_zone_pctg = data.get("neutralZonePctg"),
            neutral_zone_rank = data.get("neutralZoneRank"),
            neutral_zone_league_avg = data.get("neutralZoneLeagueAvg"),
            defensive_zone_pctg = data.get("defensiveZonePctg"),
            defensive_zone_rank = data.get("defensiveZoneRank"),
            defensive_zone_league_avg = data.get("defensiveZoneLeagueAvg"),
        )

    def to_dict(self) -> dict:
        return {
            "strength_code": self.strength_code,
            "offensive_zone_pctg": self.offensive_zone_pctg,
            "offensive_zone_rank": self.offensive_zone_rank,
            "offensive_zone_league_avg": self.offensive_zone_league_avg,
            "neutral_zone_pctg": self.neutral_zone_pctg,
            "neutral_zone_rank": self.neutral_zone_rank,
            "neutral_zone_league_avg": self.neutral_zone_league_avg,
            "defensive_zone_pctg": self.defensive_zone_pctg,
            "defensive_zone_rank": self.defensive_zone_rank,
            "defensive_zone_league_avg": self.defensive_zone_league_avg,
        }


@dataclass(slots=True, frozen=True)
class ZoneShotDifferential:
    """Shot differential metrics with league ranks."""
    shot_attempt_differential: float | None
    shot_attempt_differential_rank: int | None
    sog_differential: float | None
    sog_differential_rank: int | None

    @classmethod
    def from_dict(cls, data: dict) -> ZoneShotDifferential:
        return cls(
            shot_attempt_differential = data.get("shotAttemptDifferential"),
            shot_attempt_differential_rank = data.get("shotAttemptDifferentialRank"),
            sog_differential = data.get("sogDifferential"),
            sog_differential_rank = data.get("sogDifferentialRank"),
        )

    def to_dict(self) -> dict:
        return {
            "shot_attempt_differential": self.shot_attempt_differential,
            "shot_attempt_differential_rank": self.shot_attempt_differential_rank,
            "sog_differential": self.sog_differential,
            "sog_differential_rank": self.sog_differential_rank,
        }


@dataclass(slots=True, frozen=True)
class TeamZoneDetailResult:
    """
    Team zone time detail stats by strength code (all/es/pp/pk),
    plus shot differential with league ranks.

    Instances of this class are accessed via `client.teams.stats.edge.zone_time`.
    """
    zone_time_details: list[ZoneTimeEntry]
    shot_differential: ZoneShotDifferential

    @classmethod
    def from_dict(cls, data: dict) -> TeamZoneDetailResult:
        return cls(
            zone_time_details = [ZoneTimeEntry.from_dict(e) for e in data.get("zoneTimeDetails") or []],
            shot_differential = ZoneShotDifferential.from_dict(data.get("shotDifferential") or {}),
        )

    def to_dict(self) -> dict:
        return {
            "zone_time_details": [e.to_dict() for e in self.zone_time_details],
            "shot_differential": self.shot_differential.to_dict(),
        }
