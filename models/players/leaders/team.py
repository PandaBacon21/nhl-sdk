"""
LEADERS TEAM OBJECT
"""

from ....core.utilities import LocalizedString


class Team: 
    def __init__(self, data: dict): 
        self.name: LocalizedString = LocalizedString(data.get("teamName"))
        self.code: str | None = data.get("teamAbbrev")
        self.logo: str | None = data.get("teamLogo")
