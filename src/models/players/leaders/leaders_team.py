"""
LEADERS TEAM OBJECT
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString

@dataclass(slots=True, frozen=True)
class LeadersTeam:
    name: LocalizedString
    code: str | None
    logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> LeadersTeam:
        return cls(
            name=LocalizedString(data.get("teamName")),
            code=data.get("teamAbbrev"),
            logo=data.get("teamLogo"),
        )

    def to_dict(self) -> dict:
        return {
            "name": str(self.name),
            "code": self.code,
            "logo": self.logo,
        }