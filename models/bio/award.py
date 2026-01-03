
from ..localized_string import LocalizedString

class Award: 
    def __init__(self, data: dict): 
        self.trophy: LocalizedString = LocalizedString(data.get("trophy"))
        self.seasons: list = data.get("seasons") or []
    
    def __str__(self) -> str:
        if not self.seasons:
            return f"Trophy: {self.trophy}"
        seasons = ", ".join(
            str(season.get("seasonId"))
            for season in self.seasons
            if isinstance(season, dict)
            )
        return f"Trophy: {self.trophy}, Seasons: [{seasons}]"