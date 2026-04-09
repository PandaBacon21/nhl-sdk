"""
CAREER STATS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Career:
    """
    Represents a player's career statistics.

    Separates career totals into regular season and playoff statistics.
    """

    regular_season: CareerStats
    playoffs: CareerStats

    @classmethod
    def from_dict(cls, data: dict) -> Career:
        regular_season_data: dict = data.get("regularSeason") or {}
        playoffs_data: dict = data.get("playoffs") or {}

        return cls(
            regular_season=CareerStats.from_dict(regular_season_data),
            playoffs=CareerStats.from_dict(playoffs_data),
        )


@dataclass(slots=True, frozen=True)
class CareerStats:
    """
    Aggregated career statistics for a player.

    All values represent cumulative or averaged statistics across
    a player's entire career for a specific game context
    (regular season or playoffs).
    """

    assists: int | None
    avg_toi: str | None
    faceoff_win_pctg: float | None
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
    def from_dict(cls, data: dict) -> CareerStats:
        return cls(
            assists=data.get("assists"),
            avg_toi=data.get("avgToi"),
            faceoff_win_pctg=data.get("faceoffWinningPctg"),
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
            "avg_toi": self.avg_toi,
            "faceoff_win_pctg": self.faceoff_win_pctg,
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