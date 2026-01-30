"""
GAME OBJECT
"""

from ......core.utilities import LocalizedString


class Game:
    def __init__(self, data: dict): 
        self.game_id: int | None = data.get("gameId")
        self.team_abbrev: str | None = data.get("teamAbbrev")
        self.home_road_flag: str | None = data.get("homeRoadFlag")
        self.game_date: str | None = data.get("gameDate")
        self.goals: int | None = data.get("goals")
        self.assists: int | None = data.get("assists")
        self.team_name: LocalizedString = LocalizedString(data=data.get("commonName"))
        self.opponent_name: LocalizedString = LocalizedString(data=data.get("opponentCommonName"))
        self.points: int | None = data.get("points")
        self.plus_minus: int | None = data.get("plusMinus")
        self.pp_goals: int | None = data.get("powerPlayGoals")
        self.pp_points: int | None = data.get("powerPlayPoints")
        self.gw_goals: int | None = data.get("gameWinningGoals")
        self.ot_goals: int | None = data.get("otGoals")
        self.shots: int | None = data.get("shots")
        self.shifts: int | None = data.get("shifts")
        self.sh_goals: int | None = data.get("shorthandedGoals")
        self.sh_points: int | None = data.get("shorthandedPoints")
        self.opponent_abbrev: str | None = data.get("opponentAbbrev")
        self.pim: int | None = data.get("pim")
        self.toi: str | None = data.get("toi")

    def to_dict(self) -> dict:
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