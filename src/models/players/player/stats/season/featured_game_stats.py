"""
LAST 5 GAME STATS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class FeaturedGame:
    """
    Represents a single game from a player's recent performance.
    """

    assists: int | None
    game_date: str | None
    game_id: int | None
    game_type_id: int | None
    goals: int | None
    home_road_flag: str | None
    opponent_abbrev: str | None
    pim: int | None
    plus_minus: int | None
    points: int | None
    pp_goals: int | None
    shifts: int | None
    sh_goals: int | None
    shots: int | None
    team_abbrev: str | None
    toi: str | None

    @classmethod
    def from_dict(cls, data: dict) -> FeaturedGame:
        return cls(
            assists=data.get("assists"),
            game_date=data.get("gameDate"),
            game_id=data.get("gameId"),
            game_type_id=data.get("gameTypeId"),
            goals=data.get("goals"),
            home_road_flag=data.get("homeRoadFlag"),
            opponent_abbrev=data.get("opponentAbbrev"),
            pim=data.get("pim"),
            plus_minus=data.get("plusMinus"),
            points=data.get("points"),
            pp_goals=data.get("powerPlayGoals"),
            shifts=data.get("shifts"),
            sh_goals=data.get("shorthandedGoals"),
            shots=data.get("shots"),
            team_abbrev=data.get("teamAbbrev"),
            toi=data.get("toi"),
        )

    def to_dict(self) -> dict:
        return {
            "assists": self.assists,
            "game_date": self.game_date,
            "game_id": self.game_id,
            "game_type_id": self.game_type_id,
            "goals": self.goals,
            "home_road_flag": self.home_road_flag,
            "opponent_abbrev": self.opponent_abbrev,
            "pim": self.pim,
            "plus_minus": self.plus_minus,
            "points": self.points,
            "pp_goals": self.pp_goals,
            "shifts": self.shifts,
            "sh_goals": self.sh_goals,
            "shots": self.shots,
            "team_abbrev": self.team_abbrev,
            "toi": self.toi,
        }