"""
SEASON STAT TEAM
"""

from ....core.utilities import LocalizedString

class SeasonTeam: 
    def __init__(self, data: dict): 
        self.common_name: LocalizedString | None = LocalizedString(data.get("teamCommonName"))
        self.name: LocalizedString | None = LocalizedString(data.get("teamName"))