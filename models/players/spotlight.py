"""
SPOTLIGHT PLAYER
"""

from ...core.utilities import LocalizedString

class Spotlight: 
    def __init__(self, data: dict): 
        self.pid: int | None = data.get("playerId")
        self.name: LocalizedString = LocalizedString(data=data.get("name"))
        self.slug: str | None = data.get("playerSlug")
        self.position: str | None = data.get("position")
        self.number: int | None = data.get("sweaterNumber")
        self.team_id: str | None = data.get("teamId")
        self.headshot: str | None = data.get("headshot")
        self.team_code: str | None = data.get("teamTriCode")
        self.team_logo: str | None = data.get("teamLogo")
        self.sortId: int | None = data.get("sortId")


    def to_dict(self) -> dict:
        return {
            "player_id": self.pid,
            "name": self.name.default,
            "slug": self.slug,
            "position": self.position,
            "sweater_number": self.number,
            "team_id": self.team_id,
            "team_code": self.team_code,
            "team_logo": self.team_logo,
            "headshot": self.headshot,
            "sort_id": self.sortId,
        }