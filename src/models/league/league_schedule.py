"""
LEAGUE SCHEDULE MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ..teams.team.team_schedule.team_schedule_result import ScheduleGame


@dataclass(slots=True, frozen=True)
class GameDay:
    date: str | None
    day_abbrev: str | None
    number_of_games: int | None
    date_promo: list
    games: list[ScheduleGame]

    @classmethod
    def from_dict(cls, data: dict) -> GameDay:
        return cls(
            date = data.get("date"),
            day_abbrev = data.get("dayAbbrev"),
            number_of_games = data.get("numberOfGames"),
            date_promo = data.get("datePromo") or [],
            games = [ScheduleGame.from_dict(g) for g in data.get("games") or []],
        )


@dataclass(slots=True, frozen=True)
class LeagueScheduleResult:
    next_start_date: str | None
    previous_start_date: str | None
    game_week: list[GameDay]

    @classmethod
    def from_dict(cls, data: dict) -> LeagueScheduleResult:
        return cls(
            next_start_date = data.get("nextStartDate"),
            previous_start_date = data.get("previousStartDate"),
            game_week = [GameDay.from_dict(d) for d in data.get("gameWeek") or []],
        )
