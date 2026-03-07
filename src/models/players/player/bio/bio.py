"""
PLAYER BIO DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .bio_team import BioTeam
from .weight import Weight
from .height import Height
from .birth_details import BirthDetails
from .legacy import Legacy
from .media import Media
from .draft import Draft

from .....core.utilities import LocalizedString, _to_bool

@dataclass(slots=True, frozen=True)
class Bio:
    player_id: int 
    first_name: LocalizedString 
    last_name: LocalizedString 
    number: int | None 
    position: str | None 
    team: BioTeam 
    hand: str | None 
    is_active: bool | None 
    height: Height 
    weight: Weight 
    birth_details: BirthDetails 
    draft: Draft 
    legacy: Legacy 
    media: Media 


    @classmethod
    def from_dict(cls, data: dict) -> Bio:
        return cls(
            player_id = data["playerId"],
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            number = data.get("sweaterNumber"),
            position = data.get("position"),
            team = BioTeam.from_dict(data),
            hand = data.get("shootsCatches"),
            is_active = _to_bool(data.get("isActive")),
            height = Height.from_dict(data),
            weight = Weight.from_dict(data),
            birth_details = BirthDetails.from_dict(data),
            draft = Draft.from_dict(data),
            legacy = Legacy.from_dict(data),
            media = Media.from_dict(data)
        )
  