"""
SHARED PRIMITIVE TYPES FOR TEAMS EDGE (LEAGUE-WIDE)
"""
from __future__ import annotations
from dataclasses import dataclass

from ...players.player.player_stats.edge.player_edge_types import (
    OverlayTeam, OverlayGameOutcome, OverlayPeriodDescriptor,
)


@dataclass(slots=True, frozen=True)
class TeamEdgeOverlay:
    """Game context for a peak team stat — no player component."""
    game_date: str | None
    away_team: OverlayTeam
    home_team: OverlayTeam
    game_outcome: OverlayGameOutcome
    period_descriptor: OverlayPeriodDescriptor
    game_type: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgeOverlay:
        return cls(
            game_date = data.get("gameDate"),
            away_team = OverlayTeam.from_dict(data.get("awayTeam") or {}),
            home_team = OverlayTeam.from_dict(data.get("homeTeam") or {}),
            game_outcome = OverlayGameOutcome.from_dict(data.get("gameOutcome") or {}),
            period_descriptor = OverlayPeriodDescriptor.from_dict(data.get("periodDescriptor") or {}),
            game_type = data.get("gameType"),
        )

    def to_dict(self) -> dict:
        return {
            "game_date": self.game_date,
            "away_team": self.away_team.to_dict(),
            "home_team": self.home_team.to_dict(),
            "game_outcome": self.game_outcome.to_dict(),
            "period_descriptor": self.period_descriptor.to_dict(),
            "game_type": self.game_type,
        }


@dataclass(slots=True, frozen=True)
class TeamEdgePeak:
    """An imperial/metric measurement with an optional game context overlay."""
    imperial: float | None
    metric: float | None
    overlay: TeamEdgeOverlay | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgePeak:
        overlay_data = data.get("overlay")
        return cls(
            imperial = data.get("imperial"),
            metric = data.get("metric"),
            overlay = TeamEdgeOverlay.from_dict(overlay_data) if overlay_data else None,
        )

    def to_dict(self) -> dict:
        return {
            "imperial": self.imperial,
            "metric": self.metric,
            "overlay": self.overlay.to_dict() if self.overlay else None,
        }
