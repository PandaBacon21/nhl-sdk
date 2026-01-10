"""
TEAMS COLLECTION
"""

from ..resources.api_web import teams


class Teams: 
    """
    Teams Collection

    This is the primary interface for Team related data. 
    """
    def __init__(self, team_code: str): 
        self.code = team_code