"""
TEAM GOALIE STAT MODEL
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class TeamGoalieStat:
    """A single goalie's stats entry for a team's club-stats response."""
    player_id: int | None
    headshot: str | None
    first_name: LocalizedString
    last_name: LocalizedString
    games_played: int | None
    games_started: int | None
    wins: int | None
    losses: int | None
    overtime_losses: int | None
    goals_against_average: float | None
    save_percentage: float | None
    shots_against: int | None
    saves: int | None
    goals_against: int | None
    shutouts: int | None
    goals: int | None
    assists: int | None
    points: int | None
    penalty_minutes: int | None
    time_on_ice: str | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamGoalieStat:
        return cls(
            player_id = data.get("playerId"),
            headshot = data.get("headshot"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            games_played = data.get("gamesPlayed"),
            games_started = data.get("gamesStarted"),
            wins = data.get("wins"),
            losses = data.get("losses"),
            overtime_losses = data.get("overtimeLosses"),
            goals_against_average = data.get("goalsAgainstAverage"),
            save_percentage = data.get("savePercentage"),
            shots_against = data.get("shotsAgainst"),
            saves = data.get("saves"),
            goals_against = data.get("goalsAgainst"),
            shutouts = data.get("shutouts"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
            penalty_minutes = data.get("penaltyMinutes"),
            time_on_ice = data.get("timeOnIce"),
        )
