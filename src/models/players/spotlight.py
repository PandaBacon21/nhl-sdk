"""
SPOTLIGHT PLAYER
"""
from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class Spotlight:
    """
    Represents a spotlighted player summary.
    """
    pid: int | None
    name: LocalizedString
    slug: str | None
    position: str | None
    number: int | None
    team_id: str | None
    headshot: str | None
    team_code: str | None
    team_logo: str | None
    sort_id: int | None

    @classmethod
    def from_dict(cls, data: dict) -> Spotlight:
        return cls(
            pid=data.get("playerId"),
            name=LocalizedString(data.get("name")),
            slug=data.get("playerSlug"),
            position=data.get("position"),
            number=data.get("sweaterNumber"),
            team_id=data.get("teamId"),
            headshot=data.get("headshot"),
            team_code=data.get("teamTriCode"),
            team_logo=data.get("teamLogo"),
            sort_id=data.get("sortId"),
        )

    def to_dict(self) -> dict:
        return {
            "player_id": self.pid,
            "name": str(self.name),
            "slug": self.slug,
            "position": self.position,
            "sweater_number": self.number,
            "team_id": self.team_id,
            "team_code": self.team_code,
            "team_logo": self.team_logo,
            "headshot": self.headshot,
            "sort_id": self.sort_id,
        }
