"""
PLAYER BIO DATA CLASS
"""

from ..team import Team
from .weight import Weight
from .height import Height
from .birth_details import BirthDetails
from .legacy import Legacy
from .media import Media
from .draft import Draft

from ...core.utilities import LocalizedString, _to_bool

class Bio:
    def __init__(self, data: dict): 

        self.player_id: int = data["playerId"]
        self.first_name: LocalizedString = LocalizedString(data.get("firstName"))
        self.last_name: LocalizedString = LocalizedString(data.get("lastName"))
        self.number: int | None = data.get("sweaterNumber")
        self.position: str | None = data.get("position")
        self.team: Team = Team(data)
        self.hand: str | None = data.get("shootsCatches")
        self.is_active: bool | None = _to_bool(data.get("isActive"))
        self.height: Height = Height(data)
        self.weight: Weight = Weight(data)
        self.birth_details: BirthDetails = BirthDetails(data)
        self.draft: Draft  = Draft(data)
        self.legacy: Legacy = Legacy(data)
        self.media: Media = Media(data)

  