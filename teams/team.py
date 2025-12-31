"""
Team Object
"""

from resources.api_web import teams


class Team: 
    def __init__(self, team_code: str): 
        self.code = team_code