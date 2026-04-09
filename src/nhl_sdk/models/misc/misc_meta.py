from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class MetaPlayerTeam:
    team_id: int | None
    abbrev: str | None
    force: bool | None

    @classmethod
    def from_dict(cls, data: dict) -> MetaPlayerTeam:
        return cls(
            team_id = data.get("teamId"),
            abbrev = data.get("abbrev"),
            force = data.get("force"),
        )


@dataclass(slots=True, frozen=True)
class MetaPlayer:
    player_id: int | None
    player_slug: str | None
    action_shot: str | None
    name: LocalizedString
    current_teams: list[MetaPlayerTeam]

    @classmethod
    def from_dict(cls, data: dict) -> MetaPlayer:
        return cls(
            player_id = data.get("playerId"),
            player_slug = data.get("playerSlug"),
            action_shot = data.get("actionShot"),
            name = LocalizedString(data.get("name")),
            current_teams = [MetaPlayerTeam.from_dict(t) for t in (data.get("currentTeams") or [])],
        )


@dataclass(slots=True, frozen=True)
class MetaTeam:
    team_id: int | None
    tricode: str | None
    team_slug: str | None
    name: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> MetaTeam:
        return cls(
            team_id = data.get("teamId"),
            tricode = data.get("tricode"),
            team_slug = data.get("teamSlug"),
            name = LocalizedString(data.get("name")),
        )


@dataclass(slots=True, frozen=True)
class MiscMeta:
    players: list[MetaPlayer]
    teams: list[MetaTeam]
    season_states: list

    @classmethod
    def from_dict(cls, data: dict) -> MiscMeta:
        return cls(
            players = [MetaPlayer.from_dict(p) for p in (data.get("players") or [])],
            teams = [MetaTeam.from_dict(t) for t in (data.get("teams") or [])],
            season_states = data.get("seasonStates") or [],
        )
