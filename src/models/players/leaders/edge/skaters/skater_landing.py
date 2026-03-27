"""
SKATER EDGE LANDING MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ....player.player_stats.edge.player_edge_types import EdgeSeason, LeaderPlayer, EdgeValue, EdgeOverlay


@dataclass(slots=True, frozen=True)
class SkaterPeakLeader:
    """Leader entry for a peak speed stat (hardest shot or max skating speed)."""
    player: LeaderPlayer
    stat: EdgeValue
    overlay: EdgeOverlay | None

    @classmethod
    def from_dict(cls, data: dict, stat_key: str) -> SkaterPeakLeader:
        overlay_data = data.get("overlay")
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            stat = EdgeValue.from_dict(data.get(stat_key) or {}),
            overlay = EdgeOverlay.from_dict(overlay_data) if overlay_data else None,
        )


@dataclass(slots=True, frozen=True)
class SkaterDistanceLeader:
    """Leader entry for a skating distance stat."""
    player: LeaderPlayer
    distance_skated: EdgeValue
    overlay: EdgeOverlay | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterDistanceLeader:
        overlay_data = data.get("overlay")
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            distance_skated = EdgeValue.from_dict(data.get("distanceSkated") or {}),
            overlay = EdgeOverlay.from_dict(overlay_data) if overlay_data else None,
        )


@dataclass(slots=True, frozen=True)
class SogAreaDetail:
    """Shot on goal detail for a specific ice area."""
    area: str | None
    sog: int | None
    sog_percentile: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SogAreaDetail:
        return cls(
            area = data.get("area"),
            sog = data.get("sog"),
            sog_percentile = data.get("sogPercentile"),
        )


@dataclass(slots=True, frozen=True)
class SkaterSOGLeader:
    """Leader entry for high danger shots on goal."""
    player: LeaderPlayer
    sog: int | None
    shot_location_details: list[SogAreaDetail]

    @classmethod
    def from_dict(cls, data: dict) -> SkaterSOGLeader:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            sog = data.get("sog"),
            shot_location_details = [SogAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
        )


@dataclass(slots=True, frozen=True)
class SkaterZoneTimeLeader:
    """Leader entry for offensive or defensive zone time percentage."""
    player: LeaderPlayer
    zone_time: float | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterZoneTimeLeader:
        return cls(
            player = LeaderPlayer.from_dict(data.get("player") or {}),
            zone_time = data.get("zoneTime"),
        )


@dataclass(slots=True, frozen=True)
class SkaterLandingLeaders:
    """All leader categories from the skater Edge landing page."""
    hardest_shot: SkaterPeakLeader
    max_skating_speed: SkaterPeakLeader
    total_distance_skated: SkaterDistanceLeader
    distance_max_game: SkaterDistanceLeader
    high_danger_sog: SkaterSOGLeader
    offensive_zone_time: SkaterZoneTimeLeader
    defensive_zone_time: SkaterZoneTimeLeader

    @classmethod
    def from_dict(cls, data: dict) -> SkaterLandingLeaders:
        return cls(
            hardest_shot = SkaterPeakLeader.from_dict(data.get("hardestShot") or {}, stat_key="shotSpeed"),
            max_skating_speed = SkaterPeakLeader.from_dict(data.get("maxSkatingSpeed") or {}, stat_key="skatingSpeed"),
            total_distance_skated = SkaterDistanceLeader.from_dict(data.get("totalDistanceSkated") or {}),
            distance_max_game = SkaterDistanceLeader.from_dict(data.get("distanceMaxGame") or {}),
            high_danger_sog = SkaterSOGLeader.from_dict(data.get("highDangerSOG") or {}),
            offensive_zone_time = SkaterZoneTimeLeader.from_dict(data.get("offensiveZoneTime") or {}),
            defensive_zone_time = SkaterZoneTimeLeader.from_dict(data.get("defensiveZoneTime") or {}),
        )


@dataclass(slots=True, frozen=True)
class SkaterLanding:
    """Top-level model for the skater Edge landing page response."""
    seasons_with_edge: list[EdgeSeason]
    leaders: SkaterLandingLeaders

    @classmethod
    def from_dict(cls, data: dict) -> SkaterLanding:
        return cls(
            seasons_with_edge = [EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            leaders = SkaterLandingLeaders.from_dict(data.get("leaders") or {}),
        )
