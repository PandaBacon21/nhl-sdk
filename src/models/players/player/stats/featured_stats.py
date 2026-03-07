"""
FEATURED STATS
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Featured:
    """
    Represents featured statistics for a player.

    If player is retired, returns most recent season.
    """

    season: int | None
    season_stats: FeaturedStats
    career_stats: FeaturedStats

    @classmethod
    def from_dict(cls, data: dict) -> Featured:
        regular_season: dict = data.get("regularSeason") or {}
        sub_season: dict = regular_season.get("subSeason") or {}
        career: dict = regular_season.get("career") or {}
        

        return cls(
            season=data.get("season"),
            season_stats=FeaturedStats.from_dict(sub_season),
            career_stats=FeaturedStats.from_dict(career),
        )

    def to_dict(self) -> dict:
        return {
            "season": self.season,
            "season_stats": self.season_stats.to_dict(),
            "career_stats": self.career_stats.to_dict(),
        }

@dataclass(slots=True, frozen=True)
class FeaturedStats:
    """
    Highlighted statistical totals for a player.
    """

    assists: int | None
    game_winning_goals: int | None
    games_played: int | None
    goals: int | None
    ot_goals: int | None
    pim: int | None
    plus_minus: int | None
    points: int | None
    pp_goals: int | None
    pp_points: int | None
    shooting_pctg: float | None
    sh_goals: int | None
    sh_points: int | None
    shots: int | None

    @classmethod
    def from_dict(cls, data: dict) -> FeaturedStats:
        return cls(
            assists=data.get("assists"),
            game_winning_goals=data.get("gameWinningGoals"),
            games_played=data.get("gamesPlayed"),
            goals=data.get("goals"),
            ot_goals=data.get("otGoals"),
            pim=data.get("pim"),
            plus_minus=data.get("plusMinus"),
            points=data.get("points"),
            pp_goals=data.get("powerPlayGoals"),
            pp_points=data.get("powerPlayPoints"),
            shooting_pctg=data.get("shootingPctg"),
            sh_goals=data.get("shorthandedGoals"),
            sh_points=data.get("shorthandedPoints"),
            shots=data.get("shots"),
        )

    def to_dict(self) -> dict:
        return {
            "assists": self.assists,
            "game_winning_goals": self.game_winning_goals,
            "games_played": self.games_played,
            "goals": self.goals,
            "ot_goals": self.ot_goals,
            "pim": self.pim,
            "plus_minus": self.plus_minus,
            "points": self.points,
            "pp_goals": self.pp_goals,
            "pp_points": self.pp_points,
            "shooting_pctg": self.shooting_pctg,
            "sh_goals": self.sh_goals,
            "sh_points": self.sh_points,
            "shots": self.shots,
        }