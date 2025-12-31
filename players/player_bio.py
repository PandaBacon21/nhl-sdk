"""
PLAYER BIO OBJECT
"""

from typing import Any

class Bio:
    def __init__(self, data: dict): 
        self.player_id: int | None = data.get("playerId")
        self.first_name: str | None = self._handle_missing(data.get("firstName"))
        self.last_name: str | None = self._handle_missing(data.get("lastName"))
        self.number: int | None = data.get("sweaterNumber")
        self.position: str | None = data.get("position")
        self.team: "Bio.Team" = self.Team(data)
        self.hand: str | None = data.get("shootsCatches")
        self.is_active: bool | None = data.get("isActive")
        self.height: "Bio.Height" = self.Height(data)
        self.weight: "Bio.Weight" = self.Weight(data)
        self.birth_details: "Bio.BirthDetails" = self.BirthDetails(data)
        self.draft: "Bio.Draft"  = self.Draft(data)
        self.legacy: "Bio.Legacy" = self.Legacy(data)
    
    @staticmethod
    def _handle_missing(data: dict | None, cat: str = "default") -> Any:
        if not isinstance(data, dict):
            return None
        return data.get(cat)

    class Team: 
        def __init__(self, data: dict): 
            self.id: int | None = data.get("currentTeamId")
            self.name: str | None = Bio._handle_missing(data.get("fullTeamName"))
            self.name_fr: str | None = Bio._handle_missing(data.get("fullTeamName"), "fr")
            self.code: str | None = Bio._handle_missing(data.get("currentTeamAbbrev"))

    class Height: 
        def __init__(self, data: dict): 
            self.height_in: int | None = data.get("heightInInches")
            self.height_cm: int | None = data.get("heightInCentimeters")

    class Weight: 
        def __init__(self, data: dict):
            self.weight_lbs: int | None = data.get("weightInPounds")
            self.weight_kg: int | None = data.get("weightInKilograms")

    class Draft: 
        def __init__(self, data: dict):
            draft = data.get("draftDetails")

            self.year: int | None = Bio._handle_missing(draft, "year")
            self.team: str | None = Bio._handle_missing(draft, "teamAbbrev")
            self.round: int | None = Bio._handle_missing(draft, "round")
            self.pick_in_round: int | None = Bio._handle_missing(draft, "pickInRound")
            self.pick_overall: int | None = Bio._handle_missing(draft, "overallPick")

    
    class BirthDetails: 
        def __init__(self, data: dict): 
            self.birth_date: str | None = data.get("birthDate")
            self.city: str | None = Bio._handle_missing(data.get("birthCity"))
            self.state_province: str | None = Bio._handle_missing(data.get("birthStateProvince"))
            self.state_province_fr: str | None = Bio._handle_missing(data.get("birthStateProvince"), "fr")
            self.country: str | None = data.get("birthCountry")

    class Legacy: 
        def __init__(self, data: dict):
            self.in_top_100_all_time: bool | None = bool(data.get("inTop100AllTime")) 
            self.in_HHOF: bool | None = bool(data.get("inHHOF"))  