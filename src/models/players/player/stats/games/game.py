"""
GAME OBJECT
"""
from __future__ import annotations
from dataclasses import dataclass

from ......core.utilities import LocalizedString

@dataclass(slots=True, frozen=True)
class Game:
    """
    Represents available statistics for a specific game
    """
    game_id: int | None 
    team_abbrev: str | None 
    home_road_flag: str | None
    game_date: str | None 
    goals: int | None 
    assists: int | None
    team_name: LocalizedString 
    opponent_name: LocalizedString 
    points: int | None 
    plus_minus: int | None
    pp_goals: int | None 
    pp_points: int | None 
    gw_goals: int | None 
    ot_goals: int | None 
    shots: int | None 
    shifts: int | None 
    sh_goals: int | None 
    sh_points: int | None 
    opponent_abbrev: str | None 
    pim: int | None 
    toi: str | None 

    @classmethod
    def from_dict(cls, data: dict) -> Game: 
        """
        Initialize game data from raw NHL gamelogs API response.

        Parameters
        ----------
        data : dict
            Raw game log game data returned by the NHL gamelogs API. 
        """
        return cls(
            game_id = data.get("gameId"),
            team_abbrev = data.get("teamAbbrev"),
            home_road_flag = data.get("homeRoadFlag"),
            game_date = data.get("gameDate"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            team_name = LocalizedString(data=data.get("commonName")),
            opponent_name = LocalizedString(data=data.get("opponentCommonName")),
            points = data.get("points"),
            plus_minus = data.get("plusMinus"),
            pp_goals = data.get("powerPlayGoals"),
            pp_points = data.get("powerPlayPoints"),
            gw_goals = data.get("gameWinningGoals"),
            ot_goals = data.get("otGoals"),
            shots = data.get("shots"),
            shifts = data.get("shifts"),
            sh_goals = data.get("shorthandedGoals"),
            sh_points = data.get("shorthandedPoints"),
            opponent_abbrev = data.get("opponentAbbrev"),
            pim = data.get("pim"),
            toi = data.get("toi")
        )

    def to_dict(self) -> dict:
        """
        Convert game statistics to a dictionary.

        Returns
        -------
        dict
            Serializable representation of the game statistics.
        """
        return {
            "game_id": self.game_id,
            "team_abbrev": self.team_abbrev,
            "home_road_flag": self.home_road_flag,
            "game_date": self.game_date,

            "goals": self.goals,
            "assists": self.assists,
            "points": self.points,
            "plus_minus": self.plus_minus,

            "power_play_goals": self.pp_goals,
            "power_play_points": self.pp_points,
            "game_winning_goals": self.gw_goals,
            "overtime_goals": self.ot_goals,

            "shots": self.shots,
            "shifts": self.shifts,
            "shorthanded_goals": self.sh_goals,
            "shorthanded_points": self.sh_points,

            "penalty_minutes": self.pim,
            "time_on_ice": self.toi,

            "opponent_abbrev": self.opponent_abbrev,
            "team_name": self.team_name.default,
            "opponent_name": self.opponent_name.default
        }