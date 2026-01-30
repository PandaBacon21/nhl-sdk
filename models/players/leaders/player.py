"""
LEADERS SKATER OBJECTS
"""

from .team import Team
from ....core.utilities import LocalizedString


class Player: 
    def __init__(self, data: dict): 
        self.value: int | None = data.get("value")
        self.pid: str | None = data.get("id")
        self.first_name: LocalizedString | None = LocalizedString(data.get("firstName"))
        self.last_name: LocalizedString | None = LocalizedString(data.get("lastName"))
        self.number: int | None = data.get("sweaterNumber")
        self.position: str | None = data.get("position")
        self.headshot: str | None = data.get("headhshot")
        self.team: Team = Team(data)
