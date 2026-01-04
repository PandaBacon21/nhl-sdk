"""
TEAM DATA CLASS
"""

from .localized_string import LocalizedString


class Team: 
    def __init__(self, data: dict): 
        self.id: int | None = data.get("currentTeamId")
        self.name: LocalizedString = LocalizedString(data.get("fullTeamName"))
        self.code: str | None = data.get("currentTeamAbbrev")
        self.logo: str | None = data.get("teamLogo")
    
    def __str__(self) -> str: 
        return f"{self.name} ({self.code})"