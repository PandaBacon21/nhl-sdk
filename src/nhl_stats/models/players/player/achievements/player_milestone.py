"""
PLAYER MILESTONE DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PlayerMilestone:
    id: int | None
    assists: int | None
    current_team_id: int | None
    game_type_id: int | None
    games_played: int | None
    goals: int | None
    milestone: str | None
    milestone_amount: int | None
    player_full_name: str | None
    player_id: int | None
    points: int | None
    team_abbrev: str | None
    team_common_name: str | None
    team_full_name: str | None
    team_place_name: str | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayerMilestone:
        return cls(
            id = data.get("id"),
            assists = data.get("assists"),
            current_team_id = data.get("currentTeamId"),
            game_type_id = data.get("gameTypeId"),
            games_played = data.get("gamesPlayed"),
            goals = data.get("goals"),
            milestone = data.get("milestone"),
            milestone_amount = data.get("milestoneAmount"),
            player_full_name = data.get("playerFullName"),
            player_id = data.get("playerId"),
            points = data.get("points"),
            team_abbrev = data.get("teamAbbrev"),
            team_common_name = data.get("teamCommonName"),
            team_full_name = data.get("teamFullName"),
            team_place_name = data.get("teamPlaceName"),
        )
