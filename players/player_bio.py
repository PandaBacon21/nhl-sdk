"""
PLAYER BIO OBJECT
"""

from __future__ import annotations
from typing import Any

class Bio:
    def __init__(self, data: dict): 

        self.player_id: int = data["playerId"]
        self.first_name: Bio.LocalizedString = Bio.LocalizedString(data.get("firstName"))
        self.last_name: Bio.LocalizedString = Bio.LocalizedString(data.get("lastName"))
        self.number: int | None = data.get("sweaterNumber")
        self.position: str | None = data.get("position")
        self.team: Bio.Team = self.Team(data)
        self.hand: str | None = data.get("shootsCatches")
        self.is_active: bool | None = data.get("isActive")
        self.height: Bio.Height = self.Height(data)
        self.weight: Bio.Weight = self.Weight(data)
        self.birth_details: Bio.BirthDetails = self.BirthDetails(data)
        self.draft: Bio.Draft  = self.Draft(data)
        self.legacy: Bio.Legacy = self.Legacy(data)
        self.media: Bio.Media = self.Media(data)
    
    class LocalizedString:
        def __init__(self, data: dict | None):
            self._data = dict(data or {})

        def __str__(self) -> str:
            return self.default or ""   

        @property
        def default(self) -> str | None:
            return self._data.get("default")

        def get_locale(self, locale: str, *, fallback: bool = True) -> str | None:
            if locale in self._data:
                return self._data[locale]
            return self.default if fallback else None

        @property
        def locales(self) -> set:
            if len(self._data.keys()) > 1:
                return set(self._data.keys()) - {"default"}
            return set(self._data.keys())
        
    class Team: 
        def __init__(self, data: dict): 
            self.id: int | None = data.get("currentTeamId")
            self.name: Bio.LocalizedString = Bio.LocalizedString(data.get("fullTeamName"))
            self.code: str | None = data.get("currentTeamAbbrev")
            self.logo: str | None = data.get("teamLogo")
        
        def __str__(self) -> str: 
            return f"{self.name} ({self.code})"

    class Height: 
        def __init__(self, data: dict): 
            self.height_in: int | None = data.get("heightInInches")
            self.height_cm: int | None = data.get("heightInCentimeters")

        def __str__(self) -> str: 
            return f"{self.height_in} inches"

    class Weight: 
        def __init__(self, data: dict):
            self.weight_lbs: int | None = data.get("weightInPounds")
            self.weight_kg: int | None = data.get("weightInKilograms")
        
        def __str__(self) -> str: 
            return f"{self.weight_lbs} lbs"

    class Draft: 
        def __init__(self, data: dict):
            draft = data.get("draftDetails")

            self.year: int | None = self._handle_missing(draft, "year")
            self.team: str | None = self._handle_missing(draft, "teamAbbrev")
            self.round: int | None = self._handle_missing(draft, "round")
            self.pick_in_round: int | None = self._handle_missing(draft, "pickInRound")
            self.pick_overall: int | None = self._handle_missing(draft, "overallPick")

        def _handle_missing(self, data: dict | None, type: str) -> Any:
            if not isinstance(data, dict):
                return None
            return data.get(type)
    
    class BirthDetails: 
        def __init__(self, data: dict): 
            self.birth_date: str | None = data.get("birthDate")
            self.city: Bio.LocalizedString = Bio.LocalizedString(data.get("birthCity"))
            self.state_province: Bio.LocalizedString = Bio.LocalizedString(data.get("birthStateProvince"))
            self.country: str | None = data.get("birthCountry")

    class Legacy: 
        def __init__(self, data: dict):
            self.in_top_100_all_time: bool | None = bool(data.get("inTop100AllTime")) 
            self.in_HHOF: bool | None = bool(data.get("inHHOF")) 
            self.awards: list = data["awards"] if data["awards"] else []

    class Media:
        def __init__(self, data: dict):
            self.slug: str | None = data.get("playerSlug")
            self.headshot: str | None = data.get("headshot")
            self.hero_image: str | None = data.get("heroImage")
            self.badges: list = data["badges"] if data["badges"] else []