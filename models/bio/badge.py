"""
BADGE DATA CLASS
"""


from ...core.utilities import LocalizedString

class Badge: 
    def __init__(self, data: dict): 
        self.logo: LocalizedString = LocalizedString(data.get("logoUrl"))
        self.title: LocalizedString = LocalizedString(data.get("title"))
    
    def __str__(self) -> str:
        return f"Badge: {self.title}" 