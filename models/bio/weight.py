

class Weight: 
    def __init__(self, data: dict):
        self.weight_lbs: int | None = data.get("weightInPounds")
        self.weight_kg: int | None = data.get("weightInKilograms")
    
    def __str__(self) -> str: 
        return f"{self.weight_lbs} lbs"