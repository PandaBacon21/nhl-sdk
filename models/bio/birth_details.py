

from ..localized_string import LocalizedString


class BirthDetails: 
    def __init__(self, data: dict): 
        self.birth_date: str | None = data.get("birthDate")
        self.city: LocalizedString = LocalizedString(data.get("birthCity"))
        self.state_province: LocalizedString = LocalizedString(data.get("birthStateProvince"))
        self.country: str | None = data.get("birthCountry")