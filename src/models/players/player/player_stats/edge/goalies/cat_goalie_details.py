"""
CAT GOALIE DETAILS MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from ..player_edge_types import EdgeCount, EdgeSeason
from .goalie_details import CatGoaliePlayerSummary, GoalieShotLocationSummary, GoalieShotLocationAreaDetail


@dataclass(slots=True, frozen=True)
class CatGoalieDetails:
    """
    CAT endpoint NHL Edge rankings and stat summaries for a goalie.

    Includes a player summary with current season stats, seasons with edge data,
    GAA, games above .900, goal differential per 60, goal support average,
    point percentage, and shot location breakdowns.

    Instances of this class are accessed via `Stats.edge.goalie.cat_details()`.
    """
    player: CatGoaliePlayerSummary
    seasons_with_edge: list
    goals_against_avg: EdgeCount
    games_above_900: EdgeCount
    goal_differential_per_60: EdgeCount
    goal_support_avg: EdgeCount
    point_pctg: EdgeCount
    shot_location_summary: list
    shot_location_details: list

    @classmethod
    def from_dict(cls, data: dict) -> CatGoalieDetails:
        stats: dict = data.get("stats") or {}
        return cls(
            player=CatGoaliePlayerSummary.from_dict(data.get("player") or {}),
            seasons_with_edge=[EdgeSeason.from_dict(s) for s in data.get("seasonsWithEdgeStats") or []],
            goals_against_avg=EdgeCount.from_dict(stats.get("goalsAgainstAvg") or {}),
            games_above_900=EdgeCount.from_dict(stats.get("gamesAbove900") or {}),
            goal_differential_per_60=EdgeCount.from_dict(stats.get("goalDifferentialPer60") or {}),
            goal_support_avg=EdgeCount.from_dict(stats.get("goalSupportAvg") or {}),
            point_pctg=EdgeCount.from_dict(stats.get("pointPctg") or {}),
            shot_location_summary=[GoalieShotLocationSummary.from_dict(s) for s in data.get("shotLocationSummary") or []],
            shot_location_details=[GoalieShotLocationAreaDetail.from_dict(d) for d in data.get("shotLocationDetails") or []],
        )

    def to_dict(self) -> dict:
        return {
            "player": self.player.to_dict(),
            "seasons_with_edge": [s.to_dict() for s in self.seasons_with_edge],
            "goals_against_avg": self.goals_against_avg.to_dict(),
            "games_above_900": self.games_above_900.to_dict(),
            "goal_differential_per_60": self.goal_differential_per_60.to_dict(),
            "goal_support_avg": self.goal_support_avg.to_dict(),
            "point_pctg": self.point_pctg.to_dict(),
            "shot_location_summary": [s.to_dict() for s in self.shot_location_summary],
            "shot_location_details": [d.to_dict() for d in self.shot_location_details],
        }
