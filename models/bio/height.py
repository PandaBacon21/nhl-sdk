


class Height: 
    def __init__(self, data: dict): 
        self.height_in: int | None = data.get("heightInInches")
        self.height_cm: int | None = data.get("heightInCentimeters")

    def __str__(self) -> str: 
        return f"{self.height_in} inches"