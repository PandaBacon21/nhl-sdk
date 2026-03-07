"""
TEAM DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class BioTeam: 
    id: int | None 
    name: LocalizedString 
    code: str | None 
    logo: str | None 
    
    @classmethod
    def from_dict(cls, data: dict) -> BioTeam:
        return cls(
            id = data.get("currentTeamId"),
            name = LocalizedString(data.get("fullTeamName")),
            code = data.get("currentTeamAbbrev"),
            logo = data.get("teamLogo")
        )