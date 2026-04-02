"""
SHARED TEAM EDGE PRIMITIVE TYPES
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString
from .....models.players.player.player_stats.edge.player_edge_types import (
    EdgeLeagueAvg, EdgeOverlay,
)


@dataclass(slots=True, frozen=True)
class TeamEdgeMeasurement:
    """A physical measurement with imperial/metric values, a league rank, league average, and optional overlay."""
    imperial: float | None
    metric: float | None
    rank: int | None
    league_avg: EdgeLeagueAvg
    overlay: EdgeOverlay | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgeMeasurement:
        overlay_data = data.get("overlay")
        return cls(
            imperial = data.get("imperial"),
            metric = data.get("metric"),
            rank = data.get("rank"),
            league_avg = EdgeLeagueAvg.from_dict(data.get("leagueAvg") or {}),
            overlay = EdgeOverlay.from_dict(overlay_data) if overlay_data else None,
        )

    def to_dict(self) -> dict:
        return {
            "imperial": self.imperial,
            "metric": self.metric,
            "rank": self.rank,
            "league_avg": self.league_avg.to_dict(),
            "overlay": self.overlay.to_dict() if self.overlay else None,
        }


@dataclass(slots=True, frozen=True)
class TeamEdgeCount:
    """A count-based stat with a league rank and optional league average."""
    value: int | None
    rank: int | None
    league_avg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgeCount:
        league_avg_raw = data.get("leagueAvg")
        if isinstance(league_avg_raw, dict):
            league_avg = league_avg_raw.get("value")
        elif isinstance(league_avg_raw, (int, float)):
            league_avg = float(league_avg_raw)
        else:
            league_avg = None
        return cls(
            value = data.get("value"),
            rank = data.get("rank"),
            league_avg = league_avg,
        )

    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "rank": self.rank,
            "league_avg": self.league_avg,
        }


@dataclass(slots=True, frozen=True)
class TeamEdgeLogo:
    """Light and dark mode team logo URLs."""
    light: str | None
    dark: str | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamEdgeLogo:
        return cls(
            light = data.get("light"),
            dark = data.get("dark"),
        )

    def to_dict(self) -> dict:
        return {
            "light": self.light,
            "dark": self.dark,
        }


@dataclass(slots=True, frozen=True)
class TeamDetailTeam:
    """Team info included in team edge responses."""
    id: int | None
    common_name: LocalizedString
    place_name_with_preposition: LocalizedString
    abbrev: str | None
    team_logo: TeamEdgeLogo
    slug: str | None
    conference: str | None
    division: str | None
    wins: int | None
    losses: int | None
    ot_losses: int | None
    games_played: int | None
    points: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamDetailTeam:
        return cls(
            id = data.get("id"),
            common_name = LocalizedString(data.get("commonName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            abbrev = data.get("abbrev"),
            team_logo = TeamEdgeLogo.from_dict(data.get("teamLogo") or {}),
            slug = data.get("slug"),
            conference = data.get("conference"),
            division = data.get("division"),
            wins = data.get("wins"),
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
            games_played = data.get("gamesPlayed"),
            points = data.get("points"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "common_name": self.common_name.default,
            "place_name_with_preposition": self.place_name_with_preposition.default,
            "abbrev": self.abbrev,
            "team_logo": self.team_logo.to_dict(),
            "slug": self.slug,
            "conference": self.conference,
            "division": self.division,
            "wins": self.wins,
            "losses": self.losses,
            "ot_losses": self.ot_losses,
            "games_played": self.games_played,
            "points": self.points,
        }
